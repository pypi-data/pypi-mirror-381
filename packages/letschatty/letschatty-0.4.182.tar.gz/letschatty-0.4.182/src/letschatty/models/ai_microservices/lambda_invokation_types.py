from enum import StrEnum
from pydantic import BaseModel

class InvokationType(StrEnum):
    INCOMING_MESSAGE = "incoming_message"
    FOLLOW_UP = "follow_up"
    SINGLE_QUALITY_TEST = "single_quality_test"
    ALL_QUALITY_TEST = "all_quality_test"
    SMART_TAGGING = "smart_tagging"
    QUALITY_TEST_INTERACTION = "quality_test_interaction"

class Operation(StrEnum):
    RUN = "run"
    CALLBACK = "callback"

class LambdaAiEvent(BaseModel):
    type: InvokationType
    operation: Operation
    data: dict
