from langchain_huggingface import HuggingFaceEmbeddings
from ragloader.splitting import DocumentChunk
from ragloader.embedding import ChunkEmbedder, EmbeddedChunk


class HuggingFaceEmbedder(ChunkEmbedder):
    def __init__(self, hf_model_name: str, vector_length: int = 1024):
        self.model_name = hf_model_name
        self.embeddings = HuggingFaceEmbeddings(model_name=self.model_name)
        self.vector_length = vector_length

    def embed(self, chunk: DocumentChunk) -> EmbeddedChunk:
        embedding = self.embeddings.embed_query(chunk.content)
        embedded_chunk = EmbeddedChunk(document_chunk=chunk, embedding=embedding, embedding_model=self.model_name)
        return embedded_chunk
