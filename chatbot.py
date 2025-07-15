import openai

openai.api_key = "..."

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

while True:
    user_input = input("Ти: ")
    if user_input.lower() in ["вийти", "exit"]:
        break
    reply = chat_with_gpt(user_input)
    print("Бот:", reply)
