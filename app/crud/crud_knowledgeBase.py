from app.crud.base import CRUDBase
from app.models.knowledge_base import KnowledgeBase
from app.schemas.knowledge_base import KnowledgeBaseAdd, KnowledgeBaseRemove, KnowledgeBaseOut


class CRUDKnowledgeBase(CRUDBase[KnowledgeBase, KnowledgeBaseAdd, KnowledgeBaseRemove]):
    pass


crud_knowledgeBase = CRUDKnowledgeBase(KnowledgeBase)
