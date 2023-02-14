import openai
import argparse
import sys
import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

parser = argparse.ArgumentParser(description='Directly query ChatGPT using the API')
parser.add_argument('--key', type=str, help='OpenAI API key')

openai.api_key = os.getenv('OPENAI_API_KEY')

def main(args):
    if not openai.api_key and not args.key:
        parser.error('--key or OPENAI_API_KEY environment variable is required.')
    elif not openai.api_key:
        openai.api_key = args.key
    main_prompt()

def main_prompt():
    text = prompt('> ')
    if text == 'quit':
        sys.exit(1)
    elif text == 'clear':
        os.system('clear')
        main_prompt()
    else:
        query_chatgpt(text)

def query_chatgpt(query):
    prompt = query
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stream=False,
    )

    response = response.choices[0]['text'].strip()
    print(f'\n{response}\n')
    main_prompt()

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)

