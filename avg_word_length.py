# Algorithm 1 by Linda Liu

# Given a sentence, determine the average length of a word and return it as a number with integer precision.
# Round the answer up or down to the nearest whole number using system functions or your own code.

# Step 1: defining the sentence
sentence = ('The quick brown fox jumps over the lazy dog.')

# Step 2: change the sentence from a string into a list
sentence_list = list(sentence.split(" "))

# Checking the list, and removing the period from the last word in the list.
index = len(sentence_list) - 1
sentence_list[index] = "dog"
print(sentence_list)

# Step 3: counting the length of each word in sentence and totaling them up
total_length = 0
for word in sentence_list:
    total_length += len(word)

# Step 4: printing the average value
total_words = len(sentence_list)
avg_length = total_length / total_words
print("The average length of the words in the sentence is", (round(avg_length)))



