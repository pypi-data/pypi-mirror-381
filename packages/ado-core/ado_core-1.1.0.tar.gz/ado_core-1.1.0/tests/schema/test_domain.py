# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT
import json
import math

from orchestrator.schema.domain import (
    ProbabilityFunction,
    ProbabilityFunctionsEnum,
    PropertyDomain,
    VariableTypeEnum,
)


def test_comparison_with_non_domain():
    discretePropertyDomain = PropertyDomain(interval=1, domainRange=[-10, 10])
    assert (
        discretePropertyDomain != "somestring"
    ), "PropertyDomain evaluate equal to a string"
    assert discretePropertyDomain != ["a"], "PropertyDomain evaluate equal to a list"
    assert discretePropertyDomain != 3, "PropertyDomain evaluate equal to an int"


def test_probability_function_equivalanece():

    uniform = ProbabilityFunction(
        identifier=ProbabilityFunctionsEnum.UNIFORM, parameters={"a": "0", "b": 5}
    )
    uniform2 = ProbabilityFunction(
        identifier=ProbabilityFunctionsEnum.UNIFORM, parameters={"a": "0", "b": 5}
    )

    # Compare identical
    assert uniform == uniform, "ProbabilityFunction instance not equal to itself"
    assert uniform2 == uniform, "Identical probability function instances not equal"

    # Compare with same id, same number parameters, different parameters
    uniform2 = ProbabilityFunction(
        identifier=ProbabilityFunctionsEnum.UNIFORM, parameters={"a": "0", "b": 4}
    )
    assert (
        uniform2 != uniform
    ), "ProbabilityFunctions with different parameter values evaluate as equal"

    uniform2 = ProbabilityFunction(
        identifier=ProbabilityFunctionsEnum.UNIFORM, parameters={"a": "0", "c": 4}
    )
    assert (
        uniform2 != uniform
    ), "ProbabilityFunctions with different parameter names evaluate as equal"

    # Compare with different ids
    normal = ProbabilityFunction(
        identifier=ProbabilityFunctionsEnum.NORMAL, parameters={"mu": "0", "sigma": 8}
    )
    assert (
        normal != uniform
    ), "Normal probability distribution evaluates equal to uniform"

    # Compare with same id different number of parameters
    uniform2 = ProbabilityFunction(
        identifier=ProbabilityFunctionsEnum.UNIFORM,
        parameters={"a": "0", "c": 4, "b": 3},
    )
    assert uniform != uniform2

    uniform = ProbabilityFunction(identifier=ProbabilityFunctionsEnum.UNIFORM)
    uniform2 = ProbabilityFunction(
        identifier=ProbabilityFunctionsEnum.UNIFORM, parameters={"a": "0", "b": 5}
    )
    assert (
        uniform != uniform2
    ), "ProbabilityFunction without parameters evaluates equal to one with parameters"

    # Compare against non probability
    assert uniform != ["a", "b"]


def test_valid_property_domains():
    import pytest

    # Test that variableType of domain is assigned properly given valid inputs

    continuousPropertyDomain = PropertyDomain(domainRange=[-10, 10])

    assert (
        continuousPropertyDomain.variableType
        == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
    )

    discretePropertyDomain = PropertyDomain(interval=1, domainRange=[-10, 10])

    assert (
        discretePropertyDomain.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
    )

    discretePropertyDomainNoRange = PropertyDomain(interval=1)

    assert (
        discretePropertyDomain.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
    )

    categoricalPropertyDomain = PropertyDomain(values=["A", "B", 3])

    assert (
        categoricalPropertyDomain.variableType
        == VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE
    )

    domains = [
        continuousPropertyDomain,
        discretePropertyDomain,
        discretePropertyDomainNoRange,
        categoricalPropertyDomain,
    ]
    for d in domains:
        assert d == d

    # Test valueInDomain

    assert continuousPropertyDomain.valueInDomain(-11) is False
    assert continuousPropertyDomain.valueInDomain(-10) is True
    assert continuousPropertyDomain.valueInDomain(1) is True
    assert continuousPropertyDomain.valueInDomain(0.5) is True
    assert (
        continuousPropertyDomain.valueInDomain(10) is False
    )  # Range is exclusive of upper bound
    assert discretePropertyDomain.valueInDomain(-11) is False
    assert discretePropertyDomain.valueInDomain(-10) is True
    assert discretePropertyDomain.valueInDomain(1) is True
    assert discretePropertyDomain.valueInDomain(0.5) is False
    assert (
        discretePropertyDomain.valueInDomain(10) is False
    )  # Range is exclusive of upper bound
    assert discretePropertyDomainNoRange.valueInDomain(-110) is True
    assert discretePropertyDomainNoRange.valueInDomain(-10) is True
    assert discretePropertyDomainNoRange.valueInDomain(1) is True
    # For discrete variables with an interval we need at least one part of range to anchor the interval!
    # assert discretePropertyDomainNoRange.valueInDomain(0.5) is False
    assert discretePropertyDomainNoRange.valueInDomain(100) is True
    assert categoricalPropertyDomain.valueInDomain("A") is True
    assert categoricalPropertyDomain.valueInDomain(3) is True
    assert categoricalPropertyDomain.valueInDomain("F") is False
    assert categoricalPropertyDomain.valueInDomain(4) is False

    # Test that we can discriminate the different domains

    assert discretePropertyDomainNoRange != discretePropertyDomain
    assert categoricalPropertyDomain != continuousPropertyDomain
    assert discretePropertyDomain != continuousPropertyDomain
    assert discretePropertyDomainNoRange != continuousPropertyDomain
    assert categoricalPropertyDomain != discretePropertyDomain

    # Test that initialising a domain with inconsistent data raises an error

    import pydantic

    with pytest.raises(pydantic.ValidationError):
        PropertyDomain(
            variableType=VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE,
            interval=1,
        )

    with pytest.raises(pydantic.ValidationError):
        PropertyDomain(
            variableType=VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE,
            domainRange=[1, 10],
        )

    # Test that DISCRETE values with a range have either values or an interval
    with pytest.raises(pydantic.ValidationError):
        PropertyDomain(
            variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
            domainRange=[1, 10],
        )

    with pytest.raises(pydantic.ValidationError):
        PropertyDomain(
            variableType=VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE,
            values=["A", "B"],
        )

    # Test that values with no type get correct type - use an interval with a non-unit step
    domain = PropertyDomain(values=list(range(0, 10, 2)))
    assert domain.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE

    # Test that DISCRETE values with no-range but with values do not get a range assigned
    assert domain.domainRange is None

    # Test that valueInDomain for DISCRETE variables with values works as expected

    assert domain.valueInDomain(-1) is False
    assert domain.valueInDomain(10) is False
    assert domain.valueInDomain(11) is False
    assert domain.valueInDomain(9) is False
    assert domain.valueInDomain(8) is True

    # Test that values with no type get correct type -  use an interval with a unit step

    domain = PropertyDomain(values=list(range(10)))
    assert domain.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE

    # Test that DISCRETE values with no-range but with values DO NOT get a range assigned
    assert domain.domainRange is None  # * because range(0,10) = (0,1,2,3,4,5,6,7,8,9)

    # Test that valueInDomainf for DISCRETE variables with values works as expected

    assert domain.valueInDomain(-1) is False
    assert domain.valueInDomain(10) is False
    assert domain.valueInDomain(9) is True
    assert domain.valueInDomain(8) is True

    # Test that if the values are not numeric integers that the type if CATEGORICAL

    domain = PropertyDomain(values=["A", "B", "C"])
    assert domain.variableType == VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE
    assert domain.domainRange is None

    # Test that if discrete variables is initialised with domainRange and values
    # (a) The domainRange is compatible
    # (b) the domainRange is not used
    # This behaviour is for backwards compatibility for models serialised where the domainRange was calculated

    # Compatible - the passed range includes all the values
    d = PropertyDomain(
        variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
        values=list(range(10)),
        domainRange=[-2, 11],
    )
    assert d.domainRange is None

    # Incompatible - the passed range does not include all the values
    with pytest.raises(pydantic.ValidationError):
        PropertyDomain(
            variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
            values=[e / 10 for e in range(10)],
            domainRange=[0.2, 1.1],
        )

    # Test that discrete variables with values should not have interval
    with pytest.raises(pydantic.ValidationError):
        PropertyDomain(
            variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
            values=list(range(10)),
            interval=2,
        )


def test_categorical_and_continuous_property_is_subdomain():
    """Tests the issubdomain method of PropertyDomain works"""

    continuousPropertyDomain = PropertyDomain(domainRange=[-10, 10])
    assert (
        continuousPropertyDomain.variableType
        == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
    )

    categoricalPropertyDomain = PropertyDomain(values=["A", "B", 3])
    assert (
        categoricalPropertyDomain.variableType
        == VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE
    )

    # Test identity
    assert continuousPropertyDomain.model_copy().isSubDomain(continuousPropertyDomain)
    assert categoricalPropertyDomain.model_copy().isSubDomain(categoricalPropertyDomain)

    # Test  subdomains
    # We can test detection of non subdomain by inverting the tests

    # Categorical

    categoricalSubDomain = PropertyDomain(values=["A", "B"])

    assert categoricalSubDomain.isSubDomain(categoricalPropertyDomain)
    assert not categoricalPropertyDomain.isSubDomain(categoricalSubDomain)

    # Continuous

    continuousSubdomain = PropertyDomain(domainRange=[-9, 9])
    assert continuousSubdomain.isSubDomain(continuousPropertyDomain)
    assert not continuousPropertyDomain.isSubDomain(continuousSubdomain)

    # Test against a non-bounded continuous domain
    continuousPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
    )
    assert continuousSubdomain.isSubDomain(continuousPropertyDomain)


def test_unknown_property_is_subdomain():
    """Tests isSubDomain works when one or other of the domains is UNKNOWN_VARIABLE_TYPE"""

    # UNKNOWN_VARIABLE_TYPE cannot be a subdomain of any other variable type
    # All other variable types are subdomains of UNKNOWN_VARIABLE_TYPE (including itself)

    unknownPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.UNKNOWN_VARIABLE_TYPE
    )

    # Test identity
    assert unknownPropertyDomain.model_copy().isSubDomain(unknownPropertyDomain)

    # Test continuous
    continuousPropertyDomain = PropertyDomain(domainRange=[-10, 10])
    assert continuousPropertyDomain.isSubDomain(unknownPropertyDomain)
    assert not unknownPropertyDomain.isSubDomain(continuousPropertyDomain)

    # Test Categorical
    categoricalSubDomain = PropertyDomain(values=["A", "B"])
    assert categoricalSubDomain.isSubDomain(unknownPropertyDomain)
    assert not unknownPropertyDomain.isSubDomain(categoricalSubDomain)

    # Test Discrete
    discretePropertyDomain = PropertyDomain(domainRange=[1, 10], interval=1)
    assert discretePropertyDomain.isSubDomain(unknownPropertyDomain)
    assert not unknownPropertyDomain.isSubDomain(discretePropertyDomain)

    # Test Binary
    binaryPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.BINARY_VARIABLE_TYPE
    )
    assert binaryPropertyDomain.isSubDomain(unknownPropertyDomain)
    assert not unknownPropertyDomain.isSubDomain(binaryPropertyDomain)


def test_discrete_property_is_subdomain_for_domain_range():
    """Tests the issubdomain method of PropertyDomain works
    for discrete properties where otherDomain is defined with domainRange"""

    discretePropertyDomain = PropertyDomain(interval=1, domainRange=[-10, 10])
    discretePropertyDomainCopy = PropertyDomain(interval=1, domainRange=[-10, 10])
    discretePropertyDomainNoRange = PropertyDomain(interval=1)
    discretePropertyDomainNoRangeCopy = PropertyDomain(interval=1)
    assert (
        discretePropertyDomainNoRange.variableType
        == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
    )

    # Test identity
    assert discretePropertyDomain.isSubDomain(discretePropertyDomain)
    assert discretePropertyDomainNoRange.isSubDomain(discretePropertyDomainNoRange)
    assert discretePropertyDomainCopy.isSubDomain(discretePropertyDomain)
    assert discretePropertyDomainNoRangeCopy.isSubDomain(discretePropertyDomainNoRange)

    # Test against unbounded domain

    assert not discretePropertyDomainNoRange.isSubDomain(discretePropertyDomain)

    # Test  subdomains
    # We can test detection of non subdomain by inverting the tests

    # Discrete

    # A- Domain v Value

    discretePropertySubDomain = PropertyDomain(values=[7, 8, 9])
    assert discretePropertySubDomain.isSubDomain(discretePropertyDomain)
    assert not discretePropertyDomain.isSubDomain(discretePropertySubDomain)

    # Specific case where a value is at the max of range - which should be excluded
    discretePropertySubDomain = PropertyDomain(values=[7, 8, 9, 10])
    assert not discretePropertySubDomain.isSubDomain(discretePropertyDomain)

    # B- Domain v Domain

    discretePropertySubDomain = PropertyDomain(interval=2, domainRange=[-10, 10])
    assert discretePropertySubDomain.isSubDomain(discretePropertyDomain)
    assert not discretePropertyDomain.isSubDomain(discretePropertySubDomain)

    discretePropertySubDomain = PropertyDomain(interval=1, domainRange=[-9, 10])
    assert discretePropertySubDomain.isSubDomain(discretePropertyDomain)
    assert not discretePropertyDomain.isSubDomain(discretePropertySubDomain)

    # Test specific case of interval not a mod of the other
    discretePropertyDomain = PropertyDomain(interval=2, domainRange=[-10, 10])

    discretePropertySubDomain = PropertyDomain(interval=3, domainRange=[-10, 10])
    assert not discretePropertySubDomain.isSubDomain(discretePropertyDomain)


def test_discrete_property_is_subdomain_for_values():
    """Tests the issubdomain method of PropertyDomain works
    for discrete properties where otherDomain is defined with values and interval"""

    discretePropertyDomain = PropertyDomain(interval=1, domainRange=[-10, 10])

    discretePropertyDomainNoRange = PropertyDomain(interval=1)

    # Test identity
    assert discretePropertyDomain.model_copy().isSubDomain(
        discretePropertyDomainNoRange
    )

    # C - Value v Value
    discretePropertyDomain = PropertyDomain(values=[1, 2, 3, 6, 7, 10])
    discretePropertySubDomain = PropertyDomain(values=[1, 2, 3, 6])

    assert discretePropertySubDomain.isSubDomain(discretePropertyDomain)
    assert not discretePropertyDomain.isSubDomain(discretePropertySubDomain)

    # B- Value v Domain

    discretePropertyDomain = PropertyDomain(values=[2, 4, 6, 8, 10])

    discretePropertySubDomain = PropertyDomain(domainRange=[2, 11], interval=2)

    # In this case both sides should be equal
    assert discretePropertySubDomain.isSubDomain(discretePropertyDomain)
    assert discretePropertyDomain.isSubDomain(discretePropertySubDomain)

    discretePropertySubDomain = PropertyDomain(domainRange=[2, 9], interval=2)

    assert discretePropertySubDomain.isSubDomain(discretePropertyDomain)
    assert not discretePropertyDomain.isSubDomain(discretePropertySubDomain)

    discretePropertySubDomain = PropertyDomain(domainRange=[2, 9], interval=3)

    assert not discretePropertySubDomain.isSubDomain(discretePropertyDomain)


def test_discrete_property_is_subdomain_of_continuous():
    """Tests the issubdomain method of PropertyDomain works
    for discrete properties where otherDomain is defined as a continuous domain"""

    # A - Domain v Domain

    discretePropertyDomain = PropertyDomain(interval=1, domainRange=[-10, 10])

    continuousPropertyDomain = PropertyDomain(
        domainRange=[-10, 10],
        variableType=VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE,
    )

    assert discretePropertyDomain.isSubDomain(continuousPropertyDomain)
    assert not continuousPropertyDomain.isSubDomain(discretePropertyDomain)

    # B - Values v Domain

    discretePropertyDomain = PropertyDomain(values=[1, 2, 3, 6, 7, 9])

    assert discretePropertyDomain.isSubDomain(continuousPropertyDomain)
    assert not continuousPropertyDomain.isSubDomain(discretePropertyDomain)

    # Make the values invalid

    discretePropertyDomain = PropertyDomain(values=[1, 2, 3, 6, 7, 10])

    assert not discretePropertyDomain.isSubDomain(continuousPropertyDomain)

    # C - Domain v No bounds

    discretePropertyDomain = PropertyDomain(interval=1, domainRange=[-10, 10])

    continuousPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
    )

    assert discretePropertyDomain.isSubDomain(continuousPropertyDomain)

    # C - Values v No bounds

    discretePropertyDomain = PropertyDomain(values=[2, 4, 6, 8, 10])

    continuousPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
    )

    assert discretePropertyDomain.isSubDomain(continuousPropertyDomain)


def test_domain_sizes():

    import math

    import numpy as np

    # Continuous var is inf size
    continuousPropertyDomain = PropertyDomain(domainRange=[-10, 10])
    assert continuousPropertyDomain.size == math.inf
    continuousPropertyDomain = PropertyDomain()
    assert continuousPropertyDomain.size == math.inf

    # Discrete var with no range is inf
    discretePropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE, interval=2
    )
    assert discretePropertyDomain.size == math.inf

    # Discrete var with range and interval is len(arange())
    discretePropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
        domainRange=[-9, 19],
        interval=2,
    )
    assert discretePropertyDomain.size == len(np.arange(-9, 19, 2))

    # Discerte var with values is len(values)
    discretePropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
        values=[1, 2, 4, 8, 16, 32],
    )
    assert discretePropertyDomain.size == 6

    # Binary var is 2
    binaryPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.BINARY_VARIABLE_TYPE,
    )
    assert binaryPropertyDomain.size == 2

    # Unknown is inf
    unknownPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.UNKNOWN_VARIABLE_TYPE,
    )
    assert unknownPropertyDomain.size == math.inf


def test_range_in_pretty():

    from IPython.lib.pretty import pretty

    # Continuous
    continuousPropertyDomain = PropertyDomain(domainRange=[-10, 10])
    assert "Range" in pretty(
        continuousPropertyDomain
    ), "Expected continuous domain with range to output Range in pretty print"

    # Discrete
    discretePropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
        domainRange=[-9, 19],
        interval=2,
    )
    assert "Range" in pretty(
        discretePropertyDomain
    ), "Expected discrete domain with range to output Range in pretty print"

    # Discrete
    discretePropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
        values=[1, 2, 4, 8, 16, 32],
    )
    assert "Range" not in pretty(
        discretePropertyDomain
    ), "Expected discrete domain with values NOT to output a Range in pretty print"

    # Binary
    binaryPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.BINARY_VARIABLE_TYPE,
    )
    assert "Range" not in pretty(
        binaryPropertyDomain
    ), "Expected binary domain NOT to output Range in pretty print"

    # Categorical
    categoricalPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE, values=[1, 2, 3, 4]
    )
    assert "Range" not in pretty(
        categoricalPropertyDomain
    ), "Expected categorical domain with numeric values NOT to output Range in pretty print"

    # Unknown
    unknownPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.UNKNOWN_VARIABLE_TYPE, values=[1, 2, 3, 4]
    )
    assert (
        unknownPropertyDomain.variableType is VariableTypeEnum.DISCRETE_VARIABLE_TYPE
    ), "Expected UNKNOWN variable type to be converted to DISCRETE as the input values match a discrete variable"
    assert "Range" not in pretty(unknownPropertyDomain)


def test_value_in_domain():

    # continuous variable with no range - everything is in domain
    continuousPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
    )
    assert continuousPropertyDomain.valueInDomain(1e20)
    assert continuousPropertyDomain.valueInDomain(-1.6e-16)
    assert continuousPropertyDomain.valueInDomain(math.pi)
    assert continuousPropertyDomain.valueInDomain(3)
    assert not continuousPropertyDomain.valueInDomain([1, 2])
    assert not continuousPropertyDomain.valueInDomain("3")

    # unknown variable  - everything is in domain
    unknownPropertyDomain = PropertyDomain()
    assert unknownPropertyDomain.variableType == VariableTypeEnum.UNKNOWN_VARIABLE_TYPE
    assert unknownPropertyDomain.valueInDomain(1e20)
    assert unknownPropertyDomain.valueInDomain(-1.6e-16)
    assert unknownPropertyDomain.valueInDomain(math.pi)
    assert unknownPropertyDomain.valueInDomain(3)
    assert unknownPropertyDomain.valueInDomain([1, 2])
    assert unknownPropertyDomain.valueInDomain("3")
    assert unknownPropertyDomain.valueInDomain([1, 2, "MA"])

    binaryPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.BINARY_VARIABLE_TYPE
    )
    assert binaryPropertyDomain.valueInDomain(True)
    assert binaryPropertyDomain.valueInDomain(False)
    assert binaryPropertyDomain.valueInDomain(1)
    assert binaryPropertyDomain.valueInDomain(0)
    assert not binaryPropertyDomain.valueInDomain(-1)
    assert not binaryPropertyDomain.valueInDomain(2)

    categoricalPropertyDomain = PropertyDomain(
        variableType=VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE,
        values=["A100", "T4", 1.0],
    )
    assert categoricalPropertyDomain.valueInDomain("A100")
    assert categoricalPropertyDomain.valueInDomain("T4")
    assert categoricalPropertyDomain.valueInDomain(1.0)
    assert not categoricalPropertyDomain.valueInDomain("1.0")
    assert not categoricalPropertyDomain.valueInDomain(2.0)
    assert not categoricalPropertyDomain.valueInDomain("A10")

    assert categoricalPropertyDomain.values == ["A100", "T4", 1.0]


def test_property_domain_minimization_is_correct(
    property_domain_all_types: PropertyDomain,
):
    from orchestrator.cli.utils.pydantic.constants import minimize_output_context

    current_model = property_domain_all_types
    minimized_model = current_model.model_dump_json(context=minimize_output_context)
    reloaded_model = PropertyDomain.model_validate(json.loads(minimized_model))
    assert reloaded_model == current_model


def test_float_behaviour_discrete_variable_sub_domain():
    """Test sub_domain behaviour for domains with discrete variables that include floats

    floating point arithmetic introduces very rounding issues that should be handled
    """

    d1 = PropertyDomain(values=[0.1, 0.2, 0.3])
    d4 = PropertyDomain(values=[0.1, 0.2, 0.4])
    d2 = PropertyDomain(interval=0.1, domainRange=[0.1, 0.4])
    d3 = PropertyDomain(domainRange=[0.1, 0.4])

    assert d1.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
    assert d2.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
    assert d3.variableType == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE

    # This tests that the range [0.1,0.4] with interval 0.1 translates to [0.1,0.2,0.3]
    # This tests that (a) float addition of 0.1 to the range is correctly rounded c.f. 0.2+0.1 is not 0.3 in python
    # This tests that the upper bound of the range is closed i.e. 0.4 is not included (would be with arange())
    assert d1.isSubDomain(
        d2
    ), "Expected value set [0.1,0.2,0.3] to be a subdomain of range [0.1,0.4] with interval 0.1"
    assert set(d1.values) == set(
        d2.domain_values
    ), "Expected domain with range [0.1,0.4] and interval 0.1 had values [0.1,0.2,0.3]"

    # This tests that the d1 values is correctly identified as a subdomain of a continuous domain
    # This would fail if the range associated with d1 values was not correctly bounded
    assert d1.isSubDomain(
        d3
    ), "Expected value set [0.1,0.2,0.3] to be a subdomain of continuous var with range [0.1,0.4]"

    # Another test on the bounds
    assert not d4.isSubDomain(
        d1
    ), "Expected value set [0.1,0.2,0.4] to not be a subdomain of range [0.1,0.4] with interval 0.1"
    assert not d4.isSubDomain(
        d3
    ), "Expected value set [0.1,0.2,0.4] to not be a subdomain of continuous var with range [0.1,0.4]"


def test_float_behaviour_discrete_variable_value_in_domain():

    d1 = PropertyDomain(values=[0.1, 0.2, 0.3])
    d2 = PropertyDomain(interval=0.1, domainRange=[0.1, 0.4])
    d3 = PropertyDomain(domainRange=[0.1, 0.4])

    assert d1.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
    assert d2.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
    assert d3.variableType == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE

    assert d1.valueInDomain(0.3)
    assert d3.valueInDomain(0.3)
    assert d2.valueInDomain(0.3)

    assert not d2.valueInDomain(0.4)
    assert not d3.valueInDomain(0.4)
    assert not d1.valueInDomain(0.4)


def test_domain_values():

    # Test the same intervals and ranges given as int or float give same values
    d1 = PropertyDomain(interval=4, domainRange=[1, 128])
    d2 = PropertyDomain(interval=4.0, domainRange=[1.0, 128.0])

    assert (
        d1.domain_values == d2.domain_values
    ), "The same values passed as ints or floats to PropertyDomain should give same domain_values"
    assert 128 not in d1.domain_values, "Expected the upper bound to not be included"

    d1 = PropertyDomain(values=[0.1, 0.3])
    d2 = PropertyDomain(interval=0.2, domainRange=[0.1, 0.4])

    assert d1.domain_values == d2.domain_values
    assert d1.domain_values == [0.1, 0.3]

    d1 = PropertyDomain(values=[0.1, 0.2, 0.3])
    d2 = PropertyDomain(interval=0.1, domainRange=[0.1, 0.4])

    assert d1.domain_values == d2.domain_values
