from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AcceptEula = bool
AccountId = str
AdditionalModelRequestFieldsKey = str
Arn = str
AutomatedReasoningCheckTranslationConfidence = float
AutomatedReasoningConfidenceFilterThreshold = float
AutomatedReasoningLogicStatementContent = str
AutomatedReasoningNaturalLanguageStatementContent = str
AutomatedReasoningPolicyAnnotationFeedbackNaturalLanguage = str
AutomatedReasoningPolicyAnnotationIngestContent = str
AutomatedReasoningPolicyAnnotationRuleNaturalLanguage = str
AutomatedReasoningPolicyArn = str
AutomatedReasoningPolicyBuildDocumentDescription = str
AutomatedReasoningPolicyBuildDocumentName = str
AutomatedReasoningPolicyBuildWorkflowId = str
AutomatedReasoningPolicyDefinitionRuleAlternateExpression = str
AutomatedReasoningPolicyDefinitionRuleExpression = str
AutomatedReasoningPolicyDefinitionRuleId = str
AutomatedReasoningPolicyDefinitionTypeDescription = str
AutomatedReasoningPolicyDefinitionTypeName = str
AutomatedReasoningPolicyDefinitionTypeValueDescription = str
AutomatedReasoningPolicyDefinitionTypeValueName = str
AutomatedReasoningPolicyDefinitionVariableDescription = str
AutomatedReasoningPolicyDefinitionVariableName = str
AutomatedReasoningPolicyDescription = str
AutomatedReasoningPolicyFormatVersion = str
AutomatedReasoningPolicyHash = str
AutomatedReasoningPolicyId = str
AutomatedReasoningPolicyName = str
AutomatedReasoningPolicyScenarioAlternateExpression = str
AutomatedReasoningPolicyScenarioExpression = str
AutomatedReasoningPolicyTestCaseId = str
AutomatedReasoningPolicyTestGuardContent = str
AutomatedReasoningPolicyTestQueryContent = str
AutomatedReasoningPolicyVersion = str
BaseModelIdentifier = str
BedrockModelArn = str
BedrockModelId = str
BedrockRerankingModelArn = str
Boolean = bool
BrandedName = str
BucketName = str
ContentType = str
CustomMetricInstructions = str
CustomModelArn = str
CustomModelDeploymentArn = str
CustomModelDeploymentDescription = str
CustomModelDeploymentIdentifier = str
CustomModelName = str
CustomModelUnitsVersion = str
EndpointName = str
ErrorMessage = str
EvaluationBedrockModelIdentifier = str
EvaluationDatasetName = str
EvaluationJobArn = str
EvaluationJobDescription = str
EvaluationJobIdentifier = str
EvaluationJobName = str
EvaluationMetricDescription = str
EvaluationMetricName = str
EvaluationModelInferenceParams = str
EvaluationPrecomputedInferenceSourceIdentifier = str
EvaluationPrecomputedRagSourceIdentifier = str
EvaluationRatingMethod = str
EvaluatorModelIdentifier = str
FieldForRerankingFieldNameString = str
FilterKey = str
Float = float
FoundationModelArn = str
GuardrailArn = str
GuardrailBlockedMessaging = str
GuardrailConfigurationGuardrailIdString = str
GuardrailConfigurationGuardrailVersionString = str
GuardrailContextualGroundingFilterConfigThresholdDouble = float
GuardrailContextualGroundingFilterThresholdDouble = float
GuardrailCrossRegionGuardrailProfileArn = str
GuardrailCrossRegionGuardrailProfileId = str
GuardrailCrossRegionGuardrailProfileIdentifier = str
GuardrailDescription = str
GuardrailDraftVersion = str
GuardrailFailureRecommendation = str
GuardrailId = str
GuardrailIdentifier = str
GuardrailName = str
GuardrailNumericalVersion = str
GuardrailRegexConfigDescriptionString = str
GuardrailRegexConfigNameString = str
GuardrailRegexConfigPatternString = str
GuardrailRegexDescriptionString = str
GuardrailRegexNameString = str
GuardrailRegexPatternString = str
GuardrailStatusReason = str
GuardrailTopicDefinition = str
GuardrailTopicExample = str
GuardrailTopicName = str
GuardrailVersion = str
GuardrailWordConfigTextString = str
GuardrailWordTextString = str
HumanTaskInstructions = str
IdempotencyToken = str
Identifier = str
ImportedModelArn = str
ImportedModelIdentifier = str
ImportedModelName = str
InferenceProfileArn = str
InferenceProfileDescription = str
InferenceProfileId = str
InferenceProfileIdentifier = str
InferenceProfileModelSourceArn = str
InferenceProfileName = str
InstanceCount = int
InstanceType = str
InstructSupported = bool
Integer = int
JobName = str
KeyPrefix = str
KmsKeyArn = str
KmsKeyId = str
KnowledgeBaseId = str
KnowledgeBaseVectorSearchConfigurationNumberOfResultsInteger = int
LogGroupName = str
MaxResults = int
MaxTokens = int
Message = str
MetadataAttributeSchemaDescriptionString = str
MetadataAttributeSchemaKeyString = str
MetricFloat = float
MetricName = str
ModelArchitecture = str
ModelArn = str
ModelCopyJobArn = str
ModelCustomizationJobArn = str
ModelCustomizationJobIdentifier = str
ModelDeploymentName = str
ModelId = str
ModelIdentifier = str
ModelImportJobArn = str
ModelImportJobIdentifier = str
ModelInvocationIdempotencyToken = str
ModelInvocationJobArn = str
ModelInvocationJobIdentifier = str
ModelInvocationJobName = str
ModelInvocationJobTimeoutDurationInHours = int
ModelName = str
ModelSourceIdentifier = str
NonBlankString = str
OfferId = str
OfferToken = str
PaginationToken = str
PositiveInteger = int
PromptRouterArn = str
PromptRouterDescription = str
PromptRouterName = str
PromptRouterTargetModelArn = str
Provider = str
ProvisionedModelArn = str
ProvisionedModelId = str
ProvisionedModelName = str
RAGStopSequencesMemberString = str
RatingScaleItemDefinition = str
RatingScaleItemValueStringValueString = str
RequestMetadataMapKeyString = str
RequestMetadataMapValueString = str
RoleArn = str
RoutingCriteriaResponseQualityDifferenceDouble = float
S3Uri = str
SageMakerFlowDefinitionArn = str
SecurityGroupId = str
String = str
SubnetId = str
TagKey = str
TagValue = str
TaggableResourcesArn = str
TeacherModelIdentifier = str
Temperature = float
TextPromptTemplate = str
TopP = float
UsePromptResponse = bool
VectorSearchBedrockRerankingConfigurationNumberOfRerankedResultsInteger = int
kBS3Uri = str


class AgreementStatus(StrEnum):
    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    ERROR = "ERROR"


class ApplicationType(StrEnum):
    ModelEvaluation = "ModelEvaluation"
    RagEvaluation = "RagEvaluation"


class AttributeType(StrEnum):
    STRING = "STRING"
    NUMBER = "NUMBER"
    BOOLEAN = "BOOLEAN"
    STRING_LIST = "STRING_LIST"


class AuthorizationStatus(StrEnum):
    AUTHORIZED = "AUTHORIZED"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"


class AutomatedReasoningCheckLogicWarningType(StrEnum):
    ALWAYS_TRUE = "ALWAYS_TRUE"
    ALWAYS_FALSE = "ALWAYS_FALSE"


class AutomatedReasoningCheckResult(StrEnum):
    VALID = "VALID"
    INVALID = "INVALID"
    SATISFIABLE = "SATISFIABLE"
    IMPOSSIBLE = "IMPOSSIBLE"
    TRANSLATION_AMBIGUOUS = "TRANSLATION_AMBIGUOUS"
    TOO_COMPLEX = "TOO_COMPLEX"
    NO_TRANSLATION = "NO_TRANSLATION"


class AutomatedReasoningPolicyAnnotationStatus(StrEnum):
    APPLIED = "APPLIED"
    FAILED = "FAILED"


class AutomatedReasoningPolicyBuildDocumentContentType(StrEnum):
    pdf = "pdf"
    txt = "txt"


class AutomatedReasoningPolicyBuildMessageType(StrEnum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class AutomatedReasoningPolicyBuildResultAssetType(StrEnum):
    BUILD_LOG = "BUILD_LOG"
    QUALITY_REPORT = "QUALITY_REPORT"
    POLICY_DEFINITION = "POLICY_DEFINITION"


class AutomatedReasoningPolicyBuildWorkflowStatus(StrEnum):
    SCHEDULED = "SCHEDULED"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    PREPROCESSING = "PREPROCESSING"
    BUILDING = "BUILDING"
    TESTING = "TESTING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class AutomatedReasoningPolicyBuildWorkflowType(StrEnum):
    INGEST_CONTENT = "INGEST_CONTENT"
    REFINE_POLICY = "REFINE_POLICY"
    IMPORT_POLICY = "IMPORT_POLICY"


class AutomatedReasoningPolicyTestRunResult(StrEnum):
    PASSED = "PASSED"
    FAILED = "FAILED"


class AutomatedReasoningPolicyTestRunStatus(StrEnum):
    NOT_STARTED = "NOT_STARTED"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class CommitmentDuration(StrEnum):
    OneMonth = "OneMonth"
    SixMonths = "SixMonths"


class CustomModelDeploymentStatus(StrEnum):
    Creating = "Creating"
    Active = "Active"
    Failed = "Failed"


class CustomizationType(StrEnum):
    FINE_TUNING = "FINE_TUNING"
    CONTINUED_PRE_TRAINING = "CONTINUED_PRE_TRAINING"
    DISTILLATION = "DISTILLATION"
    IMPORTED = "IMPORTED"


class EntitlementAvailability(StrEnum):
    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class EvaluationJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"
    Deleting = "Deleting"


class EvaluationJobType(StrEnum):
    Human = "Human"
    Automated = "Automated"


class EvaluationTaskType(StrEnum):
    Summarization = "Summarization"
    Classification = "Classification"
    QuestionAndAnswer = "QuestionAndAnswer"
    Generation = "Generation"
    Custom = "Custom"


class ExternalSourceType(StrEnum):
    S3 = "S3"
    BYTE_CONTENT = "BYTE_CONTENT"


class FineTuningJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class FoundationModelLifecycleStatus(StrEnum):
    ACTIVE = "ACTIVE"
    LEGACY = "LEGACY"


class GuardrailContentFilterAction(StrEnum):
    BLOCK = "BLOCK"
    NONE = "NONE"


class GuardrailContentFilterType(StrEnum):
    SEXUAL = "SEXUAL"
    VIOLENCE = "VIOLENCE"
    HATE = "HATE"
    INSULTS = "INSULTS"
    MISCONDUCT = "MISCONDUCT"
    PROMPT_ATTACK = "PROMPT_ATTACK"


class GuardrailContentFiltersTierName(StrEnum):
    CLASSIC = "CLASSIC"
    STANDARD = "STANDARD"


class GuardrailContextualGroundingAction(StrEnum):
    BLOCK = "BLOCK"
    NONE = "NONE"


class GuardrailContextualGroundingFilterType(StrEnum):
    GROUNDING = "GROUNDING"
    RELEVANCE = "RELEVANCE"


class GuardrailFilterStrength(StrEnum):
    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class GuardrailManagedWordsType(StrEnum):
    PROFANITY = "PROFANITY"


class GuardrailModality(StrEnum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"


class GuardrailPiiEntityType(StrEnum):
    ADDRESS = "ADDRESS"
    AGE = "AGE"
    AWS_ACCESS_KEY = "AWS_ACCESS_KEY"
    AWS_SECRET_KEY = "AWS_SECRET_KEY"
    CA_HEALTH_NUMBER = "CA_HEALTH_NUMBER"
    CA_SOCIAL_INSURANCE_NUMBER = "CA_SOCIAL_INSURANCE_NUMBER"
    CREDIT_DEBIT_CARD_CVV = "CREDIT_DEBIT_CARD_CVV"
    CREDIT_DEBIT_CARD_EXPIRY = "CREDIT_DEBIT_CARD_EXPIRY"
    CREDIT_DEBIT_CARD_NUMBER = "CREDIT_DEBIT_CARD_NUMBER"
    DRIVER_ID = "DRIVER_ID"
    EMAIL = "EMAIL"
    INTERNATIONAL_BANK_ACCOUNT_NUMBER = "INTERNATIONAL_BANK_ACCOUNT_NUMBER"
    IP_ADDRESS = "IP_ADDRESS"
    LICENSE_PLATE = "LICENSE_PLATE"
    MAC_ADDRESS = "MAC_ADDRESS"
    NAME = "NAME"
    PASSWORD = "PASSWORD"
    PHONE = "PHONE"
    PIN = "PIN"
    SWIFT_CODE = "SWIFT_CODE"
    UK_NATIONAL_HEALTH_SERVICE_NUMBER = "UK_NATIONAL_HEALTH_SERVICE_NUMBER"
    UK_NATIONAL_INSURANCE_NUMBER = "UK_NATIONAL_INSURANCE_NUMBER"
    UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER = "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER"
    URL = "URL"
    USERNAME = "USERNAME"
    US_BANK_ACCOUNT_NUMBER = "US_BANK_ACCOUNT_NUMBER"
    US_BANK_ROUTING_NUMBER = "US_BANK_ROUTING_NUMBER"
    US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER = "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER"
    US_PASSPORT_NUMBER = "US_PASSPORT_NUMBER"
    US_SOCIAL_SECURITY_NUMBER = "US_SOCIAL_SECURITY_NUMBER"
    VEHICLE_IDENTIFICATION_NUMBER = "VEHICLE_IDENTIFICATION_NUMBER"


class GuardrailSensitiveInformationAction(StrEnum):
    BLOCK = "BLOCK"
    ANONYMIZE = "ANONYMIZE"
    NONE = "NONE"


class GuardrailStatus(StrEnum):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    VERSIONING = "VERSIONING"
    READY = "READY"
    FAILED = "FAILED"
    DELETING = "DELETING"


class GuardrailTopicAction(StrEnum):
    BLOCK = "BLOCK"
    NONE = "NONE"


class GuardrailTopicType(StrEnum):
    DENY = "DENY"


class GuardrailTopicsTierName(StrEnum):
    CLASSIC = "CLASSIC"
    STANDARD = "STANDARD"


class GuardrailWordAction(StrEnum):
    BLOCK = "BLOCK"
    NONE = "NONE"


class InferenceProfileStatus(StrEnum):
    ACTIVE = "ACTIVE"


class InferenceProfileType(StrEnum):
    SYSTEM_DEFINED = "SYSTEM_DEFINED"
    APPLICATION = "APPLICATION"


class InferenceType(StrEnum):
    ON_DEMAND = "ON_DEMAND"
    PROVISIONED = "PROVISIONED"


class JobStatusDetails(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Stopping = "Stopping"
    Stopped = "Stopped"
    Failed = "Failed"
    NotStarted = "NotStarted"


class ModelCopyJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"


class ModelCustomization(StrEnum):
    FINE_TUNING = "FINE_TUNING"
    CONTINUED_PRE_TRAINING = "CONTINUED_PRE_TRAINING"
    DISTILLATION = "DISTILLATION"


class ModelCustomizationJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class ModelImportJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"


class ModelInvocationJobStatus(StrEnum):
    Submitted = "Submitted"
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"
    PartiallyCompleted = "PartiallyCompleted"
    Expired = "Expired"
    Validating = "Validating"
    Scheduled = "Scheduled"


class ModelModality(StrEnum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    EMBEDDING = "EMBEDDING"


class ModelStatus(StrEnum):
    Active = "Active"
    Creating = "Creating"
    Failed = "Failed"


class OfferType(StrEnum):
    ALL = "ALL"
    PUBLIC = "PUBLIC"


class PerformanceConfigLatency(StrEnum):
    standard = "standard"
    optimized = "optimized"


class PromptRouterStatus(StrEnum):
    AVAILABLE = "AVAILABLE"


class PromptRouterType(StrEnum):
    custom = "custom"
    default = "default"


class ProvisionedModelStatus(StrEnum):
    Creating = "Creating"
    InService = "InService"
    Updating = "Updating"
    Failed = "Failed"


class QueryTransformationType(StrEnum):
    QUERY_DECOMPOSITION = "QUERY_DECOMPOSITION"


class RegionAvailability(StrEnum):
    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class RerankingMetadataSelectionMode(StrEnum):
    SELECTIVE = "SELECTIVE"
    ALL = "ALL"


class RetrieveAndGenerateType(StrEnum):
    KNOWLEDGE_BASE = "KNOWLEDGE_BASE"
    EXTERNAL_SOURCES = "EXTERNAL_SOURCES"


class S3InputFormat(StrEnum):
    JSONL = "JSONL"


class SearchType(StrEnum):
    HYBRID = "HYBRID"
    SEMANTIC = "SEMANTIC"


class SortByProvisionedModels(StrEnum):
    CreationTime = "CreationTime"


class SortJobsBy(StrEnum):
    CreationTime = "CreationTime"


class SortModelsBy(StrEnum):
    CreationTime = "CreationTime"


class SortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class Status(StrEnum):
    REGISTERED = "REGISTERED"
    INCOMPATIBLE_ENDPOINT = "INCOMPATIBLE_ENDPOINT"


class VectorSearchRerankingConfigurationType(StrEnum):
    BEDROCK_RERANKING_MODEL = "BEDROCK_RERANKING_MODEL"


class AccessDeniedException(ServiceException):
    """The request is denied because of missing access permissions."""

    code: str = "AccessDeniedException"
    sender_fault: bool = True
    status_code: int = 403


class ConflictException(ServiceException):
    """Error occurred because of a conflict while performing an operation."""

    code: str = "ConflictException"
    sender_fault: bool = True
    status_code: int = 400


class InternalServerException(ServiceException):
    """An internal server error occurred. Retry your request."""

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 500


class ResourceInUseException(ServiceException):
    """Thrown when attempting to delete or modify a resource that is currently
    being used by other resources or operations. For example, trying to
    delete an Automated Reasoning policy that is referenced by an active
    guardrail.
    """

    code: str = "ResourceInUseException"
    sender_fault: bool = True
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """The specified resource Amazon Resource Name (ARN) was not found. Check
    the Amazon Resource Name (ARN) and try your request again.
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = True
    status_code: int = 404


class ServiceQuotaExceededException(ServiceException):
    """The number of requests exceeds the service quota. Resubmit your request
    later.
    """

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = True
    status_code: int = 400


class ServiceUnavailableException(ServiceException):
    """Returned if the service cannot complete the request."""

    code: str = "ServiceUnavailableException"
    sender_fault: bool = False
    status_code: int = 503


class ThrottlingException(ServiceException):
    """The number of requests exceeds the limit. Resubmit your request later."""

    code: str = "ThrottlingException"
    sender_fault: bool = True
    status_code: int = 429


class TooManyTagsException(ServiceException):
    """The request contains more tags than can be associated with a resource
    (50 tags per resource). The maximum number of tags includes both
    existing tags and those included in your current request.
    """

    code: str = "TooManyTagsException"
    sender_fault: bool = True
    status_code: int = 400
    resourceName: Optional[TaggableResourcesArn]


class ValidationException(ServiceException):
    """Input validation failed. Check your request parameters and retry the
    request.
    """

    code: str = "ValidationException"
    sender_fault: bool = True
    status_code: int = 400


AcknowledgementFormDataBody = bytes


class AdditionalModelRequestFieldsValue(TypedDict, total=False):
    pass


AdditionalModelRequestFields = Dict[
    AdditionalModelRequestFieldsKey, AdditionalModelRequestFieldsValue
]


class AgreementAvailability(TypedDict, total=False):
    """Information about the agreement availability"""

    status: AgreementStatus
    errorMessage: Optional[String]


class CustomMetricBedrockEvaluatorModel(TypedDict, total=False):
    """Defines the model you want to evaluate custom metrics in an Amazon
    Bedrock evaluation job.
    """

    modelIdentifier: EvaluatorModelIdentifier


CustomMetricBedrockEvaluatorModels = List[CustomMetricBedrockEvaluatorModel]


class CustomMetricEvaluatorModelConfig(TypedDict, total=False):
    """Configuration of the evaluator model you want to use to evaluate custom
    metrics in an Amazon Bedrock evaluation job.
    """

    bedrockEvaluatorModels: CustomMetricBedrockEvaluatorModels


class RatingScaleItemValue(TypedDict, total=False):
    """Defines the value for one rating in a custom metric rating scale."""

    stringValue: Optional[RatingScaleItemValueStringValueString]
    floatValue: Optional[Float]


class RatingScaleItem(TypedDict, total=False):
    """Defines the value and corresponding definition for one rating in a
    custom metric rating scale.
    """

    definition: RatingScaleItemDefinition
    value: RatingScaleItemValue


RatingScale = List[RatingScaleItem]


class CustomMetricDefinition(TypedDict, total=False):
    """The definition of a custom metric for use in an Amazon Bedrock
    evaluation job. A custom metric definition includes a metric name,
    prompt (instructions) and optionally, a rating scale. Your prompt must
    include a task description and input variables. The required input
    variables are different for model-as-a-judge and RAG evaluations.

    For more information about how to define a custom metric in Amazon
    Bedrock, see `Create a prompt for a custom metrics (LLM-as-a-judge model
    evaluations) <https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html>`__
    and `Create a prompt for a custom metrics (RAG
    evaluations) <https://docs.aws.amazon.com/bedrock/latest/userguide/kb-evaluation-custom-metrics-prompt-formats.html>`__.
    """

    name: MetricName
    instructions: CustomMetricInstructions
    ratingScale: Optional[RatingScale]


class AutomatedEvaluationCustomMetricSource(TypedDict, total=False):
    """An array item definining a single custom metric for use in an Amazon
    Bedrock evaluation job.
    """

    customMetricDefinition: Optional[CustomMetricDefinition]


AutomatedEvaluationCustomMetrics = List[AutomatedEvaluationCustomMetricSource]


class AutomatedEvaluationCustomMetricConfig(TypedDict, total=False):
    """Defines the configuration of custom metrics to be used in an evaluation
    job. To learn more about using custom metrics in Amazon Bedrock
    evaluation jobs, see `Create a prompt for a custom metrics
    (LLM-as-a-judge model
    evaluations) <https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html>`__
    and `Create a prompt for a custom metrics (RAG
    evaluations) <https://docs.aws.amazon.com/bedrock/latest/userguide/kb-evaluation-custom-metrics-prompt-formats.html>`__.
    """

    customMetrics: AutomatedEvaluationCustomMetrics
    evaluatorModelConfig: CustomMetricEvaluatorModelConfig


class BedrockEvaluatorModel(TypedDict, total=False):
    """The evaluator model used in knowledge base evaluation job or in model
    evaluation job that use a model as judge. This model computes all
    evaluation related metrics.
    """

    modelIdentifier: EvaluatorModelIdentifier


BedrockEvaluatorModels = List[BedrockEvaluatorModel]


class EvaluatorModelConfig(TypedDict, total=False):
    """Specifies the model configuration for the evaluator model.
    ``EvaluatorModelConfig`` is required for evaluation jobs that use a
    knowledge base or in model evaluation job that use a model as judge.
    This model computes all evaluation related metrics.
    """

    bedrockEvaluatorModels: Optional[BedrockEvaluatorModels]


EvaluationMetricNames = List[EvaluationMetricName]


class EvaluationDatasetLocation(TypedDict, total=False):
    """The location in Amazon S3 where your prompt dataset is stored."""

    s3Uri: Optional[S3Uri]


class EvaluationDataset(TypedDict, total=False):
    """Used to specify the name of a built-in prompt dataset and optionally,
    the Amazon S3 bucket where a custom prompt dataset is saved.
    """

    name: EvaluationDatasetName
    datasetLocation: Optional[EvaluationDatasetLocation]


class EvaluationDatasetMetricConfig(TypedDict, total=False):
    """Defines the prompt datasets, built-in metric names and custom metric
    names, and the task type.
    """

    taskType: EvaluationTaskType
    dataset: EvaluationDataset
    metricNames: EvaluationMetricNames


EvaluationDatasetMetricConfigs = List[EvaluationDatasetMetricConfig]


class AutomatedEvaluationConfig(TypedDict, total=False):
    """The configuration details of an automated evaluation job. The
    ``EvaluationDatasetMetricConfig`` object is used to specify the prompt
    datasets, task type, and metric names.
    """

    datasetMetricConfigs: EvaluationDatasetMetricConfigs
    evaluatorModelConfig: Optional[EvaluatorModelConfig]
    customMetricConfig: Optional[AutomatedEvaluationCustomMetricConfig]


class AutomatedReasoningLogicStatement(TypedDict, total=False):
    """Represents a logical statement that can be expressed both in formal
    logic notation and natural language, providing dual representations for
    better understanding and validation.
    """

    logic: AutomatedReasoningLogicStatementContent
    naturalLanguage: Optional[AutomatedReasoningNaturalLanguageStatementContent]


AutomatedReasoningLogicStatementList = List[AutomatedReasoningLogicStatement]


class AutomatedReasoningCheckScenario(TypedDict, total=False):
    """Represents a logical scenario where claims can be evaluated as true or
    false, containing specific logical assignments.
    """

    statements: Optional[AutomatedReasoningLogicStatementList]


AutomatedReasoningCheckDifferenceScenarioList = List[AutomatedReasoningCheckScenario]


class AutomatedReasoningCheckNoTranslationsFinding(TypedDict, total=False):
    """Indicates that no relevant logical information could be extracted from
    the input for validation.
    """

    pass


class AutomatedReasoningCheckTooComplexFinding(TypedDict, total=False):
    """Indicates that the input exceeds the processing capacity due to the
    volume or complexity of the logical information.
    """

    pass


class AutomatedReasoningCheckInputTextReference(TypedDict, total=False):
    """References a portion of the original input text that corresponds to
    logical elements.
    """

    text: Optional[AutomatedReasoningNaturalLanguageStatementContent]


AutomatedReasoningCheckInputTextReferenceList = List[AutomatedReasoningCheckInputTextReference]


class AutomatedReasoningCheckTranslation(TypedDict, total=False):
    """Contains the logical translation of natural language input into formal
    logical statements, including premises, claims, and confidence scores.
    """

    premises: Optional[AutomatedReasoningLogicStatementList]
    claims: AutomatedReasoningLogicStatementList
    untranslatedPremises: Optional[AutomatedReasoningCheckInputTextReferenceList]
    untranslatedClaims: Optional[AutomatedReasoningCheckInputTextReferenceList]
    confidence: AutomatedReasoningCheckTranslationConfidence


AutomatedReasoningCheckTranslationList = List[AutomatedReasoningCheckTranslation]


class AutomatedReasoningCheckTranslationOption(TypedDict, total=False):
    """Represents one possible logical interpretation of ambiguous input
    content.
    """

    translations: Optional[AutomatedReasoningCheckTranslationList]


AutomatedReasoningCheckTranslationOptionList = List[AutomatedReasoningCheckTranslationOption]


class AutomatedReasoningCheckTranslationAmbiguousFinding(TypedDict, total=False):
    """Indicates that the input has multiple valid logical interpretations,
    requiring additional context or clarification.
    """

    options: Optional[AutomatedReasoningCheckTranslationOptionList]
    differenceScenarios: Optional[AutomatedReasoningCheckDifferenceScenarioList]


class AutomatedReasoningCheckLogicWarning(TypedDict, total=False):
    type: Optional[AutomatedReasoningCheckLogicWarningType]
    premises: Optional[AutomatedReasoningLogicStatementList]
    claims: Optional[AutomatedReasoningLogicStatementList]


class AutomatedReasoningCheckRule(TypedDict, total=False):
    """References a specific automated reasoning policy rule that was applied
    during evaluation.
    """

    id: Optional[AutomatedReasoningPolicyDefinitionRuleId]
    policyVersionArn: Optional[AutomatedReasoningPolicyArn]


AutomatedReasoningCheckRuleList = List[AutomatedReasoningCheckRule]


class AutomatedReasoningCheckImpossibleFinding(TypedDict, total=False):
    """Indicates that no valid claims can be made due to logical contradictions
    in the premises or rules.
    """

    translation: Optional[AutomatedReasoningCheckTranslation]
    contradictingRules: Optional[AutomatedReasoningCheckRuleList]
    logicWarning: Optional[AutomatedReasoningCheckLogicWarning]


class AutomatedReasoningCheckSatisfiableFinding(TypedDict, total=False):
    """Indicates that the claims could be either true or false depending on
    additional assumptions not provided in the input.
    """

    translation: Optional[AutomatedReasoningCheckTranslation]
    claimsTrueScenario: Optional[AutomatedReasoningCheckScenario]
    claimsFalseScenario: Optional[AutomatedReasoningCheckScenario]
    logicWarning: Optional[AutomatedReasoningCheckLogicWarning]


class AutomatedReasoningCheckInvalidFinding(TypedDict, total=False):
    """Indicates that the claims are logically false and contradictory to the
    established rules or premises.
    """

    translation: Optional[AutomatedReasoningCheckTranslation]
    contradictingRules: Optional[AutomatedReasoningCheckRuleList]
    logicWarning: Optional[AutomatedReasoningCheckLogicWarning]


class AutomatedReasoningCheckValidFinding(TypedDict, total=False):
    """Indicates that the claims are definitively true and logically implied by
    the premises, with no possible alternative interpretations.
    """

    translation: Optional[AutomatedReasoningCheckTranslation]
    claimsTrueScenario: Optional[AutomatedReasoningCheckScenario]
    supportingRules: Optional[AutomatedReasoningCheckRuleList]
    logicWarning: Optional[AutomatedReasoningCheckLogicWarning]


class AutomatedReasoningCheckFinding(TypedDict, total=False):
    """Represents the result of an Automated Reasoning validation check,
    indicating whether the content is logically valid, invalid, or falls
    into other categories based on the policy rules.
    """

    valid: Optional[AutomatedReasoningCheckValidFinding]
    invalid: Optional[AutomatedReasoningCheckInvalidFinding]
    satisfiable: Optional[AutomatedReasoningCheckSatisfiableFinding]
    impossible: Optional[AutomatedReasoningCheckImpossibleFinding]
    translationAmbiguous: Optional[AutomatedReasoningCheckTranslationAmbiguousFinding]
    tooComplex: Optional[AutomatedReasoningCheckTooComplexFinding]
    noTranslations: Optional[AutomatedReasoningCheckNoTranslationsFinding]


AutomatedReasoningCheckFindingList = List[AutomatedReasoningCheckFinding]


class AutomatedReasoningPolicyAddRuleAnnotation(TypedDict, total=False):
    """An annotation for adding a new rule to an Automated Reasoning policy
    using a formal logical expression.
    """

    expression: AutomatedReasoningPolicyDefinitionRuleExpression


class AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation(TypedDict, total=False):
    """An annotation for adding a new rule to the policy by converting a
    natural language description into a formal logical expression.
    """

    naturalLanguage: AutomatedReasoningPolicyAnnotationRuleNaturalLanguage


class AutomatedReasoningPolicyDefinitionRule(TypedDict, total=False):
    """Represents a formal logic rule in an Automated Reasoning policy. For
    example, rules can be expressed as if-then statements that define
    logical constraints.
    """

    id: AutomatedReasoningPolicyDefinitionRuleId
    expression: AutomatedReasoningPolicyDefinitionRuleExpression
    alternateExpression: Optional[AutomatedReasoningPolicyDefinitionRuleAlternateExpression]


class AutomatedReasoningPolicyAddRuleMutation(TypedDict, total=False):
    """A mutation operation that adds a new rule to the policy definition
    during the build process.
    """

    rule: AutomatedReasoningPolicyDefinitionRule


class AutomatedReasoningPolicyDefinitionTypeValue(TypedDict, total=False):
    """Represents a single value within a custom type definition, including its
    identifier and description.
    """

    value: AutomatedReasoningPolicyDefinitionTypeValueName
    description: Optional[AutomatedReasoningPolicyDefinitionTypeValueDescription]


AutomatedReasoningPolicyDefinitionTypeValueList = List[AutomatedReasoningPolicyDefinitionTypeValue]


class AutomatedReasoningPolicyAddTypeAnnotation(TypedDict, total=False):
    """An annotation for adding a new custom type to an Automated Reasoning
    policy, defining a set of possible values for variables.
    """

    name: AutomatedReasoningPolicyDefinitionTypeName
    description: AutomatedReasoningPolicyDefinitionTypeDescription
    values: AutomatedReasoningPolicyDefinitionTypeValueList


class AutomatedReasoningPolicyDefinitionType(TypedDict, total=False):
    """Represents a custom user-defined viarble type in an Automated Reasoning
    policy. Types are enum-based and provide additional context beyond
    predefined variable types.
    """

    name: AutomatedReasoningPolicyDefinitionTypeName
    description: Optional[AutomatedReasoningPolicyDefinitionTypeDescription]
    values: AutomatedReasoningPolicyDefinitionTypeValueList


class AutomatedReasoningPolicyAddTypeMutation(TypedDict, total=False):
    type: AutomatedReasoningPolicyDefinitionType


class AutomatedReasoningPolicyAddTypeValue(TypedDict, total=False):
    """Represents a single value that can be added to an existing custom type
    in the policy.
    """

    value: AutomatedReasoningPolicyDefinitionTypeValueName
    description: Optional[AutomatedReasoningPolicyDefinitionTypeValueDescription]


class AutomatedReasoningPolicyAddVariableAnnotation(TypedDict, total=False):
    name: AutomatedReasoningPolicyDefinitionVariableName
    type: AutomatedReasoningPolicyDefinitionTypeName
    description: AutomatedReasoningPolicyDefinitionVariableDescription


class AutomatedReasoningPolicyDefinitionVariable(TypedDict, total=False):
    name: AutomatedReasoningPolicyDefinitionVariableName
    type: AutomatedReasoningPolicyDefinitionTypeName
    description: AutomatedReasoningPolicyDefinitionVariableDescription


class AutomatedReasoningPolicyAddVariableMutation(TypedDict, total=False):
    """A mutation operation that adds a new variable to the policy definition
    during the build process.
    """

    variable: AutomatedReasoningPolicyDefinitionVariable


class AutomatedReasoningPolicyIngestContentAnnotation(TypedDict, total=False):
    """An annotation for processing and incorporating new content into an
    Automated Reasoning policy.
    """

    content: AutomatedReasoningPolicyAnnotationIngestContent


AutomatedReasoningPolicyDefinitionRuleIdList = List[AutomatedReasoningPolicyDefinitionRuleId]


class AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation(TypedDict, total=False):
    """An annotation for updating the policy based on feedback about how it
    performed on specific test scenarios.
    """

    ruleIds: Optional[AutomatedReasoningPolicyDefinitionRuleIdList]
    scenarioExpression: AutomatedReasoningPolicyScenarioExpression
    feedback: Optional[AutomatedReasoningPolicyAnnotationFeedbackNaturalLanguage]


class AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation(TypedDict, total=False):
    """An annotation for updating the policy based on feedback about how
    specific rules performed during testing or real-world usage.
    """

    ruleIds: Optional[AutomatedReasoningPolicyDefinitionRuleIdList]
    feedback: AutomatedReasoningPolicyAnnotationFeedbackNaturalLanguage


class AutomatedReasoningPolicyDeleteRuleAnnotation(TypedDict, total=False):
    """An annotation for removing a rule from an Automated Reasoning policy."""

    ruleId: AutomatedReasoningPolicyDefinitionRuleId


class AutomatedReasoningPolicyUpdateRuleAnnotation(TypedDict, total=False):
    """An annotation for modifying an existing rule in an Automated Reasoning
    policy.
    """

    ruleId: AutomatedReasoningPolicyDefinitionRuleId
    expression: AutomatedReasoningPolicyDefinitionRuleExpression


class AutomatedReasoningPolicyDeleteVariableAnnotation(TypedDict, total=False):
    """An annotation for removing a variable from an Automated Reasoning
    policy.
    """

    name: AutomatedReasoningPolicyDefinitionVariableName


class AutomatedReasoningPolicyUpdateVariableAnnotation(TypedDict, total=False):
    """An annotation for modifying an existing variable in an Automated
    Reasoning policy.
    """

    name: AutomatedReasoningPolicyDefinitionVariableName
    newName: Optional[AutomatedReasoningPolicyDefinitionVariableName]
    description: Optional[AutomatedReasoningPolicyDefinitionVariableDescription]


class AutomatedReasoningPolicyDeleteTypeAnnotation(TypedDict, total=False):
    """An annotation for removing a custom type from an Automated Reasoning
    policy.
    """

    name: AutomatedReasoningPolicyDefinitionTypeName


class AutomatedReasoningPolicyDeleteTypeValue(TypedDict, total=False):
    """Represents a value to be removed from an existing custom type in the
    policy.
    """

    value: AutomatedReasoningPolicyDefinitionTypeValueName


class AutomatedReasoningPolicyUpdateTypeValue(TypedDict, total=False):
    """Represents a modification to a value within an existing custom type."""

    value: AutomatedReasoningPolicyDefinitionTypeValueName
    newValue: Optional[AutomatedReasoningPolicyDefinitionTypeValueName]
    description: Optional[AutomatedReasoningPolicyDefinitionTypeValueDescription]


class AutomatedReasoningPolicyTypeValueAnnotation(TypedDict, total=False):
    """An annotation for managing values within custom types, including adding,
    updating, or removing specific type values.
    """

    addTypeValue: Optional[AutomatedReasoningPolicyAddTypeValue]
    updateTypeValue: Optional[AutomatedReasoningPolicyUpdateTypeValue]
    deleteTypeValue: Optional[AutomatedReasoningPolicyDeleteTypeValue]


AutomatedReasoningPolicyTypeValueAnnotationList = List[AutomatedReasoningPolicyTypeValueAnnotation]


class AutomatedReasoningPolicyUpdateTypeAnnotation(TypedDict, total=False):
    """An annotation for modifying an existing custom type in an Automated
    Reasoning policy.
    """

    name: AutomatedReasoningPolicyDefinitionTypeName
    newName: Optional[AutomatedReasoningPolicyDefinitionTypeName]
    description: Optional[AutomatedReasoningPolicyDefinitionTypeDescription]
    values: AutomatedReasoningPolicyTypeValueAnnotationList


class AutomatedReasoningPolicyAnnotation(TypedDict, total=False):
    """Contains the various operations that can be performed on an Automated
    Reasoning policy, including adding, updating, and deleting rules,
    variables, and types.
    """

    addType: Optional[AutomatedReasoningPolicyAddTypeAnnotation]
    updateType: Optional[AutomatedReasoningPolicyUpdateTypeAnnotation]
    deleteType: Optional[AutomatedReasoningPolicyDeleteTypeAnnotation]
    addVariable: Optional[AutomatedReasoningPolicyAddVariableAnnotation]
    updateVariable: Optional[AutomatedReasoningPolicyUpdateVariableAnnotation]
    deleteVariable: Optional[AutomatedReasoningPolicyDeleteVariableAnnotation]
    addRule: Optional[AutomatedReasoningPolicyAddRuleAnnotation]
    updateRule: Optional[AutomatedReasoningPolicyUpdateRuleAnnotation]
    deleteRule: Optional[AutomatedReasoningPolicyDeleteRuleAnnotation]
    addRuleFromNaturalLanguage: Optional[
        AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation
    ]
    updateFromRulesFeedback: Optional[AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation]
    updateFromScenarioFeedback: Optional[
        AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation
    ]
    ingestContent: Optional[AutomatedReasoningPolicyIngestContentAnnotation]


AutomatedReasoningPolicyAnnotationList = List[AutomatedReasoningPolicyAnnotation]
AutomatedReasoningPolicyBuildDocumentBlob = bytes


class AutomatedReasoningPolicyBuildStepMessage(TypedDict, total=False):
    """Represents a message generated during a build step, providing
    information about what happened or any issues encountered.
    """

    message: String
    messageType: AutomatedReasoningPolicyBuildMessageType


AutomatedReasoningPolicyBuildStepMessageList = List[AutomatedReasoningPolicyBuildStepMessage]


class AutomatedReasoningPolicyDefinitionElement(TypedDict, total=False):
    """Represents a single element in an Automated Reasoning policy definition,
    such as a rule, variable, or type definition.
    """

    policyDefinitionVariable: Optional[AutomatedReasoningPolicyDefinitionVariable]
    policyDefinitionType: Optional[AutomatedReasoningPolicyDefinitionType]
    policyDefinitionRule: Optional[AutomatedReasoningPolicyDefinitionRule]


class AutomatedReasoningPolicyDeleteRuleMutation(TypedDict, total=False):
    """A mutation operation that removes a rule from the policy definition
    during the build process.
    """

    id: AutomatedReasoningPolicyDefinitionRuleId


class AutomatedReasoningPolicyUpdateRuleMutation(TypedDict, total=False):
    """A mutation operation that modifies an existing rule in the policy
    definition during the build process.
    """

    rule: AutomatedReasoningPolicyDefinitionRule


class AutomatedReasoningPolicyDeleteVariableMutation(TypedDict, total=False):
    """A mutation operation that removes a variable from the policy definition
    during the build process.
    """

    name: AutomatedReasoningPolicyDefinitionVariableName


class AutomatedReasoningPolicyUpdateVariableMutation(TypedDict, total=False):
    """A mutation operation that modifies an existing variable in the policy
    definition during the build process.
    """

    variable: AutomatedReasoningPolicyDefinitionVariable


class AutomatedReasoningPolicyDeleteTypeMutation(TypedDict, total=False):
    """A mutation operation that removes a custom type from the policy
    definition during the build process.
    """

    name: AutomatedReasoningPolicyDefinitionTypeName


class AutomatedReasoningPolicyUpdateTypeMutation(TypedDict, total=False):
    type: AutomatedReasoningPolicyDefinitionType


class AutomatedReasoningPolicyMutation(TypedDict, total=False):
    """A container for various mutation operations that can be applied to an
    Automated Reasoning policy, including adding, updating, and deleting
    policy elements.
    """

    addType: Optional[AutomatedReasoningPolicyAddTypeMutation]
    updateType: Optional[AutomatedReasoningPolicyUpdateTypeMutation]
    deleteType: Optional[AutomatedReasoningPolicyDeleteTypeMutation]
    addVariable: Optional[AutomatedReasoningPolicyAddVariableMutation]
    updateVariable: Optional[AutomatedReasoningPolicyUpdateVariableMutation]
    deleteVariable: Optional[AutomatedReasoningPolicyDeleteVariableMutation]
    addRule: Optional[AutomatedReasoningPolicyAddRuleMutation]
    updateRule: Optional[AutomatedReasoningPolicyUpdateRuleMutation]
    deleteRule: Optional[AutomatedReasoningPolicyDeleteRuleMutation]


class AutomatedReasoningPolicyPlanning(TypedDict, total=False):
    """Represents the planning phase of policy build workflow, where the system
    analyzes source content and determines what operations to perform.
    """

    pass


class AutomatedReasoningPolicyBuildStepContext(TypedDict, total=False):
    """Provides context about what type of operation was being performed during
    a build step.
    """

    planning: Optional[AutomatedReasoningPolicyPlanning]
    mutation: Optional[AutomatedReasoningPolicyMutation]


class AutomatedReasoningPolicyBuildStep(TypedDict, total=False):
    """Represents a single step in the policy build process, containing context
    about what was being processed and any messages or results.
    """

    context: AutomatedReasoningPolicyBuildStepContext
    priorElement: Optional[AutomatedReasoningPolicyDefinitionElement]
    messages: AutomatedReasoningPolicyBuildStepMessageList


AutomatedReasoningPolicyBuildStepList = List[AutomatedReasoningPolicyBuildStep]


class AutomatedReasoningPolicyBuildLogEntry(TypedDict, total=False):
    """Represents a single entry in the policy build log, containing
    information about a specific step or event in the build process.
    """

    annotation: AutomatedReasoningPolicyAnnotation
    status: AutomatedReasoningPolicyAnnotationStatus
    buildSteps: AutomatedReasoningPolicyBuildStepList


AutomatedReasoningPolicyBuildLogEntryList = List[AutomatedReasoningPolicyBuildLogEntry]


class AutomatedReasoningPolicyBuildLog(TypedDict, total=False):
    """Contains detailed logging information about the policy build process,
    including steps taken, decisions made, and any issues encountered.
    """

    entries: AutomatedReasoningPolicyBuildLogEntryList


AutomatedReasoningPolicyDisjointedRuleIdList = List[AutomatedReasoningPolicyDefinitionRuleId]
AutomatedReasoningPolicyDefinitionVariableNameList = List[
    AutomatedReasoningPolicyDefinitionVariableName
]


class AutomatedReasoningPolicyDisjointRuleSet(TypedDict, total=False):
    """Represents a set of rules that operate on completely separate variables,
    indicating they address different concerns or domains within the policy.
    """

    variables: AutomatedReasoningPolicyDefinitionVariableNameList
    rules: AutomatedReasoningPolicyDisjointedRuleIdList


AutomatedReasoningPolicyDisjointRuleSetList = List[AutomatedReasoningPolicyDisjointRuleSet]
AutomatedReasoningPolicyConflictedRuleIdList = List[AutomatedReasoningPolicyDefinitionRuleId]


class AutomatedReasoningPolicyDefinitionTypeValuePair(TypedDict, total=False):
    """Associates a type name with a specific value name, used for referencing
    type values in rules and other policy elements.
    """

    typeName: AutomatedReasoningPolicyDefinitionTypeName
    valueName: AutomatedReasoningPolicyDefinitionTypeValueName


AutomatedReasoningPolicyDefinitionTypeValuePairList = List[
    AutomatedReasoningPolicyDefinitionTypeValuePair
]
AutomatedReasoningPolicyDefinitionTypeNameList = List[AutomatedReasoningPolicyDefinitionTypeName]


class AutomatedReasoningPolicyDefinitionQualityReport(TypedDict, total=False):
    """Provides a comprehensive analysis of the quality and completeness of an
    Automated Reasoning policy definition, highlighting potential issues and
    optimization opportunities.
    """

    typeCount: Integer
    variableCount: Integer
    ruleCount: Integer
    unusedTypes: AutomatedReasoningPolicyDefinitionTypeNameList
    unusedTypeValues: AutomatedReasoningPolicyDefinitionTypeValuePairList
    unusedVariables: AutomatedReasoningPolicyDefinitionVariableNameList
    conflictingRules: AutomatedReasoningPolicyConflictedRuleIdList
    disjointRuleSets: AutomatedReasoningPolicyDisjointRuleSetList


AutomatedReasoningPolicyDefinitionVariableList = List[AutomatedReasoningPolicyDefinitionVariable]
AutomatedReasoningPolicyDefinitionRuleList = List[AutomatedReasoningPolicyDefinitionRule]
AutomatedReasoningPolicyDefinitionTypeList = List[AutomatedReasoningPolicyDefinitionType]


class AutomatedReasoningPolicyDefinition(TypedDict, total=False):
    """Contains the formal logic rules, variables, and custom variable types
    that define an Automated Reasoning policy. The policy definition
    specifies the constraints used to validate foundation model responses
    for accuracy and logical consistency.
    """

    version: Optional[AutomatedReasoningPolicyFormatVersion]
    types: Optional[AutomatedReasoningPolicyDefinitionTypeList]
    rules: Optional[AutomatedReasoningPolicyDefinitionRuleList]
    variables: Optional[AutomatedReasoningPolicyDefinitionVariableList]


class AutomatedReasoningPolicyBuildResultAssets(TypedDict, total=False):
    """Contains the various assets generated during a policy build workflow,
    including logs, quality reports, and the final policy definition.
    """

    policyDefinition: Optional[AutomatedReasoningPolicyDefinition]
    qualityReport: Optional[AutomatedReasoningPolicyDefinitionQualityReport]
    buildLog: Optional[AutomatedReasoningPolicyBuildLog]


class AutomatedReasoningPolicyBuildWorkflowDocument(TypedDict, total=False):
    """Represents a source document used in the policy build workflow,
    containing the content and metadata needed for policy generation.
    """

    document: AutomatedReasoningPolicyBuildDocumentBlob
    documentContentType: AutomatedReasoningPolicyBuildDocumentContentType
    documentName: AutomatedReasoningPolicyBuildDocumentName
    documentDescription: Optional[AutomatedReasoningPolicyBuildDocumentDescription]


AutomatedReasoningPolicyBuildWorkflowDocumentList = List[
    AutomatedReasoningPolicyBuildWorkflowDocument
]


class AutomatedReasoningPolicyBuildWorkflowRepairContent(TypedDict, total=False):
    """Contains content and instructions for repairing or improving an existing
    Automated Reasoning policy.
    """

    annotations: AutomatedReasoningPolicyAnnotationList


class AutomatedReasoningPolicyWorkflowTypeContent(TypedDict, total=False):
    """Defines the content and configuration for different types of policy
    build workflows.
    """

    documents: Optional[AutomatedReasoningPolicyBuildWorkflowDocumentList]
    policyRepairAssets: Optional[AutomatedReasoningPolicyBuildWorkflowRepairContent]


class AutomatedReasoningPolicyBuildWorkflowSource(TypedDict, total=False):
    """Defines the source content for a policy build workflow, which can
    include documents, repair instructions, or other input materials.
    """

    policyDefinition: Optional[AutomatedReasoningPolicyDefinition]
    workflowContent: Optional[AutomatedReasoningPolicyWorkflowTypeContent]


Timestamp = datetime


class AutomatedReasoningPolicyBuildWorkflowSummary(TypedDict, total=False):
    """Provides a summary of a policy build workflow, including its current
    status, timing information, and key identifiers.
    """

    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    status: AutomatedReasoningPolicyBuildWorkflowStatus
    buildWorkflowType: AutomatedReasoningPolicyBuildWorkflowType
    createdAt: Timestamp
    updatedAt: Timestamp


AutomatedReasoningPolicyBuildWorkflowSummaries = List[AutomatedReasoningPolicyBuildWorkflowSummary]


class AutomatedReasoningPolicyScenario(TypedDict, total=False):
    """Represents a test scenario used to validate an Automated Reasoning
    policy, including the test conditions and expected outcomes.
    """

    expression: AutomatedReasoningPolicyScenarioExpression
    alternateExpression: AutomatedReasoningPolicyScenarioAlternateExpression
    ruleIds: AutomatedReasoningPolicyDefinitionRuleIdList
    expectedResult: AutomatedReasoningCheckResult


class AutomatedReasoningPolicySummary(TypedDict, total=False):
    """Contains summary information about an Automated Reasoning policy,
    including metadata and timestamps.
    """

    policyArn: AutomatedReasoningPolicyArn
    name: AutomatedReasoningPolicyName
    description: Optional[AutomatedReasoningPolicyDescription]
    version: AutomatedReasoningPolicyVersion
    policyId: AutomatedReasoningPolicyId
    createdAt: Timestamp
    updatedAt: Timestamp


AutomatedReasoningPolicySummaries = List[AutomatedReasoningPolicySummary]


class AutomatedReasoningPolicyTestCase(TypedDict, total=False):
    """Represents a test for validating an Automated Reasoning policy. tests
    contain sample inputs and expected outcomes to verify policy behavior.
    """

    testCaseId: AutomatedReasoningPolicyTestCaseId
    guardContent: AutomatedReasoningPolicyTestGuardContent
    queryContent: Optional[AutomatedReasoningPolicyTestQueryContent]
    expectedAggregatedFindingsResult: Optional[AutomatedReasoningCheckResult]
    createdAt: Timestamp
    updatedAt: Timestamp
    confidenceThreshold: Optional[AutomatedReasoningCheckTranslationConfidence]


AutomatedReasoningPolicyTestCaseIdList = List[AutomatedReasoningPolicyTestCaseId]
AutomatedReasoningPolicyTestCaseList = List[AutomatedReasoningPolicyTestCase]


class AutomatedReasoningPolicyTestResult(TypedDict, total=False):
    """Contains the results of testing an Automated Reasoning policy against
    various scenarios and validation checks.
    """

    testCase: AutomatedReasoningPolicyTestCase
    policyArn: AutomatedReasoningPolicyArn
    testRunStatus: AutomatedReasoningPolicyTestRunStatus
    testFindings: Optional[AutomatedReasoningCheckFindingList]
    testRunResult: Optional[AutomatedReasoningPolicyTestRunResult]
    aggregatedTestFindingsResult: Optional[AutomatedReasoningCheckResult]
    updatedAt: Timestamp


AutomatedReasoningPolicyTestList = List[AutomatedReasoningPolicyTestResult]


class BatchDeleteEvaluationJobError(TypedDict, total=False):
    """A JSON array that provides the status of the evaluation jobs being
    deleted.
    """

    jobIdentifier: EvaluationJobIdentifier
    code: String
    message: Optional[String]


BatchDeleteEvaluationJobErrors = List[BatchDeleteEvaluationJobError]


class BatchDeleteEvaluationJobItem(TypedDict, total=False):
    """An evaluation job for deletion, and it’s current status."""

    jobIdentifier: EvaluationJobIdentifier
    jobStatus: EvaluationJobStatus


BatchDeleteEvaluationJobItems = List[BatchDeleteEvaluationJobItem]
EvaluationJobIdentifiers = List[EvaluationJobIdentifier]


class BatchDeleteEvaluationJobRequest(ServiceRequest):
    jobIdentifiers: EvaluationJobIdentifiers


class BatchDeleteEvaluationJobResponse(TypedDict, total=False):
    errors: BatchDeleteEvaluationJobErrors
    evaluationJobs: BatchDeleteEvaluationJobItems


ByteContentBlob = bytes


class ByteContentDoc(TypedDict, total=False):
    """Contains the document contained in the wrapper object, along with its
    attributes/fields.
    """

    identifier: Identifier
    contentType: ContentType
    data: ByteContentBlob


class CancelAutomatedReasoningPolicyBuildWorkflowRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId


class CancelAutomatedReasoningPolicyBuildWorkflowResponse(TypedDict, total=False):
    pass


class S3Config(TypedDict, total=False):
    """S3 configuration for storing log data."""

    bucketName: BucketName
    keyPrefix: Optional[KeyPrefix]


class CloudWatchConfig(TypedDict, total=False):
    """CloudWatch logging configuration."""

    logGroupName: LogGroupName
    roleArn: RoleArn
    largeDataDeliveryS3Config: Optional[S3Config]


class Tag(TypedDict, total=False):
    """Definition of the key/value pair for a tag."""

    key: TagKey
    value: TagValue


TagList = List[Tag]


class CreateAutomatedReasoningPolicyRequest(ServiceRequest):
    name: AutomatedReasoningPolicyName
    description: Optional[AutomatedReasoningPolicyDescription]
    clientRequestToken: Optional[IdempotencyToken]
    policyDefinition: Optional[AutomatedReasoningPolicyDefinition]
    tags: Optional[TagList]


class CreateAutomatedReasoningPolicyResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    version: AutomatedReasoningPolicyVersion
    name: AutomatedReasoningPolicyName
    description: Optional[AutomatedReasoningPolicyDescription]
    definitionHash: Optional[AutomatedReasoningPolicyHash]
    createdAt: Timestamp
    updatedAt: Timestamp


class CreateAutomatedReasoningPolicyTestCaseRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    guardContent: AutomatedReasoningPolicyTestGuardContent
    queryContent: Optional[AutomatedReasoningPolicyTestQueryContent]
    expectedAggregatedFindingsResult: AutomatedReasoningCheckResult
    clientRequestToken: Optional[IdempotencyToken]
    confidenceThreshold: Optional[AutomatedReasoningCheckTranslationConfidence]


class CreateAutomatedReasoningPolicyTestCaseResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    testCaseId: AutomatedReasoningPolicyTestCaseId


class CreateAutomatedReasoningPolicyVersionRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    clientRequestToken: Optional[IdempotencyToken]
    lastUpdatedDefinitionHash: AutomatedReasoningPolicyHash
    tags: Optional[TagList]


class CreateAutomatedReasoningPolicyVersionResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    version: AutomatedReasoningPolicyVersion
    name: AutomatedReasoningPolicyName
    description: Optional[AutomatedReasoningPolicyDescription]
    definitionHash: AutomatedReasoningPolicyHash
    createdAt: Timestamp


class CreateCustomModelDeploymentRequest(ServiceRequest):
    modelDeploymentName: ModelDeploymentName
    modelArn: CustomModelArn
    description: Optional[CustomModelDeploymentDescription]
    tags: Optional[TagList]
    clientRequestToken: Optional[IdempotencyToken]


class CreateCustomModelDeploymentResponse(TypedDict, total=False):
    customModelDeploymentArn: CustomModelDeploymentArn


class S3DataSource(TypedDict, total=False):
    """The Amazon S3 data source of the model to import."""

    s3Uri: S3Uri


class ModelDataSource(TypedDict, total=False):
    """The data source of the model to import."""

    s3DataSource: Optional[S3DataSource]


class CreateCustomModelRequest(ServiceRequest):
    modelName: CustomModelName
    modelSourceConfig: ModelDataSource
    modelKmsKeyArn: Optional[KmsKeyArn]
    roleArn: Optional[RoleArn]
    modelTags: Optional[TagList]
    clientRequestToken: Optional[IdempotencyToken]


class CreateCustomModelResponse(TypedDict, total=False):
    modelArn: ModelArn


class EvaluationOutputDataConfig(TypedDict, total=False):
    """The Amazon S3 location where the results of your evaluation job are
    saved.
    """

    s3Uri: S3Uri


class EvaluationPrecomputedRetrieveAndGenerateSourceConfig(TypedDict, total=False):
    """A summary of a RAG source used for a retrieve-and-generate Knowledge
    Base evaluation job where you provide your own inference response data.
    """

    ragSourceIdentifier: EvaluationPrecomputedRagSourceIdentifier


class EvaluationPrecomputedRetrieveSourceConfig(TypedDict, total=False):
    """A summary of a RAG source used for a retrieve-only Knowledge Base
    evaluation job where you provide your own inference response data.
    """

    ragSourceIdentifier: EvaluationPrecomputedRagSourceIdentifier


class EvaluationPrecomputedRagSourceConfig(TypedDict, total=False):
    """A summary of a RAG source used for a Knowledge Base evaluation job where
    you provide your own inference response data.
    """

    retrieveSourceConfig: Optional[EvaluationPrecomputedRetrieveSourceConfig]
    retrieveAndGenerateSourceConfig: Optional[EvaluationPrecomputedRetrieveAndGenerateSourceConfig]


RAGStopSequences = List[RAGStopSequencesMemberString]


class TextInferenceConfig(TypedDict, total=False):
    """The configuration details for text generation using a language model via
    the ``RetrieveAndGenerate`` function.
    """

    temperature: Optional[Temperature]
    topP: Optional[TopP]
    maxTokens: Optional[MaxTokens]
    stopSequences: Optional[RAGStopSequences]


class KbInferenceConfig(TypedDict, total=False):
    """Contains configuration details of the inference for knowledge base
    retrieval and response generation.
    """

    textInferenceConfig: Optional[TextInferenceConfig]


class GuardrailConfiguration(TypedDict, total=False):
    """The configuration details for the guardrail."""

    guardrailId: GuardrailConfigurationGuardrailIdString
    guardrailVersion: GuardrailConfigurationGuardrailVersionString


class PromptTemplate(TypedDict, total=False):
    """The template for the prompt that's sent to the model for response
    generation.
    """

    textPromptTemplate: Optional[TextPromptTemplate]


class ExternalSourcesGenerationConfiguration(TypedDict, total=False):
    """The response generation configuration of the external source wrapper
    object.
    """

    promptTemplate: Optional[PromptTemplate]
    guardrailConfiguration: Optional[GuardrailConfiguration]
    kbInferenceConfig: Optional[KbInferenceConfig]
    additionalModelRequestFields: Optional[AdditionalModelRequestFields]


class S3ObjectDoc(TypedDict, total=False):
    """The unique wrapper object of the document from the S3 location."""

    uri: kBS3Uri


class ExternalSource(TypedDict, total=False):
    """The unique external source of the content contained in the wrapper
    object.
    """

    sourceType: ExternalSourceType
    s3Location: Optional[S3ObjectDoc]
    byteContent: Optional[ByteContentDoc]


ExternalSources = List[ExternalSource]


class ExternalSourcesRetrieveAndGenerateConfiguration(TypedDict, total=False):
    """The configuration of the external source wrapper object in the
    ``retrieveAndGenerate`` function.
    """

    modelArn: BedrockModelArn
    sources: ExternalSources
    generationConfiguration: Optional[ExternalSourcesGenerationConfiguration]


class QueryTransformationConfiguration(TypedDict, total=False):
    type: QueryTransformationType


class OrchestrationConfiguration(TypedDict, total=False):
    """The configuration details for the model to process the prompt prior to
    retrieval and response generation.
    """

    queryTransformationConfiguration: QueryTransformationConfiguration


class GenerationConfiguration(TypedDict, total=False):
    """The configuration details for response generation based on retrieved
    text chunks.
    """

    promptTemplate: Optional[PromptTemplate]
    guardrailConfiguration: Optional[GuardrailConfiguration]
    kbInferenceConfig: Optional[KbInferenceConfig]
    additionalModelRequestFields: Optional[AdditionalModelRequestFields]


class FieldForReranking(TypedDict, total=False):
    """Specifies a field to be used during the reranking process in a Knowledge
    Base vector search. This structure identifies metadata fields that
    should be considered when reordering search results to improve
    relevance.
    """

    fieldName: FieldForRerankingFieldNameString


FieldsForReranking = List[FieldForReranking]


class RerankingMetadataSelectiveModeConfiguration(TypedDict, total=False):
    """Configuration for selectively including or excluding metadata fields
    during the reranking process. This allows you to control which metadata
    attributes are considered when reordering search results.
    """

    fieldsToInclude: Optional[FieldsForReranking]
    fieldsToExclude: Optional[FieldsForReranking]


class MetadataConfigurationForReranking(TypedDict, total=False):
    """Configuration for how metadata should be used during the reranking
    process in Knowledge Base vector searches. This determines which
    metadata fields are included or excluded when reordering search results.
    """

    selectionMode: RerankingMetadataSelectionMode
    selectiveModeConfiguration: Optional[RerankingMetadataSelectiveModeConfiguration]


class VectorSearchBedrockRerankingModelConfiguration(TypedDict, total=False):
    """Configuration for the Amazon Bedrock foundation model used for reranking
    vector search results. This specifies which model to use and any
    additional parameters required by the model.
    """

    modelArn: BedrockRerankingModelArn
    additionalModelRequestFields: Optional[AdditionalModelRequestFields]


class VectorSearchBedrockRerankingConfiguration(TypedDict, total=False):
    """Configuration for using Amazon Bedrock foundation models to rerank
    Knowledge Base vector search results. This enables more sophisticated
    relevance ranking using large language models.
    """

    modelConfiguration: VectorSearchBedrockRerankingModelConfiguration
    numberOfRerankedResults: Optional[
        VectorSearchBedrockRerankingConfigurationNumberOfRerankedResultsInteger
    ]
    metadataConfiguration: Optional[MetadataConfigurationForReranking]


class VectorSearchRerankingConfiguration(TypedDict, total=False):
    type: VectorSearchRerankingConfigurationType
    bedrockRerankingConfiguration: Optional[VectorSearchBedrockRerankingConfiguration]


class MetadataAttributeSchema(TypedDict, total=False):
    key: MetadataAttributeSchemaKeyString
    type: AttributeType
    description: MetadataAttributeSchemaDescriptionString


MetadataAttributeSchemaList = List[MetadataAttributeSchema]


class ImplicitFilterConfiguration(TypedDict, total=False):
    """Configuration for implicit filtering in Knowledge Base vector searches.
    Implicit filtering allows you to automatically filter search results
    based on metadata attributes without requiring explicit filter
    expressions in each query.
    """

    metadataAttributes: MetadataAttributeSchemaList
    modelArn: BedrockModelArn


RetrievalFilter = TypedDict(
    "RetrievalFilter",
    {
        "equals": Optional["FilterAttribute"],
        "notEquals": Optional["FilterAttribute"],
        "greaterThan": Optional["FilterAttribute"],
        "greaterThanOrEquals": Optional["FilterAttribute"],
        "lessThan": Optional["FilterAttribute"],
        "lessThanOrEquals": Optional["FilterAttribute"],
        "in": Optional["FilterAttribute"],
        "notIn": Optional["FilterAttribute"],
        "startsWith": Optional["FilterAttribute"],
        "listContains": Optional["FilterAttribute"],
        "stringContains": Optional["FilterAttribute"],
        "andAll": Optional["RetrievalFilterList"],
        "orAll": Optional["RetrievalFilterList"],
    },
    total=False,
)
RetrievalFilterList = List[RetrievalFilter]


class FilterValue(TypedDict, total=False):
    pass


class FilterAttribute(TypedDict, total=False):
    """Specifies the name of the metadata attribute/field to apply filters. You
    must match the name of the attribute/field in your data source/document
    metadata.
    """

    key: FilterKey
    value: FilterValue


class KnowledgeBaseVectorSearchConfiguration(TypedDict, total=False):
    """The configuration details for returning the results from the knowledge
    base vector search.
    """

    numberOfResults: Optional[KnowledgeBaseVectorSearchConfigurationNumberOfResultsInteger]
    overrideSearchType: Optional[SearchType]
    filter: Optional[RetrievalFilter]
    implicitFilterConfiguration: Optional[ImplicitFilterConfiguration]
    rerankingConfiguration: Optional[VectorSearchRerankingConfiguration]


class KnowledgeBaseRetrievalConfiguration(TypedDict, total=False):
    """Contains configuration details for retrieving information from a
    knowledge base.
    """

    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfiguration


class KnowledgeBaseRetrieveAndGenerateConfiguration(TypedDict, total=False):
    """Contains configuration details for retrieving information from a
    knowledge base and generating responses.
    """

    knowledgeBaseId: KnowledgeBaseId
    modelArn: BedrockModelArn
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfiguration]
    generationConfiguration: Optional[GenerationConfiguration]
    orchestrationConfiguration: Optional[OrchestrationConfiguration]


class RetrieveAndGenerateConfiguration(TypedDict, total=False):
    type: RetrieveAndGenerateType
    knowledgeBaseConfiguration: Optional[KnowledgeBaseRetrieveAndGenerateConfiguration]
    externalSourcesConfiguration: Optional[ExternalSourcesRetrieveAndGenerateConfiguration]


class RetrieveConfig(TypedDict, total=False):
    """The configuration details for retrieving information from a knowledge
    base.
    """

    knowledgeBaseId: KnowledgeBaseId
    knowledgeBaseRetrievalConfiguration: KnowledgeBaseRetrievalConfiguration


class KnowledgeBaseConfig(TypedDict, total=False):
    """The configuration details for retrieving information from a knowledge
    base and generating responses.
    """

    retrieveConfig: Optional[RetrieveConfig]
    retrieveAndGenerateConfig: Optional[RetrieveAndGenerateConfiguration]


class RAGConfig(TypedDict, total=False):
    """Contains configuration details for retrieval of information and response
    generation.
    """

    knowledgeBaseConfig: Optional[KnowledgeBaseConfig]
    precomputedRagSourceConfig: Optional[EvaluationPrecomputedRagSourceConfig]


RagConfigs = List[RAGConfig]


class EvaluationPrecomputedInferenceSource(TypedDict, total=False):
    """A summary of a model used for a model evaluation job where you provide
    your own inference response data.
    """

    inferenceSourceIdentifier: EvaluationPrecomputedInferenceSourceIdentifier


class PerformanceConfiguration(TypedDict, total=False):
    """Contains performance settings for a model."""

    latency: Optional[PerformanceConfigLatency]


class EvaluationBedrockModel(TypedDict, total=False):
    """Contains the ARN of the Amazon Bedrock model or `inference
    profile <https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html>`__
    specified in your evaluation job. Each Amazon Bedrock model supports
    different ``inferenceParams``. To learn more about supported inference
    parameters for Amazon Bedrock models, see `Inference parameters for
    foundation
    models <https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html>`__.

    The ``inferenceParams`` are specified using JSON. To successfully insert
    JSON as string make sure that all quotations are properly escaped. For
    example, ``"temperature":"0.25"`` key value pair would need to be
    formatted as ``\\"temperature\\":\\"0.25\\"`` to successfully accepted in
    the request.
    """

    modelIdentifier: EvaluationBedrockModelIdentifier
    inferenceParams: Optional[EvaluationModelInferenceParams]
    performanceConfig: Optional[PerformanceConfiguration]


class EvaluationModelConfig(TypedDict, total=False):
    """Defines the models used in the model evaluation job."""

    bedrockModel: Optional[EvaluationBedrockModel]
    precomputedInferenceSource: Optional[EvaluationPrecomputedInferenceSource]


EvaluationModelConfigs = List[EvaluationModelConfig]


class EvaluationInferenceConfig(TypedDict, total=False):
    """The configuration details of the inference model for an evaluation job.

    For automated model evaluation jobs, only a single model is supported.

    For human-based model evaluation jobs, your annotator can compare the
    responses for up to two different models.
    """

    models: Optional[EvaluationModelConfigs]
    ragConfigs: Optional[RagConfigs]


class HumanEvaluationCustomMetric(TypedDict, total=False):
    """In a model evaluation job that uses human workers you must define the
    name of the metric, and how you want that metric rated ``ratingMethod``,
    and an optional description of the metric.
    """

    name: EvaluationMetricName
    description: Optional[EvaluationMetricDescription]
    ratingMethod: EvaluationRatingMethod


HumanEvaluationCustomMetrics = List[HumanEvaluationCustomMetric]


class HumanWorkflowConfig(TypedDict, total=False):
    """Contains ``SageMakerFlowDefinition`` object. The object is used to
    specify the prompt dataset, task type, rating method and metric names.
    """

    flowDefinitionArn: SageMakerFlowDefinitionArn
    instructions: Optional[HumanTaskInstructions]


class HumanEvaluationConfig(TypedDict, total=False):
    """Specifies the custom metrics, how tasks will be rated, the flow
    definition ARN, and your custom prompt datasets. Model evaluation jobs
    use human workers *only* support the use of custom prompt datasets. To
    learn more about custom prompt datasets and the required format, see
    `Custom prompt
    datasets <https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-prompt-datasets-custom.html>`__.

    When you create custom metrics in ``HumanEvaluationCustomMetric`` you
    must specify the metric's ``name``. The list of ``names`` specified in
    the ``HumanEvaluationCustomMetric`` array, must match the
    ``metricNames`` array of strings specified in
    ``EvaluationDatasetMetricConfig``. For example, if in the
    ``HumanEvaluationCustomMetric`` array your specified the names
    ``"accuracy", "toxicity", "readability"`` as custom metrics *then* the
    ``metricNames`` array would need to look like the following
    ``["accuracy", "toxicity", "readability"]`` in
    ``EvaluationDatasetMetricConfig``.
    """

    humanWorkflowConfig: Optional[HumanWorkflowConfig]
    customMetrics: Optional[HumanEvaluationCustomMetrics]
    datasetMetricConfigs: EvaluationDatasetMetricConfigs


class EvaluationConfig(TypedDict, total=False):
    """The configuration details of either an automated or human-based
    evaluation job.
    """

    automated: Optional[AutomatedEvaluationConfig]
    human: Optional[HumanEvaluationConfig]


class CreateEvaluationJobRequest(ServiceRequest):
    jobName: EvaluationJobName
    jobDescription: Optional[EvaluationJobDescription]
    clientRequestToken: Optional[IdempotencyToken]
    roleArn: RoleArn
    customerEncryptionKeyId: Optional[KmsKeyId]
    jobTags: Optional[TagList]
    applicationType: Optional[ApplicationType]
    evaluationConfig: EvaluationConfig
    inferenceConfig: EvaluationInferenceConfig
    outputDataConfig: EvaluationOutputDataConfig


class CreateEvaluationJobResponse(TypedDict, total=False):
    jobArn: EvaluationJobArn


class CreateFoundationModelAgreementRequest(ServiceRequest):
    offerToken: OfferToken
    modelId: BedrockModelId


class CreateFoundationModelAgreementResponse(TypedDict, total=False):
    modelId: BedrockModelId


class GuardrailCrossRegionConfig(TypedDict, total=False):
    """The system-defined guardrail profile that you're using with your
    guardrail. Guardrail profiles define the destination Amazon Web Services
    Regions where guardrail inference requests can be automatically routed.
    Using guardrail profiles helps maintain guardrail performance and
    reliability when demand increases.

    For more information, see the `Amazon Bedrock User
    Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html>`__.
    """

    guardrailProfileIdentifier: GuardrailCrossRegionGuardrailProfileIdentifier


GuardrailAutomatedReasoningPolicyConfigPoliciesList = List[AutomatedReasoningPolicyArn]


class GuardrailAutomatedReasoningPolicyConfig(TypedDict, total=False):
    """Configuration settings for integrating Automated Reasoning policies with
    Amazon Bedrock Guardrails.
    """

    policies: GuardrailAutomatedReasoningPolicyConfigPoliciesList
    confidenceThreshold: Optional[AutomatedReasoningConfidenceFilterThreshold]


class GuardrailContextualGroundingFilterConfig(TypedDict, total=False):
    type: GuardrailContextualGroundingFilterType
    threshold: GuardrailContextualGroundingFilterConfigThresholdDouble
    action: Optional[GuardrailContextualGroundingAction]
    enabled: Optional[Boolean]


GuardrailContextualGroundingFiltersConfig = List[GuardrailContextualGroundingFilterConfig]


class GuardrailContextualGroundingPolicyConfig(TypedDict, total=False):
    """The policy configuration details for the guardrails contextual grounding
    policy.
    """

    filtersConfig: GuardrailContextualGroundingFiltersConfig


class GuardrailRegexConfig(TypedDict, total=False):
    """The regular expression to configure for the guardrail."""

    name: GuardrailRegexConfigNameString
    description: Optional[GuardrailRegexConfigDescriptionString]
    pattern: GuardrailRegexConfigPatternString
    action: GuardrailSensitiveInformationAction
    inputAction: Optional[GuardrailSensitiveInformationAction]
    outputAction: Optional[GuardrailSensitiveInformationAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailRegexesConfig = List[GuardrailRegexConfig]


class GuardrailPiiEntityConfig(TypedDict, total=False):
    type: GuardrailPiiEntityType
    action: GuardrailSensitiveInformationAction
    inputAction: Optional[GuardrailSensitiveInformationAction]
    outputAction: Optional[GuardrailSensitiveInformationAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailPiiEntitiesConfig = List[GuardrailPiiEntityConfig]


class GuardrailSensitiveInformationPolicyConfig(TypedDict, total=False):
    """Contains details about PII entities and regular expressions to configure
    for the guardrail.
    """

    piiEntitiesConfig: Optional[GuardrailPiiEntitiesConfig]
    regexesConfig: Optional[GuardrailRegexesConfig]


class GuardrailManagedWordsConfig(TypedDict, total=False):
    type: GuardrailManagedWordsType
    inputAction: Optional[GuardrailWordAction]
    outputAction: Optional[GuardrailWordAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailManagedWordListsConfig = List[GuardrailManagedWordsConfig]


class GuardrailWordConfig(TypedDict, total=False):
    """A word to configure for the guardrail."""

    text: GuardrailWordConfigTextString
    inputAction: Optional[GuardrailWordAction]
    outputAction: Optional[GuardrailWordAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailWordsConfig = List[GuardrailWordConfig]


class GuardrailWordPolicyConfig(TypedDict, total=False):
    """Contains details about the word policy to configured for the guardrail."""

    wordsConfig: Optional[GuardrailWordsConfig]
    managedWordListsConfig: Optional[GuardrailManagedWordListsConfig]


class GuardrailContentFiltersTierConfig(TypedDict, total=False):
    """The tier that your guardrail uses for content filters. Consider using a
    tier that balances performance, accuracy, and compatibility with your
    existing generative AI workflows.
    """

    tierName: GuardrailContentFiltersTierName


GuardrailModalities = List[GuardrailModality]


class GuardrailContentFilterConfig(TypedDict, total=False):
    type: GuardrailContentFilterType
    inputStrength: GuardrailFilterStrength
    outputStrength: GuardrailFilterStrength
    inputModalities: Optional[GuardrailModalities]
    outputModalities: Optional[GuardrailModalities]
    inputAction: Optional[GuardrailContentFilterAction]
    outputAction: Optional[GuardrailContentFilterAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailContentFiltersConfig = List[GuardrailContentFilterConfig]


class GuardrailContentPolicyConfig(TypedDict, total=False):
    """Contains details about how to handle harmful content."""

    filtersConfig: GuardrailContentFiltersConfig
    tierConfig: Optional[GuardrailContentFiltersTierConfig]


class GuardrailTopicsTierConfig(TypedDict, total=False):
    """The tier that your guardrail uses for denied topic filters. Consider
    using a tier that balances performance, accuracy, and compatibility with
    your existing generative AI workflows.
    """

    tierName: GuardrailTopicsTierName


GuardrailTopicExamples = List[GuardrailTopicExample]


class GuardrailTopicConfig(TypedDict, total=False):
    name: GuardrailTopicName
    definition: GuardrailTopicDefinition
    examples: Optional[GuardrailTopicExamples]
    type: GuardrailTopicType
    inputAction: Optional[GuardrailTopicAction]
    outputAction: Optional[GuardrailTopicAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailTopicsConfig = List[GuardrailTopicConfig]


class GuardrailTopicPolicyConfig(TypedDict, total=False):
    """Contains details about topics that the guardrail should identify and
    deny.
    """

    topicsConfig: GuardrailTopicsConfig
    tierConfig: Optional[GuardrailTopicsTierConfig]


class CreateGuardrailRequest(ServiceRequest):
    name: GuardrailName
    description: Optional[GuardrailDescription]
    topicPolicyConfig: Optional[GuardrailTopicPolicyConfig]
    contentPolicyConfig: Optional[GuardrailContentPolicyConfig]
    wordPolicyConfig: Optional[GuardrailWordPolicyConfig]
    sensitiveInformationPolicyConfig: Optional[GuardrailSensitiveInformationPolicyConfig]
    contextualGroundingPolicyConfig: Optional[GuardrailContextualGroundingPolicyConfig]
    automatedReasoningPolicyConfig: Optional[GuardrailAutomatedReasoningPolicyConfig]
    crossRegionConfig: Optional[GuardrailCrossRegionConfig]
    blockedInputMessaging: GuardrailBlockedMessaging
    blockedOutputsMessaging: GuardrailBlockedMessaging
    kmsKeyId: Optional[KmsKeyId]
    tags: Optional[TagList]
    clientRequestToken: Optional[IdempotencyToken]


class CreateGuardrailResponse(TypedDict, total=False):
    guardrailId: GuardrailId
    guardrailArn: GuardrailArn
    version: GuardrailDraftVersion
    createdAt: Timestamp


class CreateGuardrailVersionRequest(ServiceRequest):
    guardrailIdentifier: GuardrailIdentifier
    description: Optional[GuardrailDescription]
    clientRequestToken: Optional[IdempotencyToken]


class CreateGuardrailVersionResponse(TypedDict, total=False):
    guardrailId: GuardrailId
    version: GuardrailNumericalVersion


class InferenceProfileModelSource(TypedDict, total=False):
    """Contains information about the model or system-defined inference profile
    that is the source for an inference profile..
    """

    copyFrom: Optional[InferenceProfileModelSourceArn]


class CreateInferenceProfileRequest(ServiceRequest):
    inferenceProfileName: InferenceProfileName
    description: Optional[InferenceProfileDescription]
    clientRequestToken: Optional[IdempotencyToken]
    modelSource: InferenceProfileModelSource
    tags: Optional[TagList]


class CreateInferenceProfileResponse(TypedDict, total=False):
    inferenceProfileArn: InferenceProfileArn
    status: Optional[InferenceProfileStatus]


SecurityGroupIds = List[SecurityGroupId]
SubnetIds = List[SubnetId]


class VpcConfig(TypedDict, total=False):
    """The configuration of a virtual private cloud (VPC). For more
    information, see `Protect your data using Amazon Virtual Private Cloud
    and Amazon Web Services
    PrivateLink <https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html>`__.
    """

    subnetIds: SubnetIds
    securityGroupIds: SecurityGroupIds


class SageMakerEndpoint(TypedDict, total=False):
    """Specifies the configuration for a Amazon SageMaker endpoint."""

    initialInstanceCount: InstanceCount
    instanceType: InstanceType
    executionRole: RoleArn
    kmsEncryptionKey: Optional[KmsKeyId]
    vpc: Optional[VpcConfig]


class EndpointConfig(TypedDict, total=False):
    """Specifies the configuration for the endpoint."""

    sageMaker: Optional[SageMakerEndpoint]


class CreateMarketplaceModelEndpointRequest(ServiceRequest):
    modelSourceIdentifier: ModelSourceIdentifier
    endpointConfig: EndpointConfig
    acceptEula: Optional[AcceptEula]
    endpointName: EndpointName
    clientRequestToken: Optional[IdempotencyToken]
    tags: Optional[TagList]


class MarketplaceModelEndpoint(TypedDict, total=False):
    """Contains details about an endpoint for a model from Amazon Bedrock
    Marketplace.
    """

    endpointArn: Arn
    modelSourceIdentifier: ModelSourceIdentifier
    status: Optional[Status]
    statusMessage: Optional[String]
    createdAt: Timestamp
    updatedAt: Timestamp
    endpointConfig: EndpointConfig
    endpointStatus: String
    endpointStatusMessage: Optional[String]


class CreateMarketplaceModelEndpointResponse(TypedDict, total=False):
    marketplaceModelEndpoint: MarketplaceModelEndpoint


class CreateModelCopyJobRequest(ServiceRequest):
    sourceModelArn: ModelArn
    targetModelName: CustomModelName
    modelKmsKeyId: Optional[KmsKeyId]
    targetModelTags: Optional[TagList]
    clientRequestToken: Optional[IdempotencyToken]


class CreateModelCopyJobResponse(TypedDict, total=False):
    jobArn: ModelCopyJobArn


class TeacherModelConfig(TypedDict, total=False):
    """Details about a teacher model used for model customization."""

    teacherModelIdentifier: TeacherModelIdentifier
    maxResponseLengthForInference: Optional[Integer]


class DistillationConfig(TypedDict, total=False):
    """Settings for distilling a foundation model into a smaller and more
    efficient model.
    """

    teacherModelConfig: TeacherModelConfig


class CustomizationConfig(TypedDict, total=False):
    """A model customization configuration"""

    distillationConfig: Optional[DistillationConfig]


ModelCustomizationHyperParameters = Dict[String, String]


class OutputDataConfig(TypedDict, total=False):
    """S3 Location of the output data."""

    s3Uri: S3Uri


class Validator(TypedDict, total=False):
    """Information about a validator."""

    s3Uri: S3Uri


Validators = List[Validator]


class ValidationDataConfig(TypedDict, total=False):
    """Array of up to 10 validators."""

    validators: Validators


RequestMetadataMap = Dict[RequestMetadataMapKeyString, RequestMetadataMapValueString]


class RequestMetadataBaseFilters(TypedDict, total=False):
    """A mapping of a metadata key to a value that it should or should not
    equal.
    """

    equals: Optional[RequestMetadataMap]
    notEquals: Optional[RequestMetadataMap]


RequestMetadataFiltersList = List[RequestMetadataBaseFilters]


class RequestMetadataFilters(TypedDict, total=False):
    """Rules for filtering invocation logs. A filter can be a mapping of a
    metadata key to a value that it should or should not equal (a base
    filter), or a list of base filters that are all applied with ``AND`` or
    ``OR`` logical operators
    """

    equals: Optional[RequestMetadataMap]
    notEquals: Optional[RequestMetadataMap]
    andAll: Optional[RequestMetadataFiltersList]
    orAll: Optional[RequestMetadataFiltersList]


class InvocationLogSource(TypedDict, total=False):
    """A storage location for invocation logs."""

    s3Uri: Optional[S3Uri]


class InvocationLogsConfig(TypedDict, total=False):
    """Settings for using invocation logs to customize a model."""

    usePromptResponse: Optional[UsePromptResponse]
    invocationLogSource: InvocationLogSource
    requestMetadataFilters: Optional[RequestMetadataFilters]


class TrainingDataConfig(TypedDict, total=False):
    """S3 Location of the training data."""

    s3Uri: Optional[S3Uri]
    invocationLogsConfig: Optional[InvocationLogsConfig]


class CreateModelCustomizationJobRequest(ServiceRequest):
    jobName: JobName
    customModelName: CustomModelName
    roleArn: RoleArn
    clientRequestToken: Optional[IdempotencyToken]
    baseModelIdentifier: BaseModelIdentifier
    customizationType: Optional[CustomizationType]
    customModelKmsKeyId: Optional[KmsKeyId]
    jobTags: Optional[TagList]
    customModelTags: Optional[TagList]
    trainingDataConfig: TrainingDataConfig
    validationDataConfig: Optional[ValidationDataConfig]
    outputDataConfig: OutputDataConfig
    hyperParameters: Optional[ModelCustomizationHyperParameters]
    vpcConfig: Optional[VpcConfig]
    customizationConfig: Optional[CustomizationConfig]


class CreateModelCustomizationJobResponse(TypedDict, total=False):
    jobArn: ModelCustomizationJobArn


class CreateModelImportJobRequest(ServiceRequest):
    jobName: JobName
    importedModelName: ImportedModelName
    roleArn: RoleArn
    modelDataSource: ModelDataSource
    jobTags: Optional[TagList]
    importedModelTags: Optional[TagList]
    clientRequestToken: Optional[IdempotencyToken]
    vpcConfig: Optional[VpcConfig]
    importedModelKmsKeyId: Optional[KmsKeyId]


class CreateModelImportJobResponse(TypedDict, total=False):
    jobArn: ModelImportJobArn


class ModelInvocationJobS3OutputDataConfig(TypedDict, total=False):
    """Contains the configuration of the S3 location of the output data."""

    s3Uri: S3Uri
    s3EncryptionKeyId: Optional[KmsKeyId]
    s3BucketOwner: Optional[AccountId]


class ModelInvocationJobOutputDataConfig(TypedDict, total=False):
    """Contains the configuration of the S3 location of the output data."""

    s3OutputDataConfig: Optional[ModelInvocationJobS3OutputDataConfig]


class ModelInvocationJobS3InputDataConfig(TypedDict, total=False):
    """Contains the configuration of the S3 location of the input data."""

    s3InputFormat: Optional[S3InputFormat]
    s3Uri: S3Uri
    s3BucketOwner: Optional[AccountId]


class ModelInvocationJobInputDataConfig(TypedDict, total=False):
    """Details about the location of the input to the batch inference job."""

    s3InputDataConfig: Optional[ModelInvocationJobS3InputDataConfig]


class CreateModelInvocationJobRequest(ServiceRequest):
    jobName: ModelInvocationJobName
    roleArn: RoleArn
    clientRequestToken: Optional[ModelInvocationIdempotencyToken]
    modelId: ModelId
    inputDataConfig: ModelInvocationJobInputDataConfig
    outputDataConfig: ModelInvocationJobOutputDataConfig
    vpcConfig: Optional[VpcConfig]
    timeoutDurationInHours: Optional[ModelInvocationJobTimeoutDurationInHours]
    tags: Optional[TagList]


class CreateModelInvocationJobResponse(TypedDict, total=False):
    jobArn: ModelInvocationJobArn


class PromptRouterTargetModel(TypedDict, total=False):
    """The target model for a prompt router."""

    modelArn: PromptRouterTargetModelArn


class RoutingCriteria(TypedDict, total=False):
    """Routing criteria for a prompt router."""

    responseQualityDifference: RoutingCriteriaResponseQualityDifferenceDouble


PromptRouterTargetModels = List[PromptRouterTargetModel]


class CreatePromptRouterRequest(ServiceRequest):
    clientRequestToken: Optional[IdempotencyToken]
    promptRouterName: PromptRouterName
    models: PromptRouterTargetModels
    description: Optional[PromptRouterDescription]
    routingCriteria: RoutingCriteria
    fallbackModel: PromptRouterTargetModel
    tags: Optional[TagList]


class CreatePromptRouterResponse(TypedDict, total=False):
    promptRouterArn: Optional[PromptRouterArn]


class CreateProvisionedModelThroughputRequest(ServiceRequest):
    clientRequestToken: Optional[IdempotencyToken]
    modelUnits: PositiveInteger
    provisionedModelName: ProvisionedModelName
    modelId: ModelIdentifier
    commitmentDuration: Optional[CommitmentDuration]
    tags: Optional[TagList]


class CreateProvisionedModelThroughputResponse(TypedDict, total=False):
    provisionedModelArn: ProvisionedModelArn


class CustomModelDeploymentSummary(TypedDict, total=False):
    """Contains summary information about a custom model deployment, including
    its ARN, name, status, and associated custom model.
    """

    customModelDeploymentArn: CustomModelDeploymentArn
    customModelDeploymentName: ModelDeploymentName
    modelArn: ModelArn
    createdAt: Timestamp
    status: CustomModelDeploymentStatus
    lastUpdatedAt: Optional[Timestamp]
    failureMessage: Optional[ErrorMessage]


CustomModelDeploymentSummaryList = List[CustomModelDeploymentSummary]


class CustomModelSummary(TypedDict, total=False):
    """Summary information for a custom model."""

    modelArn: CustomModelArn
    modelName: CustomModelName
    creationTime: Timestamp
    baseModelArn: ModelArn
    baseModelName: ModelName
    customizationType: Optional[CustomizationType]
    ownerAccountId: Optional[AccountId]
    modelStatus: Optional[ModelStatus]


CustomModelSummaryList = List[CustomModelSummary]


class CustomModelUnits(TypedDict, total=False):
    """A ``CustomModelUnit`` (CMU) is an abstract view of the hardware
    utilization that Amazon Bedrock needs to host a single copy of your
    custom model. A model copy represents a single instance of your imported
    model that is ready to serve inference requests. Amazon Bedrock
    determines the number of custom model units that a model copy needs when
    you import the custom model.

    You can use ``CustomModelUnits`` to estimate the cost of running your
    custom model. For more information, see Calculate the cost of running a
    custom model in the Amazon Bedrock user guide.
    """

    customModelUnitsPerModelCopy: Optional[Integer]
    customModelUnitsVersion: Optional[CustomModelUnitsVersion]


class DataProcessingDetails(TypedDict, total=False):
    """For a Distillation job, the status details for the data processing
    sub-task of the job.
    """

    status: Optional[JobStatusDetails]
    creationTime: Optional[Timestamp]
    lastModifiedTime: Optional[Timestamp]


class DeleteAutomatedReasoningPolicyBuildWorkflowRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    lastUpdatedAt: Timestamp


class DeleteAutomatedReasoningPolicyBuildWorkflowResponse(TypedDict, total=False):
    pass


class DeleteAutomatedReasoningPolicyRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn


class DeleteAutomatedReasoningPolicyResponse(TypedDict, total=False):
    pass


class DeleteAutomatedReasoningPolicyTestCaseRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    testCaseId: AutomatedReasoningPolicyTestCaseId
    lastUpdatedAt: Timestamp


class DeleteAutomatedReasoningPolicyTestCaseResponse(TypedDict, total=False):
    pass


class DeleteCustomModelDeploymentRequest(ServiceRequest):
    customModelDeploymentIdentifier: CustomModelDeploymentIdentifier


class DeleteCustomModelDeploymentResponse(TypedDict, total=False):
    pass


class DeleteCustomModelRequest(ServiceRequest):
    modelIdentifier: ModelIdentifier


class DeleteCustomModelResponse(TypedDict, total=False):
    pass


class DeleteFoundationModelAgreementRequest(ServiceRequest):
    modelId: BedrockModelId


class DeleteFoundationModelAgreementResponse(TypedDict, total=False):
    pass


class DeleteGuardrailRequest(ServiceRequest):
    guardrailIdentifier: GuardrailIdentifier
    guardrailVersion: Optional[GuardrailNumericalVersion]


class DeleteGuardrailResponse(TypedDict, total=False):
    pass


class DeleteImportedModelRequest(ServiceRequest):
    modelIdentifier: ImportedModelIdentifier


class DeleteImportedModelResponse(TypedDict, total=False):
    pass


class DeleteInferenceProfileRequest(ServiceRequest):
    inferenceProfileIdentifier: InferenceProfileIdentifier


class DeleteInferenceProfileResponse(TypedDict, total=False):
    pass


class DeleteMarketplaceModelEndpointRequest(ServiceRequest):
    endpointArn: Arn


class DeleteMarketplaceModelEndpointResponse(TypedDict, total=False):
    pass


class DeleteModelInvocationLoggingConfigurationRequest(ServiceRequest):
    pass


class DeleteModelInvocationLoggingConfigurationResponse(TypedDict, total=False):
    pass


class DeletePromptRouterRequest(ServiceRequest):
    promptRouterArn: PromptRouterArn


class DeletePromptRouterResponse(TypedDict, total=False):
    pass


class DeleteProvisionedModelThroughputRequest(ServiceRequest):
    provisionedModelId: ProvisionedModelId


class DeleteProvisionedModelThroughputResponse(TypedDict, total=False):
    pass


class DeregisterMarketplaceModelEndpointRequest(ServiceRequest):
    endpointArn: Arn


class DeregisterMarketplaceModelEndpointResponse(TypedDict, total=False):
    pass


class DimensionalPriceRate(TypedDict, total=False):
    """Dimensional price rate."""

    dimension: Optional[String]
    price: Optional[String]
    description: Optional[String]
    unit: Optional[String]


ErrorMessages = List[ErrorMessage]
EvaluationBedrockKnowledgeBaseIdentifiers = List[KnowledgeBaseId]
EvaluationBedrockModelIdentifiers = List[EvaluationBedrockModelIdentifier]
EvaluationPrecomputedRagSourceIdentifiers = List[EvaluationPrecomputedRagSourceIdentifier]


class EvaluationRagConfigSummary(TypedDict, total=False):
    """A summary of the RAG resources used in an Amazon Bedrock Knowledge Base
    evaluation job. These resources can be Knowledge Bases in Amazon Bedrock
    or RAG sources outside of Amazon Bedrock that you use to generate your
    own inference response data.
    """

    bedrockKnowledgeBaseIdentifiers: Optional[EvaluationBedrockKnowledgeBaseIdentifiers]
    precomputedRagSourceIdentifiers: Optional[EvaluationPrecomputedRagSourceIdentifiers]


EvaluationPrecomputedInferenceSourceIdentifiers = List[
    EvaluationPrecomputedInferenceSourceIdentifier
]


class EvaluationModelConfigSummary(TypedDict, total=False):
    """A summary of the models used in an Amazon Bedrock model evaluation job.
    These resources can be models in Amazon Bedrock or models outside of
    Amazon Bedrock that you use to generate your own inference response
    data.
    """

    bedrockModelIdentifiers: Optional[EvaluationBedrockModelIdentifiers]
    precomputedInferenceSourceIdentifiers: Optional[EvaluationPrecomputedInferenceSourceIdentifiers]


class EvaluationInferenceConfigSummary(TypedDict, total=False):
    """Identifies the models, Knowledge Bases, or other RAG sources evaluated
    in a model or Knowledge Base evaluation job.
    """

    modelConfigSummary: Optional[EvaluationModelConfigSummary]
    ragConfigSummary: Optional[EvaluationRagConfigSummary]


EvaluatorModelIdentifiers = List[EvaluatorModelIdentifier]
EvaluationTaskTypes = List[EvaluationTaskType]


class EvaluationSummary(TypedDict, total=False):
    """Summary information of an evaluation job."""

    jobArn: EvaluationJobArn
    jobName: EvaluationJobName
    status: EvaluationJobStatus
    creationTime: Timestamp
    jobType: EvaluationJobType
    evaluationTaskTypes: EvaluationTaskTypes
    modelIdentifiers: Optional[EvaluationBedrockModelIdentifiers]
    ragIdentifiers: Optional[EvaluationBedrockKnowledgeBaseIdentifiers]
    evaluatorModelIdentifiers: Optional[EvaluatorModelIdentifiers]
    customMetricsEvaluatorModelIdentifiers: Optional[EvaluatorModelIdentifiers]
    inferenceConfigSummary: Optional[EvaluationInferenceConfigSummary]
    applicationType: Optional[ApplicationType]


EvaluationSummaries = List[EvaluationSummary]


class ExportAutomatedReasoningPolicyVersionRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn


class ExportAutomatedReasoningPolicyVersionResponse(TypedDict, total=False):
    policyDefinition: AutomatedReasoningPolicyDefinition


class FoundationModelLifecycle(TypedDict, total=False):
    """Details about whether a model version is available or deprecated."""

    status: FoundationModelLifecycleStatus


InferenceTypeList = List[InferenceType]
ModelCustomizationList = List[ModelCustomization]
ModelModalityList = List[ModelModality]


class FoundationModelDetails(TypedDict, total=False):
    """Information about a foundation model."""

    modelArn: FoundationModelArn
    modelId: BedrockModelId
    modelName: Optional[BrandedName]
    providerName: Optional[BrandedName]
    inputModalities: Optional[ModelModalityList]
    outputModalities: Optional[ModelModalityList]
    responseStreamingSupported: Optional[Boolean]
    customizationsSupported: Optional[ModelCustomizationList]
    inferenceTypesSupported: Optional[InferenceTypeList]
    modelLifecycle: Optional[FoundationModelLifecycle]


class FoundationModelSummary(TypedDict, total=False):
    """Summary information for a foundation model."""

    modelArn: FoundationModelArn
    modelId: BedrockModelId
    modelName: Optional[BrandedName]
    providerName: Optional[BrandedName]
    inputModalities: Optional[ModelModalityList]
    outputModalities: Optional[ModelModalityList]
    responseStreamingSupported: Optional[Boolean]
    customizationsSupported: Optional[ModelCustomizationList]
    inferenceTypesSupported: Optional[InferenceTypeList]
    modelLifecycle: Optional[FoundationModelLifecycle]


FoundationModelSummaryList = List[FoundationModelSummary]


class GetAutomatedReasoningPolicyAnnotationsRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId


class GetAutomatedReasoningPolicyAnnotationsResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    name: AutomatedReasoningPolicyName
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    annotations: AutomatedReasoningPolicyAnnotationList
    annotationSetHash: AutomatedReasoningPolicyHash
    updatedAt: Timestamp


class GetAutomatedReasoningPolicyBuildWorkflowRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId


class GetAutomatedReasoningPolicyBuildWorkflowResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    status: AutomatedReasoningPolicyBuildWorkflowStatus
    buildWorkflowType: AutomatedReasoningPolicyBuildWorkflowType
    documentName: Optional[AutomatedReasoningPolicyBuildDocumentName]
    documentContentType: Optional[AutomatedReasoningPolicyBuildDocumentContentType]
    documentDescription: Optional[AutomatedReasoningPolicyBuildDocumentDescription]
    createdAt: Timestamp
    updatedAt: Timestamp


class GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    assetType: AutomatedReasoningPolicyBuildResultAssetType


class GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    buildWorkflowAssets: Optional[AutomatedReasoningPolicyBuildResultAssets]


class GetAutomatedReasoningPolicyNextScenarioRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId


class GetAutomatedReasoningPolicyNextScenarioResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    scenario: Optional[AutomatedReasoningPolicyScenario]


class GetAutomatedReasoningPolicyRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn


class GetAutomatedReasoningPolicyResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    name: AutomatedReasoningPolicyName
    version: AutomatedReasoningPolicyVersion
    policyId: AutomatedReasoningPolicyId
    description: Optional[AutomatedReasoningPolicyDescription]
    definitionHash: AutomatedReasoningPolicyHash
    createdAt: Optional[Timestamp]
    updatedAt: Timestamp


class GetAutomatedReasoningPolicyTestCaseRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    testCaseId: AutomatedReasoningPolicyTestCaseId


class GetAutomatedReasoningPolicyTestCaseResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    testCase: AutomatedReasoningPolicyTestCase


class GetAutomatedReasoningPolicyTestResultRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    testCaseId: AutomatedReasoningPolicyTestCaseId


class GetAutomatedReasoningPolicyTestResultResponse(TypedDict, total=False):
    testResult: AutomatedReasoningPolicyTestResult


class GetCustomModelDeploymentRequest(ServiceRequest):
    customModelDeploymentIdentifier: CustomModelDeploymentIdentifier


class GetCustomModelDeploymentResponse(TypedDict, total=False):
    customModelDeploymentArn: CustomModelDeploymentArn
    modelDeploymentName: ModelDeploymentName
    modelArn: CustomModelArn
    createdAt: Timestamp
    status: CustomModelDeploymentStatus
    description: Optional[CustomModelDeploymentDescription]
    failureMessage: Optional[ErrorMessage]
    lastUpdatedAt: Optional[Timestamp]


class GetCustomModelRequest(ServiceRequest):
    modelIdentifier: ModelIdentifier


class ValidatorMetric(TypedDict, total=False):
    """The metric for the validator."""

    validationLoss: Optional[MetricFloat]


ValidationMetrics = List[ValidatorMetric]


class TrainingMetrics(TypedDict, total=False):
    """Metrics associated with the custom job."""

    trainingLoss: Optional[MetricFloat]


class GetCustomModelResponse(TypedDict, total=False):
    modelArn: ModelArn
    modelName: CustomModelName
    jobName: Optional[JobName]
    jobArn: Optional[ModelCustomizationJobArn]
    baseModelArn: Optional[ModelArn]
    customizationType: Optional[CustomizationType]
    modelKmsKeyArn: Optional[KmsKeyArn]
    hyperParameters: Optional[ModelCustomizationHyperParameters]
    trainingDataConfig: Optional[TrainingDataConfig]
    validationDataConfig: Optional[ValidationDataConfig]
    outputDataConfig: Optional[OutputDataConfig]
    trainingMetrics: Optional[TrainingMetrics]
    validationMetrics: Optional[ValidationMetrics]
    creationTime: Timestamp
    customizationConfig: Optional[CustomizationConfig]
    modelStatus: Optional[ModelStatus]
    failureMessage: Optional[ErrorMessage]


class GetEvaluationJobRequest(ServiceRequest):
    jobIdentifier: EvaluationJobIdentifier


class GetEvaluationJobResponse(TypedDict, total=False):
    jobName: EvaluationJobName
    status: EvaluationJobStatus
    jobArn: EvaluationJobArn
    jobDescription: Optional[EvaluationJobDescription]
    roleArn: RoleArn
    customerEncryptionKeyId: Optional[KmsKeyId]
    jobType: EvaluationJobType
    applicationType: Optional[ApplicationType]
    evaluationConfig: EvaluationConfig
    inferenceConfig: EvaluationInferenceConfig
    outputDataConfig: EvaluationOutputDataConfig
    creationTime: Timestamp
    lastModifiedTime: Optional[Timestamp]
    failureMessages: Optional[ErrorMessages]


class GetFoundationModelAvailabilityRequest(ServiceRequest):
    modelId: BedrockModelId


class GetFoundationModelAvailabilityResponse(TypedDict, total=False):
    modelId: BedrockModelId
    agreementAvailability: AgreementAvailability
    authorizationStatus: AuthorizationStatus
    entitlementAvailability: EntitlementAvailability
    regionAvailability: RegionAvailability


class GetFoundationModelRequest(ServiceRequest):
    modelIdentifier: ModelIdentifier


class GetFoundationModelResponse(TypedDict, total=False):
    modelDetails: Optional[FoundationModelDetails]


class GetGuardrailRequest(ServiceRequest):
    guardrailIdentifier: GuardrailIdentifier
    guardrailVersion: Optional[GuardrailVersion]


GuardrailFailureRecommendations = List[GuardrailFailureRecommendation]
GuardrailStatusReasons = List[GuardrailStatusReason]


class GuardrailCrossRegionDetails(TypedDict, total=False):
    """Contains details about the system-defined guardrail profile that you're
    using with your guardrail for cross-Region inference.

    For more information, see the `Amazon Bedrock User
    Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html>`__.
    """

    guardrailProfileId: Optional[GuardrailCrossRegionGuardrailProfileId]
    guardrailProfileArn: Optional[GuardrailCrossRegionGuardrailProfileArn]


GuardrailAutomatedReasoningPolicyPoliciesList = List[AutomatedReasoningPolicyArn]


class GuardrailAutomatedReasoningPolicy(TypedDict, total=False):
    """Represents the configuration of Automated Reasoning policies within a
    Amazon Bedrock Guardrail, including the policies to apply and confidence
    thresholds.
    """

    policies: GuardrailAutomatedReasoningPolicyPoliciesList
    confidenceThreshold: Optional[AutomatedReasoningConfidenceFilterThreshold]


class GuardrailContextualGroundingFilter(TypedDict, total=False):
    type: GuardrailContextualGroundingFilterType
    threshold: GuardrailContextualGroundingFilterThresholdDouble
    action: Optional[GuardrailContextualGroundingAction]
    enabled: Optional[Boolean]


GuardrailContextualGroundingFilters = List[GuardrailContextualGroundingFilter]


class GuardrailContextualGroundingPolicy(TypedDict, total=False):
    """The details for the guardrails contextual grounding policy."""

    filters: GuardrailContextualGroundingFilters


class GuardrailRegex(TypedDict, total=False):
    """The regular expression configured for the guardrail."""

    name: GuardrailRegexNameString
    description: Optional[GuardrailRegexDescriptionString]
    pattern: GuardrailRegexPatternString
    action: GuardrailSensitiveInformationAction
    inputAction: Optional[GuardrailSensitiveInformationAction]
    outputAction: Optional[GuardrailSensitiveInformationAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailRegexes = List[GuardrailRegex]


class GuardrailPiiEntity(TypedDict, total=False):
    type: GuardrailPiiEntityType
    action: GuardrailSensitiveInformationAction
    inputAction: Optional[GuardrailSensitiveInformationAction]
    outputAction: Optional[GuardrailSensitiveInformationAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailPiiEntities = List[GuardrailPiiEntity]


class GuardrailSensitiveInformationPolicy(TypedDict, total=False):
    """Contains details about PII entities and regular expressions configured
    for the guardrail.
    """

    piiEntities: Optional[GuardrailPiiEntities]
    regexes: Optional[GuardrailRegexes]


class GuardrailManagedWords(TypedDict, total=False):
    type: GuardrailManagedWordsType
    inputAction: Optional[GuardrailWordAction]
    outputAction: Optional[GuardrailWordAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailManagedWordLists = List[GuardrailManagedWords]


class GuardrailWord(TypedDict, total=False):
    """A word configured for the guardrail."""

    text: GuardrailWordTextString
    inputAction: Optional[GuardrailWordAction]
    outputAction: Optional[GuardrailWordAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailWords = List[GuardrailWord]


class GuardrailWordPolicy(TypedDict, total=False):
    """Contains details about the word policy configured for the guardrail."""

    words: Optional[GuardrailWords]
    managedWordLists: Optional[GuardrailManagedWordLists]


class GuardrailContentFiltersTier(TypedDict, total=False):
    """The tier that your guardrail uses for content filters."""

    tierName: GuardrailContentFiltersTierName


class GuardrailContentFilter(TypedDict, total=False):
    type: GuardrailContentFilterType
    inputStrength: GuardrailFilterStrength
    outputStrength: GuardrailFilterStrength
    inputModalities: Optional[GuardrailModalities]
    outputModalities: Optional[GuardrailModalities]
    inputAction: Optional[GuardrailContentFilterAction]
    outputAction: Optional[GuardrailContentFilterAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailContentFilters = List[GuardrailContentFilter]


class GuardrailContentPolicy(TypedDict, total=False):
    """Contains details about how to handle harmful content.

    This data type is used in the following API operations:

    -  `GetGuardrail response
       body <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetGuardrail.html#API_GetGuardrail_ResponseSyntax>`__
    """

    filters: Optional[GuardrailContentFilters]
    tier: Optional[GuardrailContentFiltersTier]


class GuardrailTopicsTier(TypedDict, total=False):
    """The tier that your guardrail uses for denied topic filters."""

    tierName: GuardrailTopicsTierName


class GuardrailTopic(TypedDict, total=False):
    name: GuardrailTopicName
    definition: GuardrailTopicDefinition
    examples: Optional[GuardrailTopicExamples]
    type: Optional[GuardrailTopicType]
    inputAction: Optional[GuardrailTopicAction]
    outputAction: Optional[GuardrailTopicAction]
    inputEnabled: Optional[Boolean]
    outputEnabled: Optional[Boolean]


GuardrailTopics = List[GuardrailTopic]


class GuardrailTopicPolicy(TypedDict, total=False):
    """Contains details about topics that the guardrail should identify and
    deny.

    This data type is used in the following API operations:

    -  `GetGuardrail response
       body <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetGuardrail.html#API_GetGuardrail_ResponseSyntax>`__
    """

    topics: GuardrailTopics
    tier: Optional[GuardrailTopicsTier]


class GetGuardrailResponse(TypedDict, total=False):
    name: GuardrailName
    description: Optional[GuardrailDescription]
    guardrailId: GuardrailId
    guardrailArn: GuardrailArn
    version: GuardrailVersion
    status: GuardrailStatus
    topicPolicy: Optional[GuardrailTopicPolicy]
    contentPolicy: Optional[GuardrailContentPolicy]
    wordPolicy: Optional[GuardrailWordPolicy]
    sensitiveInformationPolicy: Optional[GuardrailSensitiveInformationPolicy]
    contextualGroundingPolicy: Optional[GuardrailContextualGroundingPolicy]
    automatedReasoningPolicy: Optional[GuardrailAutomatedReasoningPolicy]
    crossRegionDetails: Optional[GuardrailCrossRegionDetails]
    createdAt: Timestamp
    updatedAt: Timestamp
    statusReasons: Optional[GuardrailStatusReasons]
    failureRecommendations: Optional[GuardrailFailureRecommendations]
    blockedInputMessaging: GuardrailBlockedMessaging
    blockedOutputsMessaging: GuardrailBlockedMessaging
    kmsKeyArn: Optional[KmsKeyArn]


class GetImportedModelRequest(ServiceRequest):
    modelIdentifier: ImportedModelIdentifier


class GetImportedModelResponse(TypedDict, total=False):
    modelArn: Optional[ImportedModelArn]
    modelName: Optional[ImportedModelName]
    jobName: Optional[JobName]
    jobArn: Optional[ModelImportJobArn]
    modelDataSource: Optional[ModelDataSource]
    creationTime: Optional[Timestamp]
    modelArchitecture: Optional[String]
    modelKmsKeyArn: Optional[KmsKeyArn]
    instructSupported: Optional[InstructSupported]
    customModelUnits: Optional[CustomModelUnits]


class GetInferenceProfileRequest(ServiceRequest):
    inferenceProfileIdentifier: InferenceProfileIdentifier


class InferenceProfileModel(TypedDict, total=False):
    """Contains information about a model."""

    modelArn: Optional[FoundationModelArn]


InferenceProfileModels = List[InferenceProfileModel]


class GetInferenceProfileResponse(TypedDict, total=False):
    inferenceProfileName: InferenceProfileName
    description: Optional[InferenceProfileDescription]
    createdAt: Optional[Timestamp]
    updatedAt: Optional[Timestamp]
    inferenceProfileArn: InferenceProfileArn
    models: InferenceProfileModels
    inferenceProfileId: InferenceProfileId
    status: InferenceProfileStatus
    type: InferenceProfileType


class GetMarketplaceModelEndpointRequest(ServiceRequest):
    endpointArn: Arn


class GetMarketplaceModelEndpointResponse(TypedDict, total=False):
    marketplaceModelEndpoint: Optional[MarketplaceModelEndpoint]


class GetModelCopyJobRequest(ServiceRequest):
    jobArn: ModelCopyJobArn


class GetModelCopyJobResponse(TypedDict, total=False):
    jobArn: ModelCopyJobArn
    status: ModelCopyJobStatus
    creationTime: Timestamp
    targetModelArn: CustomModelArn
    targetModelName: Optional[CustomModelName]
    sourceAccountId: AccountId
    sourceModelArn: ModelArn
    targetModelKmsKeyArn: Optional[KmsKeyArn]
    targetModelTags: Optional[TagList]
    failureMessage: Optional[ErrorMessage]
    sourceModelName: Optional[CustomModelName]


class GetModelCustomizationJobRequest(ServiceRequest):
    jobIdentifier: ModelCustomizationJobIdentifier


class TrainingDetails(TypedDict, total=False):
    """For a Distillation job, the status details for the training sub-task of
    the job.
    """

    status: Optional[JobStatusDetails]
    creationTime: Optional[Timestamp]
    lastModifiedTime: Optional[Timestamp]


class ValidationDetails(TypedDict, total=False):
    """For a Distillation job, the status details for the validation sub-task
    of the job.
    """

    status: Optional[JobStatusDetails]
    creationTime: Optional[Timestamp]
    lastModifiedTime: Optional[Timestamp]


class StatusDetails(TypedDict, total=False):
    """For a Distillation job, the status details for sub-tasks of the job.
    Possible statuses for each sub-task include the following:

    -  NotStarted

    -  InProgress

    -  Completed

    -  Stopping

    -  Stopped

    -  Failed
    """

    validationDetails: Optional[ValidationDetails]
    dataProcessingDetails: Optional[DataProcessingDetails]
    trainingDetails: Optional[TrainingDetails]


class GetModelCustomizationJobResponse(TypedDict, total=False):
    jobArn: ModelCustomizationJobArn
    jobName: JobName
    outputModelName: CustomModelName
    outputModelArn: Optional[CustomModelArn]
    clientRequestToken: Optional[IdempotencyToken]
    roleArn: RoleArn
    status: Optional[ModelCustomizationJobStatus]
    statusDetails: Optional[StatusDetails]
    failureMessage: Optional[ErrorMessage]
    creationTime: Timestamp
    lastModifiedTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    baseModelArn: FoundationModelArn
    hyperParameters: Optional[ModelCustomizationHyperParameters]
    trainingDataConfig: TrainingDataConfig
    validationDataConfig: ValidationDataConfig
    outputDataConfig: OutputDataConfig
    customizationType: Optional[CustomizationType]
    outputModelKmsKeyArn: Optional[KmsKeyArn]
    trainingMetrics: Optional[TrainingMetrics]
    validationMetrics: Optional[ValidationMetrics]
    vpcConfig: Optional[VpcConfig]
    customizationConfig: Optional[CustomizationConfig]


class GetModelImportJobRequest(ServiceRequest):
    jobIdentifier: ModelImportJobIdentifier


class GetModelImportJobResponse(TypedDict, total=False):
    jobArn: Optional[ModelImportJobArn]
    jobName: Optional[JobName]
    importedModelName: Optional[ImportedModelName]
    importedModelArn: Optional[ImportedModelArn]
    roleArn: Optional[RoleArn]
    modelDataSource: Optional[ModelDataSource]
    status: Optional[ModelImportJobStatus]
    failureMessage: Optional[ErrorMessage]
    creationTime: Optional[Timestamp]
    lastModifiedTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    vpcConfig: Optional[VpcConfig]
    importedModelKmsKeyArn: Optional[KmsKeyArn]


class GetModelInvocationJobRequest(ServiceRequest):
    jobIdentifier: ModelInvocationJobIdentifier


class GetModelInvocationJobResponse(TypedDict, total=False):
    jobArn: ModelInvocationJobArn
    jobName: Optional[ModelInvocationJobName]
    modelId: ModelId
    clientRequestToken: Optional[ModelInvocationIdempotencyToken]
    roleArn: RoleArn
    status: Optional[ModelInvocationJobStatus]
    message: Optional[Message]
    submitTime: Timestamp
    lastModifiedTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    inputDataConfig: ModelInvocationJobInputDataConfig
    outputDataConfig: ModelInvocationJobOutputDataConfig
    vpcConfig: Optional[VpcConfig]
    timeoutDurationInHours: Optional[ModelInvocationJobTimeoutDurationInHours]
    jobExpirationTime: Optional[Timestamp]


class GetModelInvocationLoggingConfigurationRequest(ServiceRequest):
    pass


class LoggingConfig(TypedDict, total=False):
    """Configuration fields for invocation logging."""

    cloudWatchConfig: Optional[CloudWatchConfig]
    s3Config: Optional[S3Config]
    textDataDeliveryEnabled: Optional[Boolean]
    imageDataDeliveryEnabled: Optional[Boolean]
    embeddingDataDeliveryEnabled: Optional[Boolean]
    videoDataDeliveryEnabled: Optional[Boolean]


class GetModelInvocationLoggingConfigurationResponse(TypedDict, total=False):
    loggingConfig: Optional[LoggingConfig]


class GetPromptRouterRequest(ServiceRequest):
    promptRouterArn: PromptRouterArn


class GetPromptRouterResponse(TypedDict, total=False):
    promptRouterName: PromptRouterName
    routingCriteria: RoutingCriteria
    description: Optional[PromptRouterDescription]
    createdAt: Optional[Timestamp]
    updatedAt: Optional[Timestamp]
    promptRouterArn: PromptRouterArn
    models: PromptRouterTargetModels
    fallbackModel: PromptRouterTargetModel
    status: PromptRouterStatus
    type: PromptRouterType


class GetProvisionedModelThroughputRequest(ServiceRequest):
    provisionedModelId: ProvisionedModelId


class GetProvisionedModelThroughputResponse(TypedDict, total=False):
    modelUnits: PositiveInteger
    desiredModelUnits: PositiveInteger
    provisionedModelName: ProvisionedModelName
    provisionedModelArn: ProvisionedModelArn
    modelArn: ModelArn
    desiredModelArn: ModelArn
    foundationModelArn: FoundationModelArn
    status: ProvisionedModelStatus
    creationTime: Timestamp
    lastModifiedTime: Timestamp
    failureMessage: Optional[ErrorMessage]
    commitmentDuration: Optional[CommitmentDuration]
    commitmentExpirationTime: Optional[Timestamp]


class GetUseCaseForModelAccessRequest(ServiceRequest):
    pass


class GetUseCaseForModelAccessResponse(TypedDict, total=False):
    formData: AcknowledgementFormDataBody


class GuardrailSummary(TypedDict, total=False):
    """Contains details about a guardrail.

    This data type is used in the following API operations:

    -  `ListGuardrails response
       body <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListGuardrails.html#API_ListGuardrails_ResponseSyntax>`__
    """

    id: GuardrailId
    arn: GuardrailArn
    status: GuardrailStatus
    name: GuardrailName
    description: Optional[GuardrailDescription]
    version: GuardrailVersion
    createdAt: Timestamp
    updatedAt: Timestamp
    crossRegionDetails: Optional[GuardrailCrossRegionDetails]


GuardrailSummaries = List[GuardrailSummary]


class ImportedModelSummary(TypedDict, total=False):
    """Information about the imported model."""

    modelArn: ImportedModelArn
    modelName: ImportedModelName
    creationTime: Timestamp
    instructSupported: Optional[InstructSupported]
    modelArchitecture: Optional[ModelArchitecture]


ImportedModelSummaryList = List[ImportedModelSummary]


class InferenceProfileSummary(TypedDict, total=False):
    inferenceProfileName: InferenceProfileName
    description: Optional[InferenceProfileDescription]
    createdAt: Optional[Timestamp]
    updatedAt: Optional[Timestamp]
    inferenceProfileArn: InferenceProfileArn
    models: InferenceProfileModels
    inferenceProfileId: InferenceProfileId
    status: InferenceProfileStatus
    type: InferenceProfileType


InferenceProfileSummaries = List[InferenceProfileSummary]


class LegalTerm(TypedDict, total=False):
    """The legal term of the agreement."""

    url: Optional[String]


class ListAutomatedReasoningPoliciesRequest(ServiceRequest):
    policyArn: Optional[AutomatedReasoningPolicyArn]
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListAutomatedReasoningPoliciesResponse(TypedDict, total=False):
    automatedReasoningPolicySummaries: AutomatedReasoningPolicySummaries
    nextToken: Optional[PaginationToken]


class ListAutomatedReasoningPolicyBuildWorkflowsRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListAutomatedReasoningPolicyBuildWorkflowsResponse(TypedDict, total=False):
    automatedReasoningPolicyBuildWorkflowSummaries: AutomatedReasoningPolicyBuildWorkflowSummaries
    nextToken: Optional[PaginationToken]


class ListAutomatedReasoningPolicyTestCasesRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListAutomatedReasoningPolicyTestCasesResponse(TypedDict, total=False):
    testCases: AutomatedReasoningPolicyTestCaseList
    nextToken: Optional[PaginationToken]


class ListAutomatedReasoningPolicyTestResultsRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListAutomatedReasoningPolicyTestResultsResponse(TypedDict, total=False):
    testResults: AutomatedReasoningPolicyTestList
    nextToken: Optional[PaginationToken]


class ListCustomModelDeploymentsRequest(ServiceRequest):
    createdBefore: Optional[Timestamp]
    createdAfter: Optional[Timestamp]
    nameContains: Optional[ModelDeploymentName]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortModelsBy]
    sortOrder: Optional[SortOrder]
    statusEquals: Optional[CustomModelDeploymentStatus]
    modelArnEquals: Optional[CustomModelArn]


class ListCustomModelDeploymentsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    modelDeploymentSummaries: Optional[CustomModelDeploymentSummaryList]


class ListCustomModelsRequest(ServiceRequest):
    creationTimeBefore: Optional[Timestamp]
    creationTimeAfter: Optional[Timestamp]
    nameContains: Optional[CustomModelName]
    baseModelArnEquals: Optional[ModelArn]
    foundationModelArnEquals: Optional[FoundationModelArn]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortModelsBy]
    sortOrder: Optional[SortOrder]
    isOwned: Optional[Boolean]
    modelStatus: Optional[ModelStatus]


class ListCustomModelsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    modelSummaries: Optional[CustomModelSummaryList]


class ListEvaluationJobsRequest(ServiceRequest):
    creationTimeAfter: Optional[Timestamp]
    creationTimeBefore: Optional[Timestamp]
    statusEquals: Optional[EvaluationJobStatus]
    applicationTypeEquals: Optional[ApplicationType]
    nameContains: Optional[EvaluationJobName]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortJobsBy]
    sortOrder: Optional[SortOrder]


class ListEvaluationJobsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    jobSummaries: Optional[EvaluationSummaries]


class ListFoundationModelAgreementOffersRequest(ServiceRequest):
    modelId: BedrockModelId
    offerType: Optional[OfferType]


class ValidityTerm(TypedDict, total=False):
    """Describes the validity terms."""

    agreementDuration: Optional[String]


class SupportTerm(TypedDict, total=False):
    """Describes a support term."""

    refundPolicyDescription: Optional[String]


RateCard = List[DimensionalPriceRate]


class PricingTerm(TypedDict, total=False):
    """Describes the usage-based pricing term."""

    rateCard: RateCard


class TermDetails(TypedDict, total=False):
    """Describes the usage terms of an offer."""

    usageBasedPricingTerm: PricingTerm
    legalTerm: LegalTerm
    supportTerm: SupportTerm
    validityTerm: Optional[ValidityTerm]


class Offer(TypedDict, total=False):
    """An offer dictates usage terms for the model."""

    offerId: Optional[OfferId]
    offerToken: OfferToken
    termDetails: TermDetails


Offers = List[Offer]


class ListFoundationModelAgreementOffersResponse(TypedDict, total=False):
    modelId: BedrockModelId
    offers: Offers


class ListFoundationModelsRequest(ServiceRequest):
    byProvider: Optional[Provider]
    byCustomizationType: Optional[ModelCustomization]
    byOutputModality: Optional[ModelModality]
    byInferenceType: Optional[InferenceType]


class ListFoundationModelsResponse(TypedDict, total=False):
    modelSummaries: Optional[FoundationModelSummaryList]


class ListGuardrailsRequest(ServiceRequest):
    guardrailIdentifier: Optional[GuardrailIdentifier]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]


class ListGuardrailsResponse(TypedDict, total=False):
    guardrails: GuardrailSummaries
    nextToken: Optional[PaginationToken]


class ListImportedModelsRequest(ServiceRequest):
    creationTimeBefore: Optional[Timestamp]
    creationTimeAfter: Optional[Timestamp]
    nameContains: Optional[ImportedModelName]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortModelsBy]
    sortOrder: Optional[SortOrder]


class ListImportedModelsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    modelSummaries: Optional[ImportedModelSummaryList]


class ListInferenceProfilesRequest(ServiceRequest):
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    typeEquals: Optional[InferenceProfileType]


class ListInferenceProfilesResponse(TypedDict, total=False):
    inferenceProfileSummaries: Optional[InferenceProfileSummaries]
    nextToken: Optional[PaginationToken]


class ListMarketplaceModelEndpointsRequest(ServiceRequest):
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    modelSourceEquals: Optional[ModelSourceIdentifier]


class MarketplaceModelEndpointSummary(TypedDict, total=False):
    """Provides a summary of an endpoint for a model from Amazon Bedrock
    Marketplace.
    """

    endpointArn: Arn
    modelSourceIdentifier: ModelSourceIdentifier
    status: Optional[Status]
    statusMessage: Optional[String]
    createdAt: Timestamp
    updatedAt: Timestamp


MarketplaceModelEndpointSummaries = List[MarketplaceModelEndpointSummary]


class ListMarketplaceModelEndpointsResponse(TypedDict, total=False):
    marketplaceModelEndpoints: Optional[MarketplaceModelEndpointSummaries]
    nextToken: Optional[PaginationToken]


class ListModelCopyJobsRequest(ServiceRequest):
    creationTimeAfter: Optional[Timestamp]
    creationTimeBefore: Optional[Timestamp]
    statusEquals: Optional[ModelCopyJobStatus]
    sourceAccountEquals: Optional[AccountId]
    sourceModelArnEquals: Optional[ModelArn]
    targetModelNameContains: Optional[CustomModelName]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortJobsBy]
    sortOrder: Optional[SortOrder]


class ModelCopyJobSummary(TypedDict, total=False):
    """Contains details about each model copy job.

    This data type is used in the following API operations:

    -  `ListModelCopyJobs
       response <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListModelCopyJobs.html#API_ListModelCopyJobs_ResponseSyntax>`__
    """

    jobArn: ModelCopyJobArn
    status: ModelCopyJobStatus
    creationTime: Timestamp
    targetModelArn: CustomModelArn
    targetModelName: Optional[CustomModelName]
    sourceAccountId: AccountId
    sourceModelArn: ModelArn
    targetModelKmsKeyArn: Optional[KmsKeyArn]
    targetModelTags: Optional[TagList]
    failureMessage: Optional[ErrorMessage]
    sourceModelName: Optional[CustomModelName]


ModelCopyJobSummaries = List[ModelCopyJobSummary]


class ListModelCopyJobsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    modelCopyJobSummaries: Optional[ModelCopyJobSummaries]


class ListModelCustomizationJobsRequest(ServiceRequest):
    creationTimeAfter: Optional[Timestamp]
    creationTimeBefore: Optional[Timestamp]
    statusEquals: Optional[FineTuningJobStatus]
    nameContains: Optional[JobName]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortJobsBy]
    sortOrder: Optional[SortOrder]


class ModelCustomizationJobSummary(TypedDict, total=False):
    """Information about one customization job"""

    jobArn: ModelCustomizationJobArn
    baseModelArn: ModelArn
    jobName: JobName
    status: ModelCustomizationJobStatus
    statusDetails: Optional[StatusDetails]
    lastModifiedTime: Optional[Timestamp]
    creationTime: Timestamp
    endTime: Optional[Timestamp]
    customModelArn: Optional[CustomModelArn]
    customModelName: Optional[CustomModelName]
    customizationType: Optional[CustomizationType]


ModelCustomizationJobSummaries = List[ModelCustomizationJobSummary]


class ListModelCustomizationJobsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    modelCustomizationJobSummaries: Optional[ModelCustomizationJobSummaries]


class ListModelImportJobsRequest(ServiceRequest):
    creationTimeAfter: Optional[Timestamp]
    creationTimeBefore: Optional[Timestamp]
    statusEquals: Optional[ModelImportJobStatus]
    nameContains: Optional[JobName]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortJobsBy]
    sortOrder: Optional[SortOrder]


class ModelImportJobSummary(TypedDict, total=False):
    """Information about the import job."""

    jobArn: ModelImportJobArn
    jobName: JobName
    status: ModelImportJobStatus
    lastModifiedTime: Optional[Timestamp]
    creationTime: Timestamp
    endTime: Optional[Timestamp]
    importedModelArn: Optional[ImportedModelArn]
    importedModelName: Optional[ImportedModelName]


ModelImportJobSummaries = List[ModelImportJobSummary]


class ListModelImportJobsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    modelImportJobSummaries: Optional[ModelImportJobSummaries]


class ListModelInvocationJobsRequest(ServiceRequest):
    submitTimeAfter: Optional[Timestamp]
    submitTimeBefore: Optional[Timestamp]
    statusEquals: Optional[ModelInvocationJobStatus]
    nameContains: Optional[ModelInvocationJobName]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortJobsBy]
    sortOrder: Optional[SortOrder]


class ModelInvocationJobSummary(TypedDict, total=False):
    """A summary of a batch inference job."""

    jobArn: ModelInvocationJobArn
    jobName: ModelInvocationJobName
    modelId: ModelId
    clientRequestToken: Optional[ModelInvocationIdempotencyToken]
    roleArn: RoleArn
    status: Optional[ModelInvocationJobStatus]
    message: Optional[Message]
    submitTime: Timestamp
    lastModifiedTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    inputDataConfig: ModelInvocationJobInputDataConfig
    outputDataConfig: ModelInvocationJobOutputDataConfig
    vpcConfig: Optional[VpcConfig]
    timeoutDurationInHours: Optional[ModelInvocationJobTimeoutDurationInHours]
    jobExpirationTime: Optional[Timestamp]


ModelInvocationJobSummaries = List[ModelInvocationJobSummary]


class ListModelInvocationJobsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    invocationJobSummaries: Optional[ModelInvocationJobSummaries]


class ListPromptRoutersRequest(TypedDict, total=False):
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    type: Optional[PromptRouterType]


class PromptRouterSummary(TypedDict, total=False):
    promptRouterName: PromptRouterName
    routingCriteria: RoutingCriteria
    description: Optional[PromptRouterDescription]
    createdAt: Optional[Timestamp]
    updatedAt: Optional[Timestamp]
    promptRouterArn: PromptRouterArn
    models: PromptRouterTargetModels
    fallbackModel: PromptRouterTargetModel
    status: PromptRouterStatus
    type: PromptRouterType


PromptRouterSummaries = List[PromptRouterSummary]


class ListPromptRoutersResponse(TypedDict, total=False):
    promptRouterSummaries: Optional[PromptRouterSummaries]
    nextToken: Optional[PaginationToken]


class ListProvisionedModelThroughputsRequest(ServiceRequest):
    creationTimeAfter: Optional[Timestamp]
    creationTimeBefore: Optional[Timestamp]
    statusEquals: Optional[ProvisionedModelStatus]
    modelArnEquals: Optional[ModelArn]
    nameContains: Optional[ProvisionedModelName]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortByProvisionedModels]
    sortOrder: Optional[SortOrder]


class ProvisionedModelSummary(TypedDict, total=False):
    """A summary of information about a Provisioned Throughput.

    This data type is used in the following API operations:

    -  `ListProvisionedThroughputs
       response <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListProvisionedModelThroughputs.html#API_ListProvisionedModelThroughputs_ResponseSyntax>`__
    """

    provisionedModelName: ProvisionedModelName
    provisionedModelArn: ProvisionedModelArn
    modelArn: ModelArn
    desiredModelArn: ModelArn
    foundationModelArn: FoundationModelArn
    modelUnits: PositiveInteger
    desiredModelUnits: PositiveInteger
    status: ProvisionedModelStatus
    commitmentDuration: Optional[CommitmentDuration]
    commitmentExpirationTime: Optional[Timestamp]
    creationTime: Timestamp
    lastModifiedTime: Timestamp


ProvisionedModelSummaries = List[ProvisionedModelSummary]


class ListProvisionedModelThroughputsResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    provisionedModelSummaries: Optional[ProvisionedModelSummaries]


class ListTagsForResourceRequest(ServiceRequest):
    resourceARN: TaggableResourcesArn


class ListTagsForResourceResponse(TypedDict, total=False):
    tags: Optional[TagList]


class PutModelInvocationLoggingConfigurationRequest(ServiceRequest):
    loggingConfig: LoggingConfig


class PutModelInvocationLoggingConfigurationResponse(TypedDict, total=False):
    pass


class PutUseCaseForModelAccessRequest(ServiceRequest):
    formData: AcknowledgementFormDataBody


class PutUseCaseForModelAccessResponse(TypedDict, total=False):
    pass


class RegisterMarketplaceModelEndpointRequest(ServiceRequest):
    endpointIdentifier: Arn
    modelSourceIdentifier: ModelSourceIdentifier


class RegisterMarketplaceModelEndpointResponse(TypedDict, total=False):
    marketplaceModelEndpoint: MarketplaceModelEndpoint


class StartAutomatedReasoningPolicyBuildWorkflowRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowType: AutomatedReasoningPolicyBuildWorkflowType
    clientRequestToken: Optional[IdempotencyToken]
    sourceContent: AutomatedReasoningPolicyBuildWorkflowSource


class StartAutomatedReasoningPolicyBuildWorkflowResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId


class StartAutomatedReasoningPolicyTestWorkflowRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    testCaseIds: Optional[AutomatedReasoningPolicyTestCaseIdList]
    clientRequestToken: Optional[IdempotencyToken]


class StartAutomatedReasoningPolicyTestWorkflowResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn


class StopEvaluationJobRequest(ServiceRequest):
    jobIdentifier: EvaluationJobIdentifier


class StopEvaluationJobResponse(TypedDict, total=False):
    pass


class StopModelCustomizationJobRequest(ServiceRequest):
    jobIdentifier: ModelCustomizationJobIdentifier


class StopModelCustomizationJobResponse(TypedDict, total=False):
    pass


class StopModelInvocationJobRequest(ServiceRequest):
    jobIdentifier: ModelInvocationJobIdentifier


class StopModelInvocationJobResponse(TypedDict, total=False):
    pass


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    resourceARN: TaggableResourcesArn
    tags: TagList


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    resourceARN: TaggableResourcesArn
    tagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateAutomatedReasoningPolicyAnnotationsRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    annotations: AutomatedReasoningPolicyAnnotationList
    lastUpdatedAnnotationSetHash: AutomatedReasoningPolicyHash


class UpdateAutomatedReasoningPolicyAnnotationsResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    buildWorkflowId: AutomatedReasoningPolicyBuildWorkflowId
    annotationSetHash: AutomatedReasoningPolicyHash
    updatedAt: Timestamp


class UpdateAutomatedReasoningPolicyRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    policyDefinition: AutomatedReasoningPolicyDefinition
    name: Optional[AutomatedReasoningPolicyName]
    description: Optional[AutomatedReasoningPolicyDescription]


class UpdateAutomatedReasoningPolicyResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    name: AutomatedReasoningPolicyName
    definitionHash: AutomatedReasoningPolicyHash
    updatedAt: Timestamp


class UpdateAutomatedReasoningPolicyTestCaseRequest(ServiceRequest):
    policyArn: AutomatedReasoningPolicyArn
    testCaseId: AutomatedReasoningPolicyTestCaseId
    guardContent: AutomatedReasoningPolicyTestGuardContent
    queryContent: Optional[AutomatedReasoningPolicyTestQueryContent]
    lastUpdatedAt: Timestamp
    expectedAggregatedFindingsResult: AutomatedReasoningCheckResult
    confidenceThreshold: Optional[AutomatedReasoningCheckTranslationConfidence]
    clientRequestToken: Optional[IdempotencyToken]


class UpdateAutomatedReasoningPolicyTestCaseResponse(TypedDict, total=False):
    policyArn: AutomatedReasoningPolicyArn
    testCaseId: AutomatedReasoningPolicyTestCaseId


class UpdateGuardrailRequest(ServiceRequest):
    guardrailIdentifier: GuardrailIdentifier
    name: GuardrailName
    description: Optional[GuardrailDescription]
    topicPolicyConfig: Optional[GuardrailTopicPolicyConfig]
    contentPolicyConfig: Optional[GuardrailContentPolicyConfig]
    wordPolicyConfig: Optional[GuardrailWordPolicyConfig]
    sensitiveInformationPolicyConfig: Optional[GuardrailSensitiveInformationPolicyConfig]
    contextualGroundingPolicyConfig: Optional[GuardrailContextualGroundingPolicyConfig]
    automatedReasoningPolicyConfig: Optional[GuardrailAutomatedReasoningPolicyConfig]
    crossRegionConfig: Optional[GuardrailCrossRegionConfig]
    blockedInputMessaging: GuardrailBlockedMessaging
    blockedOutputsMessaging: GuardrailBlockedMessaging
    kmsKeyId: Optional[KmsKeyId]


class UpdateGuardrailResponse(TypedDict, total=False):
    guardrailId: GuardrailId
    guardrailArn: GuardrailArn
    version: GuardrailDraftVersion
    updatedAt: Timestamp


class UpdateMarketplaceModelEndpointRequest(ServiceRequest):
    endpointArn: Arn
    endpointConfig: EndpointConfig
    clientRequestToken: Optional[IdempotencyToken]


class UpdateMarketplaceModelEndpointResponse(TypedDict, total=False):
    marketplaceModelEndpoint: MarketplaceModelEndpoint


class UpdateProvisionedModelThroughputRequest(ServiceRequest):
    provisionedModelId: ProvisionedModelId
    desiredProvisionedModelName: Optional[ProvisionedModelName]
    desiredModelId: Optional[ModelIdentifier]


class UpdateProvisionedModelThroughputResponse(TypedDict, total=False):
    pass


class BedrockApi:
    service = "bedrock"
    version = "2023-04-20"

    @handler("BatchDeleteEvaluationJob")
    def batch_delete_evaluation_job(
        self, context: RequestContext, job_identifiers: EvaluationJobIdentifiers, **kwargs
    ) -> BatchDeleteEvaluationJobResponse:
        """Deletes a batch of evaluation jobs. An evaluation job can only be
        deleted if it has following status ``FAILED``, ``COMPLETED``, and
        ``STOPPED``. You can request up to 25 model evaluation jobs be deleted
        in a single request.

        :param job_identifiers: A list of one or more evaluation job Amazon Resource Names (ARNs) you
        want to delete.
        :returns: BatchDeleteEvaluationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CancelAutomatedReasoningPolicyBuildWorkflow")
    def cancel_automated_reasoning_policy_build_workflow(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        **kwargs,
    ) -> CancelAutomatedReasoningPolicyBuildWorkflowResponse:
        """Cancels a running Automated Reasoning policy build workflow. This stops
        the policy generation process and prevents further processing of the
        source documents.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy whose
        build workflow you want to cancel.
        :param build_workflow_id: The unique identifier of the build workflow to cancel.
        :returns: CancelAutomatedReasoningPolicyBuildWorkflowResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateAutomatedReasoningPolicy")
    def create_automated_reasoning_policy(
        self,
        context: RequestContext,
        name: AutomatedReasoningPolicyName,
        description: AutomatedReasoningPolicyDescription | None = None,
        client_request_token: IdempotencyToken | None = None,
        policy_definition: AutomatedReasoningPolicyDefinition | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateAutomatedReasoningPolicyResponse:
        """Creates an Automated Reasoning policy for Amazon Bedrock Guardrails.
        Automated Reasoning policies use mathematical techniques to detect
        hallucinations, suggest corrections, and highlight unstated assumptions
        in the responses of your GenAI application.

        To create a policy, you upload a source document that describes the
        rules that you're encoding. Automated Reasoning extracts important
        concepts from the source document that will become variables in the
        policy and infers policy rules.

        :param name: A unique name for the Automated Reasoning policy.
        :param description: A description of the Automated Reasoning policy.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the operation
        completes no more than once.
        :param policy_definition: The policy definition that contains the formal logic rules, variables,
        and custom variable types used to validate foundation model responses in
        your application.
        :param tags: A list of tags to associate with the Automated Reasoning policy.
        :returns: CreateAutomatedReasoningPolicyResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateAutomatedReasoningPolicyTestCase")
    def create_automated_reasoning_policy_test_case(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        guard_content: AutomatedReasoningPolicyTestGuardContent,
        expected_aggregated_findings_result: AutomatedReasoningCheckResult,
        query_content: AutomatedReasoningPolicyTestQueryContent | None = None,
        client_request_token: IdempotencyToken | None = None,
        confidence_threshold: AutomatedReasoningCheckTranslationConfidence | None = None,
        **kwargs,
    ) -> CreateAutomatedReasoningPolicyTestCaseResponse:
        """Creates a test for an Automated Reasoning policy. Tests validate that
        your policy works as expected by providing sample inputs and expected
        outcomes. Use tests to verify policy behavior before deploying to
        production.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy for
        which to create the test.
        :param guard_content: The output content that's validated by the Automated Reasoning policy.
        :param expected_aggregated_findings_result: The expected result of the Automated Reasoning check.
        :param query_content: The input query or prompt that generated the content.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the operation
        completes no more than one time.
        :param confidence_threshold: The minimum confidence level for logic validation.
        :returns: CreateAutomatedReasoningPolicyTestCaseResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateAutomatedReasoningPolicyVersion")
    def create_automated_reasoning_policy_version(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        last_updated_definition_hash: AutomatedReasoningPolicyHash,
        client_request_token: IdempotencyToken | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateAutomatedReasoningPolicyVersionResponse:
        """Creates a new version of an existing Automated Reasoning policy. This
        allows you to iterate on your policy rules while maintaining previous
        versions for rollback or comparison purposes.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy for
        which to create a version.
        :param last_updated_definition_hash: The hash of the current policy definition used as a concurrency token to
        ensure the policy hasn't been modified since you last retrieved it.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the operation
        completes no more than one time.
        :param tags: A list of tags to associate with the policy version.
        :returns: CreateAutomatedReasoningPolicyVersionResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateCustomModel")
    def create_custom_model(
        self,
        context: RequestContext,
        model_name: CustomModelName,
        model_source_config: ModelDataSource,
        model_kms_key_arn: KmsKeyArn | None = None,
        role_arn: RoleArn | None = None,
        model_tags: TagList | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> CreateCustomModelResponse:
        """Creates a new custom model in Amazon Bedrock. After the model is active,
        you can use it for inference.

        To use the model for inference, you must purchase Provisioned Throughput
        for it. You can't use On-demand inference with these custom models. For
        more information about Provisioned Throughput, see `Provisioned
        Throughput <https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html>`__.

        The model appears in ``ListCustomModels`` with a ``customizationType``
        of ``imported``. To track the status of the new model, you use the
        ``GetCustomModel`` API operation. The model can be in the following
        states:

        -  ``Creating`` - Initial state during validation and registration

        -  ``Active`` - Model is ready for use in inference

        -  ``Failed`` - Creation process encountered an error

        **Related APIs**

        -  `GetCustomModel <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModel.html>`__

        -  `ListCustomModels <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModels.html>`__

        -  `DeleteCustomModel <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModel.html>`__

        :param model_name: A unique name for the custom model.
        :param model_source_config: The data source for the model.
        :param model_kms_key_arn: The Amazon Resource Name (ARN) of the customer managed KMS key to
        encrypt the custom model.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM service role that Amazon
        Bedrock assumes to perform tasks on your behalf.
        :param model_tags: A list of key-value pairs to associate with the custom model resource.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than one time.
        :returns: CreateCustomModelResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateCustomModelDeployment")
    def create_custom_model_deployment(
        self,
        context: RequestContext,
        model_deployment_name: ModelDeploymentName,
        model_arn: CustomModelArn,
        description: CustomModelDeploymentDescription | None = None,
        tags: TagList | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> CreateCustomModelDeploymentResponse:
        """Deploys a custom model for on-demand inference in Amazon Bedrock. After
        you deploy your custom model, you use the deployment's Amazon Resource
        Name (ARN) as the ``modelId`` parameter when you submit prompts and
        generate responses with model inference.

        For more information about setting up on-demand inference for custom
        models, see `Set up inference for a custom
        model <https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html>`__.

        The following actions are related to the ``CreateCustomModelDeployment``
        operation:

        -  `GetCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html>`__

        -  `ListCustomModelDeployments <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html>`__

        -  `DeleteCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html>`__

        :param model_deployment_name: The name for the custom model deployment.
        :param model_arn: The Amazon Resource Name (ARN) of the custom model to deploy for
        on-demand inference.
        :param description: A description for the custom model deployment to help you identify its
        purpose.
        :param tags: Tags to assign to the custom model deployment.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the operation
        completes no more than one time.
        :returns: CreateCustomModelDeploymentResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateEvaluationJob")
    def create_evaluation_job(
        self,
        context: RequestContext,
        job_name: EvaluationJobName,
        role_arn: RoleArn,
        evaluation_config: EvaluationConfig,
        inference_config: EvaluationInferenceConfig,
        output_data_config: EvaluationOutputDataConfig,
        job_description: EvaluationJobDescription | None = None,
        client_request_token: IdempotencyToken | None = None,
        customer_encryption_key_id: KmsKeyId | None = None,
        job_tags: TagList | None = None,
        application_type: ApplicationType | None = None,
        **kwargs,
    ) -> CreateEvaluationJobResponse:
        """Creates an evaluation job.

        :param job_name: A name for the evaluation job.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM service role that Amazon
        Bedrock can assume to perform tasks on your behalf.
        :param evaluation_config: Contains the configuration details of either an automated or human-based
        evaluation job.
        :param inference_config: Contains the configuration details of the inference model for the
        evaluation job.
        :param output_data_config: Contains the configuration details of the Amazon S3 bucket for storing
        the results of the evaluation job.
        :param job_description: A description of the evaluation job.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than one time.
        :param customer_encryption_key_id: Specify your customer managed encryption key Amazon Resource Name (ARN)
        that will be used to encrypt your evaluation job.
        :param job_tags: Tags to attach to the model evaluation job.
        :param application_type: Specifies whether the evaluation job is for evaluating a model or
        evaluating a knowledge base (retrieval and response generation).
        :returns: CreateEvaluationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateFoundationModelAgreement")
    def create_foundation_model_agreement(
        self, context: RequestContext, offer_token: OfferToken, model_id: BedrockModelId, **kwargs
    ) -> CreateFoundationModelAgreementResponse:
        """Request a model access agreement for the specified model.

        :param offer_token: An offer token encapsulates the information for an offer.
        :param model_id: Model Id of the model for the access request.
        :returns: CreateFoundationModelAgreementResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateGuardrail")
    def create_guardrail(
        self,
        context: RequestContext,
        name: GuardrailName,
        blocked_input_messaging: GuardrailBlockedMessaging,
        blocked_outputs_messaging: GuardrailBlockedMessaging,
        description: GuardrailDescription | None = None,
        topic_policy_config: GuardrailTopicPolicyConfig | None = None,
        content_policy_config: GuardrailContentPolicyConfig | None = None,
        word_policy_config: GuardrailWordPolicyConfig | None = None,
        sensitive_information_policy_config: GuardrailSensitiveInformationPolicyConfig
        | None = None,
        contextual_grounding_policy_config: GuardrailContextualGroundingPolicyConfig | None = None,
        automated_reasoning_policy_config: GuardrailAutomatedReasoningPolicyConfig | None = None,
        cross_region_config: GuardrailCrossRegionConfig | None = None,
        kms_key_id: KmsKeyId | None = None,
        tags: TagList | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> CreateGuardrailResponse:
        """Creates a guardrail to block topics and to implement safeguards for your
        generative AI applications.

        You can configure the following policies in a guardrail to avoid
        undesirable and harmful content, filter out denied topics and words, and
        remove sensitive information for privacy protection.

        -  **Content filters** - Adjust filter strengths to block input prompts
           or model responses containing harmful content.

        -  **Denied topics** - Define a set of topics that are undesirable in
           the context of your application. These topics will be blocked if
           detected in user queries or model responses.

        -  **Word filters** - Configure filters to block undesirable words,
           phrases, and profanity. Such words can include offensive terms,
           competitor names etc.

        -  **Sensitive information filters** - Block or mask sensitive
           information such as personally identifiable information (PII) or
           custom regex in user inputs and model responses.

        In addition to the above policies, you can also configure the messages
        to be returned to the user if a user input or model response is in
        violation of the policies defined in the guardrail.

        For more information, see `Amazon Bedrock
        Guardrails <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>`__
        in the *Amazon Bedrock User Guide*.

        :param name: The name to give the guardrail.
        :param blocked_input_messaging: The message to return when the guardrail blocks a prompt.
        :param blocked_outputs_messaging: The message to return when the guardrail blocks a model response.
        :param description: A description of the guardrail.
        :param topic_policy_config: The topic policies to configure for the guardrail.
        :param content_policy_config: The content filter policies to configure for the guardrail.
        :param word_policy_config: The word policy you configure for the guardrail.
        :param sensitive_information_policy_config: The sensitive information policy to configure for the guardrail.
        :param contextual_grounding_policy_config: The contextual grounding policy configuration used to create a
        guardrail.
        :param automated_reasoning_policy_config: Optional configuration for integrating Automated Reasoning policies with
        the new guardrail.
        :param cross_region_config: The system-defined guardrail profile that you're using with your
        guardrail.
        :param kms_key_id: The ARN of the KMS key that you use to encrypt the guardrail.
        :param tags: The tags that you want to attach to the guardrail.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than once.
        :returns: CreateGuardrailResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateGuardrailVersion")
    def create_guardrail_version(
        self,
        context: RequestContext,
        guardrail_identifier: GuardrailIdentifier,
        description: GuardrailDescription | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> CreateGuardrailVersionResponse:
        """Creates a version of the guardrail. Use this API to create a snapshot of
        the guardrail when you are satisfied with a configuration, or to compare
        the configuration with another version.

        :param guardrail_identifier: The unique identifier of the guardrail.
        :param description: A description of the guardrail version.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than once.
        :returns: CreateGuardrailVersionResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateInferenceProfile")
    def create_inference_profile(
        self,
        context: RequestContext,
        inference_profile_name: InferenceProfileName,
        model_source: InferenceProfileModelSource,
        description: InferenceProfileDescription | None = None,
        client_request_token: IdempotencyToken | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateInferenceProfileResponse:
        """Creates an application inference profile to track metrics and costs when
        invoking a model. To create an application inference profile for a
        foundation model in one region, specify the ARN of the model in that
        region. To create an application inference profile for a foundation
        model across multiple regions, specify the ARN of the system-defined
        inference profile that contains the regions that you want to route
        requests to. For more information, see `Increase throughput and
        resilience with cross-region inference in Amazon
        Bedrock <https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html>`__.
        in the Amazon Bedrock User Guide.

        :param inference_profile_name: A name for the inference profile.
        :param model_source: The foundation model or system-defined inference profile that the
        inference profile will track metrics and costs for.
        :param description: A description for the inference profile.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than one time.
        :param tags: An array of objects, each of which contains a tag and its value.
        :returns: CreateInferenceProfileResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateMarketplaceModelEndpoint")
    def create_marketplace_model_endpoint(
        self,
        context: RequestContext,
        model_source_identifier: ModelSourceIdentifier,
        endpoint_config: EndpointConfig,
        endpoint_name: EndpointName,
        accept_eula: AcceptEula | None = None,
        client_request_token: IdempotencyToken | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateMarketplaceModelEndpointResponse:
        """Creates an endpoint for a model from Amazon Bedrock Marketplace. The
        endpoint is hosted by Amazon SageMaker.

        :param model_source_identifier: The ARN of the model from Amazon Bedrock Marketplace that you want to
        deploy to the endpoint.
        :param endpoint_config: The configuration for the endpoint, including the number and type of
        instances to use.
        :param endpoint_name: The name of the endpoint.
        :param accept_eula: Indicates whether you accept the end-user license agreement (EULA) for
        the model.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param tags: An array of key-value pairs to apply to the underlying Amazon SageMaker
        endpoint.
        :returns: CreateMarketplaceModelEndpointResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateModelCopyJob")
    def create_model_copy_job(
        self,
        context: RequestContext,
        source_model_arn: ModelArn,
        target_model_name: CustomModelName,
        model_kms_key_id: KmsKeyId | None = None,
        target_model_tags: TagList | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> CreateModelCopyJobResponse:
        """Copies a model to another region so that it can be used there. For more
        information, see `Copy models to be used in other
        regions <https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param source_model_arn: The Amazon Resource Name (ARN) of the model to be copied.
        :param target_model_name: A name for the copied model.
        :param model_kms_key_id: The ARN of the KMS key that you use to encrypt the model copy.
        :param target_model_tags: Tags to associate with the target model.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than one time.
        :returns: CreateModelCopyJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        """
        raise NotImplementedError

    @handler("CreateModelCustomizationJob")
    def create_model_customization_job(
        self,
        context: RequestContext,
        job_name: JobName,
        custom_model_name: CustomModelName,
        role_arn: RoleArn,
        base_model_identifier: BaseModelIdentifier,
        training_data_config: TrainingDataConfig,
        output_data_config: OutputDataConfig,
        client_request_token: IdempotencyToken | None = None,
        customization_type: CustomizationType | None = None,
        custom_model_kms_key_id: KmsKeyId | None = None,
        job_tags: TagList | None = None,
        custom_model_tags: TagList | None = None,
        validation_data_config: ValidationDataConfig | None = None,
        hyper_parameters: ModelCustomizationHyperParameters | None = None,
        vpc_config: VpcConfig | None = None,
        customization_config: CustomizationConfig | None = None,
        **kwargs,
    ) -> CreateModelCustomizationJobResponse:
        """Creates a fine-tuning job to customize a base model.

        You specify the base foundation model and the location of the training
        data. After the model-customization job completes successfully, your
        custom model resource will be ready to use. Amazon Bedrock returns
        validation loss metrics and output generations after the job completes.

        For information on the format of training and validation data, see
        `Prepare the
        datasets <https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html>`__.

        Model-customization jobs are asynchronous and the completion time
        depends on the base model and the training/validation data size. To
        monitor a job, use the ``GetModelCustomizationJob`` operation to
        retrieve the job status.

        For more information, see `Custom
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param job_name: A name for the fine-tuning job.
        :param custom_model_name: A name for the resulting custom model.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM service role that Amazon
        Bedrock can assume to perform tasks on your behalf.
        :param base_model_identifier: Name of the base model.
        :param training_data_config: Information about the training dataset.
        :param output_data_config: S3 location for the output data.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than one time.
        :param customization_type: The customization type.
        :param custom_model_kms_key_id: The custom model is encrypted at rest using this key.
        :param job_tags: Tags to attach to the job.
        :param custom_model_tags: Tags to attach to the resulting custom model.
        :param validation_data_config: Information about the validation dataset.
        :param hyper_parameters: Parameters related to tuning the model.
        :param vpc_config: The configuration of the Virtual Private Cloud (VPC) that contains the
        resources that you're using for this job.
        :param customization_config: The customization configuration for the model customization job.
        :returns: CreateModelCustomizationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateModelImportJob")
    def create_model_import_job(
        self,
        context: RequestContext,
        job_name: JobName,
        imported_model_name: ImportedModelName,
        role_arn: RoleArn,
        model_data_source: ModelDataSource,
        job_tags: TagList | None = None,
        imported_model_tags: TagList | None = None,
        client_request_token: IdempotencyToken | None = None,
        vpc_config: VpcConfig | None = None,
        imported_model_kms_key_id: KmsKeyId | None = None,
        **kwargs,
    ) -> CreateModelImportJobResponse:
        """Creates a model import job to import model that you have customized in
        other environments, such as Amazon SageMaker. For more information, see
        `Import a customized
        model <https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html>`__

        :param job_name: The name of the import job.
        :param imported_model_name: The name of the imported model.
        :param role_arn: The Amazon Resource Name (ARN) of the model import job.
        :param model_data_source: The data source for the imported model.
        :param job_tags: Tags to attach to this import job.
        :param imported_model_tags: Tags to attach to the imported model.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than one time.
        :param vpc_config: VPC configuration parameters for the private Virtual Private Cloud (VPC)
        that contains the resources you are using for the import job.
        :param imported_model_kms_key_id: The imported model is encrypted at rest using this key.
        :returns: CreateModelImportJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateModelInvocationJob")
    def create_model_invocation_job(
        self,
        context: RequestContext,
        job_name: ModelInvocationJobName,
        role_arn: RoleArn,
        model_id: ModelId,
        input_data_config: ModelInvocationJobInputDataConfig,
        output_data_config: ModelInvocationJobOutputDataConfig,
        client_request_token: ModelInvocationIdempotencyToken | None = None,
        vpc_config: VpcConfig | None = None,
        timeout_duration_in_hours: ModelInvocationJobTimeoutDurationInHours | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateModelInvocationJobResponse:
        """Creates a batch inference job to invoke a model on multiple prompts.
        Format your data according to `Format your inference
        data <https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data>`__
        and upload it to an Amazon S3 bucket. For more information, see `Process
        multiple prompts with batch
        inference <https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html>`__.

        The response returns a ``jobArn`` that you can use to stop or get
        details about the job.

        :param job_name: A name to give the batch inference job.
        :param role_arn: The Amazon Resource Name (ARN) of the service role with permissions to
        carry out and manage batch inference.
        :param model_id: The unique identifier of the foundation model to use for the batch
        inference job.
        :param input_data_config: Details about the location of the input to the batch inference job.
        :param output_data_config: Details about the location of the output of the batch inference job.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than one time.
        :param vpc_config: The configuration of the Virtual Private Cloud (VPC) for the data in the
        batch inference job.
        :param timeout_duration_in_hours: The number of hours after which to force the batch inference job to time
        out.
        :param tags: Any tags to associate with the batch inference job.
        :returns: CreateModelInvocationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreatePromptRouter")
    def create_prompt_router(
        self,
        context: RequestContext,
        prompt_router_name: PromptRouterName,
        models: PromptRouterTargetModels,
        routing_criteria: RoutingCriteria,
        fallback_model: PromptRouterTargetModel,
        client_request_token: IdempotencyToken | None = None,
        description: PromptRouterDescription | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreatePromptRouterResponse:
        """Creates a prompt router that manages the routing of requests between
        multiple foundation models based on the routing criteria.

        :param prompt_router_name: The name of the prompt router.
        :param models: A list of foundation models that the prompt router can route requests
        to.
        :param routing_criteria: The criteria, which is the response quality difference, used to
        determine how incoming requests are routed to different models.
        :param fallback_model: The default model to use when the routing criteria is not met.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure
        idempotency of your requests.
        :param description: An optional description of the prompt router to help identify its
        purpose.
        :param tags: An array of key-value pairs to apply to this resource as tags.
        :returns: CreatePromptRouterResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateProvisionedModelThroughput")
    def create_provisioned_model_throughput(
        self,
        context: RequestContext,
        model_units: PositiveInteger,
        provisioned_model_name: ProvisionedModelName,
        model_id: ModelIdentifier,
        client_request_token: IdempotencyToken | None = None,
        commitment_duration: CommitmentDuration | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateProvisionedModelThroughputResponse:
        """Creates dedicated throughput for a base or custom model with the model
        units and for the duration that you specify. For pricing details, see
        `Amazon Bedrock Pricing <http://aws.amazon.com/bedrock/pricing/>`__. For
        more information, see `Provisioned
        Throughput <https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param model_units: Number of model units to allocate.
        :param provisioned_model_name: The name for this Provisioned Throughput.
        :param model_id: The Amazon Resource Name (ARN) or name of the model to associate with
        this Provisioned Throughput.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the API request
        completes no more than one time.
        :param commitment_duration: The commitment duration requested for the Provisioned Throughput.
        :param tags: Tags to associate with this Provisioned Throughput.
        :returns: CreateProvisionedModelThroughputResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteAutomatedReasoningPolicy")
    def delete_automated_reasoning_policy(
        self, context: RequestContext, policy_arn: AutomatedReasoningPolicyArn, **kwargs
    ) -> DeleteAutomatedReasoningPolicyResponse:
        """Deletes an Automated Reasoning policy or policy version. This operation
        is idempotent. If you delete a policy more than once, each call
        succeeds. Deleting a policy removes it permanently and cannot be undone.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy to
        delete.
        :returns: DeleteAutomatedReasoningPolicyResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteAutomatedReasoningPolicyBuildWorkflow")
    def delete_automated_reasoning_policy_build_workflow(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        last_updated_at: Timestamp,
        **kwargs,
    ) -> DeleteAutomatedReasoningPolicyBuildWorkflowResponse:
        """Deletes an Automated Reasoning policy build workflow and its associated
        artifacts. This permanently removes the workflow history and any
        generated assets.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy whose
        build workflow you want to delete.
        :param build_workflow_id: The unique identifier of the build workflow to delete.
        :param last_updated_at: The timestamp when the build workflow was last updated.
        :returns: DeleteAutomatedReasoningPolicyBuildWorkflowResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceInUseException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteAutomatedReasoningPolicyTestCase")
    def delete_automated_reasoning_policy_test_case(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        test_case_id: AutomatedReasoningPolicyTestCaseId,
        last_updated_at: Timestamp,
        **kwargs,
    ) -> DeleteAutomatedReasoningPolicyTestCaseResponse:
        """Deletes an Automated Reasoning policy test. This operation is
        idempotent; if you delete a test more than once, each call succeeds.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy that
        contains the test.
        :param test_case_id: The unique identifier of the test to delete.
        :param last_updated_at: The timestamp when the test was last updated.
        :returns: DeleteAutomatedReasoningPolicyTestCaseResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceInUseException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteCustomModel")
    def delete_custom_model(
        self, context: RequestContext, model_identifier: ModelIdentifier, **kwargs
    ) -> DeleteCustomModelResponse:
        """Deletes a custom model that you created earlier. For more information,
        see `Custom
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param model_identifier: Name of the model to delete.
        :returns: DeleteCustomModelResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteCustomModelDeployment")
    def delete_custom_model_deployment(
        self,
        context: RequestContext,
        custom_model_deployment_identifier: CustomModelDeploymentIdentifier,
        **kwargs,
    ) -> DeleteCustomModelDeploymentResponse:
        """Deletes a custom model deployment. This operation stops the deployment
        and removes it from your account. After deletion, the deployment ARN can
        no longer be used for inference requests.

        The following actions are related to the ``DeleteCustomModelDeployment``
        operation:

        -  `CreateCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html>`__

        -  `GetCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html>`__

        -  `ListCustomModelDeployments <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html>`__

        :param custom_model_deployment_identifier: The Amazon Resource Name (ARN) or name of the custom model deployment to
        delete.
        :returns: DeleteCustomModelDeploymentResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteFoundationModelAgreement")
    def delete_foundation_model_agreement(
        self, context: RequestContext, model_id: BedrockModelId, **kwargs
    ) -> DeleteFoundationModelAgreementResponse:
        """Delete the model access agreement for the specified model.

        :param model_id: Model Id of the model access to delete.
        :returns: DeleteFoundationModelAgreementResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteGuardrail")
    def delete_guardrail(
        self,
        context: RequestContext,
        guardrail_identifier: GuardrailIdentifier,
        guardrail_version: GuardrailNumericalVersion | None = None,
        **kwargs,
    ) -> DeleteGuardrailResponse:
        """Deletes a guardrail.

        -  To delete a guardrail, only specify the ARN of the guardrail in the
           ``guardrailIdentifier`` field. If you delete a guardrail, all of its
           versions will be deleted.

        -  To delete a version of a guardrail, specify the ARN of the guardrail
           in the ``guardrailIdentifier`` field and the version in the
           ``guardrailVersion`` field.

        :param guardrail_identifier: The unique identifier of the guardrail.
        :param guardrail_version: The version of the guardrail.
        :returns: DeleteGuardrailResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteImportedModel")
    def delete_imported_model(
        self, context: RequestContext, model_identifier: ImportedModelIdentifier, **kwargs
    ) -> DeleteImportedModelResponse:
        """Deletes a custom model that you imported earlier. For more information,
        see `Import a customized
        model <https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param model_identifier: Name of the imported model to delete.
        :returns: DeleteImportedModelResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteInferenceProfile")
    def delete_inference_profile(
        self,
        context: RequestContext,
        inference_profile_identifier: InferenceProfileIdentifier,
        **kwargs,
    ) -> DeleteInferenceProfileResponse:
        """Deletes an application inference profile. For more information, see
        `Increase throughput and resilience with cross-region inference in
        Amazon
        Bedrock <https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html>`__.
        in the Amazon Bedrock User Guide.

        :param inference_profile_identifier: The Amazon Resource Name (ARN) or ID of the application inference
        profile to delete.
        :returns: DeleteInferenceProfileResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteMarketplaceModelEndpoint")
    def delete_marketplace_model_endpoint(
        self, context: RequestContext, endpoint_arn: Arn, **kwargs
    ) -> DeleteMarketplaceModelEndpointResponse:
        """Deletes an endpoint for a model from Amazon Bedrock Marketplace.

        :param endpoint_arn: The Amazon Resource Name (ARN) of the endpoint you want to delete.
        :returns: DeleteMarketplaceModelEndpointResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteModelInvocationLoggingConfiguration")
    def delete_model_invocation_logging_configuration(
        self, context: RequestContext, **kwargs
    ) -> DeleteModelInvocationLoggingConfigurationResponse:
        """Delete the invocation logging.

        :returns: DeleteModelInvocationLoggingConfigurationResponse
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeletePromptRouter")
    def delete_prompt_router(
        self, context: RequestContext, prompt_router_arn: PromptRouterArn, **kwargs
    ) -> DeletePromptRouterResponse:
        """Deletes a specified prompt router. This action cannot be undone.

        :param prompt_router_arn: The Amazon Resource Name (ARN) of the prompt router to delete.
        :returns: DeletePromptRouterResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteProvisionedModelThroughput")
    def delete_provisioned_model_throughput(
        self, context: RequestContext, provisioned_model_id: ProvisionedModelId, **kwargs
    ) -> DeleteProvisionedModelThroughputResponse:
        """Deletes a Provisioned Throughput. You can't delete a Provisioned
        Throughput before the commitment term is over. For more information, see
        `Provisioned
        Throughput <https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param provisioned_model_id: The Amazon Resource Name (ARN) or name of the Provisioned Throughput.
        :returns: DeleteProvisionedModelThroughputResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeregisterMarketplaceModelEndpoint")
    def deregister_marketplace_model_endpoint(
        self, context: RequestContext, endpoint_arn: Arn, **kwargs
    ) -> DeregisterMarketplaceModelEndpointResponse:
        """Deregisters an endpoint for a model from Amazon Bedrock Marketplace.
        This operation removes the endpoint's association with Amazon Bedrock
        but does not delete the underlying Amazon SageMaker endpoint.

        :param endpoint_arn: The Amazon Resource Name (ARN) of the endpoint you want to deregister.
        :returns: DeregisterMarketplaceModelEndpointResponse
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ExportAutomatedReasoningPolicyVersion")
    def export_automated_reasoning_policy_version(
        self, context: RequestContext, policy_arn: AutomatedReasoningPolicyArn, **kwargs
    ) -> ExportAutomatedReasoningPolicyVersionResponse:
        """Exports the policy definition for an Automated Reasoning policy version.
        Returns the complete policy definition including rules, variables, and
        custom variable types in a structured format.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy to
        export.
        :returns: ExportAutomatedReasoningPolicyVersionResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetAutomatedReasoningPolicy")
    def get_automated_reasoning_policy(
        self, context: RequestContext, policy_arn: AutomatedReasoningPolicyArn, **kwargs
    ) -> GetAutomatedReasoningPolicyResponse:
        """Retrieves details about an Automated Reasoning policy or policy version.
        Returns information including the policy definition, metadata, and
        timestamps.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy to
        retrieve.
        :returns: GetAutomatedReasoningPolicyResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetAutomatedReasoningPolicyAnnotations")
    def get_automated_reasoning_policy_annotations(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        **kwargs,
    ) -> GetAutomatedReasoningPolicyAnnotationsResponse:
        """Retrieves the current annotations for an Automated Reasoning policy
        build workflow. Annotations contain corrections to the rules, variables
        and types to be applied to the policy.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy whose
        annotations you want to retrieve.
        :param build_workflow_id: The unique identifier of the build workflow whose annotations you want
        to retrieve.
        :returns: GetAutomatedReasoningPolicyAnnotationsResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetAutomatedReasoningPolicyBuildWorkflow")
    def get_automated_reasoning_policy_build_workflow(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        **kwargs,
    ) -> GetAutomatedReasoningPolicyBuildWorkflowResponse:
        """Retrieves detailed information about an Automated Reasoning policy build
        workflow, including its status, configuration, and metadata.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy whose
        build workflow you want to retrieve.
        :param build_workflow_id: The unique identifier of the build workflow to retrieve.
        :returns: GetAutomatedReasoningPolicyBuildWorkflowResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetAutomatedReasoningPolicyBuildWorkflowResultAssets")
    def get_automated_reasoning_policy_build_workflow_result_assets(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        asset_type: AutomatedReasoningPolicyBuildResultAssetType,
        **kwargs,
    ) -> GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse:
        """Retrieves the resulting assets from a completed Automated Reasoning
        policy build workflow, including build logs, quality reports, and
        generated policy artifacts.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy whose
        build workflow assets you want to retrieve.
        :param build_workflow_id: The unique identifier of the build workflow whose result assets you want
        to retrieve.
        :param asset_type: The type of asset to retrieve (e.
        :returns: GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetAutomatedReasoningPolicyNextScenario")
    def get_automated_reasoning_policy_next_scenario(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        **kwargs,
    ) -> GetAutomatedReasoningPolicyNextScenarioResponse:
        """Retrieves the next test scenario for validating an Automated Reasoning
        policy. This is used during the interactive policy refinement process to
        test policy behavior.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy for
        which you want to get the next test scenario.
        :param build_workflow_id: The unique identifier of the build workflow associated with the test
        scenarios.
        :returns: GetAutomatedReasoningPolicyNextScenarioResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetAutomatedReasoningPolicyTestCase")
    def get_automated_reasoning_policy_test_case(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        test_case_id: AutomatedReasoningPolicyTestCaseId,
        **kwargs,
    ) -> GetAutomatedReasoningPolicyTestCaseResponse:
        """Retrieves details about a specific Automated Reasoning policy test.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy that
        contains the test.
        :param test_case_id: The unique identifier of the test to retrieve.
        :returns: GetAutomatedReasoningPolicyTestCaseResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetAutomatedReasoningPolicyTestResult")
    def get_automated_reasoning_policy_test_result(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        test_case_id: AutomatedReasoningPolicyTestCaseId,
        **kwargs,
    ) -> GetAutomatedReasoningPolicyTestResultResponse:
        """Retrieves the test result for a specific Automated Reasoning policy
        test. Returns detailed validation findings and execution status.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy.
        :param build_workflow_id: The build workflow identifier.
        :param test_case_id: The unique identifier of the test for which to retrieve results.
        :returns: GetAutomatedReasoningPolicyTestResultResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetCustomModel")
    def get_custom_model(
        self, context: RequestContext, model_identifier: ModelIdentifier, **kwargs
    ) -> GetCustomModelResponse:
        """Get the properties associated with a Amazon Bedrock custom model that
        you have created. For more information, see `Custom
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param model_identifier: Name or Amazon Resource Name (ARN) of the custom model.
        :returns: GetCustomModelResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetCustomModelDeployment")
    def get_custom_model_deployment(
        self,
        context: RequestContext,
        custom_model_deployment_identifier: CustomModelDeploymentIdentifier,
        **kwargs,
    ) -> GetCustomModelDeploymentResponse:
        """Retrieves information about a custom model deployment, including its
        status, configuration, and metadata. Use this operation to monitor the
        deployment status and retrieve details needed for inference requests.

        The following actions are related to the ``GetCustomModelDeployment``
        operation:

        -  `CreateCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html>`__

        -  `ListCustomModelDeployments <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html>`__

        -  `DeleteCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html>`__

        :param custom_model_deployment_identifier: The Amazon Resource Name (ARN) or name of the custom model deployment to
        retrieve information about.
        :returns: GetCustomModelDeploymentResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetEvaluationJob")
    def get_evaluation_job(
        self, context: RequestContext, job_identifier: EvaluationJobIdentifier, **kwargs
    ) -> GetEvaluationJobResponse:
        """Gets information about an evaluation job, such as the status of the job.

        :param job_identifier: The Amazon Resource Name (ARN) of the evaluation job you want get
        information on.
        :returns: GetEvaluationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetFoundationModel")
    def get_foundation_model(
        self, context: RequestContext, model_identifier: ModelIdentifier, **kwargs
    ) -> GetFoundationModelResponse:
        """Get details about a Amazon Bedrock foundation model.

        :param model_identifier: The model identifier.
        :returns: GetFoundationModelResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetFoundationModelAvailability")
    def get_foundation_model_availability(
        self, context: RequestContext, model_id: BedrockModelId, **kwargs
    ) -> GetFoundationModelAvailabilityResponse:
        """Get information about the Foundation model availability.

        :param model_id: The model Id of the foundation model.
        :returns: GetFoundationModelAvailabilityResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetGuardrail")
    def get_guardrail(
        self,
        context: RequestContext,
        guardrail_identifier: GuardrailIdentifier,
        guardrail_version: GuardrailVersion | None = None,
        **kwargs,
    ) -> GetGuardrailResponse:
        """Gets details about a guardrail. If you don't specify a version, the
        response returns details for the ``DRAFT`` version.

        :param guardrail_identifier: The unique identifier of the guardrail for which to get details.
        :param guardrail_version: The version of the guardrail for which to get details.
        :returns: GetGuardrailResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetImportedModel")
    def get_imported_model(
        self, context: RequestContext, model_identifier: ImportedModelIdentifier, **kwargs
    ) -> GetImportedModelResponse:
        """Gets properties associated with a customized model you imported.

        :param model_identifier: Name or Amazon Resource Name (ARN) of the imported model.
        :returns: GetImportedModelResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetInferenceProfile")
    def get_inference_profile(
        self,
        context: RequestContext,
        inference_profile_identifier: InferenceProfileIdentifier,
        **kwargs,
    ) -> GetInferenceProfileResponse:
        """Gets information about an inference profile. For more information, see
        `Increase throughput and resilience with cross-region inference in
        Amazon
        Bedrock <https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html>`__.
        in the Amazon Bedrock User Guide.

        :param inference_profile_identifier: The ID or Amazon Resource Name (ARN) of the inference profile.
        :returns: GetInferenceProfileResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetMarketplaceModelEndpoint")
    def get_marketplace_model_endpoint(
        self, context: RequestContext, endpoint_arn: Arn, **kwargs
    ) -> GetMarketplaceModelEndpointResponse:
        """Retrieves details about a specific endpoint for a model from Amazon
        Bedrock Marketplace.

        :param endpoint_arn: The Amazon Resource Name (ARN) of the endpoint you want to get
        information about.
        :returns: GetMarketplaceModelEndpointResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetModelCopyJob")
    def get_model_copy_job(
        self, context: RequestContext, job_arn: ModelCopyJobArn, **kwargs
    ) -> GetModelCopyJobResponse:
        """Retrieves information about a model copy job. For more information, see
        `Copy models to be used in other
        regions <https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param job_arn: The Amazon Resource Name (ARN) of the model copy job.
        :returns: GetModelCopyJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetModelCustomizationJob")
    def get_model_customization_job(
        self, context: RequestContext, job_identifier: ModelCustomizationJobIdentifier, **kwargs
    ) -> GetModelCustomizationJobResponse:
        """Retrieves the properties associated with a model-customization job,
        including the status of the job. For more information, see `Custom
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param job_identifier: Identifier for the customization job.
        :returns: GetModelCustomizationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetModelImportJob")
    def get_model_import_job(
        self, context: RequestContext, job_identifier: ModelImportJobIdentifier, **kwargs
    ) -> GetModelImportJobResponse:
        """Retrieves the properties associated with import model job, including the
        status of the job. For more information, see `Import a customized
        model <https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param job_identifier: The identifier of the import job.
        :returns: GetModelImportJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetModelInvocationJob")
    def get_model_invocation_job(
        self, context: RequestContext, job_identifier: ModelInvocationJobIdentifier, **kwargs
    ) -> GetModelInvocationJobResponse:
        """Gets details about a batch inference job. For more information, see
        `Monitor batch inference
        jobs <https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-monitor>`__

        :param job_identifier: The Amazon Resource Name (ARN) of the batch inference job.
        :returns: GetModelInvocationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetModelInvocationLoggingConfiguration")
    def get_model_invocation_logging_configuration(
        self, context: RequestContext, **kwargs
    ) -> GetModelInvocationLoggingConfigurationResponse:
        """Get the current configuration values for model invocation logging.

        :returns: GetModelInvocationLoggingConfigurationResponse
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetPromptRouter")
    def get_prompt_router(
        self, context: RequestContext, prompt_router_arn: PromptRouterArn, **kwargs
    ) -> GetPromptRouterResponse:
        """Retrieves details about a prompt router.

        :param prompt_router_arn: The prompt router's ARN.
        :returns: GetPromptRouterResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetProvisionedModelThroughput")
    def get_provisioned_model_throughput(
        self, context: RequestContext, provisioned_model_id: ProvisionedModelId, **kwargs
    ) -> GetProvisionedModelThroughputResponse:
        """Returns details for a Provisioned Throughput. For more information, see
        `Provisioned
        Throughput <https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param provisioned_model_id: The Amazon Resource Name (ARN) or name of the Provisioned Throughput.
        :returns: GetProvisionedModelThroughputResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetUseCaseForModelAccess")
    def get_use_case_for_model_access(
        self, context: RequestContext, **kwargs
    ) -> GetUseCaseForModelAccessResponse:
        """Get usecase for model access.

        :returns: GetUseCaseForModelAccessResponse
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListAutomatedReasoningPolicies")
    def list_automated_reasoning_policies(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn | None = None,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListAutomatedReasoningPoliciesResponse:
        """Lists all Automated Reasoning policies in your account, with optional
        filtering by policy ARN. This helps you manage and discover existing
        policies.

        :param policy_arn: Optional filter to list only the policy versions with the specified
        Amazon Resource Name (ARN).
        :param next_token: The pagination token from a previous request to retrieve the next page
        of results.
        :param max_results: The maximum number of policies to return in a single call.
        :returns: ListAutomatedReasoningPoliciesResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListAutomatedReasoningPolicyBuildWorkflows")
    def list_automated_reasoning_policy_build_workflows(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListAutomatedReasoningPolicyBuildWorkflowsResponse:
        """Lists all build workflows for an Automated Reasoning policy, showing the
        history of policy creation and modification attempts.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy whose
        build workflows you want to list.
        :param next_token: A pagination token from a previous request to continue listing build
        workflows from where the previous request left off.
        :param max_results: The maximum number of build workflows to return in a single response.
        :returns: ListAutomatedReasoningPolicyBuildWorkflowsResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListAutomatedReasoningPolicyTestCases")
    def list_automated_reasoning_policy_test_cases(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListAutomatedReasoningPolicyTestCasesResponse:
        """Lists tests for an Automated Reasoning policy. We recommend using
        pagination to ensure that the operation returns quickly and
        successfully.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy for
        which to list tests.
        :param next_token: The pagination token from a previous request to retrieve the next page
        of results.
        :param max_results: The maximum number of tests to return in a single call.
        :returns: ListAutomatedReasoningPolicyTestCasesResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListAutomatedReasoningPolicyTestResults")
    def list_automated_reasoning_policy_test_results(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListAutomatedReasoningPolicyTestResultsResponse:
        """Lists test results for an Automated Reasoning policy, showing how the
        policy performed against various test scenarios and validation checks.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy whose
        test results you want to list.
        :param build_workflow_id: The unique identifier of the build workflow whose test results you want
        to list.
        :param next_token: A pagination token from a previous request to continue listing test
        results from where the previous request left off.
        :param max_results: The maximum number of test results to return in a single response.
        :returns: ListAutomatedReasoningPolicyTestResultsResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListCustomModelDeployments")
    def list_custom_model_deployments(
        self,
        context: RequestContext,
        created_before: Timestamp | None = None,
        created_after: Timestamp | None = None,
        name_contains: ModelDeploymentName | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortModelsBy | None = None,
        sort_order: SortOrder | None = None,
        status_equals: CustomModelDeploymentStatus | None = None,
        model_arn_equals: CustomModelArn | None = None,
        **kwargs,
    ) -> ListCustomModelDeploymentsResponse:
        """Lists custom model deployments in your account. You can filter the
        results by creation time, name, status, and associated model. Use this
        operation to manage and monitor your custom model deployments.

        We recommend using pagination to ensure that the operation returns
        quickly and successfully.

        The following actions are related to the ``ListCustomModelDeployments``
        operation:

        -  `CreateCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html>`__

        -  `GetCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html>`__

        -  `DeleteCustomModelDeployment <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html>`__

        :param created_before: Filters deployments created before the specified date and time.
        :param created_after: Filters deployments created after the specified date and time.
        :param name_contains: Filters deployments whose names contain the specified string.
        :param max_results: The maximum number of results to return in a single call.
        :param next_token: The token for the next set of results.
        :param sort_by: The field to sort the results by.
        :param sort_order: The sort order for the results.
        :param status_equals: Filters deployments by status.
        :param model_arn_equals: Filters deployments by the Amazon Resource Name (ARN) of the associated
        custom model.
        :returns: ListCustomModelDeploymentsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListCustomModels")
    def list_custom_models(
        self,
        context: RequestContext,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        name_contains: CustomModelName | None = None,
        base_model_arn_equals: ModelArn | None = None,
        foundation_model_arn_equals: FoundationModelArn | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortModelsBy | None = None,
        sort_order: SortOrder | None = None,
        is_owned: Boolean | None = None,
        model_status: ModelStatus | None = None,
        **kwargs,
    ) -> ListCustomModelsResponse:
        """Returns a list of the custom models that you have created with the
        ``CreateModelCustomizationJob`` operation.

        For more information, see `Custom
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param creation_time_before: Return custom models created before the specified time.
        :param creation_time_after: Return custom models created after the specified time.
        :param name_contains: Return custom models only if the job name contains these characters.
        :param base_model_arn_equals: Return custom models only if the base model Amazon Resource Name (ARN)
        matches this parameter.
        :param foundation_model_arn_equals: Return custom models only if the foundation model Amazon Resource Name
        (ARN) matches this parameter.
        :param max_results: The maximum number of results to return in the response.
        :param next_token: If the total number of results is greater than the ``maxResults`` value
        provided in the request, enter the token returned in the ``nextToken``
        field in the response in this field to return the next batch of results.
        :param sort_by: The field to sort by in the returned list of models.
        :param sort_order: The sort order of the results.
        :param is_owned: Return custom models depending on if the current account owns them
        (``true``) or if they were shared with the current account (``false``).
        :param model_status: The status of them model to filter results by.
        :returns: ListCustomModelsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListEvaluationJobs")
    def list_evaluation_jobs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        status_equals: EvaluationJobStatus | None = None,
        application_type_equals: ApplicationType | None = None,
        name_contains: EvaluationJobName | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortJobsBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListEvaluationJobsResponse:
        """Lists all existing evaluation jobs.

        :param creation_time_after: A filter to only list evaluation jobs created after a specified time.
        :param creation_time_before: A filter to only list evaluation jobs created before a specified time.
        :param status_equals: A filter to only list evaluation jobs that are of a certain status.
        :param application_type_equals: A filter to only list evaluation jobs that are either model evaluations
        or knowledge base evaluations.
        :param name_contains: A filter to only list evaluation jobs that contain a specified string in
        the job name.
        :param max_results: The maximum number of results to return.
        :param next_token: Continuation token from the previous response, for Amazon Bedrock to
        list the next set of results.
        :param sort_by: Specifies a creation time to sort the list of evaluation jobs by when
        they were created.
        :param sort_order: Specifies whether to sort the list of evaluation jobs by either
        ascending or descending order.
        :returns: ListEvaluationJobsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListFoundationModelAgreementOffers")
    def list_foundation_model_agreement_offers(
        self,
        context: RequestContext,
        model_id: BedrockModelId,
        offer_type: OfferType | None = None,
        **kwargs,
    ) -> ListFoundationModelAgreementOffersResponse:
        """Get the offers associated with the specified model.

        :param model_id: Model Id of the foundation model.
        :param offer_type: Type of offer associated with the model.
        :returns: ListFoundationModelAgreementOffersResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListFoundationModels")
    def list_foundation_models(
        self,
        context: RequestContext,
        by_provider: Provider | None = None,
        by_customization_type: ModelCustomization | None = None,
        by_output_modality: ModelModality | None = None,
        by_inference_type: InferenceType | None = None,
        **kwargs,
    ) -> ListFoundationModelsResponse:
        """Lists Amazon Bedrock foundation models that you can use. You can filter
        the results with the request parameters. For more information, see
        `Foundation
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param by_provider: Return models belonging to the model provider that you specify.
        :param by_customization_type: Return models that support the customization type that you specify.
        :param by_output_modality: Return models that support the output modality that you specify.
        :param by_inference_type: Return models that support the inference type that you specify.
        :returns: ListFoundationModelsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListGuardrails")
    def list_guardrails(
        self,
        context: RequestContext,
        guardrail_identifier: GuardrailIdentifier | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListGuardrailsResponse:
        """Lists details about all the guardrails in an account. To list the
        ``DRAFT`` version of all your guardrails, don't specify the
        ``guardrailIdentifier`` field. To list all versions of a guardrail,
        specify the ARN of the guardrail in the ``guardrailIdentifier`` field.

        You can set the maximum number of results to return in a response in the
        ``maxResults`` field. If there are more results than the number you set,
        the response returns a ``nextToken`` that you can send in another
        ``ListGuardrails`` request to see the next batch of results.

        :param guardrail_identifier: The unique identifier of the guardrail.
        :param max_results: The maximum number of results to return in the response.
        :param next_token: If there are more results than were returned in the response, the
        response returns a ``nextToken`` that you can send in another
        ``ListGuardrails`` request to see the next batch of results.
        :returns: ListGuardrailsResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListImportedModels")
    def list_imported_models(
        self,
        context: RequestContext,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        name_contains: ImportedModelName | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortModelsBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListImportedModelsResponse:
        """Returns a list of models you've imported. You can filter the results to
        return based on one or more criteria. For more information, see `Import
        a customized
        model <https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param creation_time_before: Return imported models that created before the specified time.
        :param creation_time_after: Return imported models that were created after the specified time.
        :param name_contains: Return imported models only if the model name contains these characters.
        :param max_results: The maximum number of results to return in the response.
        :param next_token: If the total number of results is greater than the ``maxResults`` value
        provided in the request, enter the token returned in the ``nextToken``
        field in the response in this field to return the next batch of results.
        :param sort_by: The field to sort by in the returned list of imported models.
        :param sort_order: Specifies whetehr to sort the results in ascending or descending order.
        :returns: ListImportedModelsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListInferenceProfiles")
    def list_inference_profiles(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        type_equals: InferenceProfileType | None = None,
        **kwargs,
    ) -> ListInferenceProfilesResponse:
        """Returns a list of inference profiles that you can use. For more
        information, see `Increase throughput and resilience with cross-region
        inference in Amazon
        Bedrock <https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html>`__.
        in the Amazon Bedrock User Guide.

        :param max_results: The maximum number of results to return in the response.
        :param next_token: If the total number of results is greater than the ``maxResults`` value
        provided in the request, enter the token returned in the ``nextToken``
        field in the response in this field to return the next batch of results.
        :param type_equals: Filters for inference profiles that match the type you specify.
        :returns: ListInferenceProfilesResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListMarketplaceModelEndpoints")
    def list_marketplace_model_endpoints(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        model_source_equals: ModelSourceIdentifier | None = None,
        **kwargs,
    ) -> ListMarketplaceModelEndpointsResponse:
        """Lists the endpoints for models from Amazon Bedrock Marketplace in your
        Amazon Web Services account.

        :param max_results: The maximum number of results to return in a single call.
        :param next_token: The token for the next set of results.
        :param model_source_equals: If specified, only endpoints for the given model source identifier are
        returned.
        :returns: ListMarketplaceModelEndpointsResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListModelCopyJobs")
    def list_model_copy_jobs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        status_equals: ModelCopyJobStatus | None = None,
        source_account_equals: AccountId | None = None,
        source_model_arn_equals: ModelArn | None = None,
        target_model_name_contains: CustomModelName | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortJobsBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListModelCopyJobsResponse:
        """Returns a list of model copy jobs that you have submitted. You can
        filter the jobs to return based on one or more criteria. For more
        information, see `Copy models to be used in other
        regions <https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param creation_time_after: Filters for model copy jobs created after the specified time.
        :param creation_time_before: Filters for model copy jobs created before the specified time.
        :param status_equals: Filters for model copy jobs whose status matches the value that you
        specify.
        :param source_account_equals: Filters for model copy jobs in which the account that the source model
        belongs to is equal to the value that you specify.
        :param source_model_arn_equals: Filters for model copy jobs in which the Amazon Resource Name (ARN) of
        the source model to is equal to the value that you specify.
        :param target_model_name_contains: Filters for model copy jobs in which the name of the copied model
        contains the string that you specify.
        :param max_results: The maximum number of results to return in the response.
        :param next_token: If the total number of results is greater than the ``maxResults`` value
        provided in the request, enter the token returned in the ``nextToken``
        field in the response in this field to return the next batch of results.
        :param sort_by: The field to sort by in the returned list of model copy jobs.
        :param sort_order: Specifies whether to sort the results in ascending or descending order.
        :returns: ListModelCopyJobsResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListModelCustomizationJobs")
    def list_model_customization_jobs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        status_equals: FineTuningJobStatus | None = None,
        name_contains: JobName | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortJobsBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListModelCustomizationJobsResponse:
        """Returns a list of model customization jobs that you have submitted. You
        can filter the jobs to return based on one or more criteria.

        For more information, see `Custom
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param creation_time_after: Return customization jobs created after the specified time.
        :param creation_time_before: Return customization jobs created before the specified time.
        :param status_equals: Return customization jobs with the specified status.
        :param name_contains: Return customization jobs only if the job name contains these
        characters.
        :param max_results: The maximum number of results to return in the response.
        :param next_token: If the total number of results is greater than the ``maxResults`` value
        provided in the request, enter the token returned in the ``nextToken``
        field in the response in this field to return the next batch of results.
        :param sort_by: The field to sort by in the returned list of jobs.
        :param sort_order: The sort order of the results.
        :returns: ListModelCustomizationJobsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListModelImportJobs")
    def list_model_import_jobs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        status_equals: ModelImportJobStatus | None = None,
        name_contains: JobName | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortJobsBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListModelImportJobsResponse:
        """Returns a list of import jobs you've submitted. You can filter the
        results to return based on one or more criteria. For more information,
        see `Import a customized
        model <https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param creation_time_after: Return import jobs that were created after the specified time.
        :param creation_time_before: Return import jobs that were created before the specified time.
        :param status_equals: Return imported jobs with the specified status.
        :param name_contains: Return imported jobs only if the job name contains these characters.
        :param max_results: The maximum number of results to return in the response.
        :param next_token: If the total number of results is greater than the ``maxResults`` value
        provided in the request, enter the token returned in the ``nextToken``
        field in the response in this field to return the next batch of results.
        :param sort_by: The field to sort by in the returned list of imported jobs.
        :param sort_order: Specifies whether to sort the results in ascending or descending order.
        :returns: ListModelImportJobsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListModelInvocationJobs")
    def list_model_invocation_jobs(
        self,
        context: RequestContext,
        submit_time_after: Timestamp | None = None,
        submit_time_before: Timestamp | None = None,
        status_equals: ModelInvocationJobStatus | None = None,
        name_contains: ModelInvocationJobName | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortJobsBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListModelInvocationJobsResponse:
        """Lists all batch inference jobs in the account. For more information, see
        `View details about a batch inference
        job <https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-view.html>`__.

        :param submit_time_after: Specify a time to filter for batch inference jobs that were submitted
        after the time you specify.
        :param submit_time_before: Specify a time to filter for batch inference jobs that were submitted
        before the time you specify.
        :param status_equals: Specify a status to filter for batch inference jobs whose statuses match
        the string you specify.
        :param name_contains: Specify a string to filter for batch inference jobs whose names contain
        the string.
        :param max_results: The maximum number of results to return.
        :param next_token: If there were more results than the value you specified in the
        ``maxResults`` field in a previous ``ListModelInvocationJobs`` request,
        the response would have returned a ``nextToken`` value.
        :param sort_by: An attribute by which to sort the results.
        :param sort_order: Specifies whether to sort the results by ascending or descending order.
        :returns: ListModelInvocationJobsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListPromptRouters", expand=False)
    def list_prompt_routers(
        self, context: RequestContext, request: ListPromptRoutersRequest, **kwargs
    ) -> ListPromptRoutersResponse:
        """Retrieves a list of prompt routers.

        :param max_results: The maximum number of prompt routers to return in one page of results.
        :param next_token: Specify the pagination token from a previous request to retrieve the
        next page of results.
        :param type: The type of the prompt routers, such as whether it's default or custom.
        :returns: ListPromptRoutersResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListProvisionedModelThroughputs")
    def list_provisioned_model_throughputs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        status_equals: ProvisionedModelStatus | None = None,
        model_arn_equals: ModelArn | None = None,
        name_contains: ProvisionedModelName | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortByProvisionedModels | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListProvisionedModelThroughputsResponse:
        """Lists the Provisioned Throughputs in the account. For more information,
        see `Provisioned
        Throughput <https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param creation_time_after: A filter that returns Provisioned Throughputs created after the
        specified time.
        :param creation_time_before: A filter that returns Provisioned Throughputs created before the
        specified time.
        :param status_equals: A filter that returns Provisioned Throughputs if their statuses matches
        the value that you specify.
        :param model_arn_equals: A filter that returns Provisioned Throughputs whose model Amazon
        Resource Name (ARN) is equal to the value that you specify.
        :param name_contains: A filter that returns Provisioned Throughputs if their name contains the
        expression that you specify.
        :param max_results: THe maximum number of results to return in the response.
        :param next_token: If there are more results than the number you specified in the
        ``maxResults`` field, the response returns a ``nextToken`` value.
        :param sort_by: The field by which to sort the returned list of Provisioned Throughputs.
        :param sort_order: The sort order of the results.
        :returns: ListProvisionedModelThroughputsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: TaggableResourcesArn, **kwargs
    ) -> ListTagsForResourceResponse:
        """List the tags associated with the specified resource.

        For more information, see `Tagging
        resources <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :returns: ListTagsForResourceResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("PutModelInvocationLoggingConfiguration")
    def put_model_invocation_logging_configuration(
        self, context: RequestContext, logging_config: LoggingConfig, **kwargs
    ) -> PutModelInvocationLoggingConfigurationResponse:
        """Set the configuration values for model invocation logging.

        :param logging_config: The logging configuration values to set.
        :returns: PutModelInvocationLoggingConfigurationResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("PutUseCaseForModelAccess")
    def put_use_case_for_model_access(
        self, context: RequestContext, form_data: AcknowledgementFormDataBody, **kwargs
    ) -> PutUseCaseForModelAccessResponse:
        """Put usecase for model access.

        :param form_data: Put customer profile Request.
        :returns: PutUseCaseForModelAccessResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("RegisterMarketplaceModelEndpoint")
    def register_marketplace_model_endpoint(
        self,
        context: RequestContext,
        endpoint_identifier: Arn,
        model_source_identifier: ModelSourceIdentifier,
        **kwargs,
    ) -> RegisterMarketplaceModelEndpointResponse:
        """Registers an existing Amazon SageMaker endpoint with Amazon Bedrock
        Marketplace, allowing it to be used with Amazon Bedrock APIs.

        :param endpoint_identifier: The ARN of the Amazon SageMaker endpoint you want to register with
        Amazon Bedrock Marketplace.
        :param model_source_identifier: The ARN of the model from Amazon Bedrock Marketplace that is deployed on
        the endpoint.
        :returns: RegisterMarketplaceModelEndpointResponse
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("StartAutomatedReasoningPolicyBuildWorkflow")
    def start_automated_reasoning_policy_build_workflow(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_type: AutomatedReasoningPolicyBuildWorkflowType,
        source_content: AutomatedReasoningPolicyBuildWorkflowSource,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> StartAutomatedReasoningPolicyBuildWorkflowResponse:
        """Starts a new build workflow for an Automated Reasoning policy. This
        initiates the process of analyzing source documents and generating
        policy rules, variables, and types.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy for
        which to start the build workflow.
        :param build_workflow_type: The type of build workflow to start (e.
        :param source_content: The source content for the build workflow, such as documents to analyze
        or repair instructions for existing policies.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the operation
        completes no more than once.
        :returns: StartAutomatedReasoningPolicyBuildWorkflowResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ResourceInUseException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("StartAutomatedReasoningPolicyTestWorkflow")
    def start_automated_reasoning_policy_test_workflow(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        test_case_ids: AutomatedReasoningPolicyTestCaseIdList | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> StartAutomatedReasoningPolicyTestWorkflowResponse:
        """Initiates a test workflow to validate Automated Reasoning policy tests.
        The workflow executes the specified tests against the policy and
        generates validation results.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy to
        test.
        :param build_workflow_id: The build workflow identifier.
        :param test_case_ids: The list of test identifiers to run.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the operation
        completes no more than one time.
        :returns: StartAutomatedReasoningPolicyTestWorkflowResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceInUseException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("StopEvaluationJob")
    def stop_evaluation_job(
        self, context: RequestContext, job_identifier: EvaluationJobIdentifier, **kwargs
    ) -> StopEvaluationJobResponse:
        """Stops an evaluation job that is current being created or running.

        :param job_identifier: The Amazon Resource Name (ARN) of the evaluation job you want to stop.
        :returns: StopEvaluationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("StopModelCustomizationJob")
    def stop_model_customization_job(
        self, context: RequestContext, job_identifier: ModelCustomizationJobIdentifier, **kwargs
    ) -> StopModelCustomizationJobResponse:
        """Stops an active model customization job. For more information, see
        `Custom
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param job_identifier: Job identifier of the job to stop.
        :returns: StopModelCustomizationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("StopModelInvocationJob")
    def stop_model_invocation_job(
        self, context: RequestContext, job_identifier: ModelInvocationJobIdentifier, **kwargs
    ) -> StopModelInvocationJobResponse:
        """Stops a batch inference job. You're only charged for tokens that were
        already processed. For more information, see `Stop a batch inference
        job <https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-stop.html>`__.

        :param job_identifier: The Amazon Resource Name (ARN) of the batch inference job to stop.
        :returns: StopModelInvocationJobResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: TaggableResourcesArn, tags: TagList, **kwargs
    ) -> TagResourceResponse:
        """Associate tags with a resource. For more information, see `Tagging
        resources <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to tag.
        :param tags: Tags to associate with the resource.
        :returns: TagResourceResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self,
        context: RequestContext,
        resource_arn: TaggableResourcesArn,
        tag_keys: TagKeyList,
        **kwargs,
    ) -> UntagResourceResponse:
        """Remove one or more tags from a resource. For more information, see
        `Tagging
        resources <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to untag.
        :param tag_keys: Tag keys of the tags to remove from the resource.
        :returns: UntagResourceResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateAutomatedReasoningPolicy")
    def update_automated_reasoning_policy(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        policy_definition: AutomatedReasoningPolicyDefinition,
        name: AutomatedReasoningPolicyName | None = None,
        description: AutomatedReasoningPolicyDescription | None = None,
        **kwargs,
    ) -> UpdateAutomatedReasoningPolicyResponse:
        """Updates an existing Automated Reasoning policy with new rules,
        variables, or configuration. This creates a new version of the policy
        while preserving the previous version.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy to
        update.
        :param policy_definition: The updated policy definition containing the formal logic rules,
        variables, and types.
        :param name: The updated name for the Automated Reasoning policy.
        :param description: The updated description for the Automated Reasoning policy.
        :returns: UpdateAutomatedReasoningPolicyResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises TooManyTagsException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateAutomatedReasoningPolicyAnnotations")
    def update_automated_reasoning_policy_annotations(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        build_workflow_id: AutomatedReasoningPolicyBuildWorkflowId,
        annotations: AutomatedReasoningPolicyAnnotationList,
        last_updated_annotation_set_hash: AutomatedReasoningPolicyHash,
        **kwargs,
    ) -> UpdateAutomatedReasoningPolicyAnnotationsResponse:
        """Updates the annotations for an Automated Reasoning policy build
        workflow. This allows you to modify extracted rules, variables, and
        types before finalizing the policy.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy whose
        annotations you want to update.
        :param build_workflow_id: The unique identifier of the build workflow whose annotations you want
        to update.
        :param annotations: The updated annotations containing modified rules, variables, and types
        for the policy.
        :param last_updated_annotation_set_hash: The hash value of the annotation set that you're updating.
        :returns: UpdateAutomatedReasoningPolicyAnnotationsResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateAutomatedReasoningPolicyTestCase")
    def update_automated_reasoning_policy_test_case(
        self,
        context: RequestContext,
        policy_arn: AutomatedReasoningPolicyArn,
        test_case_id: AutomatedReasoningPolicyTestCaseId,
        guard_content: AutomatedReasoningPolicyTestGuardContent,
        last_updated_at: Timestamp,
        expected_aggregated_findings_result: AutomatedReasoningCheckResult,
        query_content: AutomatedReasoningPolicyTestQueryContent | None = None,
        confidence_threshold: AutomatedReasoningCheckTranslationConfidence | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> UpdateAutomatedReasoningPolicyTestCaseResponse:
        """Updates an existing Automated Reasoning policy test. You can modify the
        content, query, expected result, and confidence threshold.

        :param policy_arn: The Amazon Resource Name (ARN) of the Automated Reasoning policy that
        contains the test.
        :param test_case_id: The unique identifier of the test to update.
        :param guard_content: The updated content to be validated by the Automated Reasoning policy.
        :param last_updated_at: The timestamp when the test was last updated.
        :param expected_aggregated_findings_result: The updated expected result of the Automated Reasoning check.
        :param query_content: The updated input query or prompt that generated the content.
        :param confidence_threshold: The updated minimum confidence level for logic validation.
        :param client_request_token: A unique, case-sensitive identifier to ensure that the operation
        completes no more than one time.
        :returns: UpdateAutomatedReasoningPolicyTestCaseResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceInUseException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateGuardrail")
    def update_guardrail(
        self,
        context: RequestContext,
        guardrail_identifier: GuardrailIdentifier,
        name: GuardrailName,
        blocked_input_messaging: GuardrailBlockedMessaging,
        blocked_outputs_messaging: GuardrailBlockedMessaging,
        description: GuardrailDescription | None = None,
        topic_policy_config: GuardrailTopicPolicyConfig | None = None,
        content_policy_config: GuardrailContentPolicyConfig | None = None,
        word_policy_config: GuardrailWordPolicyConfig | None = None,
        sensitive_information_policy_config: GuardrailSensitiveInformationPolicyConfig
        | None = None,
        contextual_grounding_policy_config: GuardrailContextualGroundingPolicyConfig | None = None,
        automated_reasoning_policy_config: GuardrailAutomatedReasoningPolicyConfig | None = None,
        cross_region_config: GuardrailCrossRegionConfig | None = None,
        kms_key_id: KmsKeyId | None = None,
        **kwargs,
    ) -> UpdateGuardrailResponse:
        """Updates a guardrail with the values you specify.

        -  Specify a ``name`` and optional ``description``.

        -  Specify messages for when the guardrail successfully blocks a prompt
           or a model response in the ``blockedInputMessaging`` and
           ``blockedOutputsMessaging`` fields.

        -  Specify topics for the guardrail to deny in the ``topicPolicyConfig``
           object. Each
           `GuardrailTopicConfig <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicConfig.html>`__
           object in the ``topicsConfig`` list pertains to one topic.

           -  Give a ``name`` and ``description`` so that the guardrail can
              properly identify the topic.

           -  Specify ``DENY`` in the ``type`` field.

           -  (Optional) Provide up to five prompts that you would categorize as
              belonging to the topic in the ``examples`` list.

        -  Specify filter strengths for the harmful categories defined in Amazon
           Bedrock in the ``contentPolicyConfig`` object. Each
           `GuardrailContentFilterConfig <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html>`__
           object in the ``filtersConfig`` list pertains to a harmful category.
           For more information, see `Content
           filters <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters>`__.
           For more information about the fields in a content filter, see
           `GuardrailContentFilterConfig <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html>`__.

           -  Specify the category in the ``type`` field.

           -  Specify the strength of the filter for prompts in the
              ``inputStrength`` field and for model responses in the
              ``strength`` field of the
              `GuardrailContentFilterConfig <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html>`__.

        -  (Optional) For security, include the ARN of a KMS key in the
           ``kmsKeyId`` field.

        :param guardrail_identifier: The unique identifier of the guardrail.
        :param name: A name for the guardrail.
        :param blocked_input_messaging: The message to return when the guardrail blocks a prompt.
        :param blocked_outputs_messaging: The message to return when the guardrail blocks a model response.
        :param description: A description of the guardrail.
        :param topic_policy_config: The topic policy to configure for the guardrail.
        :param content_policy_config: The content policy to configure for the guardrail.
        :param word_policy_config: The word policy to configure for the guardrail.
        :param sensitive_information_policy_config: The sensitive information policy to configure for the guardrail.
        :param contextual_grounding_policy_config: The contextual grounding policy configuration used to update a
        guardrail.
        :param automated_reasoning_policy_config: Updated configuration for Automated Reasoning policies associated with
        the guardrail.
        :param cross_region_config: The system-defined guardrail profile that you're using with your
        guardrail.
        :param kms_key_id: The ARN of the KMS key with which to encrypt the guardrail.
        :returns: UpdateGuardrailResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateMarketplaceModelEndpoint")
    def update_marketplace_model_endpoint(
        self,
        context: RequestContext,
        endpoint_arn: Arn,
        endpoint_config: EndpointConfig,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> UpdateMarketplaceModelEndpointResponse:
        """Updates the configuration of an existing endpoint for a model from
        Amazon Bedrock Marketplace.

        :param endpoint_arn: The Amazon Resource Name (ARN) of the endpoint you want to update.
        :param endpoint_config: The new configuration for the endpoint, including the number and type of
        instances to use.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :returns: UpdateMarketplaceModelEndpointResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateProvisionedModelThroughput")
    def update_provisioned_model_throughput(
        self,
        context: RequestContext,
        provisioned_model_id: ProvisionedModelId,
        desired_provisioned_model_name: ProvisionedModelName | None = None,
        desired_model_id: ModelIdentifier | None = None,
        **kwargs,
    ) -> UpdateProvisionedModelThroughputResponse:
        """Updates the name or associated model for a Provisioned Throughput. For
        more information, see `Provisioned
        Throughput <https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html>`__
        in the `Amazon Bedrock User
        Guide <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html>`__.

        :param provisioned_model_id: The Amazon Resource Name (ARN) or name of the Provisioned Throughput to
        update.
        :param desired_provisioned_model_name: The new name for this Provisioned Throughput.
        :param desired_model_id: The Amazon Resource Name (ARN) of the new model to associate with this
        Provisioned Throughput.
        :returns: UpdateProvisionedModelThroughputResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises ThrottlingException:
        """
        raise NotImplementedError
