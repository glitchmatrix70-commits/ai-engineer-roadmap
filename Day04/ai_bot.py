knowledge_base = {
    "hi": "Hello! How can I assist you today?",
    "Hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What would you like to know?",
    "Hello": "Hi there! What would you like to know?",
    "hey": "Hey! I'm here to help. What do you want to ask?",
    "Hey": "Hey! I'm here to help. What do you want to ask?",
    "How are you?": "I'm just a bot, but I'm functioning as expected! How can I help you?",
    "Who are you?": "I am an AI Knowledge Bot designed to answer your questions about AI, programming, and related topics.",
    "Who is your creator?": "I was created by Nancy Sagar, an AI enthusiast and developer.",
    "What is AI?": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "What is Python?": "Python is a popular programming language known for its simple syntax and versatility.",
    "What is Machine Learning?": "Machine Learning is a branch of AI where computers learn patterns from data without being explicitly programmed.",
    "What is Deep Learning?": "Deep Learning is a subset of Machine Learning that uses neural networks with many layers.",
    "What is a chatbot?": "A chatbot is a program that can simulate conversations with users.",
    "Who created Python?": "Python was created by Guido van Rossum.",
    "What is an API?": "An API (Application Programming Interface) allows different software applications to communicate with each other.",
    "What is JSON?": "JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging data.",
    "What is ChatGPT?": "ChatGPT is an AI language model developed by OpenAI that can answer questions and generate text.",
    "What is programming?": "Programming is the process of writing instructions that tell a computer what to do."
}

def answer_question(question):
    if question in knowledge_base:
        return knowledge_base[question]
    else:
        return "I'm sorry, I don't have an answer to that question."

def main():
    print("Welcome to the AI Knowledge Bot!")
    while True:
        user_input = input("Ask me a question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = answer_question(user_input)
        print(response)

if __name__ == "__main__":
    main()
