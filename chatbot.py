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

class Chatbot:

    def __init__(self):

        # Set your OpenAI API key and organization (if applicable)
        openai.api_key = secrets.OPENAI_API_KEY
        openai.organization = "org-6Sx3QSqdmkskgXbQf8AsccbW"
        # openai.Model.list()

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

        # Prepend the system message to the conversation
        messages.insert(0, {"role": "system", "content": config.system_content})
        
        logging.info("Received conversation: %s", messages)

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

            response = {
                "reply": reply,
                'tokens': tokens,
              }
            return response

        except openai.error.OpenAIError as e:
            print(e)
            return "I'm sorry, I had an error generating a response."
