import openai

openai.api_key = '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'

def generate_novel(title, protagonist_name, protagonist_age, protagonist_gender):
    prompt = f"標題：{title}\n\n故事開始：\n主角是一個名叫{protagonist_name}的{protagonist_age}歲{protagonist_gender}。"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=4000,
        temperature=0.7,
        n=1
    )
    novel = response.choices[0].text
    
    return novel

while True:
    print("請輸入小說標題：")
    title = input()
    print("請輸入主角姓名：")
    protagonist_name = input()
    print("請輸入主角年齡：")
    protagonist_age = input()
    print("請輸入主角性別：")
    protagonist_gender = input()
    rule="請輸出超過2000字並以小說格式撰寫完成"
    rule=input()
    novel = generate_novel(title, protagonist_name, protagonist_age, protagonist_gender)
    print(novel)
