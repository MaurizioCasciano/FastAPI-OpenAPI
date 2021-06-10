# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/oasis-open/cti-stix2-json-schemas/master/schemas/sdos/attack-pattern.json
#   timestamp: 2021-06-10T13:29:34+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field


class Type(Enum):
    """
    The type of this object, which MUST be the literal `attack-pattern`.
    """

    attack_pattern = 'attack-pattern'


class SpecVersion(Enum):
    """
    The version of the STIX specification used to represent this object.
    """

    field_2_0 = '2.0'
    field_2_1 = '2.1'


class Properties(BaseModel):
    __root__: Any = Field(
        ...,
        _schema='http://json-schema.org/draft-07/schema#',
        description='Rules for custom properties',
        patternProperties={
            '^[a-z][a-z0-9_]{0,245}_bin$': {'$ref': '../common/binary.json'},
            '^[a-z][a-z0-9_]{0,245}_hex$': {'$ref': '../common/hex.json'},
            '^([a-z][a-z0-9_]{2,249})|id$': {
                'anyOf': [
                    {'type': 'array', 'minItems': 1},
                    {'type': 'string'},
                    {'type': 'integer'},
                    {'type': 'boolean'},
                    {'type': 'number'},
                    {'type': 'object'},
                ]
            },
        },
        title='properties',
    )


class Identifier(BaseModel):
    __root__: str = Field(
        ...,
        _schema='http://json-schema.org/draft-07/schema#',
        description='Represents identifiers across the CTI specifications. The format consists of the name of the top-level object being identified, followed by two dashes (--), followed by a UUIDv4.',
        regex='^[a-z][a-z0-9-]+[a-z0-9]--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',
        title='identifier',
    )


class Timestamp(BaseModel):
    __root__: str = Field(
        ...,
        _schema='http://json-schema.org/draft-07/schema#',
        description="Represents timestamps across the CTI specifications. The format is an RFC3339 timestamp, with a required timezone specification of 'Z'.",
        regex='^[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\\.[0-9]+)?Z$',
        title='timestamp',
    )


class ExternalReferenceItem(BaseModel):
    source_name: str = Field(
        ...,
        description='The source within which the external-reference is defined (system, registry, organization, etc.)',
        regex='^cve$',
    )
    external_id: str = Field(
        ...,
        description='An identifier for the external reference content.',
        regex='^CVE-\\d{4}-(0\\d{3}|[1-9]\\d{3,})$',
    )


class ExternalReferenceItem1(BaseModel):
    source_name: str = Field(
        ...,
        description='The source within which the external-reference is defined (system, registry, organization, etc.)',
        regex='^capec$',
    )
    external_id: str = Field(
        ...,
        description='An identifier for the external reference content.',
        regex='^CAPEC-\\d+$',
    )


class UrlRegex(BaseModel):
    __root__: AnyUrl = Field(
        ...,
        _schema='http://json-schema.org/draft-07/schema#',
        description='Matches a URI according to RFC 3986.',
        title='url-regex',
    )


class Dictionary(BaseModel):
    """
    A dictionary captures a set of key/value pairs
    """

    pass


class Selector(BaseModel):
    __root__: str = Field(
        ..., regex='^([a-z0-9_-]{3,249}(\\.(\\[\\d+\\]|[a-z0-9_-]{1,250}))*|id)$'
    )


class GranularMarking(BaseModel):
    """
    The granular-marking type defines how the list of marking-definition objects referenced by the marking_refs property to apply to a set of content identified by the list of selectors in the selectors property.
    """

    selectors: List[Selector] = Field(
        ...,
        description='A list of selectors for content contained within the STIX object in which this property appears.',
        min_items=1,
    )
    lang: Optional[str] = Field(
        None,
        description='Identifies the language of the text identified by this marking.',
    )
    marking_ref: Identifier


class KillChainPhase(BaseModel):
    """
    The kill-chain-phase represents a phase in a kill chain.
    """

    kill_chain_name: str = Field(..., description='The name of the kill chain.')
    phase_name: str = Field(..., description='The name of the phase in the kill chain.')


class HashesType(Dictionary):
    """
    The Hashes type represents one or more cryptographic hashes, as a special set of key/value pairs
    """

    pass


class ExternalReference1(BaseModel):
    """
    External references are used to describe pointers to information represented outside of STIX.
    """

    description: Optional[str] = Field(None, description='A human readable description')
    url: Optional[UrlRegex] = Field(
        None, description='A URL reference to an external resource.'
    )
    hashes: Optional[HashesType] = Field(
        None, description='Specifies a dictionary of hashes for the file.'
    )


class ExternalReference(BaseModel):
    __root__: Union[
        ExternalReference1,
        ExternalReferenceItem,
        ExternalReferenceItem1,
        Union[Any, Any, Any],
    ] = Field(
        ...,
        _schema='http://json-schema.org/draft-07/schema#',
        description='External references are used to describe pointers to information represented outside of STIX.',
        title='external-reference',
    )


class Core:
    """
    Common properties and behavior across all STIX Domain Objects and STIX Relationship Objects.
    """

    type: str = Field(
        ...,
        description='The type property identifies the type of STIX Object (SDO, Relationship Object, etc). The value of the type field MUST be one of the types defined by a STIX Object (e.g., indicator).',
        max_length=250,
        min_length=3,
        not_={'enum': ['action']},
        regex='^([a-z][a-z0-9]*)+(-[a-z0-9]+)*\\-?$',
        title='type',
    )
    spec_version: SpecVersion = Field(
        ...,
        description='The version of the STIX specification used to represent this object.',
    )
    id: Identifier = Field(
        ...,
        description='The id property universally and uniquely identifies this object.',
    )
    created_by_ref: Optional[Identifier] = Field(
        None,
        description='The ID of the Source object that describes who created this object.',
    )
    labels: Optional[List[str]] = Field(
        None,
        description='The labels property specifies a set of terms used to describe this object.',
        min_items=1,
    )
    created: Timestamp = Field(
        ...,
        description='The created property represents the time at which the first version of this object was created. The timstamp value MUST be precise to the nearest millisecond.',
    )
    modified: Timestamp = Field(
        ...,
        description='The modified property represents the time that this particular version of the object was modified. The timstamp value MUST be precise to the nearest millisecond.',
    )
    revoked: Optional[bool] = Field(
        None,
        description='The revoked property indicates whether the object has been revoked.',
    )
    confidence: Optional[int] = Field(
        None,
        description='Identifies the confidence that the creator has in the correctness of their data.',
        ge=0.0,
        le=100.0,
    )
    lang: Optional[str] = Field(
        None, description='Identifies the language of the text content in this object.'
    )
    external_references: Optional[List[ExternalReference]] = Field(
        None,
        description='A list of external references which refers to non-STIX information.',
        min_items=1,
    )
    object_marking_refs: Optional[List[Identifier]] = Field(
        None,
        description='The list of marking-definition objects to be applied to this object.',
        min_items=1,
    )
    granular_markings: Optional[List[GranularMarking]] = Field(
        None,
        description='The set of granular markings that apply to this object.',
        min_items=1,
    )
    extensions: Optional[Dict[str, Any]] = Field(
        None,
        description='Specifies any extensions of the object, as a dictionary.',
        minProperties=1,
        patternProperties={
            '^extension-definition--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$': {
                'allOf': [{'$ref': '../common/extension.json'}]
            }
        },
    )


class AttackPatternDTO(Core):
    """
    Attack Patterns are a type of TTP that describe ways that adversaries attempt to compromise targets.
    """

    type: Optional[Type] = Field(
        None,
        description='The type of this object, which MUST be the literal `attack-pattern`.',
    )
    aliases: Optional[List[str]] = Field(
        None, description='Alternative names used to identify this Attack Pattern.'
    )
    id: Optional[Any] = Field(None, regex='^attack-pattern--', title='id')
    name: Optional[str] = Field(
        None, description='The name used to identify the Attack Pattern.'
    )
    description: Optional[str] = Field(
        None,
        description='A description that provides more details and context about the Attack Pattern, potentially including its purpose and its key characteristics.',
    )
    kill_chain_phases: Optional[List[KillChainPhase]] = Field(
        None,
        description='The list of kill chain phases for which this attack pattern is used.',
        min_items=1,
    )