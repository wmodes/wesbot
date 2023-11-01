# extract mail from mbox and make json file in py format
py ~/dev/wesbot/scripts/extract-mbox.py /Users/wmodes/Downloads/Takeout\ 2/Mail/training.mbox > email2.py

# convert json in py format to jsonl
py ~/dev/wesbot/scripts/json2sjonl.py email2.py email2.jsonl

# concatenate jsonl records
cat common.jsonl discord.jsonl email.jsonl email2.jsonl > data.jsonl

# split samples into training and test
python  ~/dev/wesbot/scripts/split-samples.py data.jsonl 10
