
    [tmbeck] Create a python script that allows someone to use chatgpt from the command line. The python script should use command line parameters to set any options (such as API keys, credentials, URLs to API endpoints, etc.) with defaults for chatgpt. The python script should provide an interactive prompt. Prompts for user input should begin with "Prompt: " and responses from chatgpt should begin with "ChatGPT: ".

    [chatgpt] Sure, here's an example Python script that allows someone to use ChatGPT from the command line using the OpenAI API:

```python
import openai
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Chat with ChatGPT')
parser.add_argument('--model', default='text-davinci-002', help='OpenAI GPT-3 model to use')
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
```

    To use this script, save it to a file (e.g., chatgpt.py) and run it from the command line using Python:

```shell
python chatgpt.py --key YOUR_OPENAI_API_KEY
```

    You can also specify other options using command line arguments, for example:

```shell
python chatgpt.py --key YOUR_OPENAI_API_KEY --model text-davinci-002 --temperature 0.8 --max_tokens 150 --prompt "Hello, ChatGPT! "
```

    This will start an interactive prompt where you can type messages to ChatGPT and receive responses. Type "exit" to exit the program.
