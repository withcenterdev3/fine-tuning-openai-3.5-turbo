import openai
files = openai.File.list()
# print(files)
for f in files['data']:
    print(f.id)
    res = openai.File.delete(f.id)
    print(res)