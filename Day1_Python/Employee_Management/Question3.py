sentence = input("Enter a sentence: ")

words = sentence.split()

words_upper = tuple(word.upper() for word in words )

#Save both to file
with open('sentence_data.txt', 'w') as f:
    f.write("List "+str(words) +"\n")
    f.write("Tuple in UpperCase: "+str(words_upper) +"\n") 

with open('sentence_data.txt','r') as f:
    print(f.read)
