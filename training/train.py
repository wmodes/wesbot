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
parser.add_argument("--state", type=str, metavar="FTJOBID", nargs='?', const="fetch", help="Retrieve the state of a fine-tuning job")
parser.add_argument("--cancel", type=str, metavar="FTJOBID", nargs='?', const="fetch", help="Cancel a fine-tuning job")
parser.add_argument("--events", type=str, metavar="FTJOBID", nargs='?', const="fetch", help="List events from a fine-tuning job")
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

# continously monitor events
def monitor_events(ft_id):
    print("# MONITORING TRAINING PROGRESS")
    last_message = ""
    escape_monitor = False
    waiting_indicator("reset")
    while not escape_monitor:
        ft_events_results = openai.FineTuningJob.list_events(id=ft_id, limit=1)
        ft_message = ft_events_results.data[0].message
        if ft_message != last_message:            # Clear the entire line
            sys.stdout.write("\033[K")
            sys.stdout.flush()
            display_event_on_same_line(ft_message)
            last_message = ft_message
        # check if "completed" in message
        if "completed" in ft_message:
            escape_monitor = True
        wait_a_bit(event_check_interval, waiting_indicator_interval)

def get_state(ft_id):
    print("# FINE-TUNING JOB DETAILS")
    state_results = openai.FineTuningJob.retrieve(ft_id)
    print(str(state_results) + "\n")

def get_list(n):
    results = openai.FineTuningJob.list(limit=n)
    return(results) 

def fetch_ft_id():
    ft_list = get_list(5)  # You can change the limit as needed
    active_jobs = [job for job in ft_list.data if job["status"] == "running"]
    if active_jobs:
        # Sort the active jobs by their creation time in descending order
        sorted_jobs = sorted(active_jobs, key=lambda job: job["created_at"], reverse=True)
        return sorted_jobs[0]["id"]
    return None

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
    ft_init_results = openai.FineTuningJob.create(training_file=upload_results.id, model=config.OPENAI_BASE_MODEL,hyperparameters=config.HYPERPARAMETERS)
    print("fine-tuning init: " + str(ft_init_results) + "\n")
    ft_id = ft_init_results.id
    print("\nUse the following command to check the status of your fine-tuning job:")
    print(f"python train.py --state {ft_id}")
    print("or")
    print(f"python train.py --events {ft_id} --monitor")
    if (monitor):
        monitor_events(ft_id)
        get_state(ft_id)

if args.list:
    num = 20
    print("fine-tuning list: " + str(get_list(num)) + "\n")

if args.state:
    if args.state == "fetch":
        args.state = fetch_ft_id()
        if not args.state:
            print("No running fine-tuning jobs found.")
            exit(1)
    results = get_state(args.state)
    print("fine-tuning state: " + str(results) + "\n")
    
if args.cancel:
    if args.cancel == "fetch":
        args.cancel = fetch_ft_id()
        if not args.cancel:
            print("No running fine-tuning jobs found.")
            exit(1)
    results = openai.FineTuningJob.cancel(args.cancel)
    print("fine-tuning cancel: " + str(results) + "\n")

if args.events:
    if args.events == "fetch":
        args.events = fetch_ft_id()
        if not args.events:  # Typo: Change "argsevents" to "args.events"
            print("No running fine-tuning jobs found.")
            exit(1)
    if not monitor:
        results = openai.FineTuningJob.list_events(id=args.events, limit=1)
        print("fine-tuning events: " + str(results) + "\n")
    else:
        monitor_events(args.events)
        get_state(args.events)

if args.delete:
    arg_str = f"ft:{config.OPENAI_PARAMS['model']}:{config.OPENAI_ORG}"
    results = openai.Model.delete(args.delete)