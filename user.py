
import gradio
Interface(
    fn=main,
    inputs=[
        Audio(
            source="microphone",
            type="filepath",
        ),
    ],
    outputs=[
        Textbox(label="You said: "),
        Textbox(label="AI said: "),
        Textbox(label="AI said (English): "),
        "html",
    ],
    live=True,
    allow_flagging="never",
).launch()