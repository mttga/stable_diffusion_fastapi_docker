import os
from utils import LOCAL_MODELS_DIR
from models import MODEL_REGISTRY
import torch

def main():

    # create the local cache folder if doesn't exist
    os.makedirs(LOCAL_MODELS_DIR, exist_ok=True)

    for model_name, model_config in MODEL_REGISTRY.items():
        _ = model_config['pipe_class'].from_pretrained(
            model_config['repo_name'],
            safety_checker=None,
            torch_dtype=torch.float16,
            cache_dir=LOCAL_MODELS_DIR
        )

if __name__=='__main__':
    main()
