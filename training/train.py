"""
train.py - Fine-tune a trained model

This file contains the code for fine-tuning a trained model. It is based on the code from the OpenAI API documentation: https://platform.openai.com/docs/guides/fine-tuning/create-a-fine-tuned-model

Author: Wes Modes
Date: 2023
"""

import openai
import argparse
import sys
sys.path.append('..')
import config
import mysecrets
import time

# Set your OpenAI API key and organization (if applicable)
openai.api_key = mysecrets.OPENAI_API_KEY
openai.organization = config.OPENAI_ORG

# Globals
monitor = False
event_check_interval = 3
waiting_indicator_interval = 0.25

# Initialize argparse for command-line options
parser = argparse.ArgumentParser(description="OpenAI Fine-Tuning Script")

# Add command-line options
parser.add_argument("--train", type=str, metavar="FILENAME", help="Start fine-tuning with the specified training file")
parser.add_argument("--list", action="store_true", help="List fine-tuning jobs")
parser.add_argument("--state", type=str, metavar="FTJOBID", help="Retrieve the state of a fine-tuning job")
parser.add_argument("--cancel", type=str, metavar="FTJOBID", help="Cancel a fine-tuning job")
parser.add_argument("--events", type=str, metavar="FTJOBID", help="List events from a fine-tuning job")
parser.add_argument("--delete", type=str, metavar="MODEL", help="Delete a fine-tuned model")
parser.add_argument("--monitor", action="store_true", help="Keep monitoring results")

args = parser.parse_args()

# indicate waiting for response
wait_state_indicator = -1
def waiting_indicator(state=None):
    global wait_state_indicator
    if state:
        wait_state_indicator = -1
        return
    wait_state_characters = ['|', '/', '-', '\\']
    if wait_state_indicator == -1:
        backspace_maybe = ''
    else:
        backspace_maybe = '\b'  # Erase the previous character
    wait_state_indicator = (wait_state_indicator + 1) % len(wait_state_characters)
    print(backspace_maybe + wait_state_characters[wait_state_indicator], end="")
    sys.stdout.flush()

# wait a bit
def wait_a_bit(seconds, indicator_interval):
    if indicator_interval > seconds:
        waiting_indicator()
        time.sleep(seconds)
    else:
        num_iterations = int(seconds / indicator_interval)
        for _ in range(num_iterations):
            waiting_indicator()
            time.sleep(indicator_interval)

def display_event_on_same_line(msg):
    # Clear the entire line
    sys.stdout.write("\033[K")
    sys.stdout.flush()
    print('\r' + msg + "    ", end="")

# continuously monitor events
def monitor_events(ft_id):
    last_message = ""
    escape_monitor = False
    waiting_indicator("reset")
    while not escape_monitor:
        ft_events_results = openai.FineTuningJob.list_events(id=ft_id, limit=1)
        ft_message = ft_events_results.data[0].message
        if ft_message != last_message:
            display_event_on_same_line(ft_message)
            last_message = ft_message
        # check if "completed" in message
        if "completed" in ft_message:
            escape_monitor = True
        wait_a_bit(event_check_interval, waiting_indicator_interval)

# If no arguments are provided, display the help message
if not any(vars(args).values()):
    parser.print_help()

if args.monitor:
    monitor = True

if args.train:
    print("# UPLOADING JSONL TRAINING FILE")
    upload_results = openai.File.create(
        file=open(args.train, "rb"),
        purpose='fine-tune'
    )
    print("upload results: " + str(upload_results) + "\n")
    print("# STARTING FINE-TUNING JOB")
    ft_init_results = openai.FineTuningJob.create(training_file=upload_results.id, model=config.BASE_MODEL)
    print("fine-tuning init: " + str(ft_init_results) + "\n")
    ft_id = ft_init_results.id
    print("\nUse the following command to check the status of your fine-tuning job:")
    print(f"python train.py --state {ft_id}")
    print("or")
    print(f"python train.py --events {ft_id} --monitor")
    if (monitor):
        monitor_events(ft_id)

def test_cycle():
    for i in range(1,10):
        ft_message = "Sheep number " + str(i)
        print('\r' + ft_message + "    ", end="")
        waiting_indicator()
        waiting_indicator()
        waiting_indicator()
        sys.stdout.flush()
        time.sleep(1)

if args.list:
    results = openai.FineTuningJob.list(limit=10)
    print("fine-tuning list: " + str(results) + "\n")

if args.state:
    results = openai.FineTuningJob.retrieve(args.state)
    print("fine-tuning state: " + str(results) + "\n")

if args.cancel:
    results = openai.FineTuningJob.cancel(args.cancel)
    print("fine-tuning cancel: " + str(results) + "\n") 

if args.events:
    if (not monitor):
        results = openai.FineTuningJob.list_events(id=args.events, limit=1)
        print("fine-tuning events: " + str(results) + "\n") 
    else:
        monitor_events(args.events)

if args.delete:
    arg_str = f"ft:{config.MODEL}:{config.OPENAI_ORG}"
    results = openai.Model.delete(args.delete)
