# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import enum
import typing

import numpy as np
import pydantic
from pydantic import ConfigDict


class VariableTypeEnum(str, enum.Enum):
    """Used to denote if the values of a property are discrete, continuous etc."""

    CONTINUOUS_VARIABLE_TYPE = (
        "CONTINUOUS_VARIABLE_TYPE"  # the value of the variable is continuous
    )
    DISCRETE_VARIABLE_TYPE = (
        "DISCRETE_VARIABLE_TYPE"  # the value of the variable is discrete
    )
    CATEGORICAL_VARIABLE_TYPE = (
        "CATEGORICAL_VARIABLE_TYPE"  # the value of the variable is a category label
    )
    BINARY_VARIABLE_TYPE = "BINARY_VARIABLE_TYPE"  # the value of the variable is binary
    UNKNOWN_VARIABLE_TYPE = "UNKNOWN_VARIABLE_TYPE"  # the type of value of the variable is unknown/unspecified
    IDENTIFIER_VARIABLE_TYPE = "IDENTIFIER_VARIABLE_TYPE"  # the value is some type of, possible unique, identifier


class ProbabilityFunctionsEnum(str, enum.Enum):
    UNIFORM = "uniform"  # A uniform distribution
    NORMAL = "normal"  # A normal distribution
    # Can easily add more


def is_float_range(
    interval: float,
    domain_range: list[int | float],
) -> bool:
    "Returns True if an on interval or domain range is a float"

    return any(isinstance(x, float) for x in [interval, *domain_range])


def _internal_range_values(lower, upper, interval) -> list:
    """Returns the values in the half-open [lower,upper) range

    If all values are integers uses arange
    If one value is a float uses linspace and then removes the last value

    All values are rounded to 10 decimal places

    This function is required due to floating precision issues.
    The rounding deals with issues like 0.2+0.1 = 0.30000000000000004
    linspace delas with issue like arange(0.1,0.4,0.1) includes 0.4

    """

    if not is_float_range(interval=interval, domain_range=[lower, upper]):
        return list(np.arange(lower, upper, interval))
    num = int(np.floor((upper - lower) / interval)) + 1
    values = [lower + i * interval for i in range(num)]
    if values[-1] == upper:
        values = values[:-1]
    # values = np.linspace(lower, upper, num)[:-1]
    return list(np.round(values, 10))


class ProbabilityFunction(pydantic.BaseModel):
    identifier: ProbabilityFunctionsEnum = pydantic.Field(
        default=ProbabilityFunctionsEnum.UNIFORM
    )
    # Whatever parameters the probability function takes.
    # Should take range, interval, and categories
    parameters: dict | None = pydantic.Field(default=None)

    model_config = ConfigDict(frozen=True, extra="forbid")

    def __eq__(self, other: "ProbabilityFunction"):

        try:
            assert (
                self.identifier == other.identifier
            ), f"Probability functions type is not the same {self.identifier, other.identifier}"
            if self.parameters:
                assert (
                    len(
                        set(self.parameters.keys()).difference(
                            set(other.parameters.keys())
                        )
                    )
                    == 0
                ), f"The other probability function has a different number of parameters {self.parameters, other.parameters}"
                for k in self.parameters:
                    assert (
                        self.parameters[k] == other.parameters[k]
                    ), f"The value of parameter {k} differs: {self.parameters[k], other.parameters[k]}"
                retval = True
            else:
                retval = not other.parameters

        except (AttributeError, AssertionError) as error:
            print(error)
            retval = False

        return retval


class PropertyDomain(pydantic.BaseModel):
    """Describes the domain of a property"""

    values: list[typing.Any] | None = pydantic.Field(
        default=None, description="The values for a discrete or categorical domain"
    )
    interval: int | float | None = pydantic.Field(
        default=None,
        description="The interval between discrete values variables. Do not set if values is set",
    )  # Only makes sense for discrete variables.
    domainRange: list[int | float] | None = pydantic.Field(
        description="The range of the domain for discrete or continuous variables. Inclusive of lower bound exclusive of upper bound. Calculated automatically if values is given.",
        default=None,
        validate_default=True,
        min_length=2,
        max_length=2,
        frozen=True,
    )  # For discrete/continuous variables
    variableType: VariableTypeEnum = pydantic.Field(
        default=VariableTypeEnum.UNKNOWN_VARIABLE_TYPE, validate_default=True
    )
    probabilityFunction: ProbabilityFunction = pydantic.Field(
        default=ProbabilityFunction()
    )

    model_config = ConfigDict(frozen=True, extra="forbid")

    def _repr_pretty_(self, p, cycle=False):

        if cycle:  # pragma: nocover
            p.text("Cycle detected")
        else:
            p.text(f"Type: {self.variableType.value}")
            p.breakable()
            if self.values:
                p.text(f"Values: {self.values}")
                p.breakable()
            if self.interval:
                p.text(f"Interval: {self.interval}")
                p.breakable()
            if self.domainRange and self.variableType in [
                VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE,
                VariableTypeEnum.DISCRETE_VARIABLE_TYPE,
            ]:
                p.text(f"Range: {self.domainRange}")
                p.breakable()

    @pydantic.field_validator("interval")
    def interval_requires_no_values(
        cls, interval, values: "pydantic.FieldValidationInfo"
    ):

        if interval is not None:
            assert (
                values.data.get("values") is None
            ), f"Cannot specify interval ({interval} if values are specified ({values.data.get('values')}"

        return interval

    @pydantic.field_validator("domainRange")
    def range_requirements(
        cls,
        passed_range: list[int | float] | None,
        otherFields: "pydantic.FieldValidationInfo",
    ):

        values = otherFields.data.get("values")
        if passed_range is not None and values:
            # Check if the two are compatible - this is for backwards compatibility
            result = min(passed_range) <= min(values) and max(values) < max(
                passed_range
            )
            if not result:
                raise ValueError(
                    f"Passed domainRange ({passed_range}) and values ({values} are not compatible"
                )
            # Forget the passed range
            passed_range = None

        return passed_range

    @pydantic.field_validator("variableType")
    def variableType_matches_values(cls, value, values: "pydantic.FieldValidationInfo"):

        import numbers

        # If the variable type is unknown assign it
        if value == VariableTypeEnum.UNKNOWN_VARIABLE_TYPE:
            # Check if we can give a more specific type
            # Rules:
            # If values provided and all numbers == DISCRETE_VARIABLE_TYPE
            # if values provided and not all numbers == CATEGORICAL_VARIABLE_TYPE
            # if range provided and no interval == CONTINUOUS_VARIABLE_TYPE
            # if range provide  and interval == DISCRETE_VARIABLE_TYPE
            # if interval ==  DISCRETE_VARIABLE_TYPE

            if values.data.get("values") is not None:
                if all(
                    isinstance(e, numbers.Number) for e in values.data.get("values")
                ):
                    value = VariableTypeEnum.DISCRETE_VARIABLE_TYPE
                else:
                    value = VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE
            elif values.data.get("domainRange") is not None:
                if values.data.get("interval") is not None:
                    value = VariableTypeEnum.DISCRETE_VARIABLE_TYPE
                else:
                    value = VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
            elif values.data.get("interval") is not None:
                value = VariableTypeEnum.DISCRETE_VARIABLE_TYPE

        if value == VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE:
            assert values.data.get("values") is not None
            assert values.data.get("interval") is None
            if not all(
                isinstance(e, numbers.Number) for e in values.data.get("values")
            ):
                assert values.data.get("domainRange") is None
        elif value == VariableTypeEnum.DISCRETE_VARIABLE_TYPE:
            # Discrete must have either values or an interval
            # If it has a range it must have an interval
            valuesCheck = values.data.get("values") is not None
            intervalCheck = values.data.get("interval") is not None
            assert valuesCheck or intervalCheck

        elif value == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE:
            assert values.data.get("values") is None
            assert values.data.get("interval") is None

        return value

    @pydantic.model_serializer
    def minimize_serialization(
        self, info: "pydantic.SerializationInfo"
    ) -> dict[str, typing.Any]:

        import numbers

        from orchestrator.utilities.pydantic import (
            model_dict_representation_with_field_exclusions_for_custom_model_serializer,
        )

        dict_representation = (
            model_dict_representation_with_field_exclusions_for_custom_model_serializer(
                model=self, info=info
            )
        )

        if not info.context or not info.context.get("minimize_output", False):
            return dict_representation

        # We can remove domainRange if values are defined
        if self.values and "domainRange" in dict_representation:
            del dict_representation["domainRange"]

        # We can remove variableType according to the rules
        # defined in:
        # https://github.ibm.com/Discovery-Orchestrator/ad-orchestrator/issues/1505#issuecomment-123891159
        if "variableType" in dict_representation:
            can_delete_variable_type = False
            match self.variableType:
                case VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE:
                    # We can remove the variableType for categorical variables
                    # if we have values and the values are not all numbers
                    can_delete_variable_type = self.values and not all(
                        isinstance(v, numbers.Number) for v in self.values
                    )
                case VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE:
                    # We can remove the variableType for continuous variables
                    # if the domain range is defined
                    can_delete_variable_type = bool(self.domainRange)
                case VariableTypeEnum.DISCRETE_VARIABLE_TYPE:
                    # We can remove the variableType for discrete variables if:
                    # - values are defined
                    # - the domain range is defined AND the interval is defined
                    #   OR
                    #   the domain range IS NOT defined AND the interval is defined
                    if self.values:
                        can_delete_variable_type = True
                    elif self.domainRange:
                        can_delete_variable_type = self.interval is not None
                    elif self.interval is not None:
                        can_delete_variable_type = True
                case VariableTypeEnum.UNKNOWN_VARIABLE_TYPE:
                    can_delete_variable_type = True
                case _:
                    # We need to always serialize:
                    # - BINARY_VARIABLE_TYPE
                    # - IDENTIFIER_VARIABLE_TYPE
                    pass

            if can_delete_variable_type:
                del dict_representation["variableType"]

        return dict_representation

    def __eq__(self, other):
        """Two domains are considered the same if they have identical values for the properties"""

        try:
            iseq = (
                self.variableType == other.variableType
                and self.domainRange == other.domainRange
                and self.interval == other.interval
                and self.values == other.values
                and self.probabilityFunction == other.probabilityFunction
            )
        except AttributeError:
            # One of the objects is not a PropertyDomain
            iseq = False

        return iseq

    @property
    def domain_values(self) -> list:

        if self.variableType in {
            VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE,
            VariableTypeEnum.UNKNOWN_VARIABLE_TYPE,
        }:
            raise ValueError(
                "Cannot generate domain values for continuous or unknown variables"
            )
        if self.variableType == VariableTypeEnum.BINARY_VARIABLE_TYPE:
            return [False, True]

        if self.values:
            return self.values

        return _internal_range_values(
            lower=min(self.domainRange),
            upper=max(self.domainRange),
            interval=self.interval,
        )

    def valueInDomain(self, value):

        if self.variableType == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE:
            if self.domainRange is not None:
                retval = (value < max(self.domainRange)) and (
                    value >= min(self.domainRange)
                )
            else:
                import numbers

                # The domain has no range which means we just accept the value if it is a number
                retval = bool(isinstance(value, numbers.Number))
        elif self.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE:
            if self.values:
                retval = value in self.values
            else:
                if self.domainRange is not None:
                    retval = value in self.domain_values
                else:
                    # The domain has no range or values which means we just accept the value
                    retval = True
        elif self.variableType == VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE:
            retval = value in self.values
        elif self.variableType == VariableTypeEnum.UNKNOWN_VARIABLE_TYPE:
            # If the domain is unknown we just return True
            # This is required if the value is from a PropertyType with this domain for self-consistency
            # e.g. If we have a ConstitutiveProperty(identifier="smiles", PropertyDomain(type=UNKNOWN_VARIABLE_TYPE)
            # And then if we ask is smiles = (CO2) in the domain it should return True.
            retval = True
        elif self.variableType == VariableTypeEnum.BINARY_VARIABLE_TYPE:
            retval = value in [True, False, 0, 1]
        else:  # pragma: nocover
            raise ValueError(
                f"Internal error: Unknown variable type {self.variableType}"
            )

        return retval

    def isSubDomain(self, otherDomain: "PropertyDomain") -> bool:
        """Checks if the receiver is a subdomain of otherDomain.

        If the two domains are identical this method returns True"""

        if self is otherDomain:
            return True

        if self.variableType != otherDomain.variableType:
            # Unless
            # A_ this domain is discrete and the other is continuous OR
            # B_ the other domain is unknown variable type
            # NOTE: If this domain is UNKNOWN it can't be a sub-domain of any non UNKNOWN variable
            # they can't be subdomains
            if otherDomain.variableType == VariableTypeEnum.UNKNOWN_VARIABLE_TYPE:
                # We can return immediately as there is nothing else we can do with UNKNOWN
                return True
            if not (
                self.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
                and otherDomain.variableType
                == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
            ):
                return False

        retval = True
        if self.variableType == VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE:
            s = set(self.values)
            o = set(otherDomain.values)

            # The receiver is a subdomain if all its values are in otherDomain values
            # i.e. we can check this by computing the set different
            retval = len(s.difference(o)) == 0
        elif self.variableType == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE:
            # If the other domain has no range then the receiver is a subdomain
            if not otherDomain.domainRange:
                retval = True
            elif otherDomain.values:  # If the other domain has values - use those
                retval = all(
                    min(self.domainRange) <= x < max(self.domainRange)
                    for x in otherDomain.values
                )
            else:
                retval = bool(
                    min(self.domainRange) >= min(otherDomain.domainRange)
                    and max(self.domainRange) <= max(otherDomain.domainRange)
                )
        elif (
            self.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
            and otherDomain.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
        ):
            # There are four situations
            # 1. Us: DomainRange Other: DomainRange
            # 2. Us: DomainRange Other: Values
            # 3. Us: Values Other: Values
            # 4. Us: Values Other: DomainRange
            if otherDomain.interval:
                if self.interval:
                    # We both have  an interval
                    # Our interval must be divisible by domain interval
                    if self.interval % otherDomain.interval == 0:
                        # No we have to check the ranges
                        if self.domainRange and otherDomain.domainRange:
                            # Both have ranges - values must be subsets of each other
                            s = set(self.domain_values)
                            o = set(otherDomain.domain_values)
                            retval = len(s.difference(o)) == 0
                        elif self.domainRange and not otherDomain.domainRange:
                            # We have a range and the other doesn't
                            retval = True
                        elif not self.domainRange and otherDomain.domainRange:
                            # We don't have a range and the other does - can't be subdomain
                            retval = False
                        else:
                            # Neither have ranges
                            retval = True
                    else:
                        retval = False
                else:
                    # they have a domain range and interval we have values
                    # convert their domain range to values
                    s = set(self.values)
                    o = set(otherDomain.domain_values)
                    retval = len(s.difference(o)) == 0
            else:
                if self.values:
                    # we both have values
                    s = set(self.values)
                    o = set(otherDomain.values)
                    retval = len(s.difference(o)) == 0
                else:
                    # we have a domain range and interval, and they have values
                    # convert the domain range to values
                    s = set(self.domain_values)
                    o = set(otherDomain.values)
                    retval = len(s.difference(o)) == 0
        elif (
            self.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
            and otherDomain.variableType == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
        ):
            if not otherDomain.domainRange:
                # If there is no domain on the continuous variable we are subdomain
                retval = True
            elif self.values:  # If we have values - use those
                retval = all(
                    min(otherDomain.domainRange) <= x < max(otherDomain.domainRange)
                    for x in self.values
                )
            else:
                retval = bool(
                    min(self.domainRange) >= min(otherDomain.domainRange)
                    and max(self.domainRange) <= max(otherDomain.domainRange)
                )

        return retval

    @property
    def size(self) -> float | int:
        """Returns the size (number of elements) in the domain if this is countable.

        Returns math.inf if the size is not countable.
        This includes any domain with CONTINUOUS_VARIABLE_TYPE, UNKNOWN_VARIABLE_TYPE ir IDENTIFIER_VARIABLE_TYPE.
        It also includes any unbounded domain with DISCRETE_VARIABLE_TYPE.
        """

        import math

        if (
            self.variableType == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
        ):  # noqa: SIM114
            size = math.inf
        elif self.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE and (
            self.domainRange is None and self.values is None
        ):
            size = math.inf
        else:
            if self.variableType == VariableTypeEnum.DISCRETE_VARIABLE_TYPE:
                # If we have an interval we can use the range to get size
                # Otherwise the variable must have specified values, and we use the number of values.
                if self.interval is not None:
                    # Note: Intervals are inclusive of lower bound exclusive of upper if interval is 1
                    # If interval is greater than 1 it may include upper limit
                    # This is the same as "a_range" default behaviour and also of ray.tune.(q)randint.
                    a_range = _internal_range_values(
                        lower=min(self.domainRange),
                        upper=max(self.domainRange),
                        interval=self.interval,
                    )

                    size = len(a_range)
                else:
                    size = len(self.values)
            elif self.variableType == VariableTypeEnum.BINARY_VARIABLE_TYPE:
                size = 2
            elif self.variableType == VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE:
                size = len(self.values)
            else:
                size = math.inf

        return size
