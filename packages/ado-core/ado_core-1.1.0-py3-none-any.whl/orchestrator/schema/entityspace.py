# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import typing

from orchestrator.schema.domain import VariableTypeEnum
from orchestrator.schema.entity import Entity
from orchestrator.schema.property import ConstitutiveProperty
from orchestrator.schema.property_value import constitutive_property_values_from_point
from orchestrator.schema.result import MeasurementResult


class EntitySpaceRepresentation:
    """Provides explicit details of the dimensions of the space"""

    @classmethod
    def representationFromConfiguration(cls, conf: list[ConstitutiveProperty]):

        return cls(constitutiveProperties=conf)

    def __init__(
        self,
        constitutiveProperties: list[ConstitutiveProperty],
    ):

        self._constitutiveProperties = constitutiveProperties
        self._propertyLookup = {c.identifier: c for c in self._constitutiveProperties}

    @property
    def config(self) -> list[ConstitutiveProperty]:

        return self.constitutiveProperties

    @property
    def constitutiveProperties(
        self,
    ) -> list[ConstitutiveProperty]:

        return self._constitutiveProperties.copy()

    @property
    def isDiscreteSpace(self):

        non_discrete_dims = [
            d
            for d in self._constitutiveProperties
            if (
                d.propertyDomain.variableType
                == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
            )
            or (d.propertyDomain.variableType == VariableTypeEnum.UNKNOWN_VARIABLE_TYPE)
        ]

        return len(non_discrete_dims) == 0

    @property
    def size(self) -> int:
        """Returns the number of points in the space if it is defined, otherwise raises an AttributeError"""

        import functools
        import math
        import operator

        sizes = [d.propertyDomain.size for d in self._constitutiveProperties]
        if math.inf in sizes:
            raise AttributeError(
                f"Cannot calculate size of {self} as it has non-countable dimensions"
            )
        size = functools.reduce(operator.mul, sizes)

        # size will be an int, as the only float sizes can contain is math.inf
        # and if that is present we raise an Exception
        # However for typing we cast it
        return int(size)

    def __str__(self):

        return (
            f"Explicit entity-space defined by {len(self._constitutiveProperties)}"
            f" constitutive properties: {[cp.identifier for cp in self._constitutiveProperties]}"
        )

    def _repr_pretty_(self, p, cycle=False):

        import pandas as pd

        if cycle:  # pragma: nocover
            p.text("Cycle detected")
        else:
            if self.isDiscreteSpace:
                p.breakable()
                p.text(f"Number entities: {self.size}")
                p.break_()
                p.breakable()
            else:
                p.breakable()
                p.text("Space with non-discrete dimensions. Cannot count entities")
                p.breakable()

            categoricalProperties = [
                cv
                for cv in self._constitutiveProperties
                if cv.propertyDomain.variableType
                == VariableTypeEnum.CATEGORICAL_VARIABLE_TYPE
            ]

            discreteProperties = [
                cv
                for cv in self._constitutiveProperties
                if cv.propertyDomain.variableType
                == VariableTypeEnum.DISCRETE_VARIABLE_TYPE
            ]

            continuousProperties = [
                cv
                for cv in self._constitutiveProperties
                if cv.propertyDomain.variableType
                == VariableTypeEnum.CONTINUOUS_VARIABLE_TYPE
            ]

            unknownProperties = [
                cv
                for cv in self._constitutiveProperties
                if cv.propertyDomain.variableType
                == VariableTypeEnum.UNKNOWN_VARIABLE_TYPE
            ]

            binaryProperties = [
                cv
                for cv in self._constitutiveProperties
                if cv.propertyDomain.variableType
                == VariableTypeEnum.BINARY_VARIABLE_TYPE
            ]

            if categoricalProperties:
                with p.group(2, "Categorical properties:"):
                    p.breakable()
                    data = [
                        [cv.identifier, cv.propertyDomain.values]
                        for cv in categoricalProperties
                    ]
                    df = pd.DataFrame(
                        data,
                        columns=[
                            "name",
                            "values",
                        ],
                    )
                    p.pretty(df)
                p.breakable()
                p.breakable()

            if discreteProperties:
                with p.group(2, "Discrete properties:"):
                    p.breakable()
                    data = [
                        [
                            cv.identifier,
                            cv.propertyDomain.domainRange,
                            cv.propertyDomain.interval,
                            cv.propertyDomain.values,
                        ]
                        for cv in discreteProperties
                    ]
                    df = pd.DataFrame(
                        data,
                        columns=["name", "range", "interval", "values"],
                    )
                    p.pretty(df)
                p.breakable()
                p.breakable()

            if binaryProperties:
                with p.group(2, "Binary properties:"):
                    p.breakable()
                    data = [[cv.identifier] for cv in binaryProperties]
                    df = pd.DataFrame(
                        data,
                        columns=["name"],
                    )
                    p.pretty(df)
                p.breakable()
                p.breakable()

            if continuousProperties:
                with p.group(2, "Continuous properties:"):
                    p.breakable()
                    data = [
                        [cv.identifier, cv.propertyDomain.domainRange]
                        for cv in continuousProperties
                    ]
                    df = pd.DataFrame(
                        data,
                        columns=["name", "range"],
                    )
                    p.pretty(df)
                p.breakable()
                p.breakable()

            if unknownProperties:
                with p.group(2, "Properties with unknown type:"):
                    p.breakable()
                    data = [[cv.identifier] for cv in unknownProperties]
                    df = pd.DataFrame(
                        data,
                        columns=["name"],
                    )
                    p.pretty(df)
                p.breakable()
                p.breakable()

    def propertyWithIdentifier(self, identifier: str) -> ConstitutiveProperty | None:
        """Returns the constitutive property with identifier or None if there is None"""

        return self._propertyLookup.get(identifier)

    def isPointInSpace(
        self, point: dict[str, typing.Any], allow_partial_matches: bool = False
    ):
        """
        Determines if a given point is within this space based on constitutive property matches.

        :param point:
            Dictionary representing the point with constitutive property identifiers as keys and
            constitutive property values as values.
        :param allow_partial_matches:
            If True, ill return True if at least one property matches; otherwise the point must
             match all the constitutive properties of the entities.

        :return: True if the point is in the space, False otherwise.
        """
        constitutive_property_identifiers_for_point = set(point.keys())
        constitutive_property_identifiers_for_entity_space = {
            cp.identifier for cp in self._constitutiveProperties
        }

        matching_constitutive_property_identifiers = (
            constitutive_property_identifiers_for_point.intersection(
                constitutive_property_identifiers_for_entity_space
            )
        )

        # If we don't allow partial matches, all properties must match
        if not allow_partial_matches and len(
            matching_constitutive_property_identifiers
        ) != len(constitutive_property_identifiers_for_entity_space):
            return False

        # If we allow partial matches, all properties for the point must
        # match
        if len(matching_constitutive_property_identifiers) != len(
            constitutive_property_identifiers_for_point
        ):
            return False

        # Once we have checked that the identifiers match, we must
        # check that the values specified by the point are in the domain
        # of the constitutive properties.
        for constitutive_property in self.constitutiveProperties:
            if (
                constitutive_property.identifier
                not in matching_constitutive_property_identifiers
            ):
                continue

            if not constitutive_property.propertyDomain.valueInDomain(
                point[constitutive_property.identifier]
            ):
                return False

        return True

    def isEntityInSpace(self, entity: Entity):
        """Returns True if entity is in the space otherwise false

        Specifically False is returned if the entity's constitutive properties are not identical to the entityspaces

        """

        # If the set of entity property values are equal to the set of entityspace property values

        point = {
            cpv.property.identifier: cpv.value
            for cpv in entity.constitutive_property_values
        }
        return self.isPointInSpace(point)

    def isPointCompatibleWithSpace(self, point: dict[str, typing.Any]):
        """A point is compatible if the identifiers of all the entityspaces constitutive properties are keys in point

        Note: This means the point may have more dimensions (keys/constitutive properties) than the entityspace.

        Returns:
            - True if point is compatible with space otherwise false
            - False if:
                - The set of identifiers of the entityspaces constitutive properties are not a subset of points keys
        """

        retval = False
        for c in self.constitutiveProperties:
            v = point.get(c.identifier)
            retval = c.propertyDomain.valueInDomain(v) if v else False

            # Once we find a property that the entity does not have or does not have a valid value for
            # we can stop
            if not retval:
                break

        return retval

    def isEntityCompatibleWithSpace(self, entity: Entity):
        """An entity is compatible if all the entityspaces constitutive properties are also constitutive properties of the entity

        Note: This means an entity may have more constitutive properties than the entityspace.

        Returns:
            - True if entity is compatible with space otherwise false
            - False if:
                - The entityspaces constitutive properties are not a subset of entity constitutive properties
        """

        point = {
            cpv.property.identifier: cpv.value
            for cpv in entity.constitutive_property_values
        }
        return self.isPointCompatibleWithSpace(point)

    def entity_for_point(
        self,
        point: dict[str, tuple[typing.Any]],
        results: list[MeasurementResult] | None = None,
    ) -> Entity:
        """
        Parameters:
            point: A point in the space as a dictionary of "constitutive property identifier":"value" pairs
            results: An optional list of MeasurementResults to add to the entity

        Exceptions:
            Raise ValueError if the point is not in the space
        """

        constitutive_property_values = constitutive_property_values_from_point(
            point=point, properties=self._constitutiveProperties
        )

        return Entity(
            generatorid="explicit_grid_sample_generator",
            constitutive_property_values=tuple(constitutive_property_values),
            measurement_results=results or [],
        )

    def dimension_values(self) -> dict[str, list]:
        """Returns a dict with all the values along each dimension in the entity space

        The keys are constitutive property identifiers and the values are list or numpy arrays
        containing all the values for that dimension.

        Exceptions:
        Raises a ValueError if any dimension is not-discrete

        """

        if not self.isDiscreteSpace:
            raise ValueError(
                "Cannot return dimension_values for a space with continuous or unknown dimensions"
            )

        return {
            cp.identifier: cp.propertyDomain.domain_values
            for cp in self._constitutiveProperties
        }

    def sequential_point_iterator(self) -> typing.Iterator[list[typing.Any]]:
        """Returns an iterator over all the points defined by an entity space with discrete constitutive properties.

        Each point is a list of values, the value of the nth element is the value for the nth ConstitutiveProperty

        The points are iterated sequentially starting with the innermost dimension

        Raises a ValueError if the EntitySpace contains a continuous dimension
        """

        import itertools

        dimensionValues = self.dimension_values()
        return itertools.product(
            *[dimensionValues[cp.identifier] for cp in self._constitutiveProperties]
        )

    def random_point_iterator(self) -> typing.Iterator[list[typing.Any]]:
        """Returns an iterator over all the points defined by an entity space with discrete constitutive properties.

        Each point is a list of values, the value of the nth element is the value for the nth ConstitutiveProperty

        The points are iterated  randomly

        Raises a ValueError if the EntitySpace contains a continuous dimension
        """

        import random

        points = list(self.sequential_point_iterator())
        random.shuffle(points)

        return iter(points)


class ModelEntitySpaceRepresentation:
    """Details on the space are not explicit e.g. they are implicit in some model"""
