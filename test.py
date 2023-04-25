import openai

import os

openai.api_key = "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"  # 您需要使用自己的OpenAI API Key


def ask_gpt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # 您可以选择其他的模型引擎，这里使用的是Davinci模型，因为它是OpenAI提供的最强大的模型
        prompt=prompt,
        temperature=0.5,  # 控制生成响应的创造性程度，值越高，响应越创造性
        max_tokens=1500,  # 控制响应的最大长度，避免响应过长
        n=1,  # 控制生成响应的数量，这里设置为1，即只生成一个响应
        stop=None,
    )
    message = response.choices[0].text.strip()
    return message


print("Chat with AI. Type 'quit' to exit")
while True:
    try:
        prompt = input("You: ")
        if prompt.strip().lower() == "quit":
            break
        message = ask_gpt(prompt)
        print("AI: " + message)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
