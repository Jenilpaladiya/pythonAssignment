#Import necessary libraries
import re
from collections import Counter

#Open the text file and read its contents into a list of words
with open('keywords.txt', 'r') as f:
    words = f.read().split()

#Use a regular expression to remove any non-alphabetic characters from the words
words = [re.sub(r'[^a-zA-Z]', '', word) for word in words]

#Initialize empty dictionaries for storing the unigrams, bigrams, and trigrams
unigrams = {}
bigrams = {}
trigrams = {}

#Iterate through the list of words and count the number of occurrences of each unigram, bigram, and trigram
for i in range(len(words)):
    # Unigrams
    if words[i] in unigrams:
        unigrams[words[i]] += 1
    else:
        unigrams[words[i]] = 1
        
    # Bigrams
    if i < len(words)-1:
        bigram = words[i] + ' ' + words[i+1]
        if bigram in bigrams:
            bigrams[bigram] += 1
        else:
            bigrams[bigram] = 1
        
    # Trigrams
    if i < len(words)-2:
        trigram = words[i] + ' ' + words[i+1] + ' ' + words[i+2]
        if trigram in trigrams:
            trigrams[trigram] += 1
        else:
            trigrams[trigram] = 1

# Sort the dictionaries by the number of occurrences
sorted_unigrams = sorted(unigrams.items(), key=lambda x: x[1], reverse=True)
sorted_bigrams = sorted(bigrams.items(), key=lambda x: x[1], reverse=True)
sorted_trigrams = sorted(trigrams.items(), key=lambda x: x[1], reverse=True)

# Write the results to a text file
with open('results.txt', 'w') as f:
    f.write("Most common unigrams:\n")
    for unigram, count in sorted_unigrams[:10]:
        f.write(unigram + ": " + str(count) + "\n")
    f.write("\nMost common bigrams:\n")
    for bigram, count in sorted_bigrams[:10]:
        f.write(bigram + ": " + str(count) + "\n")
    f.write("\nMost common trigrams:\n")
    for trigram, count in sorted_trigrams[:10]:
        f.write(trigram + ": " + str(count) + "\n")