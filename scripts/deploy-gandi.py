"""
deploy-gandi.py - Deploy git repo and build for Gandi web hosting

Author: Wes Modes
Date: 2023
"""

import subprocess
import re
import sys
sys.path.append('..')
import config
import mysecrets

config_filepath = config.__file__

# Set your Gandi user, host, and homedir
user = mysecrets.GANDI_USER
host = mysecrets.GANDI_HOST
homedir = mysecrets.GANDI_HOMEDIR


print("## Reading Release Version")

major_version = config.MAJOR_VERSION
minor_version = config.MINOR_VERSION
patch_version = config.PATCH_VERSION
html_template = config.HTML_TEMPLATE
version_tag = config.VERSION_TAG
version_regex = config.VERSION_REGEX  

# Increment PATCH_VERSION
patch_version += 1

# Create a version_num variable
version = f"{major_version}.{minor_version}.{patch_version}"

print(f"## Updating Release Version (v{version})")

# Nodify config.py by replacing the contents of patch_version
#
# Read the content of config.py
with open(config_filepath, "r") as config_file:
    config_content = config_file.read()

# Modify the content to update PATCH_VERSION
config_content = re.sub(rf'PATCH_VERSION\s*=\s*[0-9.]*', f'PATCH_VERSION = {patch_version}', config_content)

# Write the modified content back to config.py
with open(config_filepath, "w") as config_file:
    config_file.write(config_content)

# Modify HTML_TEMPLATE by replacing the contents of VERSION_TAG
#
replacement_text = version_tag.replace("%%version%%", version)
re_search_pattern = version_regex
# print(f"replacement_text: {replacement_text}")
# print(f"re_search_pattern: {re_search_pattern}")
with open(html_template, 'r') as file:
    entire_file_as_str = file.read()

# Replace the version tag in HTML_TEMPLATE
modified_content, num_replacements = re.subn(re_search_pattern, replacement_text, entire_file_as_str)
# Check if there was a match
if num_replacements > 0:
    entire_file_as_str = modified_content

# Write the modified content back to HTML_TEMPLATE
with open(html_template, 'w') as file:
    file.write(entire_file_as_str)

# Now PATCH_VERSION in config.py has been incremented using sed, and HTML_TEMPLATE has been updated.
# You can use the updated version_num and config.py as needed in your deployment process.

print("## Pushing repo to Gandi")
subprocess.run(["git", "push", "gandi", "master"], check=True)

print("## Cleaning and deploying on Gandi")
subprocess.run(["ssh", f"{user}@{host}", "clean", f"{homedir}/default.git"], check=True)
subprocess.run(["ssh", f"{user}@{host}", "deploy", f"{homedir}/default.git"], check=True)

print("## Copying secrets.py to Gandi")
subprocess.run(["scp", "mysecrets.py", f"{user}@{host}:{homedir}/mysecrets.py"], check=True)
