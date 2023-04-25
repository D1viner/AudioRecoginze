import openai
import os

os.system('')
openai.api_key = "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"


def get_answer(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.5,
        max_tokens=1024)
    return response.choices[0].text


def ask_question():
    flag = True
    greeting = "\033[1;31m我是ChatGPT聊天机器人,我可以回答您的任何问题！如果您想退出,请输入:quit\033[0m"
    print()
    print(greeting)
    print()
    while (flag == True):
        question = input()
        if question != 'quit':
            answer = get_answer(question)
            answer = answer[2:]
            print()
            print(f"\033[1;31m机器人：{answer}\033[0m")
            print()

        else:
            flag = False
            print()
            print("\033[1;31m机器人：后会有期,bye!\033[0m")


ask_question()
