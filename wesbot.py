import os
import openai
from flask import Flask, request, render_template, jsonify  # Import 'jsonify' for returning JSON responses
from chatbot import Chatbot
import config


def app():    
    # Set the OpenAI organization and API key
    openai.organization = "org-6Sx3QSqdmkskgXbQf8AsccbW"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # list the models available to you
    openai.Model.list()

    flask_app = Flask(__name__)
    chatbot = Chatbot()  # Create an instance of the Chatbot class

    @flask_app.route('/')
    def chatbot_interaction():
        data = {"system_content" : config.system_content}
        return render_template('chat.html', data=data)

    @flask_app.route('/api/chatbot', methods=['POST'])  # Create a new route for handling POST requests
    def chatbot_api():
        # Get the JSON data from the POST request's body
        data = request.get_json()
        # Extract the 'messages' field from the JSON data
        messages = data.get('messages')
        # print("Hit endpoint with messages:", messages )

        response = chatbot.get_response(messages)

        return jsonify(response=response)  # Return the response as JSON

    return flask_app

if __name__ == '__main__':
    app = app()
    app.run(debug=True)
