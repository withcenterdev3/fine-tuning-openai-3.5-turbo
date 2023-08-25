import openai
import sys
n = len(sys.argv)
if n == 1:
    print("user content required")
    exit()

print("model_id==>",sys.argv[1])
print("user_content==>",sys.argv[2])


completion = openai.ChatCompletion.create(
  model=sys.argv[1],
  messages=[
        {"role": "system", "content": "Flutterflow Basic Troubleshooting Guide 101"},
        {"role": "user", "content": sys.argv[2]}
  ]
)

print(completion.choices[0].message)