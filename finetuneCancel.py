import openai
import sys
n = len(sys.argv)
if n == 1:
    print("job id required")
    exit()

print(sys.argv[1])

res = openai.FineTuningJob.cancel(sys.argv[1])
print(res)