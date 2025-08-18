from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("KIMI_K2_API_KEY"),
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="moonshotai/kimi-k2:free",
  messages=[
    {
      "role": "user",
      "content": "A man needs to transport a goat, a pile of grass, and a lion across a river using a small boat. The boat is only large enough to carry the man and one of the three items at a time. However, there are certain conditions that must be considered: if left alone without the man, the goat will eat the grass, and the lion will eat the goat. The lion does not eat grass, and it is assumed that the lion will not attack the man as long as they are together. The challenge is to figure out how the man can get all three — the goat, the grass, and the lion — safely across the river without any of them being harmed or eaten."
    }
  ]
)
print(completion.choices[0].message.content)