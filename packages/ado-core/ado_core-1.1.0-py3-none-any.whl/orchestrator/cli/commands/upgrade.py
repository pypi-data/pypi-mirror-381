# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import typing
from typing import Annotated

import typer

from orchestrator.cli.models.choice import HiddenSingularChoice
from orchestrator.cli.models.parameters import (
    AdoUpgradeCommandParameters,
)
from orchestrator.cli.models.types import (
    AdoUpgradeSupportedResourceTypes,
)
from orchestrator.cli.resources.actuator_configuration.upgrade import (
    upgrade_actuator_configuration,
)
from orchestrator.cli.resources.data_container.upgrade import upgrade_data_container
from orchestrator.cli.resources.discovery_space.upgrade import upgrade_discovery_space
from orchestrator.cli.resources.operation.upgrade import upgrade_operation
from orchestrator.cli.resources.sample_store.upgrade import upgrade_sample_store

if typing.TYPE_CHECKING:
    from orchestrator.cli.core.config import AdoConfiguration


def upgrade_resource(
    ctx: typer.Context,
    resource_type: Annotated[
        AdoUpgradeSupportedResourceTypes,
        typer.Argument(
            ...,
            help="The kind of the resource to upgrade.",
            show_default=False,
            click_type=HiddenSingularChoice(AdoUpgradeSupportedResourceTypes),
        ),
    ],
):
    """
    Upgrade resources and contexts.

    See https://ibm.github.io/ado/getting-started/ado/#ado-upgrade
    for detailed documentation and examples.



    Examples:



    # Upgrade all operations

    ado upgrade operations
    """

    ado_configuration: AdoConfiguration = ctx.obj

    parameters = AdoUpgradeCommandParameters(
        ado_configuration=ado_configuration,
    )

    method_mapping = {
        AdoUpgradeSupportedResourceTypes.ACTUATOR_CONFIGURATION_PLURAL: upgrade_actuator_configuration,
        AdoUpgradeSupportedResourceTypes.DATA_CONTAINER_PLURAL: upgrade_data_container,
        AdoUpgradeSupportedResourceTypes.DISCOVERY_SPACE_PLURAL: upgrade_discovery_space,
        AdoUpgradeSupportedResourceTypes.SAMPLE_STORE_PLURAL: upgrade_sample_store,
        AdoUpgradeSupportedResourceTypes.OPERATION_PLURAL: upgrade_operation,
    }

    method_mapping[resource_type](parameters=parameters)


def register_upgrade_command(app: typer.Typer):
    app.command(
        name="upgrade",
        no_args_is_help=True,
        options_metavar="",
    )(upgrade_resource)
