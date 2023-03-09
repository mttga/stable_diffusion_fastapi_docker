from .default_model import DefaultModel

# add models here if you wanna download their weigths in the Docker image
MODEL_REGISTRY = {
    'stable-diffusion-2-1-base': DefaultModel(model_name="stabilityai/stable-diffusion-2-1-base")
}
