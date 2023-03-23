from diffusers import (
    StableDiffusionPipeline,
    StableDiffusionImg2ImgPipeline,
    StableDiffusionInpaintPipeline,
    EulerDiscreteScheduler,
    LMSDiscreteScheduler
)

# add models here if you wanna download their weights in the disk
MODEL_REGISTRY = {
    'text2img':{
        'pipe_class':StableDiffusionPipeline,
        'scheduler_class':EulerDiscreteScheduler,
        'repo_name':'stabilityai/stable-diffusion-2-base',
    },
    'img2img':{
        'pipe_class':StableDiffusionImg2ImgPipeline,
        'scheduler_class':LMSDiscreteScheduler,
        'repo_name':'stabilityai/stable-diffusion-2-base',
    },
    'inpainting':{
        'pipe_class':StableDiffusionInpaintPipeline,
        'scheduler_class':EulerDiscreteScheduler,
        'repo_name':'stabilityai/stable-diffusion-2-inpainting',
    }      
}