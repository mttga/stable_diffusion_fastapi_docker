from PIL import Image
import base64
from io import BytesIO
from fastapi import HTTPException

def image_to_base64(pil_image:Image)->str:
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def base64_to_image(image_b64:str, field:str='image')->Image.Image:
    try:
        image_data = base64.b64decode(image_b64)
        image = Image.open(BytesIO(image_data))
        return image
    except Exception as e:
        raise HTTPException(
            status_code=422,
            detail=[{
                "loc": [
                    "body",
                    field
                ],
                "msg": f"Cannot decode {image} as an image.",
                "type": "value_error.number.not_ge",
            }]
        )
        
    