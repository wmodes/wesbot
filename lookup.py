"""
lookup.py - A Python module for a Lookup class handling information retrieval.

This module defines a Lookup class that constructs a lookup data structure and provides functions for retrieving information about entities.

Features:
- Initializes with a dictionary containing lookup data.
- Offers a method to look up information given a function and args.
- Returns information or an error message if the entity is not found.

Author: Wes Modes
Date: 2023
"""

import logging
import config
import sys
import json
from helpers import super_strip
sys.path.append('lookup')
import lookup_index
import lookup_contents  

# Create a logger instance for the 'lookup' module
logger = logging.getLogger('lookup_logger')

class Lookup:

    def __init__(self):
        self.index = lookup_index.lookup_index
        self.data = lookup_contents.lookup_contents

    def lookup(self, function_name, args):
        """
        Look up information given a function and args.

        Args:
          function: The name of the function to call.
          args: A list of arguments to pass to the function.

        Returns:
          The result of the function call.
        """
        # print("lookup() what did we get? ", function_name, args)
        # if the function is lookup_person
        # fix the model's tendency to put a period rather than an underscore
        function_name = function_name.replace(".", "_")
        # convert args to a dictionary
        args_dict = json.loads(args)
        name = args_dict.get('name').lower()
        # if function == "lookup_person":
        if function_name:
            # if the entity is in the index
            if name in self.index:
                # get the entity's definitive name from the index
                entity = self.index.get(name)
                # get the entity's data from self.data
                data = super_strip(self.data.get(entity))
                # construct the lookup result
                lookup_result = {
                    "name": entity,
                    "note_to_model": config.LOOKUP_CAVEAT[function_name],
                    "data": data,
                    "status": "success",
                }
                # return the lookup result
                return lookup_result
        lookup_result = {
            "name": name,
            "note_to_model": config.LOOKUP_NOTFOUND,
            "status": "error",
        }
        return lookup_result


        