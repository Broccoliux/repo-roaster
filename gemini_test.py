from roaster import client

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="say hello in one sentence"

)
print(response.text)