import openai
import asyncio

# Configure your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

async def get_openai_response(prompt: str) -> str:
    loop = asyncio.get_event_loop()
    try:
        response = await loop.run_in_executor(
            None,
            lambda: openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
            )
        )
        return response.choices[0].message["content"]
    except Exception as e:
        raise Exception(f"Error contacting OpenAI: {e}")
