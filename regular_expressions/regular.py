# %%
import re
import matplotlib.pyplot as plt

# %%
with open('references.txt', 'r') as read, open('ftps.txt', 'w') as write:
    for line in read:
        m = re.findall('[\\.a-zA-Z0-9]+/[\\./a-zA-Z0-9_#]+', line)
        if len(m) == 0:
            continue

        for href in m:
            write.write(href + '\n')

# %%
with open('2430AD.txt', 'r') as read, open('numbers.txt', 'w') as write:
    for line in read:
        m = re.findall('([0-9]+)', line)
        if len(m) == 0:
            continue

        for num in m:
            write.write(num + '\n')

# %%
with open('2430AD.txt', 'r') as read, open('Awords.txt', 'w') as write:
    for line in read:
        m = re.findall('([a-zA-Z]*[a|A]+[a-zA-Z]*)', line)
        if len(m) == 0:
            continue

        for num in m:
            write.write(num + '\n')

# %%
with open('2430AD.txt', 'r') as read,\
     open('sentence_emotional.txt', 'w') as write:
    for line in read:
        m = re.findall('[.|!|?]*([a-zA-Z0-9]+!)', line)
        if len(m) == 0:
            continue

        for num in m:
            write.write(num + '\n')

# %%
with open('2430AD.txt', 'r') as read:
    all_words = set()
    for line in read:

        words = re.findall('[a-zA-Z]+', line)
        
        if len(words) == 0:
            continue

        for word in words:
            all_words.add(word.lower())

lengths = [len(word) for word in all_words]
fig, ax = plt.subplots()
fig.patch.set_alpha(1)
plt.title('word length distribution')
plt.hist(lengths)
plt.savefig('lengths_distribution.png')
