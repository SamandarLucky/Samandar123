import openai

openai.api_key = ""
def generate_essay_response(prompt):
    # Use the correct method for chat models: openai.ChatCompletion.create()
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or gpt-3.5-turbo, or another available chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,  # Adjust based on essay length
        temperature=0.7  # Adjust creativity level
    )
    essay = response['choices'][0]['message']['content'].strip()
    return essay