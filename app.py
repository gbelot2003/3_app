# app.py
from flask import Flask, render_template, request
from conversation.conversation import Conversation

app = Flask(__name__)
conversation = Conversation()

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        conversation.add_message('user', user_input)
        assistant_response = conversation.get_response()
        return render_template('chat.html', user_input=user_input, assistant_response=assistant_response)
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
