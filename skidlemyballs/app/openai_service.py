import openai
import asyncio
import os

async def get_openai_response(prompt: str) -> str:
    loop = asyncio.get_event_loop()

    messages = [
        {"role": "system", "content": "You are a helpful assistant that creates test questions based on provided textbook content."},
        {"role": "user", "content": prompt}
    ]
    try:
        # Run the blocking OpenAI API call in an executor to avoid blocking the event loop.
        completion = await loop.run_in_executor(
            None,
            lambda: openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=16384,  # Adjust as needed
        )
        )

        # Extract the generated content from the response
        response = completion.choices[0].message["content"]
        return response
    except Exception as e:
        raise Exception(f"Error contacting OpenAI: {e}")