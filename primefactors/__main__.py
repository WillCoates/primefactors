import argparse
from . import factorize
from .formatters import formats

parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='integers to be factorized')
parser.add_argument('-f', '--format', default='repr', choices=formats.keys(), help='how to format output')
args = parser.parse_args()

formatter = formats[args.format]

for val in args.integers:
    print(formatter(factorize(val)))
