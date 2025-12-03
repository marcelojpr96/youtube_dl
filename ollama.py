import ollama  
from ollama import chat
from ollama import ChatResponse
message = ""
messages = []
def getResponse(message):
    messages.append({"role" : "user", "content" : message})
    response : ChatResponse = chat(model="llama3.2:latest", messages=messages)
    messages.append(response.message)
    return response
while message != "bye":
    message = input("give me a message : ")
    response =getResponse(message)
    # print(response)
    # print("\n\n\n----------------------------------------------------------------\n\n\n")
    # print(response.message)
    if message == "bye" :
        break
    print("\n----------------------------------------------------------------\n")
    print("Mr. Roboto",response.message.content)
print(ollama.list().models[0]["model"])