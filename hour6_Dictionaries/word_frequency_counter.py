"""
Hour 1 – Word Frequency Counter

Counts occurrence of each word in a given sentence.
"""

sentence = "ghost stays frosty ghost never quits"
freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1
print("Word Frequencies:", freq)
