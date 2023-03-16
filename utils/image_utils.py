from PIL import Image
import base64
from io import BytesIO

def image_to_base64(pil_image:Image):
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')