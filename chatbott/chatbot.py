"""
TASK 4: Basic Chatbot
CodeAlpha Python Programming Internship
Author: Avinash Kamella
"""

import random   # To pick random replies so the bot doesn't sound repetitive
import time     # To add a small typing delay — feels more like a real chat!

# ─── Response Library ─────────────────────────────────────────────────────────
# This is a dictionary where:
#   KEY   → a tuple of possible things the user might type
#   VALUE → a list of possible bot replies (random one is picked each time)
#
# Why tuples for keys? Tuples are immutable (can't be changed), which makes
# them valid dictionary keys. Lists cannot be used as dict keys in Python.

RESPONSES = {
    ("hello", "hi", "hey", "hii", "helo", "howdy"): [
        "Hey there! 👋 How can I help you today?",
        "Hello! Great to see you! 😊",
        "Hi! I'm CodeBot. What's up?"
    ],
    ("how are you", "how r u", "how are u", "wassup", "what's up", "sup"): [
        "I'm doing great, thanks for asking! 😄",
        "All good on my end! How about you?",
        "Running perfectly — no bugs today! 🤖"
    ],
    ("what is your name", "who are you", "your name", "what are you"): [
        "I'm CodeBot 🤖 — your Python-powered assistant!",
        "They call me CodeBot, built with ❤️ by Avinash.",
        "I'm CodeBot! Nice to meet you 😊"
    ],
    ("bye", "goodbye", "see you", "exit", "quit", "tata", "cya"): [
        "Goodbye! Have an awesome day! 👋",
        "See you later! Keep coding! 💻",
        "Bye bye! 😊 Take care!"
    ],
    ("thanks", "thank you", "thx", "ty", "thankyou"): [
        "You're welcome! 😊",
        "Anytime! Happy to help!",
        "No problem at all! 🙌"
    ],
    ("help", "what can you do", "options"): [
        "I can chat with you! Try saying: hello, how are you, jokes, time, or bye 😊",
        "Ask me anything! I know greetings, jokes, the time, and more!"
    ],
    ("joke", "tell me a joke", "say something funny", "funny"): [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
        "Why did the Python programmer break up? Too many TypeError exceptions! 💔",
        "I told a joke about a stack overflow... but it went over everyone's heads! 😄"
    ],
    ("what time is it", "time", "current time"): [
        # We'll handle this specially in get_response() below
        "__TIME__"
    ],
    ("who made you", "who created you", "who built you"): [
        "I was built by Avinash Kamella as part of the CodeAlpha internship! 🚀",
        "Avinash Kamella created me using Python 🐍"
    ],
    ("good morning", "morning"): [
        "Good morning! ☀️ Hope your day is amazing!",
        "Morning! Let's have a productive day! 💪"
    ],
    ("good night", "night", "gn"): [
        "Good night! 🌙 Sweet dreams!",
        "Rest well! See you tomorrow 😴"
    ],
}

# ─── Default replies when nothing matches ────────────────────────────────────
# Instead of one boring "I don't understand", we have several options

DEFAULT_REPLIES = [
    "Hmm, I didn't quite get that. 🤔 Try asking something else!",
    "I'm still learning! Could you rephrase that?",
    "Not sure about that one. Type 'help' to see what I can do! 😊",
    "Interesting! But I don't have a response for that yet."
]

# ─── Core: Find a matching response ──────────────────────────────────────────

def get_response(user_input):
    """
    Takes the user's message, cleans it up, searches for a match
    in our RESPONSES dictionary, and returns an appropriate reply.

    Steps:
    1. Lowercase + strip the input (so 'Hello' == 'hello')
    2. Loop through all keys (tuples) in RESPONSES
    3. If user input matches any word in a tuple → return a random reply
    4. If nothing matches → return a default reply
    """

    # Clean the input: lowercase and remove extra spaces
    cleaned = user_input.lower().strip()

    # Loop through each key-value pair in the dictionary
    for keywords, replies in RESPONSES.items():
        # Check if cleaned input matches any keyword in the tuple
        if cleaned in keywords:
            reply = random.choice(replies)  # Pick a random reply from the list

            # Special case: if reply is __TIME__, return the actual current time
            if reply == "__TIME__":
                current_time = time.strftime("%I:%M %p")  # e.g. 03:45 PM
                return f"The current time is ⏰ {current_time}"

            return reply

    # Nothing matched — return a random default reply
    return random.choice(DEFAULT_REPLIES)

# ─── Typing Effect ────────────────────────────────────────────────────────────

def bot_reply(message):
    """
    Simulates a typing delay before showing the bot's reply.
    Makes the chat feel more natural and human-like.
    time.sleep(seconds) pauses execution for that many seconds.
    """
    print("  CodeBot is typing...", end="\r")  # \r overwrites the same line
    time.sleep(0.8)                            # Wait 0.8 seconds
    print(f"  🤖 CodeBot: {message}          ")  # Extra spaces clear the previous line

# ─── Main Chat Loop ───────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 45)
    print("     🤖 CODEBOT — CodeAlpha Task 4")
    print("=" * 45)
    print("  Hi! I'm CodeBot. Type 'bye' to exit.\n")

    # Track conversation turns — shows the bot is stateful
    turn_count = 0

    # Infinite loop — keeps chatting until user says bye
    while True:
        try:
            user_input = input("  You: ").strip()
        except KeyboardInterrupt:
            # Handles Ctrl+C gracefully instead of crashing
            print("\n\n  🤖 CodeBot: Caught you pressing Ctrl+C! Goodbye! 👋\n")
            break

        # Don't respond to empty input
        if not user_input:
            print("  ⚠  Please type something!")
            continue

        turn_count += 1
        response = get_response(user_input)
        bot_reply(response)

        # Exit condition: if response is a goodbye message
        cleaned = user_input.lower().strip()
        if cleaned in ("bye", "goodbye", "see you", "exit", "quit", "tata", "cya"):
            print(f"\n  📊 Chat ended after {turn_count} message(s). See you! 👋\n")
            break

        print()  # Blank line between turns for readability

# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
