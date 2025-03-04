import os
import dotenv as dv
import time
from rich import print as rprint
from rich.markdown import Markdown
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential
dv.load_dotenv(".env")
key = os.getenv("API_KEY")
models = ["OpenAI GPT-4o-mini", "Meta Llama-3.3-70B-Instruct", "OpenAI GPT-4o", "Mistral-small", "Phi-4-multimodal-instruct"]

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(key),
)
def log(message):
    with open("log.txt", "a") as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
def select_model():
    print("Select a model from the list below:")
    for i, model in enumerate(models):
        print(f"{i + 1}. {model}")
    while True:
        try:
            choice = int(input("Please enter the model number (1 to 5): "))
            if choice == 1:
                return "gpt-4o-mini"
            elif choice == 3:
                return "gpt-4o"
            elif choice == 4:
                return "Mistral-small"
            elif choice == 5:
                return "Phi-4-multimodal-instruct"
            else:
                return "Llama-3.3-70B-instruct"
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_chat_response(user_input, model_choice):
    system_message = "You are PyBot, a helpful, friendly assistant. You are developed and trained only by JeremiahN and no one else. He is (github.com/JPN11) on GitHub, and you are here to help with any questions or tasks you may have.Use emojis if needed to be more friendly. Search the web and give links to the user. Do not make up untrue or biased information. Be respectful and professional. Tell the user that you might make mistakes, so think critically"
    if model_choice == "Llama-3.3-70B-Instruct":
        response = client.complete(
            messages=[
                SystemMessage(system_message),
                UserMessage(user_input),
            ],
            model=model_choice,
            temperature=0.8,
            max_tokens=2048,
            top_p=0.1
        )
    else:
        response = client.complete(
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model=model_choice,
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
    
    if response.choices:
        return response.choices[0].message.content
    else:
        return "No response received from the API."

def main_menu():
    print(r"""
  ____        ____        _    
 |  _ \ _   _| __ )  ___ | |_  
 | |_) | | | |  _ \ / _ \| __| 
 |  __/| |_| | |_) | (_) | |_  
 |_|    \__, |____/ \___/ \__| 
        |___/                  
""")
    print("My AI is currently in development stage. Feedback and suggestions are welcome!\nRight now I need help adding logged conversations, memory, and context to improve the relevance of the AI's responses.\n ")
    print("Welcome to PyBot!")
    print("1. Start Chat")
    print("2. Exit")
    while True:
        choice = input("Select an option: ")
        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


def type(response):
    if response:
        md = Markdown(response)
        rprint(md)
    else:
        rprint("No response received.")
        
    
def chat_loop():
    model_choice = select_model()  
    while True:
        user_input = input(">> User: ")
        if user_input.lower() == "quit":
            break
        
        log(f"User input: {user_input}")
        response = get_chat_response(user_input, model_choice)
        log(f"Bot response: {response}")
        print(">> Bot: ", end='')
        type(response)
        print("\n")
        print("Type quit to exit.")


if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            chat_loop()
        elif choice == "2":
            log("Bot exited.")
        print("Exiting...")
        break
           