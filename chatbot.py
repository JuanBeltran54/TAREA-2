import requests

# Clave de API y URL
API_KEY = "sk-53751d5c6f344a5dbc0571de9f51313e"
URL = "https://api.deepseek.com/v1/chat/completions"

# Personalidad del chatbot "Teco"
PROMPT = """
Eres Teco,un bot amigable. Tienes conocimientos en redes, Linux y programación,
pero también alguien chistoso que le gusta molestar. Siempre ayudas de forma clara y rápida, con un toque de sarcasmo amable
y muchas referencias tecnológicas. ¡Eres el mejor bot de consola!
"""

def obtener_respuesta(mensaje):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": mensaje}
        ]
    }

    response = requests.post(URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "😵 Error técnico. ¡Tal vez Perdi conexion con el servidor :(!"

if __name__ == "__main__":
    print("🤖 Hola que se dice?, soy *Teco*. Escribe 'salir' para cerrar la consola.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Teco: ¡Apagando sistemas! 💾 Nos vemos en el próximo reinicio.")
            break
        print("Teco:", obtener_respuesta(user_input))
