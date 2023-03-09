from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch

class DefaultModel:
    
    def __init__(
        self,
        model_name:str="stabilityai/stable-diffusion-2-base",
        scheduler=None,
    ):
        # default scheduler is EulerDiscreteScheduler
        if scheduler is None:
            scheduler = EulerDiscreteScheduler.from_pretrained(
                model_name,
                subfolder="scheduler"
            )
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_name,
            scheduler=scheduler,
            safety_checker=None,
            torch_dtype=torch.float16,
        )

    def prepare(self, accelerator):
        self.pipe.to(accelerator.device)
        self.pipe.enable_xformers_memory_efficient_attention()
        self.pipe = accelerator.prepare(self.pipe)


    def generate(
        self,
        prompt:str,
        width:int,
        height:int,
        cfg_scale:int,
        steps:int,
        number_of_images:int,
        seed:int,
    ):
        images = self.pipe(
            prompt,
            width=width,
            height=height,
            generator=torch.Generator(device='cuda').manual_seed(seed),
            num_images_per_prompt=number_of_images,
            num_inference_steps=steps,
            guidance_scale=cfg_scale
        ).images

        return images









