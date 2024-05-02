import random

# This list contains the random responses (you can add your own or translate them into your own language too)
# random_responses = ["That is quite interesting, please tell me more.",
#                   "I see. Do go on.",
#                   "Why do you say that?",
#                   "Funny weather we've been having, isn't it?",
#                   "Let's change the subject.",
#                   "Did you catch the game last night?"]

random_responses = ["흥미로운 질문이군요, 더 말해주세요.",
                    "그렇군요. 계속해보시죠.",
                    "왜 그렇게 말씀하셨죠?",
                    "오늘 날씨가 재밌네요, 그렇지 않나요?",
                    "대화 주제를 변경합시다.",
                    "어젯밤 경기 보셨나요?"]

# print("Hello, I am Marvin, the simple robot.")
# print("You can end this conversation at any time by typing 'bye'")
# print("After typing each answer, press 'enter'")
# print("How are you today?")

print("안녕하세요, 저는 마빈, 간단한 로봇입니다.")
print("'안녕'이라고 입력하면 이 대화를 종료할 수 있습니다.")
print("답안을 작성한 후, 'enter'를 누르세요,")
print("오늘은 어떠셨나요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "안녕":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

# print("It was nice talking to you, goodbye!")
print("대화 즐거웠어요, 안녕!")