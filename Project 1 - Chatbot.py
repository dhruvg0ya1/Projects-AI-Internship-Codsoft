import re
import random

def get_random_response(responses):
    return random.choice(responses)

def better_chatbot(user_input):
    rules = {
        r'(hi|hello|hey)(\s|!|\.|$)': ['Hello!', 'Hi there!', 'Hey!'],
        r'how are you(\s|!|\.|$)': ['I am good, thank you!', 'Fine, thanks!'],
        r'what is your name(\s|!|\.|$)': ['I am a chatbot created by OpenAI.', 'Call me ChatBot.'],
        r'bye|goodbye(\s|!|\.|$)': ['Goodbye!', 'See you later!'],
        r'(what can you do|tell me about yourself)(\s|!|\.|$)': [
            "I'm a simple chatbot that can engage in basic conversation.",
            "I can answer questions and provide information within my programming.",
            "Feel free to ask me anything!"
        ],
        r'(tell me a joke|say something funny)(\s|!|\.|$)': [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised."
        ],
        r'(thanks|thank you)(\s|!|\.|$)': ['You\'re welcome!', 'No problem!', 'Happy to help!'],
        r'(.*)': ['I\'m not sure I understand. Could you rephrase that?', 'I didn\'t get that. Can you ask something else?']
    }

    for pattern, responses in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return get_random_response(responses)

# Improved chatbot loop
print("ChatBot: Hello! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye!")
        break

    response = better_chatbot(user_input)
    print("ChatBot:", response)