import os
from dotenv import load_dotenv
from chatmanager import Chatmanager
load_dotenv()

def main():
    api_key = os.getenv("CHATGPT_API_KEY")
    gpt_model = os.getenv("CHATGPT_MODEL")
    chat_manager = Chatmanager(api_key, gpt_model, 3000)

    print("Chat started Type 'new' to start a new chat, exit to end the conversation")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chat ended.")
            break
        elif user_input.lower() == "new":
            chat_manager.start_new_chat()
            print("Starting a new chat...")
        else:
            chat_manager.add_user_message(user_input)
            assistant_reply = chat_manager.get_response()
            print("ChatGPT:", assistant_reply)
if __name__ == "__main__":
    main()