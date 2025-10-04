# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import pydantic
import typer
import yaml
from rich.status import Status

from orchestrator.cli.models.parameters import AdoCreateCommandParameters
from orchestrator.cli.utils.output.prints import (
    ADO_CREATE_DRY_RUN_CONFIG_VALID,
    ERROR,
    INFO,
    SUCCESS,
    WARN,
    console_print,
    magenta,
)
from orchestrator.cli.utils.pydantic.updaters import override_values_in_pydantic_model
from orchestrator.cli.utils.resources.formatters import most_important_status_update
from orchestrator.core.operation.config import (
    DiscoveryOperationResourceConfiguration,
    OperatorModuleConf,
)
from orchestrator.core.operation.operation import OperationException, OperationOutput
from orchestrator.core.operation.resource import (
    OperationExitStateEnum,
)


def create_operation(parameters: AdoCreateCommandParameters):

    import orchestrator.modules.operators.orchestrate
    from orchestrator.modules.actuators.base import MeasurementError

    try:
        op_resource_configuration = (
            DiscoveryOperationResourceConfiguration.model_validate(
                yaml.safe_load(parameters.resource_configuration_file.read_text())
            )
        )
        validate_operation(op_resource_configuration)
    except (pydantic.ValidationError, ValueError) as e:
        console_print(
            f"{ERROR}The operation configuration provided was not valid:\n{e}",
            stderr=True,
        )
        raise typer.Exit(1) from e

    if parameters.override_values:
        op_resource_configuration = override_values_in_pydantic_model(
            model=op_resource_configuration, override_values=parameters.override_values
        )

    if len(op_resource_configuration.spaces) > 1:
        console_print(
            f"{ERROR}the spaces field only supports one value for now.", stderr=True
        )
        raise typer.Exit(1)

    with Status("Validating actuator configurations for operation") as status:
        try:
            op_resource_configuration.validate_actuatorconfigurations(
                parameters.ado_configuration.project_context
            )
        except ValueError as e:
            status.stop()
            console_print(
                f"{ERROR}The actuator configuration validation failed:\n{e}",
                stderr=True,
            )
            raise typer.Exit(1) from e

    if parameters.dry_run:
        console_print(ADO_CREATE_DRY_RUN_CONFIG_VALID, stderr=True)
        return

    try:
        operation_output = orchestrator.modules.operators.orchestrate.orchestrate(
            base_operation_configuration=op_resource_configuration,
            project_context=parameters.ado_configuration.project_context,
            discovery_space_identifier=op_resource_configuration.spaces[0],
            discovery_space_configuration=None,
        )

    except MeasurementError as e:
        console_print(
            f"{ERROR}A measurement error was encountered while running the operation:\n\t{e}",
            stderr=True,
        )
        raise typer.Exit(1) from e
    except ValueError as e:
        console_print(
            f"{ERROR}Failed to create operation:\n\t{e}",
            stderr=True,
        )
        raise typer.Exit(1) from e
    except KeyboardInterrupt as e:
        console_print(
            f"{INFO}Operation creation has been stopped due to a keyboard interrupt.",
            stderr=True,
        )
        raise typer.Exit(3) from e
    except OperationException as e:
        console_print(
            f"{ERROR}An unexpected error occurred. "
            f"Operation {magenta(e.operation.identifier)} did not run successfully:\n\n"
            f"{most_important_status_update(e.operation.status).message}",
            stderr=True,
        )
        raise typer.Exit(1) from e
    except BaseException as e:
        console_print(
            f"{ERROR}An unexpected error occurred. Failed to create operation:\n\n{e}",
            stderr=True,
        )
        raise

    output_operation_result(result=operation_output)


def validate_operation(
    resource_configuration: DiscoveryOperationResourceConfiguration,
) -> None:
    import orchestrator.modules.operators.base

    if isinstance(
        resource_configuration.operation.module,
        OperatorModuleConf,
    ):
        module_name = resource_configuration.operation.module.moduleName
        module_class = resource_configuration.operation.module.moduleClass
        import importlib

        try:
            operation: orchestrator.modules.operators.base.DiscoveryOperationBase = (
                getattr(importlib.import_module(module_name), module_class)
            )
        except ModuleNotFoundError as e:
            console_print(
                f"{ERROR}Cannot run operation. Operator {module_name}.{module_class} is not installed.",
                stderr=True,
            )
            raise typer.Exit(1) from e

        operation.validateOperationParameters(
            resource_configuration.operation.parameters
        )

    # AP: it is an OperationFunctionConf
    else:

        import orchestrator.modules.operators.collections

        configuration_model = (
            orchestrator.modules.operators.collections.operationCollectionMap[
                resource_configuration.operation.module.operationType
            ].configuration_model_for_operation(
                resource_configuration.operation.module.operatorName
            )
        )

        if not configuration_model:
            console_print(
                f"{WARN}No configuration model was available for operation "
                f"{resource_configuration.operation.module.operatorName} of type "
                f"{resource_configuration.operation.module.operationType}",
                stderr=True,
            )
            return

        configuration_model.model_validate(resource_configuration.operation.parameters)


def output_operation_result(result: OperationOutput):
    # Output some padding
    console_print("", stderr=True)

    match result.exitStatus.exit_state:
        case OperationExitStateEnum.SUCCESS:
            console_print(
                f"{SUCCESS}Created operation with identifier {magenta(result.operation.identifier)} "
                "and it finished successfully.",
            )
        case OperationExitStateEnum.ERROR:
            console_print(
                f"{WARN}Created operation with identifier {magenta(result.operation.identifier)} "
                "but it exited with an unexpected error.",
                stderr=True,
            )
            raise typer.Exit(2)
        case OperationExitStateEnum.FAIL:
            console_print(
                f"{ERROR}Created operation with identifier {magenta(result.operation.identifier)} "
                "but it reported that it failed.",
                stderr=True,
            )
            raise typer.Exit(2)
        case _:
            console_print(
                f"{ERROR}Operation exit state {result.exitStatus.exit_state} was unsupported.",
                stderr=True,
            )
            raise typer.Exit(1)
