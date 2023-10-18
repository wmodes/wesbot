"""
routes.py - Chatbot App Routes

This file contains the routes for the Chatbot app. The routes are defined in a blueprint, which makes it easier to organize the code and reuse it in other applications. The blueprint is registered with the Flask app in the 'factory.py' file.

Author: Wes Modes
Date: 2023
"""

import flask
import config

def routes(chatbot):
    """Creates a blueprint for the chatbot routes."""

    routes_blueprint = flask.Blueprint("routes", __name__)

    # Define the route for the chatbot interaction page
    @routes_blueprint.route("/")
    def chatbot_interaction():
        # Pass the system_content to the chatbot interaction page
        # print(config.system_content)
        # data = {"system_content": config.system_content}
        
        return flask.render_template("chat.html", system_content=config.system_content)

    # Define the route for the chatbot API
    @routes_blueprint.route("/api/chatbot", methods=["POST"])
    def chatbot_api():
        """Handles POST requests to the chatbot API."""

        # Get the JSON data from the POST request's body
        data = flask.request.get_json()

        # Extract the 'messages' field from the JSON data
        messages = data.get("messages")

        # print("messages:", messages)

        # Generate a response to the messages
        response = chatbot.get_response(messages)

        # Response is an object of the form: 
        #   { reply: 'Hey there! How can I help you today?', 
        #     tokens: 1978,
        #     status: 'success' }

        # print("response:", response)

        # Pass on the response
        return flask.jsonify(response)

    return routes_blueprint