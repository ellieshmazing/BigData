'''Modified from https://github.com/kavgan/nlp-in-practice/blob/master/tf-idf/Keyword%20Extraction%20with%20TF-IDF%20and%20SKlearn.ipynb'''
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        fname = feature_names[idx]
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results

# put the common code into several methods
def get_keywords(idx):

    #generate tf-idf for the given document
    tf_idf_vector=tfidf.transform(cv.transform([content[idx]]))

    #sort the tf-idf vectors by descending order of scores
    sortedItems=sort_coo(tf_idf_vector.tocoo())

    #extract only the top n; n here is 10
    keywords=extract_topn_from_vector(featureNames, sortedItems, 10)
    
    return keywords

#Read Json into a dataframe
articles = pd.read_json("../Articles/Breitbart/Extracted/articles.json")
trainArticles = pd.read_json("../Articles/Breitbart/Extracted/articlesCAT.json")

#Create array of all article content
trainContent = trainArticles['Content'].tolist()
content = articles['Content'].tolist()

#Create vocabulary of words
#Ignore words that appear in 85% of documents
#cv = CountVectorizer(max_df=.85, max_features=10000)
cv = CountVectorizer(max_df=.85)
wordcountVector = cv.fit_transform(content)
print(wordcountVector.shape)

#Generate IDF from vocab list
tfidf = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf.fit(wordcountVector)

#Extract feature names
featureNames = cv.get_feature_names_out()

#Generate tf-idf vector for document
tfidfVector = tfidf.transform(cv.transform(content))
tfidfTrainVector = tfidf.transform(cv.transform(trainContent))

#Get keywords for all documents in training set
results = []
for i in range(tfidfVector.shape[0]):
    
    # get vector for a single document
    currVector = tfidfVector[i]
    
    #sort the tf-idf vector by descending order of scores
    sortedItems = sort_coo(currVector.tocoo())

    #extract only the top n; n here is 10
    keywords = extract_topn_from_vector(featureNames, sortedItems, 25)
    
    results.append(keywords)
    
#Get keywords for all documents in training set
resultsTrain = []
for i in range(tfidfTrainVector.shape[0]):
    
    # get vector for a single document
    currVector = tfidfTrainVector[i]
    
    #sort the tf-idf vector by descending order of scores
    sortedItems = sort_coo(currVector.tocoo())

    #extract only the top n; n here is 10
    keywordsTrain = extract_topn_from_vector(featureNames, sortedItems, 25)
    
    resultsTrain.append(keywordsTrain)
    
results = np.reshape(np.array(results), (-1, len(results)))
resultsTrain = np.reshape(np.array(resultsTrain), (-1, len(resultsTrain)))
    
df = pd.DataFrame(np.concatenate((articles, results.T), axis=1), columns=['Title','Time','Author','Content','Original Content', 'Category','Keywords'])
dfTrain = pd.DataFrame(np.concatenate((trainArticles, resultsTrain.T), axis=1), columns=['Title','Time','Author','Content','Original Content', 'Category','Keywords'])

df.to_json('ArticlesKeywords.json')
dfTrain.to_json('ArticlesTrainKeywords.json')