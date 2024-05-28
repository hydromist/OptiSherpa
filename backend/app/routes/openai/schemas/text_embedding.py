from ..models import *
from typing import List, Optional, Union

__all__ = [
    "OpenaiTextEmbeddingRequest",
    "OpenaiTextEmbeddingResponse",
    "OpenaiEmbeddingUsage",
    "OpenaiEmbedding",
]


class OpenaiTextEmbeddingRequest(BaseModel):
    input: Union[str, List[Union[str, List[int]]]] = Field(
        ...,
        description="Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model.",
    )

    model: str = Field(
        ..., description="ID of the model to use. You can use the List models API to see all of your available models."
    )

    encoding_format: Optional[str] = Field(
        "float",
        description="The format to return the embeddings in. Can be either 'float' or 'base64'. Defaults to 'float'.",
    )

    dimensions: Optional[int] = Field(
        None, description="The number of dimensions the resulting output embeddings should have."
    )

    user: Optional[str] = Field(
        None, description="A unique identifier representing your end-user, which can help monitor and detect abuse."
    )


class OpenaiEmbeddingUsage(BaseModel):
    prompt_tokens: int = Field(..., description="The number of tokens used by the prompt.")
    total_tokens: int = Field(..., description="The total number of tokens used by the request.")


class OpenaiEmbedding(BaseModel):
    embedding: List[float] = Field(
        ...,
        description="The embedding vector, which is a list of floats. The length of vector depends on the model as listed in the [embedding guide](https://platform.openai.com/docs/guides/embeddings).",
    )
    index: int = Field(..., description="The index of the embedding in the list of embeddings.")
    object: Literal["embedding"] = Field(..., description="The object type, which is always 'embedding'.")


class OpenaiTextEmbeddingResponse(BaseModel):
    data: List[OpenaiEmbedding] = Field(..., description="The list of embeddings generated by the model.")
    model: str = Field(..., description="The name of the model used to generate the embedding.")
    object: Literal["list"] = Field(..., description="The object type, which is always 'list'.")
    usage: OpenaiEmbeddingUsage = Field(..., description="The usage information for the request.")
