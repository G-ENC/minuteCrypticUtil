import random 
import numpy as np

# word = 
letters = list("friends")
# word = next((word in word for words if ))
# print(letters)
# word = ""

common_words = open("common_words.txt").read().split()
# print(common_words.read())
word = ''
def constructWord(letters):

    if len(letters) == 0:
        return ""
    else:
        letter = random.choice(letters)
        letters.remove(letter)
        return letter + constructWord(letters)



words = []
for n in range(10000):
    letters = list("friends")
    word = constructWord(letters)
    # word = word[0].upper() + word[1:]
    words.append(word)
    # print(np.array(words))


# answer = next((w for w in common_words if w in set(words)),None)

answer = next((w for w in words if w in set(common_words) and w != "friends" ), None)
print(answer)

# # word = ""
# # letters = list("friends")
# # word = constructWord(word, letters) 


# def constructWord(word, letters):    
#     if len(letters) == 0:
#         print(word)
#         return word
#     else:
#         letter = random.choice(letters)
#         word = word + letter
#         letters.remove(letter)
#         # if len(word) == 7:
#             # print(word)
#         return constructWord(word, letters)