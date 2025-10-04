# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import typing
from typing import Annotated

import typer

from orchestrator.cli.exceptions.handlers import (
    handle_no_related_resource,
    handle_resource_does_not_exist,
)
from orchestrator.cli.models.choice import HiddenPluralChoice
from orchestrator.cli.models.parameters import AdoShowDetailsCommandParameters
from orchestrator.cli.models.types import AdoShowDetailsSupportedResourceTypes
from orchestrator.cli.resources.discovery_space.show_details import (
    show_discovery_space_details,
)
from orchestrator.cli.resources.operation.show_details import show_operation_details
from orchestrator.cli.utils.output.prints import ERROR, console_print
from orchestrator.core.samplestore.base import (
    FailedToDecodeStoredEntityError,
    FailedToDecodeStoredMeasurementResultForEntityError,
)
from orchestrator.metastore.base import (
    NoRelatedResourcesError,
    ResourceDoesNotExistError,
)

if typing.TYPE_CHECKING:
    from orchestrator.cli.core.config import AdoConfiguration


def show_details_for_resources(
    ctx: typer.Context,
    resource_type: Annotated[
        AdoShowDetailsSupportedResourceTypes,
        typer.Argument(
            ...,
            help="The kind of the resource to show details for.",
            show_default=False,
            click_type=HiddenPluralChoice(AdoShowDetailsSupportedResourceTypes),
        ),
    ],
    resource_id: Annotated[
        str,
        typer.Argument(
            ...,
            help="The id of the resource to show details for.",
            show_default=False,
        ),
    ],
):
    """
    Show a high-level overview of a resource and what resources are related to it.

    For spaces, it will show the size of the space, and information about the entities.
    For operations, it will show information about measured entities.

    See https://ibm.github.io/ado/getting-started/ado/#ado-show-details
    for detailed documentation and examples.



    Examples:



    # Show the size of a space and what operations have been run on it

    ado show details space <space-id>




    # Show how many entities were measured as part of an operation

    ado show details operation <operation-id>
    """
    ado_configuration: AdoConfiguration = ctx.obj
    parameters = AdoShowDetailsCommandParameters(
        ado_configuration=ado_configuration, resource_id=resource_id
    )

    method_mapping = {
        AdoShowDetailsSupportedResourceTypes.DISCOVERY_SPACE: show_discovery_space_details,
        AdoShowDetailsSupportedResourceTypes.OPERATION: show_operation_details,
    }

    try:
        method_mapping[resource_type](parameters=parameters)
    except ResourceDoesNotExistError as e:
        handle_resource_does_not_exist(
            error=e, project_context=ado_configuration.project_context
        )
    except NoRelatedResourcesError as e:
        handle_no_related_resource(
            error=e, project_context=ado_configuration.project_context
        )
    except (
        FailedToDecodeStoredEntityError,
        FailedToDecodeStoredMeasurementResultForEntityError,
    ) as e:
        console_print(f"{ERROR}{e}", stderr=True)
        raise typer.Exit(1)


def register_show_details_command(app: typer.Typer):
    app.command(
        name="details",
        no_args_is_help=True,
        options_metavar="",
    )(show_details_for_resources)
