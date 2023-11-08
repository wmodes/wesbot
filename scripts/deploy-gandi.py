"""
deploy-gandi.py - Deploy git repo and build for Gandi web hosting

Author: Wes Modes
Date: 2023
"""

import subprocess
import re
import sys
import argparse  # Import the argparse module

sys.path.append('..')
import config
import mysecrets

config_filepath = config.__file__

# Set your Gandi user, host, and homedir
user = mysecrets.GANDI_USER
host = mysecrets.GANDI_HOST
homedir = mysecrets.GANDI_HOMEDIR

# Create a command line argument parser
parser = argparse.ArgumentParser(description="Deploy git repo and build for Gandi web hosting")
parser.add_argument("--clean", action="store_true", help="Activate cleaning at Gandi")

args = parser.parse_args()

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

# Modify config.py by replacing the contents of patch_version
with open(config_filepath, "r") as config_file:
    config_content = config_file.read()

config_content = re.sub(rf'PATCH_VERSION\s*=\s*[0-9.]*', f'PATCH_VERSION = {patch_version}', config_content)

with open(config_filepath, "w") as config_file:
    config_file.write(config_content)

# Modify HTML_TEMPLATE by replacing the contents of VERSION_TAG
replacement_text = version_tag.replace("%%version%%", version)
re_search_pattern = version_regex

with open(html_template, 'r') as file:
    entire_file_as_str = file.read()

modified_content, num_replacements = re.subn(re_search_pattern, replacement_text, entire_file_as_str)
if num_replacements > 0:
    entire_file_as_str = modified_content

with open(html_template, 'w') as file:
    file.write(entire_file_as_str)

print("## Pushing repo to Gandi")
subprocess.run(["git", "push", "gandi", "master"], check=True)

if args.clean:  # Check if the --clean option is activated
    print("## Cleaning Environment at Gandi")
    subprocess.run(["ssh", f"{user}@{host}", "clean", "default.git"], check=True)

print("## Deploying on Gandi")
subprocess.run(["ssh", f"{user}@{host}", "deploy", "default.git"], check=True)

print("## Copying secrets.py to Gandi")
subprocess.run(["scp", config.MYSECRETS, f"{user}@{host}:{homedir}/mysecrets.py"], check=True)
