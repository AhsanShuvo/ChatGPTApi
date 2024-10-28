from typing import List, Dict
from openai import OpenAI

class Chatmanager:
    def __init__(self, api_key: str, gpt_model: str, max_token = 3000):
        self.messages: List[Dict] = []
        self.max_tokens = max_token
        self.start_new_chat()
        self.client = OpenAI(api_key = api_key)
        self.gpt_model = gpt_model

    def start_new_chat(self, ):
        """
        Start a new chat with ChatGPT
        """
        self.messages = [
            {"role": "system", "content": "You are ChatGPT, a helpful assistant"}
        ]

    def trim_messages(self):
        while sum(len(m["content"]) for m in self.messages) > self.max_tokens:
            self.messages.pop(1)

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})
        self.trim_messages()

    def get_response(self):
        response = self.client.chat.completions.create(
            model = self.gpt_model,
            messages = self.messages
        )
        assistant_reply = response.choices[0].message["content"]
        self.messages.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply
