from fastapi import APIRouter
from routes.conversation import router as conversation


router = APIRouter(prefix="/v1")

router.include_router(conversation, tags=["Conversation"])