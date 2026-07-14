
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def bot(input_text):
    response = client.responses.create(
        input=input_text,
        model="llama-3.3-70b-versatile",
    )
    return response.output_text

def main():
    print("Welcome to the AI Knowledge Bot!")
    while True:
        user_input = input("Ask me a question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = bot(user_input)
        print(response)

if __name__ == "__main__":
    main()

