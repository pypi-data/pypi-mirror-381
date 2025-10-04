# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

from orchestrator.cli.models.parameters import AdoEditCommandParameters
from orchestrator.cli.utils.resources.handlers import handle_edit_resource_metadata
from orchestrator.core.resources import CoreResourceKinds


def edit_operation(parameters: AdoEditCommandParameters):
    handle_edit_resource_metadata(
        resource_id=parameters.resource_id,
        resource_type=CoreResourceKinds.OPERATION,
        project_context=parameters.ado_configuration.project_context,
        editor=parameters.editor,
    )
