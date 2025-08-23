import math
import numpy as np
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]
    docs = [line.lower().split() for line in text.split('\n')]
    N = len(docs)
    # 2. go over each unique word and calculate its term frequency, and its document frequency
    all_words = []
    for doc in docs:
        all_words += doc
    vocabulary = list(set(all_words))

    tf = {}
    df = {}
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        df[word] = sum([word in doc for doc in docs])/N

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    tfidf_matrix = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            x = 1 / df[word]
            tfidf.append(tf[word][doc_index] * math.log(x, 10)) 
        tfidf_matrix.append(tfidf)
    print("TF-IDF: ", tfidf_matrix)
    print("========================================================")

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    def find_nearest_pair(data):
        N = len(data)
        dist = np.empty((N, N), dtype=float)
        for i, sent1 in enumerate(data):
            for j, sent2 in enumerate(data):
                if i == j:
                    dist[i,j] = np.inf
                else:
                    dist[i,j] = distance(sent1, sent2)
        print(np.unravel_index(np.argmin(dist), dist.shape))
        print("dist: ", dist)
   
    def distance(row1, row2):
        sum = 0
        for i in range(len(row1)):
            sum = sum + abs(row1[i] - row2[i])
        return sum

    find_nearest_pair(tfidf_matrix)

main(text)
