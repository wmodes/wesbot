import json
import random
import sys
import os

def split_jsonl(input_filename, test_percentage):
    # Expand the tilde in the input_filename to the user's home directory
    input_filename = os.path.expanduser(input_filename)

    # Determine the output filenames
    input_basename = os.path.basename(input_filename)
    training_filename = input_basename.replace('.jsonl', '-training.jsonl')
    test_filename = input_basename.replace('.jsonl', '-test.jsonl')

    # Get the directory of the input file
    input_dir = os.path.dirname(input_filename)

    # Construct the full paths for training and test data files
    training_filepath = os.path.join(input_dir, training_filename)
    test_filepath = os.path.join(input_dir, test_filename)

    # Initialize lists to store the training and test data
    training_data = []
    test_data = []

    with open(input_filename, 'r') as input_file:
        for line in input_file:
            # Load each line as a JSON object
            data = json.loads(line)

            # Determine whether this line goes to training or test
            if random.random() < test_percentage / 100:
                test_data.append(data)
            else:
                training_data.append(data)

    # Write the training data to the training file
    with open(training_filepath, 'w') as training_file:
        for item in training_data:
            training_file.write(json.dumps(item, ensure_ascii=False) + '\n')

    # Write the test data to the test file
    with open(test_filepath, 'w') as test_file:
        for item in test_data:
            test_file.write(json.dumps(item, ensure_ascii=False) + '\n')

    print(f"Data split into training and test sets. Training data saved to {training_filepath}. Test data saved to {test_filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_jsonl.py input_filename test_percentage")
        sys.exit(1)

    input_filename = sys.argv[1]
    test_percentage = float(sys.argv[2])

    split_jsonl(input_filename, test_percentage)
