import openai

# list models
models = openai.Model.list()

for m in models['data']:
    print("owned by::", m.owned_by, " ID::", m.id,)
    
print(len(models.data))
    