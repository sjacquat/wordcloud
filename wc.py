#Author: Scott Foster
#Date: July 29, 2020
#Simple script to read in txt file and produce word cloud myimage
#eliminating punctuations and uninteresting words.

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
# import fileupload
import io
import sys


#function to calculate frequecines of words in given txt file
def calculate_frequencies(file_contents):
    # Uninteresting words and punctuations to ignore
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and",
    "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you",
    "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they",
    "them", "their", "what", "which", "who", "whom", "this", "that", "am",
    "are", "was", "were", "be", "been", "being","have", "has", "had", "do",
    "does", "did", "but", "at", "by", "with", "from", "here", "when", "where",
    "how", "all", "any", "both", "each", "few", "more", "some", "such", "no",
    "nor", "too", "very", "can", "will", "just"]


    newString = file_contents.lower().rstrip()
    words = []
    result = {}

    for word in newString.split():
        if word.isalpha() and word not in uninteresting_words:
            words.append(word)
    for word in words:
        if word not in result:
            result[word] = 1
        result[word] += 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()

# enter name of file to be read ("xyz.txt")
fname = input("Enter file name: ")
#create file handler
fh = open(fname)
fileString = fh.read()

calculate_frequencies(fileString)
# Display your wordcloud image

myimage = calculate_frequencies(fileString)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
