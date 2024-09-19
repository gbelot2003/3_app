from flask import Blueprint, render_template, request
from conversation.chat import Chat as Conversation # Importa desde el paquete directamente

chat_bp = Blueprint('chat', __name__)
conversation = Conversation()

@chat_bp.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        conversation.add_message('user', user_input)
        assistant_response = conversation.get_response()
        return render_template('chat.html', user_input=user_input, assistant_response=assistant_response)
    return render_template('chat.html')
