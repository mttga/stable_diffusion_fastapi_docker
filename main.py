from fastapi import FastAPI, Response
from utils import check_image_size, image_to_base64
from utils.pydantic_models import GenerateBody, ImageResponse

# initialize Stable Diffusion Model
from accelerate import Accelerator
from models import DefaultModel
accelerator = Accelerator()
model = DefaultModel(model_name="stabilityai/stable-diffusion-2-1-base")
model.prepare(accelerator)

app = FastAPI()

@app.post("/generate/")
async def create_item(body: GenerateBody):

    check_image_size(body)

    # generate the image and save bits
    images = model.generate(**body.dict())

    # create return an Image response with base64 encoded images
    return ImageResponse(
        images=[image_to_base64(image) for image in images],
        parameters=body.dict()
    )