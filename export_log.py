#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import argparse
from pydriller import Repository
import pandas as pd
import pm4py

parser = argparse.ArgumentParser()
parser.add_argument('--repo', dest='repo', type=str, help='Add the address of the repo (local or remote).')
parser.add_argument('--export_name', dest='export_name', type=str, help='Add the name of the export files.')
args = parser.parse_args()

if args.export_name:
    repo = args.export_name
else:
    repo = ''

if args.export_name:
    export_name = args.export_name
else:
    export_name = 'log'

timestamps = []
hashes = []
messages = []
authors_names = []
authors_emails = []
modified_files = []
merge_yns = []

for commit in Repository(repo).traverse_commits():
    timestamps.append(commit.author_date.isoformat())
    hashes.append(commit.hash)
    messages.append(commit.msg)
    authors_names.append(commit.author.name)
    authors_emails.append(commit.author.email)
    modified_files.append(';'.join([file.filename for file in commit.modified_files]))
    merge_yns.append(commit.merge)

df = pd.DataFrame({'author_timestamp': timestamps, 'hash': hashes, 'commit_message': messages, 'author_name': authors_names, 'author_email': authors_emails, 'modified_files': modified_files, 'merge': merge_yns})
# df.to_csv(export_name + '.csv', sep='§')

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar='§')
    writer.writerows(table)


dataframe = pm4py.format_dataframe(df, case_id='author_name', activity_key='commit_message', timestamp_key='author_timestamp')
event_log = pm4py.convert_to_event_log(dataframe)

pm4py.write_xes(event_log, export_name + '.xes')
