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

    def get_response(self, messages, recursion_depth=0):
        """
        Generate a response to a conversation.

        Args:
          messages: A list of message objects representing the conversation.

        Returns:
          The chatbot's response.
        """

        if (not messages):
            messages = []

        # Check the recursion depth against the limit
        if recursion_depth >= config.LOOKUP_RECURSE_LIMIT:
            # If the recursion limit is reached, return a response indicating the limit is exceeded
            response = {
                'reply': config.LOOKUP_RECURSE_WARNING,
                'tokens': -1,
                'status': 'error',
            }
            return response

        # Prepend the system message to the conversation if it's not already there
        if messages[0]['role'] != 'system':
            # Each system content is preceeded by the default domain focus
            system_content = config.SYSTEM_MSGS[config.domain_common]
            messages.insert(0, {"role": "system", "content": system_content})

        # print("\nWhat were we passed (messages)?")
        # self.custom_pretty_print(messages)

        # construct the chat params
        chatParams = config.OPENAI_PARAMS

        # add the messages to the chat params
        chatParams["messages"] = messages

        # add the functions to the chat params if functions are enabled
        if config.USE_FUNCTIONS:
            chatParams['functions'] = config.OPENAI_FUNCTIONS

        # print("\nWhat are we passing (chatParams)?")
        # self.custom_pretty_print(chatParams)

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
            # Example assistant response:
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
            #             { "message": {
            #                     "role": "assistant",
            #                     "content": null,
            #                     "function_call": {
            #                         "name": "lookup_proper_noun",
            #                         "arguments": "{\"name\":\"Benzy\"}"
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
                messages.append(response['choices'][0]['message'])
                # Extract the function name and arguments
                function_name = response['choices'][0]['message']['function_call']['name']
                function_args = response['choices'][0]['message']['function_call']['arguments']
                # print(f"function_name: {function_name}\nfunction_args: {function_args}")
                # Call the Lookup class with the function name and arguments
                results = self.lookup.lookup(function_name, function_args)
                # print(f"results from lookup: {results}")
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

            # Increment the recursion depth for the recursive call
            recursion_depth += 1

            # Call this method recursively with the new message history and incremented depth
            return self.get_response(messages, recursion_depth)

        except openai.error.OpenAIError as e:
            print(e)
            reply = "I'm sorry, I had an error generating a response. Please try again later."

            response = {
                'reply': reply,
                'tokens': -1,
                'status': 'error',
              }
            return response
