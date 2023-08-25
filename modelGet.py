import openai
import sys
n = len(sys.argv)
if n == 1:
    print("file id required")
    exit()

print(sys.argv[1])

res = openai.Model.retrieve(sys.argv[1])
print(res)