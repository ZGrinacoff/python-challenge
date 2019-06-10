import os
# Import string module instead of regex. Not familiar enough with regex yet to complete.
import string

# Create file path.
paragraph_txt = os.path.join('paragraph_1.txt')

# Create empty string to hold .txt file and begin analysis.
paragraph = ''

# Read in .txt file and store contents in paragraph string.
with open (paragraph_txt, 'r') as txtfile:
    paragraph = txtfile.read()
    #print(paragraph)

# Sentence count can be determined by locating punctuation: . or ! or ?
# Add up all such cases to be equal to total sentence count.
sent_count = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
print(sent_count)