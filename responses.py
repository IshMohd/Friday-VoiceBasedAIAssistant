import random

responses = [
    "I'm sorry, but I can't help with that right now.",
    "I'm still learning! Can you try something else?",
    "I can play music, open websites, and fetch news. Try one of those!",
    "That’s above my pay grade. Maybe ask Google?",
    "Oops! My AI brain doesn’t have that info yet!"
]

def get_response():
    #Returns a random response.
    return random.choice(responses)
