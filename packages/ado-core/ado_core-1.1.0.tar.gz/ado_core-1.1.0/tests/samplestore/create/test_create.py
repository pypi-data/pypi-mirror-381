# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT
import re

import pytest

from orchestrator.core.resources import CoreResourceKinds


def test_resource_creation(
    resource_generator_from_file, create_resources, sql_store, request
):
    _resource_kind, generator = resource_generator_from_file
    resource = request.getfixturevalue(generator)()
    create_resources(resources=[resource], db=sql_store)
    assert sql_store.containsResourceWithIdentifier(identifier=resource.identifier)


def test_invalid_resource_creation(
    resource_generator_from_file, create_resources, sql_store, request
):
    _resource_kind, generator = resource_generator_from_file
    resource = request.getfixturevalue(generator)()
    with pytest.raises(
        ValueError,
        match=r"Cannot add resource, .*, that is not a subclass of ADOResource",
    ):
        create_resources(resources=[resource.config], db=sql_store)


def test_resource_cannot_be_created_twice(
    resource_generator_from_file, create_resources, sql_store, request
):
    _resource_kind, generator = resource_generator_from_file
    resource = request.getfixturevalue(generator)()
    create_resources(resources=[resource], db=sql_store)
    with pytest.raises(
        ValueError,
        match=f"Resource with id {re.escape(resource.identifier)} already present. "
        "Use updateResource if you want to overwrite it",
    ):
        create_resources([resource])


def test_create_operation_with_related_space(
    random_operation_resource_from_file,
    random_space_resource_from_db,
    create_resource_with_related_identifiers,
    sql_store,
    get_single_resource_by_identifier,
    get_related_resource_identifiers_by_identifier,
):
    quantity = 3

    operation = random_operation_resource_from_file()
    space_ids = [random_space_resource_from_db().identifier for _ in range(quantity)]
    create_resource_with_related_identifiers(
        resource=operation,
        related_identifiers=space_ids,
        db=sql_store,
    )

    assert (
        get_single_resource_by_identifier(
            operation.identifier, kind=CoreResourceKinds.OPERATION
        )
        is not None
    )
    related_resource_identifiers = get_related_resource_identifiers_by_identifier(
        identifier=operation.identifier
    )["IDENTIFIER"].values
    for space_id in space_ids:
        assert space_id in related_resource_identifiers


def test_exception_on_resource_with_related_identifier_if_related_id_does_not_exist(
    random_operation_resource_from_file,
    random_space_resource_from_db,
    create_resource_with_related_identifiers,
    sql_store,
):
    operation = random_operation_resource_from_file()
    nonexistent_related_id = "IDoNotExist"
    with pytest.raises(
        ValueError,
        match=f"Unknown resource identifier passed {re.escape(str([nonexistent_related_id]))}",
    ):
        create_resource_with_related_identifiers(
            resource=operation,
            related_identifiers=[nonexistent_related_id],
            db=sql_store,
        )


def test_add_entities_to_sample_store(
    random_entities,
    random_sql_sample_store,
    add_entities_to_sample_store,
):
    quantity = 3
    entities = random_entities(quantity=quantity)
    add_entities_to_sample_store(random_sql_sample_store(), entities)


def test_upsert_entities_to_sample_store(
    random_entities,
    random_sql_sample_store,
    upsert_entities_to_sample_store,
):
    quantity = 3
    entities = random_entities(quantity=quantity)
    upsert_entities_to_sample_store(random_sql_sample_store(), entities)


def test_add_measurement_request_to_sample_store(
    ml_multi_cloud_benchmark_performance_experiment,
    random_ml_multi_cloud_benchmark_performance_measurement_requests,
    random_sql_sample_store,
):
    assert ml_multi_cloud_benchmark_performance_experiment is not None

    number_entities = 3
    measurements_per_result = 1
    requests = random_ml_multi_cloud_benchmark_performance_measurement_requests(
        number_entities=number_entities, measurements_per_result=measurements_per_result
    )
    sample_store = random_sql_sample_store()
    request_db_id = sample_store.add_measurement_request(request=requests)
    assert request_db_id is not None
    sample_store.add_measurement_results(
        results=requests.measurements,
        skip_relationship_to_request=False,
        request_db_id=request_db_id,
    )


def test_add_external_entities(random_sql_sample_store, entity):

    sample_store = random_sql_sample_store()

    # Ensure the identifier of the entity is not in the DB
    assert len(sample_store.entity_identifiers().intersection({entity.identifier})) == 0

    # Add the entity and ensure it's there
    sample_store.add_external_entities([entity])
    assert len(sample_store.entity_identifiers().intersection({entity.identifier})) == 1

    #
    retrieved_entity = sample_store.entityWithIdentifier(entity.identifier)
    assert retrieved_entity is not None
    assert len(retrieved_entity.propertyValues) == len(entity.propertyValues)
    for i, property_value in enumerate(entity.propertyValues):
        assert (
            abs(property_value.value - retrieved_entity.propertyValues[i].value) < 1e-15
        )
