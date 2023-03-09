from fastapi import FastAPI, Response
from utils import GenerateBody, check_image_size
from io import BytesIO

# initialize Stable Diffusion Model
from accelerate import Accelerator
from models import DefaultModel
accelerator = Accelerator()
model = DefaultModel(model_name="stabilityai/stable-diffusion-2-1-base")
model.prepare(accelerator)

app = FastAPI()

@app.post("/generate/",
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response
)
async def create_item(body: GenerateBody):

    check_image_size(body)

    # generate the image and save bits
    images = model.generate(**body.dict())
    buffer = BytesIO()
    images[0].save(buffer, format="png")

    return Response(buffer.getvalue(), media_type="image/png")