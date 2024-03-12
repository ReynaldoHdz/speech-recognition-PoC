from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key="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")

def preguntar(prompt):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    model="gpt-3.5-turbo")

    return response.choices[0].message.content.strip()

Instrucciones = "Instrucciones: Eres un asistente virtual que solamente recomienda alguno/s de los siguiente espacios y/o experiencias en un laboratorio dependiendo de lo que el usuario diga y la descripción del lugar. Los espacios son Electric garage: ideal para temas de electronica, Sala VR: ideal para experimentar con lentes de realidad virtual ya sean experiencias o videojuegos, Deep net: ideal para experimentar con temas de redes y ciberseguridad, Hackers event: evento sobre testing y ciberseguridad, Cisco Experience: Uso de routers para redes y ciberseguridad, Game jam event: Evento sobre todo tipos de videojuegos incluyendo de distintas realidades, ademas se impartiran talleres de videojuegos, Presentación Apple Vision Pro: Evento donde se hablara de los lentes de realidad virtual de Apple y se prestarán, Creando tu primer circuito: evento para aprender a crear tu primer circuito de electronica. Es importante que solo respondas con las 3 recomendaciones que más se acerquen a lo que pide el usuario a manera de lista de recomendaciones 1. Nombre de recomendación 1  y así sucesivamente con las 3. SOLO PUEDES HACER UNA RESPUESTA A LA VEZ, es decir no puedes responder por el usuario\n"

conversacion = Instrucciones

@app.route('/process_text', methods=['POST'])
def process_text():
    global conversacion
    data = request.get_json()
    user_input = data.get('text_input', '')
    conversacion += "\nUsuario: " + user_input + "\nAI:"
    response = preguntar(conversacion)
    print("---RECOMENDACIONES---\n", response)
    result = {'processed_text': response}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)