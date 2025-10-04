# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import pydantic
import pytest

from orchestrator.schema.observed_property import ObservedProperty
from orchestrator.schema.property import (
    AbstractProperty,
    AbstractPropertyDescriptor,
    ConcreteProperty,
    ConcretePropertyDescriptor,
    ConstitutiveProperty,
    ConstitutivePropertyDescriptor,
    Property,
    PropertyDescriptor,
)


@pytest.fixture
def property_descriptor():
    return PropertyDescriptor(identifier="my_prop")


@pytest.fixture
def abstract_property_descriptor():
    return AbstractPropertyDescriptor(identifier="my_abs_prop")


@pytest.fixture
def concrete_property_descriptor():
    return ConcretePropertyDescriptor(identifier="my_conc_prop")


@pytest.fixture
def constitutive_property_descriptor():
    return ConstitutivePropertyDescriptor(identifier="my_conc_prop")


@pytest.mark.parametrize(
    "pairs",
    [
        (Property(identifier="my_prop", metadata={"key": "value"}), PropertyDescriptor),
        (
            AbstractProperty(identifier="my_abs_prop", metadata={"key": "value"}),
            AbstractPropertyDescriptor,
        ),
        (
            ConcreteProperty(identifier="my_conc_prop", metadata={"key": "value"}),
            ConcretePropertyDescriptor,
        ),
        (
            ConstitutiveProperty(identifier="my_cons_prop", metadata={"key": "value"}),
            ConstitutivePropertyDescriptor,
        ),
    ],
    ids=["base", "abstract", "concrete", "constitutive"],
)
def test_descriptor_property_init(pairs: tuple[Property, type[PropertyDescriptor]]):
    """Test PropertyDescriptor can be initialized with a Property"""

    prop, descriptor_class = pairs
    assert descriptor_class(identifier="test")
    with pytest.raises(pydantic.ValidationError):
        descriptor_class.model_validate(
            prop
        )  # The before validator is not called if an instance of the incorrect class is passed
    assert descriptor_class.model_validate(prop.model_dump())


def test_descriptor_equality_error():
    """Test objects not having an identifier field return False for equality"""

    descriptor = PropertyDescriptor(identifier="my_desc")
    assert descriptor != 1, "Expected descriptor not to equal an integer"
    assert (
        descriptor != "my_desc"
    ), "Experiment descriptor to not equal its identifier as a bare string"
    assert descriptor == Property(
        identifier="my_desc"
    ), "Experiment descriptor to be equal to property with same id"


@pytest.mark.parametrize(
    "pairs",
    [
        (PropertyDescriptor, Property),
        (AbstractPropertyDescriptor, AbstractProperty),
        (ConcretePropertyDescriptor, ConcreteProperty),
        (ConstitutivePropertyDescriptor, ConstitutiveProperty),
    ],
    ids=["base", "abstract", "concrete", "constitutive"],
)
def test_property_from_descriptor(
    pairs: tuple[type[PropertyDescriptor], type[Property]],
):
    """Test you can create a property from a descriptor and vice versa"""

    ident = "my_id"
    descriptor_class, property_class = pairs
    desc = descriptor_class(identifier=ident)
    prop = property_class.from_descriptor(desc)
    assert prop.identifier == ident
    assert desc.property_to_descriptor(prop) == desc


@pytest.mark.parametrize(
    "prop",
    [
        Property(identifier="my_prop", metadata={"key": "value"}),
        AbstractProperty(identifier="my_abs_prop", metadata={"key": "value"}),
        ConcreteProperty(identifier="my_conc_prop", metadata={"key": "value"}),
        ConstitutiveProperty(identifier="my_cons_prop", metadata={"key": "value"}),
    ],
)
def test_property_pretty(prop: Property):
    """Test pretty print of properties is as expected inc. metadata"""

    assert str(prop)


# For use in next two tests
@pytest.fixture
def descriptor(request):
    return request.getfixturevalue(request.param)


@pytest.mark.parametrize(
    "descriptor",
    [
        "property_descriptor",
        "abstract_property_descriptor",
        "concrete_property_descriptor",
        "constitutive_property_descriptor",
    ],
    indirect=True,
)
def test_descriptor_pretty(descriptor):
    """Test pretty print of descriptors is as expected"""

    from IPython.lib.pretty import pretty

    assert (
        pretty(descriptor) == f"{descriptor.identifier} "
    ), "Expected pretty of descriptor to be descriptor id"


@pytest.mark.parametrize(
    "descriptor",
    [
        "abstract_property_descriptor",
        "concrete_property_descriptor",
        "constitutive_property_descriptor",
    ],
    indirect=True,  # Resolve strings to fixtures - you can't use them directly
)
def test_descriptor_string_representation(descriptor):
    """Test __str__ of descriptors is as expected"""
    # NOTE PropertyDescriptor does not have custom __str__ method

    prefix = "ap" if isinstance(descriptor, AbstractPropertyDescriptor) else "cp"

    assert (
        f"{descriptor}" == f"{prefix}-{descriptor.identifier}"
    ), f"Expected str rep of descriptor to be {prefix}-{descriptor.identifier}, was {descriptor}"


def test_observed_property_hashable(experiment_reference):

    ap = AbstractPropertyDescriptor(identifier="test")
    op = ObservedProperty(targetProperty=ap, experimentReference=experiment_reference)
    d = {op: "some_key"}
    assert d


def test_property_equivalence_non_property(requiredProperties):
    """Test the property equivalence works"""

    # non-equivalence to non-Property subclass is determined by missing attributes identifier and propertyDomain
    for p in requiredProperties:
        assert p == p
        assert p != "somestring", "Property evaluated equivalent to random string"
        assert p != 3, "Property evaluated equivalent to integer"


def test_abstract_property_identifier_and_string_representation(
    target_property_list, abstract_properties: list[AbstractPropertyDescriptor]
):

    for t, p in zip(target_property_list, abstract_properties):
        assert p.identifier == t
        assert str(p) == f"ap-{t}"

        concrete = ConcreteProperty(
            identifier="test", abstractProperty=AbstractProperty.from_descriptor(p)
        )
        assert concrete.identifier == "test"
        assert str(concrete) == "cp-test"


def test_constitutive_property_identifier_and_string_representation(
    constitutive_property_list, constitutive_properties
):
    for t, p in zip(constitutive_property_list, constitutive_properties):
        assert p.identifier == t
        assert str(p) == f"cp-{t}"
