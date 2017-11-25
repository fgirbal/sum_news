import nltk

w = nltk.word_tokenize("The country has experience in searching for lost subs after the Kursk sank 17 years ago.")
POS_tags = nltk.pos_tag(w)
print POS_tags