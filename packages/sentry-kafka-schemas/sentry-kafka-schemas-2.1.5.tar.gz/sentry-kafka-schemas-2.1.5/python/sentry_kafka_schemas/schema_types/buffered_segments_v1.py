from typing import Literal, Dict, TypedDict, Any, Union, Required, List


class BufferedSegment(TypedDict, total=False):
    """ buffered_segment. """

    spans: Required["_SegmentSpans"]
    """
    minItems: 1

    Required property
    """



class SpanEvent(TypedDict, total=False):
    """ span_event. """

    event_id: "_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUuid"
    """
    minLength: 32
    maxLength: 36
    """

    organization_id: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUint"]
    """
    minimum: 0

    Required property
    """

    project_id: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUint"]
    """
    minimum: 0

    Required property
    """

    key_id: "_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUint"
    """ minimum: 0 """

    trace_id: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUuid"]
    """
    minLength: 32
    maxLength: 36

    Required property
    """

    span_id: Required[str]
    """
    The span ID is a unique identifier for a span within a trace. It is an 8 byte hexadecimal string.

    Required property
    """

    parent_span_id: Union[str, None]
    """ The parent span ID is the ID of the span that caused this span. It is an 8 byte hexadecimal string. """

    start_timestamp: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsPositivefloat"]
    """
    minimum: 0

    Required property
    """

    end_timestamp: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsPositivefloat"]
    """
    minimum: 0

    Required property
    """

    retention_days: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUint16"]
    """
    minimum: 0
    maximum: 65535

    Required property
    """

    downsampled_retention_days: "_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUint16"
    """
    minimum: 0
    maximum: 65535
    """

    received: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsPositivefloat"]
    """
    minimum: 0

    Required property
    """

    name: Required[str]
    """ Required property """

    status: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpanstatus"]
    """ Required property """

    is_remote: Required[bool]
    """ Required property """

    kind: "_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpankind"
    links: List["SpanLink"]
    attributes: Dict[str, "_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalue"]


class SpanLink(TypedDict, total=False):
    """ span_link. """

    trace_id: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUuid"]
    """
    minLength: 32
    maxLength: 36

    Required property
    """

    span_id: Required[str]
    """ Required property """

    attributes: Dict[str, "_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalue"]
    sampled: bool


class _FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalue(TypedDict, total=False):
    type: Required["_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalueType"]
    """ Required property """

    value: Required[Union[Union[int, float], None, str, bool, List[Any], Dict[str, Any]]]
    """ Required property """



_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalueType = Union[Literal['boolean'], Literal['integer'], Literal['double'], Literal['string'], Literal['array'], Literal['object']]
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSATTRIBUTEVALUETYPE_BOOLEAN: Literal['boolean'] = "boolean"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalueType' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSATTRIBUTEVALUETYPE_INTEGER: Literal['integer'] = "integer"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalueType' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSATTRIBUTEVALUETYPE_DOUBLE: Literal['double'] = "double"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalueType' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSATTRIBUTEVALUETYPE_STRING: Literal['string'] = "string"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalueType' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSATTRIBUTEVALUETYPE_ARRAY: Literal['array'] = "array"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalueType' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSATTRIBUTEVALUETYPE_OBJECT: Literal['object'] = "object"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsAttributevalueType' enum"""



_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsPositivefloat = Union[int, float]
""" minimum: 0 """



_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpankind = Union[Literal['internal'], Literal['server'], Literal['client'], Literal['producer'], Literal['consumer']]
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSSPANKIND_INTERNAL: Literal['internal'] = "internal"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpankind' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSSPANKIND_SERVER: Literal['server'] = "server"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpankind' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSSPANKIND_CLIENT: Literal['client'] = "client"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpankind' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSSPANKIND_PRODUCER: Literal['producer'] = "producer"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpankind' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSSPANKIND_CONSUMER: Literal['consumer'] = "consumer"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpankind' enum"""



_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpanstatus = Union[Literal['ok'], Literal['error']]
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSSPANSTATUS_OK: Literal['ok'] = "ok"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpanstatus' enum"""
_FILECOLONINGESTSPANSFULLSTOPV1FULLSTOPSCHEMAFULLSTOPJSONNUMBERSIGNDEFINITIONSSPANSTATUS_ERROR: Literal['error'] = "error"
"""The values for the '_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsSpanstatus' enum"""



_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUint = int
""" minimum: 0 """



_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUint16 = int
"""
minimum: 0
maximum: 65535
"""



_FileColonIngestSpansFullStopV1FullStopSchemaFullStopJsonNumberSignDefinitionsUuid = str
"""
minLength: 32
maxLength: 36
"""



_SegmentSpans = List["SpanEvent"]
""" minItems: 1 """

