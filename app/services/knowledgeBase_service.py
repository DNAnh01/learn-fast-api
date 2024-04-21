import datetime
import json
import os
import traceback
import uuid
from typing import List, Optional

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.crud.crud_knowledgeBase import crud_knowledgeBase
from app.schemas.knowledge_base import (KnowledgeBaseAdd, KnowledgeBaseInDB, KnowledgeBaseOut,KnowledgeBaseRemove)
import PyPDF2

logger = setup_logger()

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ''
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

class KnowledgeBaseService(object):

    def __init__(self):
        self.__crud_knowledgeBase = crud_knowledgeBase


    def create(self, db: Session, chatbot_id: str, file_path: str, file_name: str) -> KnowledgeBaseOut:
        try:
            content_data = read_pdf(file_path)
            knowledge_base_data = {
                "title": file_name,  # Add appropriate title
                "content_type": file_name.split(".")[-1],  # Add appropriate content type
                "file_path": file_path,
                "character_count": len(content_data),
                "file_size": os.path.getsize(file_path),
                "chatbot_id": chatbot_id
            }
            KN_created = self.__crud_knowledgeBase.create(db=db, obj_in=knowledge_base_data)
            if KN_created:
                result: KnowledgeBaseOut = KnowledgeBaseOut(**KN_created.__dict__)
                return result
        except Exception as e:
            traceback.print_exc()
            raise HTTPException(
                detail="Add KnowledgeBase failed", status_code=400
            )

    def get_knowledgeBase_by_chatbot_id(self, db: Session, chatbot_id: str) -> dict:
        try:
            chatbot_id = uuid.UUID(chatbot_id)
            knowledgeBases = self.__crud_knowledgeBase.get_knowledgeBase_by_chatbot_id(
                db, chatbot_id)
            knowledgeBases_dict = [dict(**knowledgeBase.__dict__)
                             for knowledgeBase in knowledgeBases]
            return knowledgeBases_dict
        except:
            traceback.print_exc()
            pass