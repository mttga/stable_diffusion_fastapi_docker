from pydantic import BaseModel, Field
from typing import Union, List

class BaseBody(BaseModel):
    prompt: str = Field(
        ...,
        max_length=300,
        description="The text prompt for generating the image."
    )
    negative_prompt: Union[str, None] = Field(
        default=None,
        max_length=300,
        description="Negative prompt for what you don't want in the image."
    )
    cfg_scale: int = Field(
        default=7,
        ge=0,
        le=20,
        description="Level of text guidance."
    )
    steps: int = Field(
        default=30,
        ge=10,
        le=150,
        description="Number of diffusion steps."
    )
    number_of_images: int = Field(
        default=1,
        ge=1,
        le=8,
        description="Number of images to generate."
    )
    seed: Union[int, None] = Field(
        default=None,
        example=208513106212,
        description="Random seed for generation."
    )

class Text2ImageBody(BaseBody):
    width: int = Field(
        default=768,
        ge=512,
        le=1024,
        description="The width of the image."
    )
    height: int = Field(
        default=768,
        ge=512,
        le=1024,
        description="The width of the image."
    )

class Img2ImgBody(BaseBody):
    image: str = Field(
        ...,
        description="Base64 encoded string of the image."
    )

class InpaintingBody(Img2ImgBody):
    mask_image: str = Field(
        ...,
        description="Base64 encoded string of the mask image."
    )

class ImageResponse(BaseModel):
    images: List[str] = Field(default=None, title="Image", description="The generated images in base64 format.")
    parameters: dict