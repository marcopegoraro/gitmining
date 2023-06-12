# GitMining: extracting event logs from Git repositories #

## Description ##

The script allows for flexible analysis of commits from Git repositories. The commits are exported in the form of an event log, and can be analyzed with process mining techniques.
The script extracts relevant information from each commit, such as the author's timestamp, commit hash, commit activity, commit message, author's name, author's email, and merge status.

The log is extracted from a Git repository as a CSV file (optionally, it can also be converted to the XES format). This version extracts the following attributes:

| Attribute | Type | Description |
| -------- | -------- | -------- |
| `author_timestamp`   | ISO timestamp   | Date and time of the commit.   |
| `hash`   | string   | Hash of the commit; event identifier.   |
| `activity`  | string   | Label of the commit; based on Conventional Commits. Optional.   |
| `commit_message`   | textual   | Textual description of the changes in the commit.   |
| `author_name`   | string   | Name of the contributor.   |
| `author_email`   | string   | E-mail of the contributor.   |
| `merge`   | boolean   | A boolean flag indicating whether the commit is a merge or not.   |

## Requirements ##

The script utilizes Python 3.9+ with the [`pydriller`](https://pydriller.readthedocs.io/en/latest/), [`pandas`](https://pandas.pydata.org/), and [`pm4py`](https://pm4py.fit.fraunhofer.de/) libraries. They can be installed in most Python environments with `pip`:

`pip install pydriller pandas pm4py`

Be sure to also install the requirements of these three libraries (some are external to Python; consult the respective websites).

## Usage ##

This script allows you to analyze a Git repository and export commit information to a CSV file as an event log. The script supports command-line arguments for customization.

### Executing the script ###

To execute the script, open a terminal an simply input

`python export_log.py`

You will then need to provide the parameters, described in the next section.

### Command-line Arguments ###

The script accepts the following command-line arguments:

- `-r` or `--repo`: Specifies the address or path of the Git repository. It can be a local or remote repository. The default value is the empty string: the script will extract a log from a Git repository cloned in the same folder, if any.
- `-o` or `--output-name`: Sets the name of the export file(s). The default value is "log", which generates a file called `log.csv`.
- `-x` or `--xes`: Enables the creation of an XES export file, in addition to the CSV file. The XES file will have the same name of the CSV file.
- `-c` or `--conventional-commits`: Indicates that the repository follows the Conventional Commits initiative. This flag enables specific processing of commit messages.

These parameters, their meaning, and the default values can also be visualized with the help command:

`python export_log.py --help`

or

`python export_log.py -h`
