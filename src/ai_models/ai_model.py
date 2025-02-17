from openai import OpenAI

def get_ai_model_response(prompt: str):

    # prompt('AI Model',prompt)
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="qwen/qwen-vl-plus:free",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt
            },
            {
            "type": "image_url",
            "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            }
            }
        ]
        }
    ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content