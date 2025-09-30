from transformers import pipeline
import gradio as gr

# Use default model
model = pipeline('summarization')

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# Use Gradio Blocks
with gr.Blocks() as demo:
    textbox = gr.Textbox(label="Enter text block to summarize", lines=4)
    outputbox = gr.Textbox(label="Summary")
    btn = gr.Button("Summarize")
    
    # Connect button to function
    btn.click(fn=predict, inputs=textbox, outputs=outputbox)

# Launch the app
demo.launch(share=True)