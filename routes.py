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
import mysecrets
from flask_httpauth import HTTPBasicAuth
from helpers import super_strip

# Create a logger instance for the 'routes' module
logger = logging.getLogger('httpd_logger')

# Initialize HTTPBasicAuth for handling basic authentication
auth = HTTPBasicAuth()

def log_to_chat(date, client_id, log_object):
    """
    Helper function to log data to CHAT_LOG.

    Args:
      date: The timestamp for the log entry.
      client_id: The client_id for the log entry.
      log_object: The messages object to be logged.
    """
    # Convert the log_object to a JSON-formatted string
    log_object_str = json.dumps(log_object)
    # Log the data to CHAT_LOG
    with open(config.CHAT_LOG, 'a') as log_file:
        log_file.write(f"{date} - {client_id} - {log_object_str}\n")

@auth.verify_password 
def verify_password(username, password):
    if username in mysecrets.AUTH and mysecrets.AUTH[username] == password:
        return username

def routes(chatbot):
    """Creates a blueprint for the chatbot routes."""

    routes_blueprint = flask.Blueprint("routes", __name__)

    # Define the route for the chatbot interaction page
    @routes_blueprint.route("/")
    def chatbot_interaction():
        # Pass the system_content to the chatbot interaction page
        # print(config.system_content)
        # data = {"system_content": config.system_content}

        major_version = config.MAJOR_VERSION
        minor_version = config.MINOR_VERSION
        patch_version = config.PATCH_VERSION

        # Extracting the final portion of the model number
        model_suffix = config.OPENAI_FINE_TUNE_ID.split(":")[-1]

        # Creating the fingerprint by combining the model suffix and temperature
        fingerprint = f"{model_suffix}-{config.OPENAI_PARAMS['temperature']}"

        # Create a version_num variable
        version = f"{major_version}.{minor_version}.{patch_version} ({fingerprint})"
        
        return flask.render_template("chat.html", 
                system_content=super_strip(config.SYSTEM_MSGS[config.domain_common]),
                token_max=config.TOKEN_MAX,
                version=version)

    # Define the route for the chatbot API
    @routes_blueprint.route("/api/chatbot", methods=["POST"])
    def chatbot_api():
        """Handles POST requests to the chatbot API."""

        # Get the JSON data from the POST request's body
        data = flask.request.get_json()        
        # Extract the 'messages' field from the JSON data
        messages = data.get("messages")

        # client_ip for logging
        client_ip = flask.request.remote_addr # cleared
        # client_id for logging
        client_id = data.get("client_id") # cleared
        # timestamp for logging
        timestamp = time.strftime("%d/%b/%Y:%H:%M:%S +0000", time.gmtime())
        # content_length for loggging: Convert to a JSON string and get char count
        content_length = len(json.dumps(data))
        # user agaent for logging
        user_agent = flask.request.headers.get('User-Agent')

        # Log an entry in HTTPD format
        log_entry = f'{client_ip} - {client_id} - [{timestamp}] "POST /api/chatbot HTTP/1.1" 200 {content_length} "{user_agent}"'
        logger.info(log_entry)

        # If the chat has only three entries (the system message, the user message, and the assistant message), then the user has just started the chat. In this case, we log the assistant message to CHAT_LOG.
        if len(messages) == 2:
            # Log the start of the chat
            system_message = {"role": "system", "content": "New conversation"}
            log_to_chat(timestamp, client_id, system_message)
            # Get the assistant message which is the second message
            assistant_message = messages[0]
            # Log the assistant message to CHAT_LOG
            log_to_chat(timestamp, client_id, assistant_message)

        # Get last message from the conversation
        user_message = messages[-1]
        # Log the user request data to CHAT_LOG
        log_to_chat(timestamp, client_id, user_message)

        # print("messages:", messages)

        # Generate a response to the messages
        response = chatbot.get_response(messages)

        # Response is an object of the form: 
        #     { 'message': {
        #             "role": "assistant",
        #             "content": "Hey there! Not much, just hangin'.'"
        #         },
        #         'tokens': 1978,
        #         'status': 'success' }

        # Get message chat object
        message = response["message"]
        # Log the response to CHAT_LOG
        log_to_chat(timestamp, client_id, message)


        # print("routes.py: raw response:", response)

        # Pass on the response
        return flask.jsonify(response)
    
    # Define a route for serving the images in /static/img
    @routes_blueprint.route('/img/<filename>')
    def serve_image(filename):
        return flask.send_from_directory('static/img', filename)
    
    # Define a route for serving the favicon.ico file
    @routes_blueprint.route('/favicon.ico')
    def favicon():
        return flask.send_from_directory('static/img', 'favicon.ico')

    # Define a route to return the contents of the HTTPD log with basic authentication
    @routes_blueprint.route('/log/httpd')
    @auth.login_required
    def httpd_log():
        try:
            with open(config.ACCESS_LOG, 'r') as log_file:
                log_content = log_file.read()
            response = flask.Response(log_content, content_type='text/plain')
            return response
        except FileNotFoundError:
            return "HTTPD log file not found."
        
    # Define a route to return the contents of the chat log with basic authentication
    @routes_blueprint.route('/log/chat')
    @auth.login_required
    def chat_log():
        try:
            with open(config.CHAT_LOG, 'r') as log_file:
                log_content = log_file.read()
            response = flask.Response(log_content, content_type='text/plain')
            return response
        except FileNotFoundError:
            return "CHAT log file not found."

    return routes_blueprint