import openai
import sys
n = len(sys.argv)
if n == 1:
    print("file id required")
    exit()

print(sys.argv[1])


completion = openai.ChatCompletion.create(
  model=sys.argv[1],
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": sys.argv[2]}
  ]
)

print(completion.choices[0].message)