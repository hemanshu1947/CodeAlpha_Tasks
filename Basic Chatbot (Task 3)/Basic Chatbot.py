# Basic ChatBot

# Function for chatbot replies
def chatbot_reply(user_input):

    # Predefined responses
    if user_input == "hello" or user_input == "hi":
        return "Hello! How can I help you?"

    elif user_input == "how are you":
        return "I am fine. How are you?"

    elif user_input == "what is your name":
        return "My name is Papi."

    elif user_input == "who created you":
        return "I was created using Python."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


# Main program
print("=== Simple Rule-Based ChatBot ===")
print("Type 'bye' to exit\n")

# Loop to keep chatbot running
while True:

    # Taking input from user
    user = input("You: ").lower()

    # Function call
    response = chatbot_reply(user)

    # Output from chatbot
    print("Bot:", response)

    # Exit condition
    if user == "bye":
        break