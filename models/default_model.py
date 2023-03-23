import os
from typing import Union
import torch
from PIL.Image import Image

from utils import LOCAL_MODELS_DIR


class DefaultModel:
    
    def __init__(
        self,
        model_config:dict
    ):
        # default scheduler is EulerDiscreteScheduler
        scheduler = model_config['scheduler_class'].from_pretrained(
            model_config['repo_name'],
            subfolder="scheduler",
            cache_dir=LOCAL_MODELS_DIR,
        )
        self.pipe = model_config['pipe_class'].from_pretrained(
            model_config['repo_name'],
            scheduler=scheduler,
            safety_checker=None,
            torch_dtype=torch.float16,
            cache_dir=LOCAL_MODELS_DIR,
        )

    def prepare(self, accelerator):
        self.pipe.to(accelerator.device)
        self.pipe.enable_xformers_memory_efficient_attention()
        self.pipe = accelerator.prepare(self.pipe)
        return self

    def generate(
        self,
        prompt:str,
        cfg_scale:int,
        steps:int,
        number_of_images:int,
        seed:int,
        width:Union[None, int]=None,
        height:Union[None, int]=None,
        image:Union[None, Image] = None,
        mask_image:Union[None, Image] = None
    ):
        # prepare the pipe arguments
        kwargs = {
            'prompt': prompt,
            'generator': torch.Generator(device='cuda').manual_seed(seed),
            'num_images_per_prompt': number_of_images,
            'num_inference_steps': steps,
            'guidance_scale': cfg_scale,
        }
        if width is not None:
            kwargs['width'] = width
            kwargs['height'] = width
        if height is not None:
            kwargs['height'] = height
            if width is None:
                kwargs['width'] = height
        if image is not None:
            kwargs['image'] = image
        if mask_image is not None:
            kwargs['mask_image'] = mask_image

        # run the pipeline
        images = self.pipe(**kwargs).images

        return images









