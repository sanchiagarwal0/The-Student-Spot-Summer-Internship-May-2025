# Basic Conditional Chatbot

A simple chatbot implemented in Python using conditional statements (if/elif/else) to respond to user input.

## How It Works

The chatbot operates on a straightforward pattern-matching principle:

1. Takes user input and converts it to lowercase for consistent matching
2. Checks the input against a series of conditional statements
3. Returns predefined responses when keywords are detected
4. Continues the conversation until the user types "quit"

## Features

- Responds to common greetings (hi, hello)
- Answers basic questions about itself
- Tells a simple joke
- Handles unrecognized input gracefully
- Easy to extend with new responses

## Code Structure

```python
while True:
    user_input = input().lower()
    
    if user_input == 'quit':
        # Exit condition
    elif 'hello' in user_input:
        # Response to greetings
    elif 'how are you' in user_input:
        # Response to wellbeing check
    # ... more conditions ...
    else:
        # Default response