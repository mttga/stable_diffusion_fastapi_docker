from fastapi import FastAPI, Response
from utils import check_image_size, image_to_base64, base64_to_image
from utils.pydantic_models import Text2ImageBody, Img2ImgBody, InpaintingBody, ImageResponse

# initialize Stable Diffusion Models
from accelerate import Accelerator
from models import DefaultModel, MODEL_REGISTRY

accelerator = Accelerator()
text2img_model  = DefaultModel(MODEL_REGISTRY['dream_mtt']).prepare(accelerator)
img2img_model   = DefaultModel(MODEL_REGISTRY['img2img']).prepare(accelerator)
inpaiting_model = DefaultModel(MODEL_REGISTRY['inpainting']).prepare(accelerator)

# api
app = FastAPI()

@app.post("/text2img/")
async def text2image(body: Text2ImageBody):

    check_image_size(body)
    body = body.dict()

    # generate the image and save bits
    images = text2img_model.generate(**body)

    # create return an Image response with base64 encoded images
    return ImageResponse(
        images=[image_to_base64(image) for image in images],
        parameters=body
    )

@app.post("/img2img/")
async def img2img(body: Img2ImgBody):

    # check and transform
    body = body.dict()
    body['image'] = base64_to_image(body['image'])

    # generate the image and save bits
    images = img2img_model.generate(**body)

    # create return an Image response with base64 encoded images
    return ImageResponse(
        images=[image_to_base64(image) for image in images],
        parameters={k:v for k,v in body.items() if 'image' not in k}
    )

@app.post("/inpainting/")
async def inpainting(body: InpaintingBody):

    body = body.dict()
    body['image'] = base64_to_image(body['image'])
    body['mask_image'] = base64_to_image(body['mask_image'], 'mask_image')

    # generate the image and save bits
    images = inpaiting_model.generate(**body)

    # create return an Image response with base64 encoded images
    return ImageResponse(
        images=[image_to_base64(image) for image in images],
        parameters={k:v for k,v in body.items() if 'image' not in k}
    )