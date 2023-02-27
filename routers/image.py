from fastapi import FastAPI, status, HTTPException, APIRouter
from fastapi.responses import JSONResponse
import schemas
import cv2
import numpy as np
import base64


router = APIRouter(prefix="/image", tags=["Image"])


@router.post("/imageupload")
async def process_image(image_fields: schemas.ImageInput):

    try:
        image_fields_dict = image_fields.dict()
        image = np.fromstring(base64.b64decode(image_fields_dict.get("image_data")), dtype=np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_COLOR)

        cv2.imwrite('localoutput.png', img)


        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "success"},
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(e)},
        )