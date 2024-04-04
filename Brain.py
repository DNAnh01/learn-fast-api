import random

from openai import OpenAI
import PyPDF2

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ''
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

class Brain(object):
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.knowledge_base = [{'role':'system', 'content':'You are a helpful assistant. The first prompt will be a long text,'
                                        'and any messages that you get be regarding that. Please answer any '
                                        'questions and requests having in mind the first prompt '}]
        self.client = OpenAI()
        self.chatSessions = []
        self.brain_id = random.randint(100000,999999)

    def add_knowledge_base(self, content):
        # Check file type
        if ".txt" in content:
            content = read_file(content)
        elif ".pdf" in content:
            content = read_pdf(content)
        self.knowledge_base.append({'role': 'user', 'content': content})
        print("Current KnowledgeBases: " + str(len(self.knowledge_base)))
        return self.knowledge_base.index({'role': 'user', 'content': content})

    def remove_knowledge_base(self, content_id):
        self.knowledge_base.remove(self.knowledge_base[content_id])
        return True

    def new_chat_session(self):
        knowledge_base = []
        for item in self.knowledge_base:
            knowledge_base.append(item)
        chat_session = {
            "id": random.randint(100000,999999),
            "knowledgeBase": knowledge_base
        }
        self.chatSessions.append(chat_session)
        return chat_session['id']

    def ask_question(self, question, chat_session_id = None):
        if not chat_session_id:
            chat_session_id = self.new_chat_session()
        for chat_session in self.chatSessions:
            if chat_session['id'] == chat_session_id:
                chat_session['knowledgeBase'].append({'role': 'user', 'content': question})
                response = self.client.chat.completions.create(
                    model = self.model,
                    messages = chat_session['knowledgeBase']
                )
                print(chat_session['knowledgeBase'])
                return response.choices[0].message.content, chat_session_id


