import sys
import openai

n = len(sys.argv)
if n == 1:
    print("file id missing")
    exit()

res = openai.File.delete(sys.argv[1])
print(res)