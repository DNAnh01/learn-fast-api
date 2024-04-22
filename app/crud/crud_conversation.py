from app.crud.base import CRUDBase
from app.models.conversation import Conversation
from app.schemas.conversation import ConversationCreate, ConversationUpdate


class CRUDconversation(CRUDBase[Conversation, ConversationCreate, ConversationUpdate]):
    pass


crud_conversation = CRUDconversation(Conversation)
