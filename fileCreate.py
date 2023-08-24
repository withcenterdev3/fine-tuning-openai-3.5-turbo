import openai
import sys
n = len(sys.argv)
if n == 1:
    print("file path required")
    exit()

fileRes = openai.File.create(
  file=open(sys.argv[1], "rb"),
  purpose='fine-tune',
  user_provided_filename=sys.argv[1]
)
print(fileRes)
print(fileRes.id)
