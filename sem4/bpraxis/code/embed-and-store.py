embeddings = AzureOpenAIEmbeddings(
    azure_deployment="sdllm_embedding_3_large_eastus_test",
    openai_api_version="2024-02-01",
)
store = LocalFileStore("./cache/")

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    embeddings, store, namespace=embeddings.model
)

vectorstore = FAISS.from_documents(documents=all_splits, embedding=cached_embedder)