def greet(name):
    return f"Hello, {name}!"

import gradio as gr

iface = gr.Interface(fn=greet, inputs="text", outputs="text", title="Greeting App", description="Enter your name to receive a greeting.")
iface.launch()