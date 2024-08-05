from openai import OpenAI
from config import client_data

client = client_data


def get_model_response(prompt):
    response = client.completions.create(
        model="asst_BCfTUDpmvFKdNu4Gc6BC1qxp",
        prompt=prompt
    )
    return response["choices"][0]["text"]


user_input = input("Вы: ")
while user_input.lower() != "exit":
    response = get_model_response(user_input)
    print("Помощник:", response)
    user_input = input("Вы: ")


# manor load