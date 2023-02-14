import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#Monkey and cat oare both animals, so they have the highest semantic similarity.
#Monkey and banana obviously are related words, so they have the quite high semantic similarity.
#cat and banana obviously are reletivly unrelated words, so they have the lowest semantic similarity.
# I'm perhaps a little suprised that the difference between monkey and cat is nearly 0.2 compared to monkey and banana. I thought the latter would have closer similarity.

word4 = nlp("foot")
word5 = nlp("ball")
word6 = nlp("egg")

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

#There was some semantic similarity between ball and foot (football)
#suprisingly little between ball and egg (approx 0.19). I'm thinking of a rugby ball, so perhaps that's why i find it suprising!
#less suprisingly little similarity between foot and egg

#When running the simpler model on the example file, there was an error message
#which stated that the smaller models has no word vectors.
#it suggest that you can make your own vectors or use a larger model like en_core_web_md
#As such this model gave much lower semantic similarities than the previos model.