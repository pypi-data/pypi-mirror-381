from pydantic import BaseModel, Field
from typing import Dict, Any

from letschatty.models.utils.types.identifier import StrObjectId
from .lambda_invokation_types import InvokationType, Operation, LambdaAiEvent
from .expected_output import ExpectedOutputSmartTag, ExpectedOutputQualityTest
from ...models.company.assets.ai_agents_v2.ai_agents_decision_output import IncomingMessageDecisionAction

class SmartTaggingCallbackMetadata(BaseModel):
    chat_id: StrObjectId
    company_id: StrObjectId

class ComparisonAnalysisCallbackMetadata(BaseModel):
    test_case_id: StrObjectId
    company_id : StrObjectId

class InteractionCallbackMetadata(BaseModel):
    test_case_id: StrObjectId
    chat_example_id: StrObjectId
    ai_agent_id: StrObjectId
    company_id: StrObjectId
    interaction_index: int

class IncomingMessageCallbackEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.INCOMING_MESSAGE
    operation: Operation = Operation.CALLBACK
    data: IncomingMessageDecisionAction
    callback_metadata: Dict[str, Any] = Field(default_factory=dict)

class QualityTestCallbackEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.SINGLE_QUALITY_TEST
    operation: Operation = Operation.CALLBACK
    data: ExpectedOutputQualityTest
    callback_metadata: ComparisonAnalysisCallbackMetadata

class QualityTestInteractionCallbackEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.QUALITY_TEST_INTERACTION
    operation: Operation = Operation.CALLBACK
    data: IncomingMessageDecisionAction
    callback_metadata: InteractionCallbackMetadata

class SmartTaggingCallbackEvent(LambdaAiEvent):
    type: InvokationType = InvokationType.SMART_TAGGING
    operation: Operation = Operation.CALLBACK
    data: ExpectedOutputSmartTag
    callback_metadata: SmartTaggingCallbackMetadata
