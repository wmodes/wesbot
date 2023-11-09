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

# Create a logger instance for the 'routes' module
logger = logging.getLogger('httpd_logger')

# Initialize HTTPBasicAuth for handling basic authentication
auth = HTTPBasicAuth()

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
        
        return flask.render_template("chat.html", system_content=config.SYSTEM_MSGS[config.domain_common])

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
            with open(config.LOG, 'r') as log_file:
                log_content = log_file.read()
            response = flask.Response(log_content, content_type='text/plain')
            return response
        except FileNotFoundError:
            return "HTTPD log file not found."

    return routes_blueprint