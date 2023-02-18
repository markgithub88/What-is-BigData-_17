import nltk
from nltk import word_tokenize
text = word_tokenize("I enjoy biking on the trails")
output = nltk.pos_tag(text)
print(output)

text = word_tokenize("I like sunny days")
output = nltk.pos_tag(text)
print(output)









