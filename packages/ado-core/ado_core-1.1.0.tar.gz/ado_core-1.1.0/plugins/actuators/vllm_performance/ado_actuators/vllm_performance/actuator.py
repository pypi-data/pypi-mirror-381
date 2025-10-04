# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import json
import logging
import os
import uuid

import ray
import yaml
from ado_actuators.vllm_performance.actuator_parameters import (
    VLLMPerformanceTestParameters,
)
from ado_actuators.vllm_performance.env_manager import (
    EnvironmentManager,
)
from ado_actuators.vllm_performance.experiment_executor import (
    run_resource_and_workload_experiment,
    run_workload_experiment,
)

from orchestrator.core.actuatorconfiguration.config import GenericActuatorParameters
from orchestrator.modules.actuators.base import (
    ActuatorBase,
    DeprecatedExperimentError,
    MissingConfigurationForExperimentError,
)
from orchestrator.modules.actuators.catalog import ExperimentCatalog
from orchestrator.modules.actuators.measurement_queue import MeasurementQueue
from orchestrator.modules.operators.orchestrate import CLEANER_ACTOR
from orchestrator.schema.entity import Entity
from orchestrator.schema.experiment import Experiment, ParameterizedExperiment
from orchestrator.schema.reference import ExperimentReference
from orchestrator.schema.request import MeasurementRequest

logger = logging.getLogger(__name__)


# An Actuator must do three things
# 1. Provide a catalog of Experiments it can execute - the catalog method
# 2. Provide a way to run those experiments asynchronously - the submit method
# 3. Provide the results of the experiments - via the Results Queue
@ray.remote
class VLLMPerformanceTest(ActuatorBase):

    identifier = "vllm_performance"  # The user-facing label you want this actuator to be called by
    parameters_class = (
        VLLMPerformanceTestParameters  # we tell ado what our parameters class is
    )

    @classmethod
    def catalog(
        cls, actuator_configuration: GenericActuatorParameters | None = None
    ) -> ExperimentCatalog:
        """Returns the Experiments your actuator provides"""

        # The catalog be formed in code here or read from a file containing the Experiments models
        # This shows reading from a file

        path = os.path.abspath(__file__)
        path = os.path.split(path)[0]
        with open(os.path.join(path, "experiments.yaml")) as f:
            data = yaml.safe_load(f)
            experiments = [Experiment(**data[e]) for e in data]

        return ExperimentCatalog(
            catalogIdentifier=cls.identifier,
            experiments={e: e for e in experiments},
        )

    def __init__(
        self,
        queue: MeasurementQueue,
        params: VLLMPerformanceTestParameters,
    ):
        """
        queue: Queue where experiment results are put for consumers
        params: This actuators configuration parameters (Note: Soon this will be a model defined by the Actuator)
        """

        # Set logging and the ivar self._stateUpdateQueue and self._parameters
        super().__init__(queue=queue, params=params)
        # Set parameters
        self.actuator_parameters = params
        # çreate environment manager actor
        self.env_manager = None

        if self.actuator_parameters.namespace:
            try:
                self.env_manager = EnvironmentManager.remote(
                    namespace=params.namespace,
                    max_concurrent=params.max_environments,
                    in_cluster=params.in_cluster,
                    verify_ssl=params.verify_ssl,
                )
            except Exception as error:
                self.log.warning(
                    f"Unable to create kubernetes environment manager due to {error}. "
                    f"Will not be able to execute experiments requiring deploying on k8s"
                )
            else:
                # add to clean up
                try:
                    cleaner_handle = ray.get_actor(name=CLEANER_ACTOR)
                    cleaner_handle.add_to_cleanup.remote(handle=self.env_manager)
                except Exception as e:
                    print(
                        f"Failed to register custom actors for clean up {e}. Make sure you clean it up"
                    )

        # initialize local port
        self.local_port = 10000

    async def submit(
        self,
        entities: list[Entity],
        experimentReference: ExperimentReference,
        requesterid: str,
        requestIndex: int,
    ) -> list[str]:
        """Runs experimentReference on entities

        The result of running the experiment is expected to be returned asynchronously via the stateUpdateQueue
        as a MeasurementRequest instance

        :param entities: A list of Entity instances representing the entities to be measured
        :param experimentReference: An ExperimentReference defining the experiment to run on the entities.
               Expected to come from the actuators catalog.
        :param requesterid: Unique identifier of the requester of this measurement
        :param requestIndex: The index of this request i.e. this is the ith request by the requester in the current run

        Returns:
            A list with the ids of the experiments it submitted.
            NOTE: An actuator may not submit all entities in one batch.

        Raises:
            DeprecatedExperimentError: if the experimentReference points to an experiment that is deprecated.
            MissingConfigurationForExperimentError
        """

        # The following steps MUST be done
        # How they are implemented is up to the developer

        # 1. Create MeasurementRequest(s) instances representing the experiments to be performed
        # 2. Asynchronously launch the experiments -> placing their results in the resultsQueue
        # 3. Return the ids of the MeasurementRequests submit to the caller of this function

        # Here we give an example of creating the MeasurementRequests in this method
        # and executing asynchronously via a remote ray function

        # Create MeasurementRequest(s)
        # You can create one for all entities or one for each entity or any split
        # NOTE: ALL must have same requestIndex - this is used to maintain timeseries of requests
        request = MeasurementRequest(
            operation_id=requesterid,
            requestIndex=requestIndex,
            experimentReference=experimentReference,
            entities=entities,
            requestid=str(uuid.uuid4())[:6],  # Create UID as you like
        )

        # Check if the requested experiment is deprecated
        experiment = self.__class__.catalog().experimentForReference(
            request.experimentReference
        )
        """
        Check if the experiment has parameterization fields and create the right ParameterizedExperiment instance
        Note: this is necessary for getting values of optional properties that the discoverySpace overrides
        """
        if experimentReference.parameterization:
            experiment = ParameterizedExperiment(
                parameterization=experimentReference.parameterization,
                **experiment.model_dump(),
            )

        if experiment.deprecated is True:
            raise DeprecatedExperimentError(f"Experiment {experiment} is deprecated")

        if experiment.identifier == "performance-testing-full":
            if not self.env_manager:
                raise MissingConfigurationForExperimentError(
                    f"Actuator configuration did not contain sufficient information for a kubernetes environment manager to be created. "
                    f"Experiment {experiment} requires a kubernetes environment manager to be executable."
                )

            if self.actuator_parameters.node_selector == "":
                node_selector = {}
            else:
                try:
                    node_selector = json.loads(self.actuator_parameters.node_selector)
                except Exception as e:
                    logger.error(
                        f"Error loading node selector {self.actuator_parameters.node_selector} - {e}"
                    )
                    raise Exception(
                        f"Error loading node selector {self.actuator_parameters.node_selector} - {e}"
                    )

            # Execute experiment
            # Note: Here the experiment instance is just past for convenience since we retrieved it above
            run_resource_and_workload_experiment.remote(
                request=request,
                experiment=experiment,
                state_update_queue=self._stateUpdateQueue,
                actuator_parameters=self.actuator_parameters,
                node_selector=node_selector,
                env_manager=self.env_manager,
                local_port=self.local_port,
            )
            self.local_port += len(request.entities)
        else:
            run_workload_experiment.remote(
                request=request,
                experiment=experiment,
                state_update_queue=self._stateUpdateQueue,
                actuator_parameters=self.actuator_parameters,
            )

        return [request.requestid]
