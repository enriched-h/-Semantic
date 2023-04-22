# -Semantic

This Python code demonstrates how to use spaCy, an open-source software library for advanced natural language processing, to calculate similarities between words, tokens and sentences.

To run the code, you need to have spaCy installed on your machine. The code starts by loading the 'en_core_web_md' model using the spacy.load() method. Then, it creates three word objects for the words 'cat', 'monkey', and 'banana'.

The code then calculates the similarity scores between these words using the word.similarity() method. It prints out the similarity scores between 'cat' and 'monkey', 'banana' and 'monkey', and 'banana' and 'cat'.

The code then creates a list of tokens for the words 'cat', 'apple', 'monkey', and 'banana' using the nlp() method. It then loops through each token and calculates the similarity score between each pair of tokens using token.similarity(). The results are printed to the console.

Finally, the code compares a given sentence "Why is my cat on the car" with a list of sentences using the sentence.similarity() method. The similarity score between the model sentence and each of the sentences in the list is printed to the console.

This code can be used as a starting point for more complex natural language processing tasks, such as text classification or sentiment analysis.
