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
from helpers import super_strip

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

    def custom_pretty_print(self, data, depth=0, current_depth=0):
        if current_depth > depth:
            print(data)
        else:
            if isinstance(data, dict):
                print("{")
                for key, value in data.items():
                    print("  " * (current_depth + 1), key, end=': ')
                    self.custom_pretty_print(value, depth, current_depth + 1)
                print("  " * current_depth + "}")
            elif isinstance(data, list):
                print("[")
                for item in data:
                    print("  " * (current_depth + 1), end='')
                    self.custom_pretty_print(item, depth, current_depth + 1)
                print("  " * current_depth + "]")
            else:
                print(data)

    def get_response(self, messages):
        """
        Generate a response to a conversation.

        Args:
          messages: A list of message objects representing the conversation
            including the latest message from the user.

        Returns:
          The chatbot's response.
        """

        if (not messages):
            messages = []

        # Prepend the system message to the conversation if it's not already there
        if messages[0]['role'] != 'system':
            # Each system content is preceeded by the default domain focus
            system_content = super_strip(config.SYSTEM_MSGS[config.domain_common])
            messages.insert(0, {"role": "system", "content": system_content})

        # If full lookup is enabled, we call the lookup class to get additional data
        if config.USE_FULL_LOOKUP:
            # get the user prompt
            prompt = messages[-1]['content']
            # get the lookup data
            lookup_data = self.lookup.lookup(prompt)
            # print(f"\nlookup data returned: {lookup_data}")
            # if we got lookup data, replace the user prompt with the lookup data (which includes the user prompt)
            if lookup_data:
                messages[-1]['content'] = lookup_data

        # construct the chat params
        chatParams = config.OPENAI_PARAMS

        # add the messages to the chat params
        chatParams["messages"] = messages

        # add the functions to the chat params if functions are enabled
        if config.USE_FUNCTIONS:
            chatParams['functions'] = config.OPENAI_FUNCTIONS

        # print("\nWhat are we passing (chatParams)?")
        self.custom_pretty_print(chatParams)

        try:
            # Use the OpenAI API to generate a response
            response = openai.ChatCompletion.create(**chatParams)
        
            # print("\nWhat did we get (response)?")
            # self.custom_pretty_print(response)

            # ASSISTANT RESPONSE
            #
            # If we have a response, extract the reply and number of tokens
            # (this is also the base case of any recursion)
            #
            # Example assistant response from API:
            #
            #     {   "choices": [
            #             { "message": {
            #                     "role": "assistant",
            #                     "content": "Hey there! Not much, just hangin'.'"
            #                 },
            #                 "finish_reason": "stop"
            #             }, # ...
            #         ], # ...
            #     }
            #
            # Is this a normal model response? i.e. not a function call?
            if 'function_call' not in response['choices'][0]['message']:
                # print(f"We have a normal response!")
                # Extract the generated response
                # reply = response['choices'][0]['message']['content']
                message = response['choices'][0]['message']

                # Extract number of tokens
                tokens = response['usage']['total_tokens']

                response = {
                    'message': message,
                    'tokens': tokens,
                    'status': 'success',
                    }
                return response

            # FUNCTION CALL
            #
            # If we have a function call, get the function name and arguments
            #
            # Example response from API with function call:
            #
            #     {   "choices": [
            #             { "message": {
            #                     "role": "assistant",
            #                     "content": null,
            #                     "function_call": {
            #                         "context": "lookup_proper_noun",
            #                         "arguments": "{\"context\":\"Who is Benzy?\"}"
            #                     }
            #                 },
            #                 "finish_reason": "function_call"
            #             }, # ...
            #         ], # ... 
            #     }
            #
            # if functions are enabled
            if config.USE_FUNCTIONS:
                # print(f"We have a function call!")
                # Add function call message to message history
                #   {"role": "assistant", "content": null, "function_call": {"name": "get_current_weather", "arguments": "{ \"location\": \"Boston, MA\"}"}},
                # NOTE: we don't need to do this because the results of the lookup will be added to the message history as a client message
                # messages.append(response['choices'][0]['message'])
                # Extract the function name and arguments
                function_name = response['choices'][0]['message']['function_call']['name']
                function_args = response['choices'][0]['message']['function_call']['arguments']
                # Extract the user prompt
                prompt = messages[-1]['content']
                print(f"Here was the prompt that triggered a lookup: {prompt}")
                # print(f"function_name: {function_name}\nfunction_args: {function_args}")
                # Call the Lookup class which returns a string that we will assemble into a message
                lookup_results = self.lookup.lookup(prompt, function_name, function_args)
                print(f"results from lookup: {lookup_results}")
            # if functions are disabled
            else:
                # return a message that functions are disabled
                lookup_results = config.LOOKUP_DISABLED
            
            # Response is an object of the form: 
            #     { 'message': {
            #             "role": "assistant",
            #             "content": "Hey there! Not much, just hangin'.'"
            #         },
            #         'tokens': 1978,
            #         'status': 'success' }
            response = {
                'message': {
                    'role': 'lookup',
                    'content': lookup_results,
                },
                'tokens': -1,
                'status': 'success',
            }
            return response

        except openai.error.OpenAIError as e:
            print(e)

            response = {
                'message': {
                    'role': 'lookup',
                    'content': config.CHATBOT_ERROR_MSG,
                },
                'tokens': -1,
                'status': 'error',
              }
            return response
