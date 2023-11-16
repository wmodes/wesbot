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
sys.path.append('lookup')
import lookup_index
import lookup_contents  

# Create a logger instance for the 'lookup' module
logger = logging.getLogger('lookup_logger')

class Lookup:

    def __init__(self):
        self.index = lookup_index.lookup_index
        self.data = lookup_contents.lookup_contents

    def lookup(self, function, args):
        """
        Look up information given a function and args.

        Args:
          function: The name of the function to call.
          args: A list of arguments to pass to the function.

        Returns:
          The result of the function call.
        """
        print("lookup() what did we get? ", function, args)
        # if the function is lookup_entity
        if function == "lookup_entity":
            # convert args to a dictionary
            args_dict = json.loads(args)
            name = args_dict.get('name').lower()
            # if the entity is in the index
            if name in self.index:
                # get the entity's definitive name from the index
                entity = self.index.get(name)
                # get the entity's data from self.data
                data = self.data.get(entity)
                # return the data
                return f"{config.LOOKUP_WARNING}\n\n{data}"
        return config.LOOKUP_NOTFOUND


        