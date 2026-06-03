```python
import random
import time

RESPONSES = {
    ("hello", "hi", "hey", "hii", "helo", "howdy"): [
        "Hey there! How can I help you today?",
        "Hello! Nice to see you.",
        "Hi! I'm CodeBot. What's up?"
    ],
    ("how are you", "how r u", "how are u", "wassup", "what's up", "sup"): [
        "I'm doing great, thanks for asking!",
        "All good on my end. How about you?",
        "Running perfectly today."
    ],
    ("what is your name", "who are you", "your name", "what are you"): [
        "I'm CodeBot, your Python assistant.",
        "They call me CodeBot.",
        "I'm CodeBot. Nice to meet you."
    ],
    ("bye", "goodbye", "see you", "exit", "quit", "tata", "cya"): [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Take care."
    ],
    ("thanks", "thank you", "thx", "ty", "thankyou"): [
        "You're welcome!",
        "Happy to help.",
        "No problem."
    ],
    ("help", "what can you do", "options"): [
        "I can chat with you. Try saying hello, asking for the time, or telling me to tell a joke.",
        "Ask me something. I know greetings, jokes, time, and basic conversation."
    ],
    ("joke", "tell me a joke", "say something funny", "funny"): [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the Python programmer break up? Too many TypeErrors.",
        "I told a joke about stack overflow, but it went over everyone's head."
    ],
    ("what time is it", "time", "current time"): [
        "__TIME__"
    ],
    ("who made you", "who created you", "who built you"): [
        "I was built by Avinash Kamella as part of a Python project.",
        "Avinash Kamella created me using Python."
    ],
    ("good morning", "morning"): [
        "Good morning! Hope you have a productive day.",
        "Morning! Have a great day ahead."
    ],
    ("good night", "night", "gn"): [
        "Good night!",
        "Sleep well."
    ],
}

DEFAULT_REPLIES = [
    "I didn't quite understand that.",
    "Could you rephrase that?",
    "I'm still learning. Try asking something else.",
    "I don't have a response for that yet."
]


def get_response(user_input):
    cleaned = user_input.lower().strip()

    for keywords, replies in RESPONSES.items():
        if cleaned in keywords:
            reply = random.choice(replies)

            if reply == "__TIME__":
                return f"Current time: {time.strftime('%I:%M %p')}"

            return reply

    return random.choice(DEFAULT_REPLIES)


def bot_reply(message):
    print("CodeBot is typing...", end="\r")
    time.sleep(0.8)
    print(f"CodeBot: {message}          ")


def main():
    print("=" * 40)
    print("CodeBot - Basic Chatbot")
    print("=" * 40)
    print("Type 'bye' to exit.\n")

    turn_count = 0

    while True:
        try:
            user_input = input("You: ").strip()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        if not user_input:
            print("Please enter a message.")
            continue

        turn_count += 1

        response = get_response(user_input)
        bot_reply(response)

        if user_input.lower().strip() in (
            "bye", "goodbye", "see you",
            "exit", "quit", "tata", "cya"
        ):
            print(f"\nChat ended after {turn_count} messages.")
            break

        print()


if __name__ == "__main__":
    main()
```
