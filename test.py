from roaster import client

response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Say hello."
)

for chunk in response:
    if chunk.text:
        print(chunk.text, end="")

