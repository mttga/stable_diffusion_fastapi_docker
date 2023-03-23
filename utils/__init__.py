import os
from .image_utils import image_to_base64, base64_to_image
from .fastapi_utils import check_image_size

LOCAL_MODELS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'model_files')