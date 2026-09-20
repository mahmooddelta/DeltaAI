from fastapi import APIRouter



router = APIRouter()

@router.get("/conversation")
async def get_conversation():
    return {"message": "Hello World"}