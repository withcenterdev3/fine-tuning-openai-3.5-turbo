import openai
import sys
n = len(sys.argv)
if n == 1:
    print("file id required")
    exit()
res = openai.File.download(sys.argv[1])
print(res)