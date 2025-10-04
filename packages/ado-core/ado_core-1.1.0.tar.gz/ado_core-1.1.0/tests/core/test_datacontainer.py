# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import orchestrator.core
import orchestrator.utilities.location
from orchestrator.core import DataContainerResource
from orchestrator.core.datacontainer.resource import DataContainer, TabularData


def test_tabular_data(testTabularDataString):

    df = testTabularDataString.dataframe()
    newdf = TabularData.from_dataframe(df)
    assert testTabularDataString.data == newdf.data


def test_data_container_resource(
    data_container_resource, testTabularDataString, test_sample_store_location
):

    assert (
        data_container_resource.kind
        == orchestrator.core.resources.CoreResourceKinds.DATACONTAINER
    )
    assert data_container_resource.identifier.split("-")[0] == "datacontainer"

    assert isinstance(data_container_resource.config, DataContainer)
    assert (
        data_container_resource.config.tabularData["important_entities"]
        == testTabularDataString
    )
    assert (
        data_container_resource.config.locationData["entity_location"]
        == test_sample_store_location
    )

    assert isinstance(
        data_container_resource.config.tabularData["important_entities"],
        TabularData,
    )
    assert isinstance(
        data_container_resource.config.locationData["entity_location"],
        orchestrator.utilities.location.SQLStoreConfiguration,
    )

    # Test ser/deser

    dc = DataContainerResource.model_validate(data_container_resource.model_dump())

    assert isinstance(dc.config.tabularData["important_entities"], TabularData)
    assert isinstance(
        dc.config.locationData["entity_location"],
        orchestrator.utilities.location.SQLStoreConfiguration,
    )

    assert (
        data_container_resource.config.tabularData["important_entities"]
        == testTabularDataString
    )
    assert (
        data_container_resource.config.locationData["entity_location"]
        == test_sample_store_location
    )


def test_datacontainer_pretty(data_container_resource):
    from IPython.lib.pretty import pretty

    assert hasattr(data_container_resource, "_repr_pretty_")
    pretty(data_container_resource)
