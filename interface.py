import argparse
from os import mkdir, listdir
from os.path import dirname, abspath
from pathlib import Path
from re import search
from process_file import process_file

parser = argparse.ArgumentParser()
parser.add_argument('template', help='the template to search in the audio')
parser.add_argument('sample', help='audio .wav to search for the template')
args = parser.parse_args()

# create the report directory
# report directories are are created in the directory containing this module
# the report directories are named sequentially report_x
report_number = -1
for path in listdir(dirname(abspath(__file__))):
    is_report = search('report_(\d*)', path)
    if is_report:
        report_number = max(report_number, int(is_report.group(1)))
out_path = Path(dirname(abspath(__file__)), f'report_{report_number+1}')
mkdir(out_path)

# process the specified file
if args.sample:
    process_file(args.sample, args.template, out_path)

# record and process sound