llm = AzureChatOpenAI(
    openai_api_version="2024-02-01",
    azure_deployment="sdllm_gpt_35_eastus",
    temperature=0.1,
)