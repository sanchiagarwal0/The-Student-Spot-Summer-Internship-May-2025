#basic chatbot
print("Hello! I'm a basic chatbot. Type 'quit' to end the conversation.")

while True:
    user_input = input("You: ").lower()
    
    if user_input == 'quit':
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    elif 'hello' in user_input or 'hi' in user_input:
        print("Chatbot: Hi there! How can I help you?")
    
    elif 'how are you' in user_input:
        print("Chatbot: I'm just a program, but I'm functioning well! How about you?")
    
    elif 'your name' in user_input:
        print("Chatbot: I'm ChatBot 1.0. What's your name?")
    
    elif 'weather' in user_input:
        print("Chatbot: I'm not connected to weather services, but I hope it's nice where you are!")
    
    elif 'thank' in user_input:
        print("Chatbot: You're welcome! Is there anything else I can help with?")
    
    elif 'joke' in user_input:
        print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
    
    elif 'help' in user_input:
        print("Chatbot: I can respond to greetings, tell you my name, tell a joke, or chat about the weather.")
    
    else:
        print("Chatbot: I'm not sure I understand. Could you try asking something else?")