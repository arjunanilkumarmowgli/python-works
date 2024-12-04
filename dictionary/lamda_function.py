#  addition
add=lambda n1,n2:n1+n2
print(add(10,20))

# substraction
sub=lambda n1,n2:n1-n2
print(sub(10,20))

# finding cube of number
cube=lambda n:n**3
print(cube(10))

#max
max_two =lambda str1,str2:str1 if len(str2)>len(str2) else str2
print(max_two("hai","morning"))


#min
min_two =lambda str1,str2:str1 if len(str1)<len(str2) else str2
print(min_two("hai","morning"))

#smart_sub
smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2>num1
print(smart_sub(143,30))

# length of word
words=["hai","hello","kiihii","apple","test",
       "morning"]
# def get_length(word):
    # return len(word)
#print(max(words,key=get_length))
        # or
get_length=lambda word:len(word)
print(max(words,key=get_length))


text="this is a simple programming question to find word with maximum number of characters"
words=text.split(" ")
# def get_length(w):
#   return len(w)
# print(max(words,key=get_length))

        # or

# lambda method
get_length=lambda word:len(word)
print(max(words,key=get_length))


# print the sentence in size  reverse orderlike  large words to smallest words
text="this is a simple programming question to find word with maximum number of characters"
words=text.split(" ")
def get_legth(w):
    return len(w)
srt_words=sorted(words,key=get_legth,reverse=True)
print(srt_words)


# find repeating word in the sentence
text="this is a simple programming question to  word find word with maximum number of characters"
words=text.split(" ")
def get_count(w):
    return words.count(w)
frequent_word=max(words,key=get_count)
print(frequent_word)

# most recuresive character
text="ABAABBC"
def get_count(char):
    return text.count(char)
most_frequent_character=max(text,key=get_count)
print(most_frequent_character)
# least recuresive character
least_frequent_character=min(text,key=get_count)
print(least_frequent_character)
