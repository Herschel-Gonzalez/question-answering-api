from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Especifica el modelo de question answering de Hugging Face que deseas utilizar
model_name = "timpal0l/mdeberta-v3-base-squad2"
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Carga el tokenizer y el modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

@app.route('/api/answer', methods=['POST'])
def answer_question():
    # Obtén los datos de la pregunta y el contexto de la solicitud POST
    print(request.json)
    question = request.json['question']
    context = request.json['context']

    # Tokeniza la pregunta y el contexto
    inputs = tokenizer.encode_plus(question, context, return_tensors='pt', truncation=False)

    # Realiza la inferencia con el modelo
    outputs = model(**inputs)
    start_scores = outputs.start_logits
    end_scores = outputs.end_logits
    # Obtiene el índice de inicio y fin de la respuesta más probable
    answer_start = torch.argmax(start_scores)
    answer_end = torch.argmax(end_scores) + 1


    # Decodifica la respuesta
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][answer_start:answer_end]))

    # Devuelve la respuesta como JSON
    return jsonify({'answer': answer})
if __name__ == '__main__':
    app.run(debug=True)

