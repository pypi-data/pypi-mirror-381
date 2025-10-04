# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import importlib.metadata
import typing
from typing import Annotated

import pydantic
from pydantic import ConfigDict

from orchestrator.schema.observed_property import (
    ObservedProperty,
)
from orchestrator.schema.property import (
    AbstractPropertyDescriptor,
    ConcretePropertyDescriptor,
    ConstitutiveProperty,
    MeasuredPropertyTypeEnum,
    Property,
)
from orchestrator.schema.property_value import ConstitutivePropertyValue, PropertyValue
from orchestrator.schema.reference import (
    ExperimentReference,
    check_parameterization_validity,
    identifier_for_parameterized_experiment,
    reference_string_from_fields,
)
from orchestrator.schema.virtual_property import (
    PropertyAggregationMethod,
    PropertyAggregationMethodEnum,
    VirtualObservedProperty,
)

if typing.TYPE_CHECKING:  # pragma: nocover
    from orchestrator.schema.entity import Entity


class Experiment(pydantic.BaseModel):
    """Represents an experiment that can measure properties of an entities"""

    actuatorIdentifier: str = pydantic.Field(
        description="""The id of the actuator that can execute this experiment or parameterized versions of it"""
    )
    identifier: str = pydantic.Field(
        description="""The name of the experiment.
            Must be unique in the scope of the catalog of this experiments actuator."""
    )
    metadata: dict = pydantic.Field(
        default={},
        description=""" Metadata about the experiment. Sufficient to track its source. Can be custom format per actuator""",
    )
    targetProperties: list[AbstractPropertyDescriptor | ConcretePropertyDescriptor] = (
        pydantic.Field(
            description="""The target properties this experiment aims to measure
            (can be ConcreteProperty or AbstractProperty instances)"""
        )
    )
    requiredProperties: tuple[ObservedProperty | ConstitutiveProperty, ...] = (
        pydantic.Field(
            default=(),
            frozen=True,
            description="""The properties this experiment needs values of as inputs
            (ObservedProperty or ConstitutiveProperty)""",
        )
    )
    deprecated: bool = pydantic.Field(
        default=False,
        description="Marks whether an experiment is deprecated or not. Defaults to False.",
    )
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        json_schema_extra={
            "version": importlib.metadata.version(distribution_name="ado-core")
        },
    )
    optionalProperties: tuple[ConstitutiveProperty, ...] = pydantic.Field(
        default=(),
        frozen=True,
        description="""The optional properties this experiment can take as input. Must have default values specified in parameterization""",
    )
    defaultParameterization: tuple[ConstitutivePropertyValue, ...] = pydantic.Field(
        validate_default=True,
        default=(),
        frozen=True,
        description="""Default values for the optional properties""",
    )

    @classmethod
    def experimentWithAbstractPropertyIdentifiers(
        cls,
        identifier: str,
        actuatorIdentifier: str,
        targetProperties: [str],
        propertyType: MeasuredPropertyTypeEnum = MeasuredPropertyTypeEnum.MEASURED_PROPERTY_TYPE,
        requiredConstitutiveProperties: [str] = None,
        metadata: dict | None = None,
        deprecated: bool = False,
    ):
        """Factory method for creating an Experiment instance when you have a list of abstract property ids

        :param identifier: The name of the measurement
            Must be unique in the scope of this experiments actuator i.e. the actuator can use this id to identify
            the experiment to run.
        :param actuatorIdentifier: The id of the actuator that can execute this experiment.
            This id and its format just need to be common between the Experiment and its Actuator.
            The purpose is that an actuator can check if it "owns" this Experiment
        :param targetProperties: A list of the (abstract) identifiers of the properties this experiment will attempt to measure
        :param propertyType: The type of the properties.
        :param requiredConstitutiveProperties: A list of the identifiers of the constitutive properties this experiment requires values for as inputs
        :param metadata: Metadata about the experiment. Sufficient to track its source. Can be custom format per actuator
        :param deprecated: Marks an experiment as deprecated.
        """

        targetProperties = [
            AbstractPropertyDescriptor(identifier=t, propertyType=propertyType)
            for t in targetProperties
        ]
        if requiredConstitutiveProperties is not None:
            requiredConstitutiveProperties = [
                ConstitutiveProperty(identifier=t)
                for t in requiredConstitutiveProperties
            ]
        else:
            requiredConstitutiveProperties = []

        metadata = metadata if metadata is not None else {}

        return cls(
            identifier=identifier,
            actuatorIdentifier=actuatorIdentifier,
            targetProperties=targetProperties,
            requiredProperties=requiredConstitutiveProperties,
            metadata=metadata,
            deprecated=deprecated,
        )

    @pydantic.field_validator("optionalProperties")
    def validate_optional_properties(
        cls,
        optionalProperties: list[ConstitutiveProperty],
        values: "pydantic.FieldValidationInfo",
    ):

        # Check all optional properties have unique identifiers
        if len({p.identifier for p in optionalProperties}) != len(
            [p.identifier for p in optionalProperties]
        ):
            count = {}
            for p in optionalProperties:
                count[p.identifier] = count.get(p.identifier, 0) + 1

            # VV: Report just the optionalProperties with conflicting names
            duplicates = [
                p
                for p in optionalProperties
                if p.identifier in [k for k, v in count.items() if v > 1]
            ]
            raise ValueError(
                f"Optional properties provided containing duplicate identifiers: {duplicates}"
            )

        # Check no optional property is a required property
        assert (
            len(
                {p.identifier for p in optionalProperties}.intersection(
                    {p.identifier for p in values.data.get("requiredProperties")}
                )
            )
            == 0
        )

        return optionalProperties

    @pydantic.field_validator("defaultParameterization")
    def validate_default_parameterization(
        cls,
        value: list[ConstitutivePropertyValue],
        values: "pydantic.FieldValidationInfo",
    ):

        if not value:
            if values.data.get("optionalProperties"):
                raise AssertionError(
                    "optionalProperties specified without parameterization"
                )
        else:
            if not values.data.get("optionalProperties"):
                raise AssertionError(
                    "default parameterization specified without optionalProperties being specified"
                )
            try:
                check_parameterization_validity(
                    values.data.get("optionalProperties"), value
                )
            except pydantic.ValidationError as error:
                raise error
            else:
                # Check all optionalProperties are parameterized
                mapping = {c.property.identifier: c for c in value}
                isNotParameterized = [
                    v
                    for v in values.data.get("optionalProperties")
                    if mapping.get(v.identifier) is None
                ]
                if len(isNotParameterized) > 0:
                    raise AssertionError(
                        f"optionalProperties do not have default parameterization. Missing: {[v.identifier for v in isNotParameterized]}"
                    )

        return value

    def __eq__(self, other):
        """Experiments are equal if they have the same identifier"""

        if isinstance(other, Experiment):
            return (
                (self.actuatorIdentifier == other.actuatorIdentifier)
                and (self.identifier == other.identifier)
                and (self.identifier == other.identifier)
            )
        return False

    def __str__(self):

        return reference_string_from_fields(
            actuator_identifier=self.actuatorIdentifier,
            experiment_identifier=self.identifier,
        )

    def __hash__(self):

        return hash(str(self))

    def _repr_pretty_(self, p, cycle=False):

        if cycle:  # pragma: nocover
            p.text("Cycle detected")
        else:
            p.text(f"Identifier: {self.actuatorIdentifier}.{self.identifier}")
            p.break_()
            if self.metadata.get("description"):
                p.break_()
                p.text(self.metadata["description"])
                p.break_()
            p.break_()
            with p.group(2, "Required Inputs:"):
                p.break_()
                with p.group(4, "Constitutive Properties:"):
                    p.break_()
                    if self.requiredConstitutiveProperties:
                        for c in self.requiredConstitutiveProperties:
                            p.pretty(c)
                            p.break_()
                    else:
                        p.text("No required constitutive properties specified")
                        p.break_()

                if self.requiredObservedProperties:
                    p.break_()
                    with p.group(4, "Observed Properties:"):
                        p.break_()
                        for o in self.requiredObservedProperties:
                            p.pretty(o)
                            p.break_()

            p.break_()
            if self.optionalProperties:

                mapping = {c.identifier: c for c in self.optionalProperties}

                with p.group(2, "Optional Inputs and Default Values:"):
                    p.break_()
                    for value in self.defaultParameterization:
                        prop = mapping[value.property.identifier]
                        p.pretty(prop)
                        p.break_()
                        p.text(f"Default value: {value.value}")
                        p.breakable()
                        p.breakable()

            p.breakable()
            with p.group(2, "Outputs:"):
                p.breakable()
                for c in self.observedProperties:
                    p.text(f"{c.identifier}")
                    p.breakable()

            p.breakable()
            p.breakable()

    def isValidParameterization(
        self, parameterization: list[ConstitutivePropertyValue]
    ):
        """Returns True if the list of values given by parameterization is valid, otherwise False"""

        try:
            check_parameterization_validity(
                list(self.optionalProperties), parameterization
            )
        except (ValueError, AssertionError) as error:
            print(error)
            retval = False
        else:
            retval = True

        return retval

    @property
    def reference(self) -> ExperimentReference:
        """Returns an ExperimentReference for the receiver"""

        return ExperimentReference(
            experimentIdentifier=self.identifier,
            actuatorIdentifier=self.actuatorIdentifier,
        )

    @property
    def observedProperties(self) -> list[ObservedProperty]:
        """Returns a list of ObservedProperty instances representing the properties measured by the receiver

        Note: New ObservedProperty objects are returned on each call"""

        return [
            ObservedProperty(targetProperty=target, experimentReference=self.reference)
            for target in self.targetProperties
        ]

    def observedPropertyForTargetIdentifier(
        self, targetIdentifier: str
    ) -> ObservedProperty | None:
        """Returns an ObservedProperty instance for the given targetIdentifier or None if none exists"""

        v = [
            p
            for p in self.observedProperties
            if p.targetProperty.identifier == targetIdentifier
        ]

        return None if len(v) == 0 else v[0]

    def hasTargetPropertyWithIdentifier(self, identifier):
        """Returns True if the receiver has a target property called identifier"""

        v = [p for p in self.targetProperties if p.identifier == identifier]

        return len(v) != 0

    def hasTargetProperty(self, prop: Property):
        """Returns True if  prop is one of the receivers target properties"""

        return self.hasTargetPropertyWithIdentifier(prop.identifier)

    def hasObservedPropertyWithIdentifier(self, identifier):
        """Returns True if the receiver has a target property called identifier"""

        v = [p for p in self.observedProperties if p.identifier == identifier]

        return len(v) != 0

    def hasObservedProperty(self, prop: ObservedProperty):
        """Returns True if  prop is one of the receivers observed properties"""

        return self.hasObservedPropertyWithIdentifier(prop.identifier)

    def has_same_base_as_experiment(self, otherExperiment: "Experiment"):
        """Returns True if the base experiment is the same as the base experiment of otherExperiment"""

        return self.identifier == otherExperiment.identifier

    def has_same_base_as_experiment_reference(self, reference: "ExperimentReference"):
        """Returns True if the base experiment is the same as the base experiment of reference"""

        return self.identifier == reference.experimentIdentifier

    def experimentProvidesRequirements(
        self, experiment: "Experiment", exactMatch=True
    ) -> bool:
        """Returns True if experiment would measure ALL required observed properties of the receiver

        If the receiver has no required observed properties this method will always return False.

        This method handles required properties that are Observed or Abstract

        params:
            experiment: The experiment to check against
            exactMath: If True `experiment` must provide exactly the same property i.e. matching parameterization.
                If False `experiment` must have the same base experiment.
        """

        retval = True
        if len(self.requiredObservedProperties) == 0:
            retval = False
        else:
            if exactMatch:
                for req in self.requiredObservedProperties:
                    if not experiment.hasObservedProperty(req):
                        retval = False
                        break
            else:
                for input_ref in self.references_of_required_input_experiments:
                    # Compare the supplied experiment to the input ref
                    # If it is not equal to all required input refs then it doesn't provide all requirements
                    if not experiment.reference.compareWithoutParameterization(
                        input_ref
                    ):
                        retval = False
                        break

        return retval

    def virtualObservedPropertyFromIdentifier(
        self, identifier
    ) -> VirtualObservedProperty | None:
        """Returns a list of VirtualObservedProperty instances that could be calculated by the receiver given a virtual property identifier

        A virtual property identifier has two parts - the base property identifier and the aggregation method identifier
        The base property identifier can be the identifier of an ObservedProperty or a target property.
        The aggregation method identifier must be one of the know aggregation method identifiers

        This method finds the observed properties of the receiver that match the base property identifier
        and creates virtual properties for them.
        A single VirtualObservedProperty is created in either case
        If the base property identifier matches a TargetProperty then a VirtualObservedProperty is created
        for each ObservedProperty that has that TargetProperty

        Exceptions:
            Raises ValueError if identifier is not a virtual property identifier

        Returns:
            None if the receiver has no observed or target properties that match the base property ident.
            Otherwise, a list of VirtualObservedProperty instances.
            This list will be of length 1 if the base-property-identifier matches an ObservedProperty.
            If the base property identifier matches a TargetProperty then a VirtualObservedProperty is created
            for each ObservedProperty that has that TargetProperty.

        """

        if not VirtualObservedProperty.isVirtualPropertyIdentifier(identifier):
            raise ValueError(f"{identifier} is not a valid virtual property identifier")

        propertyIdentifier, aggregationMethod = VirtualObservedProperty.parseIdentifier(
            identifier
        )
        aggregationMethod = PropertyAggregationMethod(
            identifier=PropertyAggregationMethodEnum(aggregationMethod)
        )

        # Check if it's an observed property
        ops = [o for o in self.observedProperties if o.identifier == propertyIdentifier]
        if len(ops) > 0:
            # Should only be one observed property with a given identifier
            op = ops[0]
            vp = VirtualObservedProperty(
                baseObservedProperty=op, aggregationMethod=aggregationMethod
            )
            print(vp.identifier, identifier)
            assert vp.identifier == identifier
            retval = vp
        else:
            # Not an observed property - Check if it's a target property
            ops = [
                o
                for o in self.observedProperties
                if o.targetProperty.identifier == propertyIdentifier
            ]
            if len(ops) > 0:
                # Should only be one target property with a given identifier
                op = ops[0]
                vp = VirtualObservedProperty(
                    baseObservedProperty=op, aggregationMethod=aggregationMethod
                )
                assert (
                    vp.baseObservedProperty.targetProperty.identifier
                    == propertyIdentifier
                )
                retval = vp
            else:
                # Not observed or target property - return None
                retval = None

        return retval

    @property
    def requiredConstitutiveProperties(self) -> list[ConstitutiveProperty]:
        """The constitutive properties an entity must have for the experiment to operate on it

        An empty list will be returned if the experiment did not define these.
        In this case you must read the experiment documentation to discover these properties
        """

        return [
            e for e in self.requiredProperties if isinstance(e, ConstitutiveProperty)
        ]

    @property
    def requiredObservedProperties(self) -> list[ObservedProperty]:
        """The observed properties an entity must have measured values for, for the experiment to operate on it

        An empty list will be returned if the experiment does not require any other measured property values.
        """

        return [e for e in self.requiredProperties if isinstance(e, ObservedProperty)]

    @property
    def references_of_required_input_experiments(
        self,
    ) -> set[ExperimentReference]:
        """Returns references to the Experiments, this experiment requires to have been measured on an Entity before it can run"""

        return {op.experimentReference for op in self.requiredObservedProperties}

    def valueForOptionalProperty(
        self, property_identifier: str
    ) -> ConstitutivePropertyValue:
        """Returns the parameterized value of the optional property property_identifier

        Raises:
            ValueError, If property_identifier is not the id of any optionalProperty"""

        values = [
            v
            for v in self.defaultParameterization
            if v.property.identifier == property_identifier
        ]

        # There should be one value - if not there is an error
        if len(values) == 0:
            props = [
                p
                for p in self.optionalProperties
                if p.identifier == property_identifier
            ]
            if len(props) == 0:
                raise ValueError(
                    f"Experiment {self.identifier} has no optional property {property_identifier}."
                    f" Known optional properties: {self.optionalProperties}"
                )
            # pragma: nocover
            raise ValueError(
                f"Experiment {self.identifier} has no value for optional property {property_identifier}."
                f" This is inconsistent as all properties and must have values on construction. "
                f"Known optional properties: {self.optionalProperties}. "
                f"Set default values: {self.defaultParameterization}"
            )

        return values[0]

    def propertyValuesFromEntity(self, entity: "Entity", target=False) -> dict:
        """Given an entity returns the values for the required and optional properties of the Experiment instance

        If a required property is an ObservedProperty it may have multiple values.
        This method will return all values if more than one
        i.e. the value of the property identifier in the returned dictionary will be a list.

        If there is only one value for the property the value of the property identifier in the returned dictionary will be that value

        Parameters:
            entity: An Entity
            target: If True observed properties will be added to a key with the target property name rather than the observed property name.
                e.g. if experiment A measurements property x, then with target=False, the key in the returned dictionary will be A.x
                     if target=True it will be 'x'.
                In the later case if the experiment depends on A.x and B.x both values will be added to 'x'

        Return:
            A dictionary of property identifier: property value pairs

        Raise:
            ValueError: If entity does not have a value for a required property of the Experiment instance
        """

        # 1. Get the values for required properties - these will be constitutive or observed properties of the entity
        identifierValueMap = {}
        for prop in self.requiredProperties:
            if isinstance(prop, ObservedProperty):
                values = entity.valuesForProperty(prop)
                ident = prop.targetProperty.identifier if target else prop.identifier
                if not values:
                    raise ValueError(
                        f"Entity {entity} has no value for required observed property {prop.identifier}"
                    )

                if len(values) > 1:
                    identifierValueMap[ident] = [v.value for v in values]
                else:
                    identifierValueMap[ident] = values[0].value
            else:

                try:
                    identifierValueMap[prop.identifier] = (
                        entity.valueForConstitutivePropertyIdentifier(
                            prop.identifier
                        ).value
                    )
                except AttributeError:
                    raise ValueError(
                        f"Entity {entity} has no value for required constitutive property {prop.identifier}"
                    )

        # 2. Get the values for the optional properties
        # These may be in the Entity (because they were used to define the EntitySpace) or the Experiment
        for optionalProperty in self.optionalProperties:
            # Check if this property was added to the entity space - if it was the Entity value for the property takes precedence
            entityValue = entity.valueForConstitutivePropertyIdentifier(
                optionalProperty.identifier
            )
            if entityValue is not None:
                # Use the Entity value
                identifierValueMap[optionalProperty.identifier] = entityValue.value
            else:
                # Use the parameterized value
                identifierValueMap[optionalProperty.identifier] = (
                    self.valueForOptionalProperty(optionalProperty.identifier).value
                )

        return identifierValueMap


class ParameterizedExperiment(Experiment):
    """Represents an Experiment where default optional parameters have been overridden

    Note: The parameterization cannot be empty or have any values which are the same as default values
    """

    parameterization: list[ConstitutivePropertyValue] = pydantic.Field(
        default=[],
        description="Values for optional properties",
    )
    model_config = ConfigDict(extra="forbid", frozen=True)
    mapping: dict = pydantic.Field(
        description="Private attribute", default={}, exclude=True
    )

    @property
    def parameterizedIdentifier(self) -> str:
        """
        The identifier for the parameterized version of the experiment.
        Different parameterized versions of an experiment have a different parameterized identifier.
        Their experimentIdentifier field, which identifies the base experiment, will be the same.
        """
        if not self.parameterization:
            raise ValueError(
                "Parameterization cannot be empty in a ParameterizedExperiment"
            )

        return identifier_for_parameterized_experiment(
            self.identifier, self.parameterization
        )

    def __eq__(self, other: "ParameterizedExperiment"):
        """ParameterizedExperiments are equal if they have the same parameterizedIdentifier

        A ParameterizedExperiment can only be equal to another ParameterizedExperiment
        A ParameterizedExperiment is not equal to its parent Experiment.
        """

        retval = False
        if isinstance(other, ParameterizedExperiment):
            retval = (self.actuatorIdentifier == other.actuatorIdentifier) and (
                self.parameterizedIdentifier == other.parameterizedIdentifier
            )

        return retval

    def __str__(self):

        return reference_string_from_fields(
            actuator_identifier=self.actuatorIdentifier,
            experiment_identifier=self.parameterizedIdentifier,
        )

    def __hash__(self):

        return hash(str(self))

    def _repr_pretty_(self, p, cycle=False):

        # This should print the parameterized id and base id
        p.text(f"Parameterized Identifier:{self.parameterizedIdentifier}")
        p.break_()
        super()._repr_pretty_(p)

        mapping = {c.identifier: c for c in self.optionalProperties}
        with p.group(2, "Parameterization:"):
            p.break_()
            for value in self.parameterization:
                prop = mapping[value.property.identifier]
                p.pretty(prop)
                p.break_()
                p.text(f"Parameterized value: {value.value}")
                p.break_()
                p.break_()

    @pydantic.field_validator("parameterization")
    def validate_not_empty_parameterization(
        cls, parameterization: list[PropertyValue], values
    ):

        # Check it's not empty - it is raise error as should use ParameterizedExperiment
        assert parameterization, "Custom parameterization cannot be empty"

        # Someone could try to initialize this object with a parameterization
        # but no optionalParameters or defaultParameterization
        # Hence we have to check here
        # We only need to check if one of the two is there as once it is the base
        # class validators will check for the other

        # Check there are optional properties to parameterize
        assert values.data.get(
            "optionalProperties"
        ), "Cannot parameterize an experiment with no optionalProperties"

        return parameterization

    @pydantic.model_validator(mode="after")
    def validate_parameterization(self):

        check_parameterization_validity(
            list(self.optionalProperties), self.parameterization
        )

        defaultParameterizationMap = {
            v.property.identifier: v for v in self.defaultParameterization
        }

        customParameterizationMap = {
            v.property.identifier: v for v in self.parameterization
        }

        # build the mapping private var
        for p in self.optionalProperties:
            customValue = customParameterizationMap.get(p.identifier)
            self.mapping[p.identifier] = (
                customValue
                if customValue is not None
                else defaultParameterizationMap[p.identifier]
            )

        # Now check that none of the parameterized values are the same as the defaults
        for v in self.defaultParameterization:
            if customParameterizationMap.get(v.property.identifier):
                assert (
                    v.value != customParameterizationMap[v.property.identifier].value
                ), f"Default value {v.value} for property {v.property.identifier} is the same as the custom value, { customParameterizationMap[v.property.identifier].value}"

        # Finally update identifier

        return self

    @property
    def reference(self) -> ExperimentReference:

        return ExperimentReference(
            experimentIdentifier=self.identifier,
            actuatorIdentifier=self.actuatorIdentifier,
            parameterization=self.parameterization,
        )

    def valueForOptionalProperty(
        self, property_identifier
    ) -> ConstitutivePropertyValue:
        """Returns the parameterized value of the optional property property_identifier

        Raises:
            ValueError, If property_identifier is not the id of any optionalProperty"""

        try:
            retval = self.mapping[property_identifier]
        except KeyError:
            raise ValueError(
                f"No optional property called {property_identifier}. Known optional properties {self.optionalProperties}"
            )

        return retval


def experiment_type_discriminator(experiment):

    if isinstance(experiment, ParameterizedExperiment):
        return "Parameterized"
    if isinstance(experiment, Experiment):
        return "Base"
    if isinstance(experiment, dict):
        if experiment.get("parameterization", None):
            return "Parameterized"
        return "Base"

    raise ValueError(
        f"Unable to determine experiment type for experiment: {experiment}"
    )


ExperimentType = Annotated[
    Annotated[Experiment, pydantic.Tag("Base")]
    | Annotated[ParameterizedExperiment, pydantic.Tag("Parameterized")],
    pydantic.Discriminator(experiment_type_discriminator),
]
