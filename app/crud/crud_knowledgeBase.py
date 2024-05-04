from uuid import UUID

from sqlalchemy import asc
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.knowledge_base import KnowledgeBase
from app.schemas.knowledge_base import (KnowledgeBaseAdd, KnowledgeBaseOut,
                                        KnowledgeBaseRemove)


class CRUDKnowledgeBase(CRUDBase[KnowledgeBase, KnowledgeBaseAdd, KnowledgeBaseRemove]):
    def get_knowledgeBase_by_chatbot_id(self, db: Session, chatbot_id: UUID):
        result = (db.query(KnowledgeBase)
                  .filter(KnowledgeBase.chatbot_id == chatbot_id)
                  .filter(KnowledgeBase.deleted_at == None)
                  .order_by(asc(KnowledgeBase.created_at))
                  .all())
        return result


crud_knowledgebase = CRUDKnowledgeBase(KnowledgeBase)
