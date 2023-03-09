from fastapi import HTTPException

def check_image_size(body):
    # check that widht and height are supported
    if body.width not in {512, 576, 640, 704, 768, 832, 896, 960, 1024}:
        raise HTTPException(
            status_code=422,
            detail=[{
                "loc": [
                    "body",
                    "width"
                ],
                "msg": "Width must be one of 512, 576, 640, 704, 768, 832, 896, 960, 1024",
                "type": "value_error.number.not_ge",
            }]
        )
    if body.height not in {512, 576, 640, 704, 768, 832, 896, 960, 1024}:
        raise HTTPException(
            status_code=422,
            detail=[{
                "loc": [
                    "body",
                    "height"
                ],
                "msg": "Height must be one of 512, 576, 640, 704, 768, 832, 896, 960, 1024",
                "type": "value_error.number.not_ge",
            }]
        )