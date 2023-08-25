import openai
import sys
n = len(sys.argv)
if n == 1:
    print("job id required")
    exit()

print(sys.argv[1])

res = openai.FineTuningJob.retrieve(sys.argv[1])
print(res)

# List up to 10 events from a fine-tuning job
events = openai.FineTuningJob.list_events(id=sys.argv[1], limit=10)
for e in events['data']:
    print("created_at::", e.created_at,"message::", e.message)


# print(events)