import openai

openai.api_key = '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'

print("請輸入詩歌題目：")
title = input()
print("請輸入一句本詩歌發想語：")
poem_start = input()

while True:
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"題目：{title}\n\n詩歌發想語：{poem_start}\n\n",
        max_tokens=2000,
        temperature=0.7
    )

    poem = response.choices[0].text.strip()
    print("---------------------------------")
    print(poem)

    print("是否重新生成一次？(y/n)")
    choice = input()
    if choice.lower() != "y":
        break
