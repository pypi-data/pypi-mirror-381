from pydantic import BaseModel
from letschatty.models.ai_microservices.lambda_invokation_types import InvokationType, Operation, LambdaAiEvent
from letschatty.models.utils.types import StrObjectId

class ChatData(BaseModel):
    chat_id: StrObjectId
    company_id: StrObjectId

class IncomingMessageEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.INCOMING_MESSAGE
    operation: Operation = Operation.RUN
    data: ChatData

class FollowUpEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.FOLLOW_UP
    operation: Operation = Operation.RUN
    data: ChatData

class QualityTestEventData(BaseModel):
    chat_example_id: StrObjectId
    company_id: StrObjectId
    ai_agent_id: StrObjectId

class QualityTestEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.SINGLE_QUALITY_TEST
    operation: Operation = Operation.RUN
    data: QualityTestEventData

class AllQualityTestEventData(BaseModel):
    company_id: StrObjectId
    ai_agent_id: StrObjectId

class AllQualityTestEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.ALL_QUALITY_TEST
    operation: Operation = Operation.RUN
    data: AllQualityTestEventData

class SmartTaggingEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.SMART_TAGGING
    operation: Operation = Operation.RUN
    data: ChatData
