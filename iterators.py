# %%
import numpy as np


def fasta_gen(path):
    with open(path) as fasta:

        name = ''
        sequence = ''
        for line in fasta:
            if line[0] == '>':
                if sequence != '':
                    yield name, sequence
                    sequence = ''

                name = line[1:-1]
            else:
                sequence += line[:-1]
        yield name, sequence


for name, seq in fasta_gen('sequences-2.fasta'):
    print(name, seq[:10])


# %%


class RandomSeq:
    def __init__(self, path,
                 probs={'replace': 0.1,
                        'delition': 0.1,
                        'insertion': 0.1,
                        'gap': 0.1}):
        self.path = path
        self.probs = probs.copy()

    def modify(self, sequence):
        new_seq = ''
        for letter in sequence:
            if np.random.binomial(1, self.probs['replace']):
                new_seq += np.random.choice(['A', 'C', 'G', 'T'])
                continue

            if np.random.binomial(1, self.probs['delition']):
                continue

            if np.random.binomial(1, self.probs['insertion']):
                new_seq += np.random.choice(['A', 'C', 'G', 'T'])
                new_seq += letter
                continue

            if np.random.binomial(1, self.probs['gap']):
                new_seq += '-'
                continue

            new_seq += letter

        return new_seq

    def __iter__(self):
        while True:
            for id, line in fasta_gen(self.path):
                yield self.modify(line)


my_seq_gen = RandomSeq('sequences-2.fasta')
for i, line in enumerate(my_seq_gen):
    print(line[10:])

    if i > 1000:
        break

# %%


def iter_append(iterable, item):
    return iter((*iterable, item))


for i in iter_append([1, 2, 3], 'ABACABA'):
    print(i)


# %%

def nested_list_unpacker(x):
    answer = []

    try:
        for item in x:
            answer += nested_list_unpacker(item)

        return answer

    except TypeError:
        return [x]


nested_list_unpacker([1, [2], [[3]], [], [4, 5, [6]], [7, [8, [9]]]])
