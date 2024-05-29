import random

import PyPDF2
from openai import OpenAI


def read_file(file_path):
    """Read content from a text file and return."""
    with open(file_path, "r") as file:
        return file.read()


def read_pdf(file_path):
    """Read text from a PDF file and return."""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ""
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


class Brain(object):
    def __init__(self, name, model):
        """Initialize a Brain object with given name and model."""
        self.name = name
        self.model = model
        self.knowledge_base = [
            {
                "role": "system",
                "content": "You are a helpful assistant. The first prompt will be a long text,"
                "and any messages that you get be regarding that. Please answer any "
                "questions and requests having in mind the first prompt ",
            }
        ]
        self.client = OpenAI()
        self.chatSessions = []
        self.brain_id = random.randint(100000, 999999)

    def add_knowledge_base(self, content):
        """Add knowledge to Brain's knowledge base from a file."""
        # Check file type
        if ".txt" in content:
            content = read_file(content)
        elif ".pdf" in content:
            content = read_pdf(content)
        self.knowledge_base.append({"role": "user", "content": content})
        print("Current KnowledgeBases: " + str(len(self.knowledge_base)))
        return self.knowledge_base.index({"role": "user", "content": content})

    def remove_knowledge_base(self, content_id):
        """Remove a piece of knowledge from Brain's knowledge base."""
        self.knowledge_base.remove(self.knowledge_base[content_id])
        return True

    def new_chat_session(self):
        """Create a new chat session with a copy of the current knowledge base."""
        knowledge_base = []
        for item in self.knowledge_base:
            knowledge_base.append(item)
        chat_session = {
            "id": random.randint(100000, 999999),
            "knowledgeBase": knowledge_base,
        }
        self.chatSessions.append(chat_session)
        return chat_session["id"]

    def ask_question(self, question, chat_session_id=None):
        """Ask a question and get a response from Brain."""
        if not chat_session_id:
            chat_session_id = self.new_chat_session()
        for chat_session in self.chatSessions:
            if chat_session["id"] == chat_session_id:
                chat_session["knowledgeBase"].append(
                    {"role": "user", "content": question}
                )
                response = self.client.chat.completions.create(
                    model=self.model, messages=chat_session["knowledgeBase"]
                )
                print(chat_session["knowledgeBase"])
                return response.choices[0].message.content, chat_session_id


selectedBrain = ""
brains = []
selectedSession = ""
while True:
    print("Current brains: ")
    for _brain in brains:
        print(brains.index(_brain), _brain.name, sep=". ")
    if selectedBrain == "":
        print("You didn't select a brain, please select a brain or create a new one.")
    else:
        print("Selected Brain: " + selectedBrain.name)
        if not selectedSession == "":
            print("Selected Session: " + str(selectedSession))
    option = int(
        input(
            "Select an option:\n1. Select a brain\n2. Create a Brain\n3. Add Knowledge Base\n4. Ask a question\n5. New chat session\n"
        )
    )
    if option == 1:
        currentBrains = ""
        for _brain in brains:
            currentBrains = (
                currentBrains
                + str(brains.index(_brain))
                + ". "
                + str(_brain.name)
                + "\n"
            )
        selectBrain = int(input(currentBrains))
        selectedBrain = brains[selectBrain]
    if option == 2:
        brain_name = input("Brain Name: ")
        brain = Brain(name=brain_name, model="gpt-3.5-turbo")
        brains.append(brain)
        selectedBrain = brain
        selectedSession = ""
    if option == 3:
        file_path = input("File path: ")
        selectedBrain.add_knowledge_base(file_path)
    if option == 4:
        question = input("Input your question: ")
        if selectedSession == "":
            response, chat_session_id = selectedBrain.ask_question(question)
            print(response)
            selectedSession = chat_session_id
        else:
            response, chat_session_id = selectedBrain.ask_question(
                question, chat_session_id=selectedSession
            )
            print(response)
    if option == 5:
        selectedSession = selectedBrain.new_chat_session()
