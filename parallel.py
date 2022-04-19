#!/usr/bin/env python3

# %%
import argparse
import sys
from concurrent.futures import ProcessPoolExecutor
from Bio import SeqIO
import gzip
from threading import Lock
from collections import defaultdict


# %%

s_print_lock = Lock()


def s_print(*a, **b):
    with s_print_lock:
        print(*a, **b)


def eval_seq(record):
    stats = defaultdict(int)

    for letter in record.seq:
        stats[letter] += 1

    answer = ''
    answer += f'Contig {record.id}:\t'

    for letter in stats:
        answer += f'{letter}={stats[letter]}, '

    answer = answer[:-2]

    s_print(answer)


def create_fasta_iter(fasta_file):
    with gzip.open(fasta_file, 'rt') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            yield record


# %%

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-f', '--fasta', type=str, help='fasta file')
    parser.add_argument('-t', '--thread', default=1,
                        type=int, help='Number of threads')

    args = vars(parser.parse_args())

    fasta_file = args['fasta']
    n_threads = args['thread']

    with ProcessPoolExecutor(n_threads) as pool:
        results = pool.map(eval_seq, create_fasta_iter(fasta_file))
