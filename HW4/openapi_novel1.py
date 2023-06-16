import openai

openai.api_key = 'Your API TOKEN'
print("請輸入小說標題：")
title = input()
print("請輸入主角姓名：")
protagonist_name = input()
print("請輸入主角年齡：")
protagonist_age = input()
print("請輸入主角性別：")
protagonist_gender = input()

prompt = f"標題：{title}\n\n故事開始：\n主角是一個名叫{protagonist_name}的{protagonist_age}歲{protagonist_gender}。"
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=4000,
    temperature=0.7,
)

print(response.choices[0].text)
