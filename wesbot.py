import os
import openai
from flask import Flask, request, render_template, jsonify  # Import 'jsonify' for returning JSON responses
from chatbot import Chatbot
import config

def configure_openai():
    # Set the OpenAI organization and API key
    openai.organization = "org-6Sx3QSqdmkskgXbQf8AsccbW"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()

def create_app():
    app = Flask(__name__)
    chatbot = Chatbot()  # Create an instance of the Chatbot class

    @app.route('/')
    def chatbot_interaction():
        user_input = request.args.get('user_input')

        if user_input:
            response = chatbot.get_response(user_input)
        else:
            response = config.starter_content

        return render_template('chat.html', user_input=user_input, response=response)

    @app.route('/api/chatbot', methods=['POST'])  # Create a new route for handling POST requests
    def chatbot_api():
        # Get the JSON data from the POST request's body
        data = request.get_json()
        # Extract the 'messages' field from the JSON data
        messages = data.get('messages')
        # print("Hit endpoint with messages:", messages )

        response = chatbot.get_response(messages)

        return jsonify(response=response)  # Return the response as JSON

    return app

if __name__ == '__main__':
    configure_openai()  # Call the configuration function
    app = create_app()
    app.run(debug=True)
