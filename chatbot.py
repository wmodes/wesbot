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
import mysecrets
import lookup

# Create a logger instance for the 'chatbot' module
logger = logging.getLogger('chatbot_logger')

class Chatbot:

    def __init__(self):

        # Set your OpenAI API key and organization (if applicable)
        openai.api_key = mysecrets.OPENAI_API_KEY
        openai.organization = config.OPENAI_ORG
        # openai.Model.list()

        # instantiate a Lookup class
        self.lookup = lookup.Lookup()

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

        # Each system content is preceeded by the default domain focus
        system_content = config.SYSTEM_MSGS[config.domain_common]
           
        # logging.info("system_content: %s", system_content)

        # Prepend the system message to the conversation
        messages.insert(0, {"role": "system", "content": system_content})
        
        # logging.info("Received conversation: %s", messages)

        try:
            if config.USE_FUNCTIONS:
                functions = config.OPENAI_FUNCTIONS
                # Use the OpenAI API to generate a response
                response = openai.ChatCompletion.create(
                    model=config.OPENAI_PARAMS['model'],
                    messages=messages,
                    temperature=config.OPENAI_PARAMS['temperature'],
                    top_p=config.OPENAI_PARAMS['top_p'],
                    frequency_penalty=config.OPENAI_PARAMS['frequency_penalty'],
                    presence_penalty=config.OPENAI_PARAMS['presence_penalty'],
                    stream=config.OPENAI_PARAMS['stream'],
                    functions=functions
                )
            else:
                # Use the OpenAI API to generate a response
                response = openai.ChatCompletion.create(
                    model=config.OPENAI_PARAMS['model'],
                    messages=messages,
                    temperature=config.OPENAI_PARAMS['temperature'],
                    top_p=config.OPENAI_PARAMS['top_p'],
                    frequency_penalty=config.OPENAI_PARAMS['frequency_penalty'],
                    presence_penalty=config.OPENAI_PARAMS['presence_penalty'],
                    stream=config.OPENAI_PARAMS['stream']
                )

        except openai.error.OpenAIError as e:
            print(e)
            reply = "I'm sorry, I had an error generating a response. Please try again later."

            response = {
                'reply': reply,
                'tokens': -1,
                'status': 'error',
              }
            return response

        print("response: %s", response)

        # ASSISTANT RESPONSE
        #
        # If we have a response, extract the reply and number of tokens
        # (this is also the base case of any recursion)
        #
        # Example assistant response:
        #
        #     {   "choices": [
        #             { # ...
        #                 "message": {
        #                     "role": "assistant",
        #                     "content": "Hey there! Not much, just hangin'.'"
        #                 },
        #                 "finish_reason": "stop"
        #             }
        #         ], # ...
        #     }
        #
        # Is this a normal model response? i.e. not a function call?
        if 'function_call' not in response['choices'][0]['message']:
            # Extract the generated response
            reply = response['choices'][0]['message']['content']

            # Extract number of tokens
            tokens = response['usage']['total_tokens']

            response = {
                'reply': reply,
                'tokens': tokens,
                'status': 'success',
                }
            return response

        # FUNCTION CALL
        #
        # If we have a function call, get the function name and arguments
        #
        # Example response with function call:
        #
        #     {   "choices": [
        #             { # ...
        #                 "message": {
        #                     "role": "assistant",
        #                     "content": null,
        #                     "function_call": {
        #                         "name": "get_entity_info",
        #                         "arguments": "{\"name\":\"Benzy\"}"
        #                     }
        #                 },
        #                 "finish_reason": "function_call"
        #             }
        #         ], # ... 
        #     }
        #
        # if functions are enabled
        if config.USE_FUNCTIONS:
            # Add function call message to message history
            #   {"role": "assistant", "content": null, "function_call": {"name": "get_current_weather", "arguments": "{ \"location\": \"Boston, MA\"}"}},
            messages.append(response['choices'][0]['message'])
            # Extract the function name and arguments
            function_name = response['choices'][0]['message']['function_call']['name']
            function_args = response['choices'][0]['message']['function_call']['arguments']
            logging.info("function_name: %s", function_name)
            logging.info("function_args: %s", function_args)
            # Call the Lookup class with the function name and arguments
            results = self.lookup.lookup(function_name, function_args)
        # if functions are disabled
        else:
            # return a message that functions are disabled
            results = "Sorry, functions are disabled. You will have to improvise a response to the prompt." 

        # Construct new message with results
        #   {"role": "function", "name": "get_current_weather", "content": "{\"temperature\": "22", \"unit\": \"celsius\", \"description\": \"Sunny\"}"}
        response = {
            'role': 'function',
            'name': function_name,
            'content': results,
        }
        # Add response to message history
        messages.append(response)
        # Call this method recursively with the new message history
        return self.get_response(messages)


