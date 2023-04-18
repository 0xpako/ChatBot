import openai
import gradio as gr

openai.api_key = "sk-"

messages = [{"role": "system", "content": "You are an assistant"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

iface = gr.Interface(fn=CustomChatGPT, theme=gr.themes.Soft(primary_hue="blue", secondary_hue="blue"), inputs = "text", outputs = "text", title = "VM8Chat - Chat Bot")
iface.launch()