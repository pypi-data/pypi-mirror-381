from enum import Enum

# Lazy import moved to value property below to avoid import-time side effects


class EmbeddingModelsMapper(Enum):
    """Mapper from embedding models' names and embedding models."""
    paraphrase_multilingual_mpnet = "paraphrase_multilingual_mpnet"
    all_mpnet_base = "all_mpnet_base"
    openai_ada = "openai_ada"
    legal_bert = "legal_bert"
    OrlikB_KartonBERT_USE_base_v1 = "OrlikB_KartonBERT_USE_base_v1"
    HuggingFace = "HuggingFace"

    def value(self, **kwargs):
        if self.name == "paraphrase_multilingual_mpnet":
            from .embedders.paraphrase_multilingual_mpnet import ParaphraseMultilingualMpnet
            return ParaphraseMultilingualMpnet()
        elif self.name == "all_mpnet_base":
            from .embedders.all_mpnet_base import AllMpnetBase
            return AllMpnetBase()
        elif self.name == "openai_ada":
            from .embedders.openai_ada import OpenAIAda
            return OpenAIAda()
        elif self.name == "legal_bert":
            from .embedders.legal_bert import LegalBertBaseUncased
            return LegalBertBaseUncased()
        elif self.name == "HuggingFace":
            from .embedders.huggingface_embedder import HuggingFaceEmbedder
            hf_model_name = kwargs.get("hf_model_name")
            if not hf_model_name:
                raise ValueError("'hf_model_name' must be provided for HuggingFace embedder.")
            return HuggingFaceEmbedder(hf_model_name=hf_model_name)
        else:
            raise ValueError(f"Unknown embedder: {self.name}")
