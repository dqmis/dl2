# For info on the gemini names see https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versioning#gemini-model-versions
GEMINI_MODEL_NAMES = ["gemini-1.0-pro-vision-001", "gemini-1.5-pro-preview-0409", "gemini-1.5-pro-preview-0514", "gemini-1.5-flash-preview-0514"]
GEMINI_PROJECT_ID = "logic-lm"
GEMINI_LOCATION = "europe-west4"
GEMINI_SERVICE_ACCOUNT = "job-graber"

MODEL_LARGE_CONTEXT = GEMINI_MODEL_NAMES + ["gpt-4"]

# for the experiments
DATASET_NAMES = ("ProntoQA", "ProofWriter", "FOLIO", "LogicalDeduction", "AR-LSAT")
SPLIT_USED_IN_PAPER = "dev"