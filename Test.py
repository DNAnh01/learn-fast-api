from Brain import Brain
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
    option = int(input("Select an option:\n1. Select a brain\n2. Create a Brain\n3. Add Knowledge Base\n4. Ask a question\n5. New chat session\n"))
    if option == 1:
        currentBrains = ""
        for _brain in brains:
            currentBrains = currentBrains + str(brains.index(_brain)) + ". " + str(_brain.name) + "\n"
        selectBrain = int(input(currentBrains))
        selectedBrain = brains[selectBrain]
    if option == 2:
        brain_name = input("Brain Name: ")
        brain = Brain(name = brain_name, model = 'gpt-3.5-turbo')
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
            response, chat_session_id = selectedBrain.ask_question(question, chat_session_id = selectedSession)
            print(response)
    if option == 5:
        selectedSession = selectedBrain.new_chat_session()
