import openai
import sys
n = len(sys.argv)
if n == 1:
    print("file id required")
    exit()

print(sys.argv[1])

jobRes = openai.FineTuningJob.create(training_file=sys.argv[1], model="gpt-3.5-turbo")
print(jobRes)