"""
routes.py - Chatbot App Routes

This file contains the routes for the Chatbot app. The routes are defined in a blueprint, which makes it easier to organize the code and reuse it in other applications. The blueprint is registered with the Flask app in the 'factory.py' file.

Author: Wes Modes
Date: 2023
"""

import flask
import config
import logging
import time
import json

# Create a logger instance for the 'routes' module
logger = logging.getLogger('httpd_logger')

def routes(chatbot):
    """Creates a blueprint for the chatbot routes."""

    routes_blueprint = flask.Blueprint("routes", __name__)

    # Define the route for the chatbot interaction page
    @routes_blueprint.route("/")
    def chatbot_interaction():
        # Pass the system_content to the chatbot interaction page
        # print(config.system_content)
        # data = {"system_content": config.system_content}
        
        return flask.render_template("chat.html", system_content=config.domain_content[config.default_domain_focus])

    # Define the route for the chatbot API
    @routes_blueprint.route("/api/chatbot", methods=["POST"])
    def chatbot_api():
        """Handles POST requests to the chatbot API."""

        # Get the JSON data from the POST request's body
        data = flask.request.get_json()

        # get client_id from the request
        client_id = data.get("client_id") # cleared

        # get user info
        client_ip = flask.request.remote_addr # cleared

        # Get the current timestamp in the desired format
        timestamp = time.strftime("%d/%b/%Y:%H:%M:%S +0000", time.gmtime())

        # Extract the 'messages' field from the JSON data
        messages = data.get("messages")

        # Extract the 'domain_focus' field from the JSON data
        domain = data.get("domain")

        # Convert the data structure to a JSON string
        json_str = json.dumps(data)

        # Get the character count of the JSON string
        content_length = len(json_str)

        # Log an entry in HTTPD format
        log_entry = f'{client_ip} - {client_id} - [{timestamp}] "POST /api/chatbot HTTP/1.1 ({domain})" 200 {content_length}'
        logger.info(log_entry)

        # print("messages:", messages)

        # Generate a response to the messages
        response = chatbot.get_response(messages, domain)

        # Response is an object of the form: 
        #   { reply: 'Hey there! How can I help you today?', 
        #     tokens: 1978,
        #     status: 'success' }

        # print("response:", response)

        # Pass on the response
        return flask.jsonify(response)
    
    # Define a route for serving the favicon.ico file
    @routes_blueprint.route('/favicon.ico')
    def favicon():
        return flask.send_from_directory('static/img', 'favicon.ico')

    return routes_blueprint