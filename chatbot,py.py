def bot(user_input):

    user_input = user_input.lower()  # make it case-insensitive


    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "I don't understand that."

def chatbot():
    print("Chatbot: Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = bot(user_input)
        print("Chatbot:", response)

        if user_input.lower() == "bye":
            break



# Start the chatbot
chatbot()

        
