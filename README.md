# Stable Diffusion API with FastAPI (Docker)

This repo implements an API with FastAPI that is capable of generating images using Stable Diffusion. It could serve as a perfect starting point for implementing a custom backend stable-diffusion API with FastAPI. The schema of the API resembles the one. Everything you need is embedded in the Dockerfile, so you can just build the Docker image and start play with it.

|  Request                                    | Response                                  |
|:-------------------------------------------:|:-----------------------------------------:|
|  <img src="https://i.ibb.co/VWKhx63/fastapi-request.png" alt="fastapi-request" width="400" height="250"> |  <img src="https://i.ibb.co/WKGX1Tj/fast-api-response.png" alt="fast-api-response" width="400" height="250"> |

## API Request Schema

This API request schema is used to generate an image with stable diffusion based on a text prompt. The following are the details of the API request:

- HTTP method: POST
- Endpoint: http://localhost/generate/
- Request headers:
  - Accept: image/png
  - Content-Type: application/json
- Request body: a JSON object with the following fields:
  - prompt: a string that represents the text prompt for generating the image.
  - width: an integer that represents the width of the image.
  - height: an integer that represents the height of the image.
  - cfg_scale: an integer that represents the scale of the diffusion configuration.
  - steps: an integer that represents the number of steps to be taken during the diffusion process.
  - number_of_images: an integer that represents the number of images to be generated.
  - seed: an integer that represents the seed for the random number generator used during the image generation process.

Example request:

```bash
curl -X 'POST' \
  'http://localhost/generate/' \
  -H 'accept: image/png' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Illustration of a Stable Diffusion FastAPI API, comic novel, ligth pastel colors",
  "width": 512,
  "height": 512,
  "cfg_scale": 7,
  "steps": 30,
  "number_of_images": 1,
  "seed": 208513106212
}'
```

With minimal work you can add Img2Img, impainting etc. requests.

## How to use it

The Dockerfile in this repo automatically downloads the latest version of Stable Diffusion (2.1) inside the image and uses Accelerate and Xformers to enable fast and distributed inference. The accelerate_config.yaml file should be modified in order to allow distributed inference and mixed precision as per the instructions in the [Hugging Face Accelerate reference](https://huggingface.co/docs/accelerate/package_reference/cli).

1. Change the base image to the one that contains the CUDA toolkit compatible with your machine.
2. Build the image with: ```sudo docker build  --progress=plain -t dream:v0 .```
3. Run the API with the bash command: ```bash run_api.sh```

You can now visit http://localhost/docs to interact with the API.

