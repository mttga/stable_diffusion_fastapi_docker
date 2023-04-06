# Stable Diffusion API with FastAPI (Docker)

This repo implements an API with FastAPI that is capable of generating images using Stable Diffusion. It could serve as a perfect starting point for implementing a custom backend stable-diffusion API with FastAPI. The schema of the API resembles the one. Everything you need is embedded in the Dockerfile, so you can just build the Docker image and start play with it.

### API request
![api_response](https://drive.google.com/uc?export=view&id=1foKdDAjY9-gjcrkpvnxPUoBvnJHcr8uI)

### API response
![api_request](https://drive.google.com/uc?export=view&id=1d2F1z6NA6NCi0YaSBMEpEpBnmpB9JdPP)


## How to use it

The Dockerfile in this repo automatically downloads the latest version of Stable Diffusion (2.1) inside the image and uses Accelerate and Xformers to enable fast and distributed inference. The accelerate_config.yaml file should be modified in order to allow distributed inference and mixed precision as per the instructions in the [Hugging Face Accelerate reference](https://huggingface.co/docs/accelerate/package_reference/cli).

1. Change the base image to the one that contains the CUDA toolkit compatible with your machine.
2. Build the image with: ```sudo docker build  --progress=plain -t dream:v0 .```
3. Run the API with the bash command: ```bash run_api.sh```

You can now visit http://localhost/docs to interact with the API.

## API Request Schema

The api implements text2img, img2img and inpainting schemas. Please visit http://localhost/docs to check the documentation and parameters of the update schema. Following might not updated.

### 1. Text2Image

**POST** `/text2img/`

Generate an image based on a text prompt.

- Request Body (application/json): Text2ImageBody
- Responses:
  - 200: Successful Response
  - 422: Validation Error (HTTPValidationError)

### 2. Img2Img

**POST** `/img2img/`

Generate a new image based on the input image and a text prompt.

- Request Body (application/json): Img2ImgBody
- Responses:
  - 200: Successful Response
  - 422: Validation Error (HTTPValidationError)

### 3. Inpainting

**POST** `/inpainting/`

Perform inpainting on an input image based on a text prompt and a mask image.

- Request Body (application/json): InpaintingBody
- Responses:
  - 200: Successful Response
  - 422: Validation Error (HTTPValidationError)

## Schemas

### Text2ImageBody

| Field           | Type    | Description                                     | Default |
| --------------- | ------- | ----------------------------------------------- | ------- |
| prompt          | string  | The text prompt for generating the image.       |         |
| negative_prompt | string  | Negative prompt for what you don't want in the image. | None    |
| cfg_scale       | integer | Level of text guidance.                         | 7       |
| steps           | integer | Number of diffusion steps.                      | 30      |
| number_of_images| integer | Number of images to generate.                   | 1       |
| seed            | integer | Random seed for generation.                     | None    |
| width           | integer | The width of the image.                         | 768     |
| height          | integer | The height of the image.                        | 768     |

### Img2ImgBody

| Field           | Type    | Description                                     | Default |
| --------------- | ------- | ----------------------------------------------- | ------- |
| prompt          | string  | The text prompt for generating the image.       |         |
| negative_prompt | string  | Negative prompt for what you don't want in the image. | None    |
| cfg_scale       | integer | Level of text guidance.                         | 7       |
| steps           | integer | Number of diffusion steps.                      | 30      |
| number_of_images| integer | Number of images to generate.                   | 1       |
| seed            | integer | Random seed for generation.                     | None    |
| image           | string  | Base64 encoded string of the image.             |         |

### InpaintingBody

| Field           | Type    | Description                                     | Default |
| --------------- | ------- | ----------------------------------------------- | ------- |
| prompt          | string  | The text prompt for generating the image.       |         |
| negative_prompt | string  | Negative prompt for what you don't want in the image. | None    |
| cfg_scale       | integer | Level of text guidance.                         | 7       |
| steps           | integer | Number of diffusion steps.                      | 30      |
| number_of_images| integer | Number of images to generate.                   | 1       |
| seed            | integer | Random seed for generation.                     | None    |
| image           | string  | Base64 encoded string of the image.             |         |
| mask_image      | string  | Base64 encoded string of the mask image.        |         |


### Example of usage:

```python
api_url = "http://localhost:80/generate/"

prompt = "reinassance painting of a Penguin"
negative_prompt = "out of focus, comic"

request_body = {
    "prompt": prompt,
    "negative_prompt":negative_prompt,
    "width": 768,
    "height": 768,
    "cfg_scale": 9,
    "steps": 100,
    "number_of_images": 1,
    "seed": 5
}

response = requests.post(api_url, json=request_body)
def decode_image(img):
    img = io.BytesIO(base64.b64decode(img))
    img = Image.open(img)
    return img

images_base64 = response.json()['images']
images = [decode_image(img) for img in images_base64]
```

## Fine Tuning

The repo contains the official dreamboot training script that can be used to fine tune Stable Diffusion with new concepts. Refer to the [official documentation](https://github.com/huggingface/diffusers/tree/b2c1e0d6d4ffbd93fc0c381e5b9cdf316ca4f99f/examples/dreambooth). Once the model is trained, simply add it in the [model_registry](models/model_registry.py).