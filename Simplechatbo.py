print("Simple Chatbot (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")
    
    elif user == "how are you":
        print("Bot: I'm fine! What about you?")
    
    elif user == "your name":
        print("Bot: I am a simple chatbot.")
    
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break
    
    else:
        print("Bot: Sorry, I don't understand.")