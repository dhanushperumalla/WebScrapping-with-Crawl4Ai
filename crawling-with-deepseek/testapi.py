from groq import Groq
from dotenv import load_dotenv

# api_key = "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"
load_dotenv(dotenv_path="dev.env")
import os
api_key = os.getenv("GROQ_API_KEY")

print(api_key)
client = Groq(api_key=api_key)

print

completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[
      {
        "role": "user",
        "content": "hii"
      },
      {
        "role": "assistant",
        "content": "Hi! How are you doing today? Is there something I can help you with or would you like to chat?"
      },
      {
        "role": "user",
        "content": "hwllo\n"
      },
      {
        "role": "assistant",
        "content": "<think>\nOkay, the user just said \"hwllo.\" That looks like a typo for \"hello.\" Maybe they were in a hurry or their keyboard is acting up. I should respond in a friendly way to make them feel comfortable. I'll acknowledge their greeting and maybe add a smiley to keep it warm. Something like, \"Hello! How can I assist you today? 😊\" should work. That way, I'm inviting them to ask for help without being too formal.\n</think>\n\nHello! How can I assist you today? 😊"
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=0.6,
    max_completion_tokens=4096,
    top_p=0.95,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
