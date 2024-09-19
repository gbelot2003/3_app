from flask import Flask
from routes.chat_routes import chat_bp  # Asegúrate de que la ruta sea correcta

app = Flask(__name__)

# Registrar el blueprint
app.register_blueprint(chat_bp)

if __name__ == '__main__':
    app.run(debug=True)
