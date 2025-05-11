print("🤖 Welcome to ChatBot!")
user_name = input("What's your name? ")

print(f"Hello, {user_name}! Type 'bye' anytime to exit.\n")

while True:
    user_input = input(f"{user_name}: ").lower()

    if user_input == "bye":
        print(f"Bot: Goodbye, {user_name}! Take care.")
        break
    elif "hello" in user_input:
        print(f"Bot: Hello, {user_name}! How can I assist you today?")
    elif "how are you" in user_input:
        print("Bot: I'm just code, but I'm functioning well. Thanks for asking!")
    elif "your name" in user_input:
        print("Bot: I'm ChatBot, your friendly terminal assistant!")
    else:
        print("Bot: Hmm, I didn't understand that. Can you try again?")
