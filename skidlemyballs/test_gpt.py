from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key='your-api-key')

def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',  # or 'gpt-4' if available
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Example usage
if __name__ == '__main__':
    user_prompt = input('Enter your prompt: ')
    reply = get_chatgpt_response(user_prompt)
    print(f'ChatGPT: {reply}')
