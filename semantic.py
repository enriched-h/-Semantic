import spacy #This statement should work if you have spaCy installed 

nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana ')


word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Similarities between cat, monkey and banana and think of an example of your own:
# What I find interesting the most is that there is greater similarity between banana monkey than there is between banana cat,
# that makes sense since it is not be a popular fact bananas are a cat's favourite fruit 
# My similarity example radio stethoscope


# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model
# 'en_core_web_md'.
# The second output is similar to the first one in structure, but the scores indicate different levels of similarity between the items being 
# compared. The scores in the first output are generally higher than those in the second output, which implies that the items in the first 
# output are more similar to each other
