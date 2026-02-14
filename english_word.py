import random
from random import randint, randrange

open_file = open("English_word.txt")
data = open_file.read()
open_file.close()
words_data = data.splitlines()
#print(words_data)

English_dict = {}
id = 1
for line in words_data:
    English, Japanese = line.split(",")
    English_dict[id] = English, Japanese
    id = id + 1
#print(English_dict)

dict_len = len(English_dict)

while True:
    num = randint(1,dict_len)
    English, Japanese = English_dict[num]
    print("\n"+English+"\n")
    dummy = input()
    if dummy == "":
        print(Japanese)
    elif dummy == "end":
        break
    else:
        break

    print("\n""--- Next --- "+"\n")
    dummy = input()
    if dummy == "":
        print("")
    elif dummy == "end":
        break
    else:
        break

    #日本語から英語
    num = randint(1,dict_len)
    English, Japanese = English_dict[num]
    print("\n"+Japanese+"\n")
    dummy = input()
    if dummy == "":
        print(English)
    elif dummy == "end":
        break
    else:
        break

    print("\n""--- Next ---- "+"\n")
    dummy = input()
    if dummy == "":
        print("")
    elif dummy == "end":
        break
    else:
        break