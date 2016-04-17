import argparse
from get_earlist.get_earlist import GetEarlist

parser = argparse.ArgumentParser()
parser.add_argument("--file", dest="filename", help="path to input file", metavar="FILE")

args = parser.parse_args()

processing = GetEarlist()

with open(args.filename, 'r') as reader:
    for line in reader:
        input_string = line.strip()
        output = processing.process_string(input_string)
        print input_string + ' => ' + output
