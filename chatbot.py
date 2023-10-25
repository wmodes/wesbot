"""
chatbot.py - A Python module for an OpenAI-powered chatbot.

This module defines a Chatbot class that interacts with the OpenAI API to generate responses to conversations.

Features:
- Initializes with OpenAI API key and organization (if applicable).
- Provides a method to get responses to conversations.
- Handles exceptions and error messages gracefully.

Author: Wes Modes
Date: 2023
"""

import openai
import logging
import config
import api_secrets

# Create a logger instance for the 'chatbot' module
logger = logging.getLogger('chatbot_logger')

class Chatbot:

    def __init__(self):

        # Set your OpenAI API key and organization (if applicable)
        openai.api_key = api_secrets.OPENAI_API_KEY
        openai.organization = "org-6Sx3QSqdmkskgXbQf8AsccbW"
        # openai.Model.list()

        # This is done instead in javascript
        # self.domain_focus = config.default_domain_focus

    def get_response(self, messages, domain_focus=None):
        """
        Generate a response to a conversation.

        Args:
          messages: A list of message objects representing the conversation.

        Returns:
          The chatbot's response.
        """

        if (not messages):
            messages = []

        # 
        # domain specifc system content 
        # Each system content is preceeded by the default domain focus
        system_content = config.domain_content[config.default_domain_focus]
        # Now add the domain-specific content if it exists and isn't still the default
        # print ("domain_focus before domain-specific content: " + str(domain_focus))
        if domain_focus:
            if domain_focus != config.default_domain_focus and domain_focus in config.domain_content:
                system_content = system_content + "\n" + config.domain_content[domain_focus]
                # print ("domain_focus after domain-specific content: " + str(domain_focus))
            else:
                pass
                # print("Domain focus not found in domain content: " + domain_focus)
        else:
            pass
            # print("No domain focus provided.")
           
        # logging.info("system_content: %s", system_content)

        # Prepend the system message to the conversation
        messages.insert(0, {"role": "system", "content": system_content})
        
        # logging.info("Received conversation: %s", messages)

        try:
            # Use the OpenAI API to generate a response
            response = openai.ChatCompletion.create(
                model=config.model,
                messages=messages,
            )

            # Extract the generated response
            reply = response['choices'][0]['message']['content']

            # Extract number of tokens
            tokens = response['usage']['total_tokens']

            # Check for a domain change
            # we used to do this here and pass it to the javascript
            # but we realized it was better to keep the domain change in the reply
            #
            # Use a regular expression to find [[topic]] at the beginning of the reply
            # match = re.match(r'^\[\[(.*?)\]\]', reply)
            # if match:
            #     # Extract the topic
            #     topic = match.group(1).strip().lower()
            #     # Remove the matched portion from the reply and any following whitespace
            #     reply = re.sub(r'^\[\[.*?\]\]', '', reply).lstrip()
            #     # Change the domain focus
            #     self.domain_focus = topic
            #     logging.info("Domain focus changed to %s", self.domain_focus)

            response = {
                'reply': reply,
                'tokens': tokens,
                'status': 'success',
              }
            return response

        except openai.error.OpenAIError as e:
            print(e)
            reply = "I'm sorry, I had an error generating a response. Please try again later."

            response = {
                'reply': reply,
                'tokens': -1,
                'status': 'error',
              }
            return response
