import asyncio
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
dotenv_path = find_dotenv()
print(f"Using dotenv file: {dotenv_path}")  # Debug print
load_dotenv(dotenv_path)

# Initialize OpenAI client with API key from .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file.")
print(f"Loaded API key: {api_key[:4]}...")  # Debug print (partial key for safety)

client = OpenAI(api_key=api_key)

async def get_openai_response(prompt: str, model="gpt-4o", max_tokens=150, temperature=0.7) -> str:
    loop = asyncio.get_event_loop()
    messages = [
        {"role": "system", "content": "You are a helpful assistant that creates test questions based on provided textbook content."},
        {"role": "user", "content": prompt}
    ]
    
    try:
        completion = await loop.run_in_executor(
            None,
            lambda: client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        raise Exception(f"Error contacting OpenAI: {e}")

# Example usage:
if __name__ == '__main__':
    user_prompt = input('Enter your prompt: ')

    async def main():
        reply = await get_openai_response(user_prompt)
        print(f'ChatGPT: {reply}')

    asyncio.run(main())
