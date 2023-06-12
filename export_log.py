import argparse

from pydriller import Repository
import pandas as pd
import pm4py

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-r', '--repo', help='Address/path of the repo (local or remote).', default='\\')
parser.add_argument('-o', '--output_name', help='Name of the export file(s).', default='"log____"')
parser.add_argument('-x', '--xes', help='Creates an XES export file.', action='store_true')
parser.add_argument('-c', '--conventional-commits', dest='conventional_commits', help='Indicates that the repository follows the Conventional Commits initiative.', action='store_true')
args = parser.parse_args()

timestamps = []
hashes = []
activities = []
messages = []
authors_names = []
authors_emails = []
merge_yns = []

for commit in Repository(args.repo).traverse_commits():
    timestamps.append(commit.author_date.isoformat())
    hashes.append(commit.hash)
    if args.conventional_commits:
        activities.append(commit.msg.split(' ')[0].split('(')[0].replace(':', '').lower())
    messages.append(commit.msg)
    authors_names.append(commit.author.name)
    authors_emails.append(commit.author.email)
    merge_yns.append(commit.merge)

if args.conventional_commits:
    df = pd.DataFrame({'author_timestamp': timestamps, 'hash': hashes, 'activity': activities, 'commit_message': messages, 'author_name': authors_names, 'author_email': authors_emails, 'merge': merge_yns})
else:
    df = pd.DataFrame({'author_timestamp': timestamps, 'hash': hashes, 'activity': messages, 'author_name': authors_names, 'author_email': authors_emails, 'merge': merge_yns})
df.to_csv(args.output_name + '.csv')

if args.xes:
    dataframe = pm4py.format_dataframe(df, case_id='author_name', activity_key='activity', timestamp_key='author_timestamp')
    event_log = pm4py.convert_to_event_log(dataframe)

    pm4py.write_xes(event_log, args.output_name + '.xes')
