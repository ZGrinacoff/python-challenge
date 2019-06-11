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
#print(sent_count)

# Create a string of letters(upper & lower) to reference when looping through txt.
# This will help to remove characters that aren't actually letters.
# Perform this task before trying to get word count.
# Will later split paragraph into list which will make it more difficult to get total letter count later.
letters = string.ascii_letters + " "
#print(letters)

for l in paragraph:
    if l not in letters:
        paragraph = paragraph.replace(l, '')
#print(paragraph)

cleaned_paragraph = paragraph.split(' ')
#print(cleaned_paragraph)

# Create letter count variable which will be initialized at 0.
# Loop to get count and set to variable.
letter_count = 0
for word in cleaned_paragraph:
    letter_count += len(word)
#print(letter_count)

# Get total word count and set equL to new variable word count.
word_count = len(cleaned_paragraph)
print(word_count)


