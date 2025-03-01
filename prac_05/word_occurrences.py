#estimated time:15 mins

word_to_count = {} #create a dict to store words and count
text = input('Text: ') #ask input

#split the text into words
words = text.split()

# using LBYL pattern to count
for word in words:
    word_to_count[word] = word_to_count.get(word,0) + 1

#sort dict by alphabetical order
sorted_word_count = sorted(word_to_count.items())

#find the longest word
max_length = max((len(word) for word in words))

#print in the required formating
for word, count in sorted_word_count:
    print(f"{word:{max_length}} : {count}")



