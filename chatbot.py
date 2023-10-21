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
import secrets
import re

class Chatbot:

    def __init__(self):

        # Set your OpenAI API key and organization (if applicable)
        openai.api_key = secrets.OPENAI_API_KEY
        openai.organization = "org-6Sx3QSqdmkskgXbQf8AsccbW"
        # openai.Model.list()

        self.domain_focus = config.default_domain_focus

        # Set the logging level 
        logging.basicConfig(level=logging.DEBUG)

    def get_response(self, messages):
        """
        Generate a response to a conversation.

        Args:
          messages: A list of message objects representing the conversation.

        Returns:
          The chatbot's response.
        """

        if (not messages):
            messages = []

        # Create the system message a message object with the role 'system' and domain-specific content
        logging.info("Domain: %s", self.domain_focus)
        # Each domain-specific content is preceeded by the default domain focus
        system_content = config.domain_content[config.default_domain_focus]
        # Now add the domain-specific content if it exists and isn't still the default
        if (self.domain_focus in config.domain_content):
            if (self.domain_focus != config.default_domain_focus):
                system_content = system_content + "\n" + config.domain_content[self.domain_focus]
        else:
            print("Domain focus not found in domain content: " + self.domain_focus)
           
        logging.debug("system_content: %s", system_content)

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
            # Use a regular expression to find [[topic]] at the beginning of the reply
            match = re.match(r'^\[\[(.*?)\]\]', reply)
            if match:
                # Extract the topic
                topic = match.group(1)
                # Remove the matched portion from the reply and any following whitespace
                reply = re.sub(r'^\[\[.*?\]\]', '', reply).lstrip()
                # Change the domain focus
                self.domain_focus = topic.strip().lower()
                logging.info("Domain focus changed to %s", self.domain_focus)

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
