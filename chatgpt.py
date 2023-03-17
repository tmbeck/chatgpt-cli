import openai
import argparse
import sys
import colorama
from colorama import Fore, Style

# Set up argument parser
parser = argparse.ArgumentParser(description='Chat with ChatGPT')
parser.add_argument('--model', default='text-davinci-002', choices=['text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001', 'text-davinci-002-001'], help='OpenAI GPT-3 model to use')
parser.add_argument('--key', required=True, help='OpenAI API key')
parser.add_argument('--temperature', default=0.7, type=float, help='Sampling temperature')
parser.add_argument('--max_tokens', default=100, type=int, help='Maximum number of tokens to generate')
parser.add_argument('--chatgptplus', action='store_true', help='Use a ChatGPT+ model')
args = parser.parse_args()

# Set up OpenAI API credentials
openai.api_key = args.key

# Set up ChatGPT
if args.chatgptplus:
    models = ['text-davinci-002-001', 'text-davinci-002']
else:
    models = ['text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001']
if args.model not in models:
    raise ValueError(f'Invalid model "{args.model}", must be one of {models}')
def chat(prompt):
    response = openai.Completion.create(
        engine=args.model,
        prompt=prompt,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices[0].text.strip()
    return message

# Function to handle KeyboardInterrupt
def handle_keyboard_interrupt():
    print(Fore.MAGENTA + Style.BRIGHT + '\nGoodbye!' + Style.RESET_ALL)
    sys.exit(0)

# Start interactive prompt
colorama.init() # Initialize colorama
while True:
    try:
        # Reset prompt
        prompt = 'Prompt: '

        # Get user input
        user_input = input(prompt)

        # Exit if user types "exit"
        if user_input == 'exit':
            break

        # Get ChatGPT response
        response = chat(user_input)

        # Print ChatGPT response
        print(f'ChatGPT: {response}')

        # Add ChatGPT response to prompt
        prompt += response.strip()

    except KeyboardInterrupt:
        handle_keyboard_interrupt()
