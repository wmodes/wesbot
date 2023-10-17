import openai
import os
import logging
import json
import config

class Chatbot:

    def __init__(self):
        # Set your OpenAI API key and organization (if applicable)
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.organization = "org-6Sx3QSqdmkskgXbQf8AsccbW"
        openai.Model.list()

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
                model="gpt-3.5-turbo",
                messages=messages,
            )

            # Pretty-print the JSON object
            formatted_response = json.dumps(response, indent=4)
            # Print the formatted JSON
            # print("response:", formatted_response)

            # Extract and return the generated response
            reply = response['choices'][0]['message']['content']
            # print("Reply:", reply)
            return reply

        except openai.error.OpenAIError as e:
            print(e)
            return "I'm sorry, I had an error generating a response."
