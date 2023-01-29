import os
import openai
import config
#create the api key from here:https://beta.openai.com/account/api-keys
openai.api_key = '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'
response = openai.Completion.create(
engine="davinci",
prompt="How was universe created?\n\n1.",
temperature=0.3,
max_tokens=64,
top_p=1,
frequency_penalty=0.5,
presence_penalty=0)
print(response)
/* Sample Response
{
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "logprobs": null,
      "text": " Big Bang Theory\n\n2. Steady State Theory\n\n3. Creationism\n\n\nWhat is the Big Bang theory?\n\n1. The universe was created by a big bang.\n\n2. The universe has always existed.\n\n\nWhat is the Steady State Theory?\n\n\nWhat is the"
    }
  ],
  "created": 1675018230,
  "id": "cmpl-6e730YejBqYnEgvwehNZU3bY9wGh2",
  "model": "davinci",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 64,
    "prompt_tokens": 9,
    "total_tokens": 73
  }
}
*/
