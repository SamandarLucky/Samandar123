import openai

openai.api_key = "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"
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
