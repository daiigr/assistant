from elevenlabs import play
from elevenlabs.client import ElevenLabs
from openai import OpenAI

audioClient = ElevenLabs(
  api_key="", # Defaults to ELEVEN_API_KEY
)





textClient = OpenAI(
    api_key="", # Defaults to OPENAI_API_KEY
)


systemPrompt = "you are a personal assistant helping daniel, a 19 year old computer science student"


messages = [{"role": "system", "content": systemPrompt}]
inputText = ""
output = ""

while True:
  # read text input
  inputText = input("Enter question: ")
  inputMessage = {"role": "user", "content": inputText}
  messages.append(inputMessage)

  stream = textClient.chat.completions.create(
      model="gpt-4",
      messages=messages,
      stream=True,
  )

  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
        output += chunk.choices[0].delta.content

  audio = audioClient.generate(
    text= output,
    voice="Dorothy",
    model="eleven_multilingual_v2"
  )

  play(audio)

  appendMessage = {"role": "assistant", "content": output}  
  messages.append(appendMessage)
