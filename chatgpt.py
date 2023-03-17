import openai
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Chat with ChatGPT')
parser.add_argument('--model', default='text-davinci-002', choices=['text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001'], help='OpenAI GPT-3 model to use')
parser.add_argument('--key', required=True, help='OpenAI API key')
parser.add_argument('--temperature', default=0.7, type=float, help='Sampling temperature')
parser.add_argument('--max_tokens', default=100, type=int, help='Maximum number of tokens to generate')
parser.add_argument('--prompt', default='', help='Initial prompt for the conversation')
args = parser.parse_args()

# Set up OpenAI API credentials
openai.api_key = args.key

# Set up ChatGPT
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

# Start interactive prompt
prompt = args.prompt
while True:
    # Get user input
    user_input = input(f'Prompt: {prompt}')

    # Exit if user types "exit"
    if user_input == 'exit':
        break

    # Add user input to prompt
    prompt += user_input.strip()

    # Get ChatGPT response
    response = chat(prompt)

    # Print ChatGPT response
    print(f'ChatGPT: {response}')

    # Add ChatGPT response to prompt
    prompt += response.strip()
