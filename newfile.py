import openai
# Initialize the API key
openai.api_key = "add your open ai key here"


def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message 

user_prompt = "Write a summary of the benefits of exercise."
chatbot_response = chat_with_chatgpt(user_prompt)
print(chatbot_response)