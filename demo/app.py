import gradio as gr
from deepmultilingualpunctuation import PunctuationModel

# Fungsi prediksi punctuation
def predict_punctuation(text):
    model = PunctuationModel("Rizkinoor16/fullstop-indonesian-punctuation-prediction")
    result = model.restore_punctuation(text)
    return result

demo = gr.Interface(fn=predict_punctuation, inputs="text", outputs="text")
    
if __name__ == "__main__":
    demo.launch()    