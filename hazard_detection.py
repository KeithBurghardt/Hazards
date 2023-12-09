import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import sklearn
import matplotlib
import random
import pickle as pk
import os,random,sys
from scipy.stats import uniform, randint, beta
from glob import glob
from sklearn.metrics import auc, accuracy_score, confusion_matrix, mean_squared_error
from sklearn.model_selection import cross_val_score, GridSearchCV, KFold, RandomizedSearchCV, train_test_split
from sklearn.metrics import accuracy_score,roc_auc_score,f1_score
from sklearn.svm import SVC
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('stsb-xlm-r-multilingual')
clf = pk.load(open('finalized_model_SVM.sav','rb'))


def load_data(file):
    data=pd.read_json(file,lines=True)
    if 'Twitter' in data['mediaType'].drop_duplicates().values:
        authors = []
        engagement_types=[]
        tweet_ids = []
        engagementParentIds = []
        for line in data['mediaTypeAttributes'].values:
            line = ast.literal_eval(line)

            try:
                if 'twitterData' in line.keys():
                    if 'twitterAuthorScreenname' in line['twitterData'].keys():
                        author = line['twitterData']['twitterAuthorScreenname']
                    if 'engagementType' in line['twitterData'].keys():
                        engagement_type = line['engagementType']
                    if 'tweetId' in line['twitterData'].keys():
                        tweet_id = line['twitterData']['tweetId']
                    if 'engagementParentId' in line['twitterData'].keys():
                        if str(line['twitterData']['engagementParentId']) != 'null':
                            engagementParentId = line['twitterData']['engagementParentId']

            except:
                author=np.nan
                engagement_type=np.nan
                tweet_id = np.nan
                engagementParentId = np.nan

            authors.append(author)
            engagement_types.append(engagement_type)
            engagementParentIds.append(engagementParentId)
            tweet_ids.append(tweet_id)
        data['twitterAuthorScreenname'] = authors
        data['engagementType'] = engagement_types
        data['tweetId']=tweet_ids
        data['engagementParentId'] = engagementParentIds
    return data

def main(argv):
    file = argv[0]
    data = load_data(file)
    text_col = 'contentText'
    if 'contentText' not in twitter_data.columns:
        text_col = 'text'
    if text_col not in twitter_data.columns: print(file)
    twitter_data[text_col] = twitter_data[text_col].astype("string")
    all_pred = []
    tweets = []
    for ii,tweet in enumerate(twitter_data[text_col].values):
        tweets.append(str(tweet))
        if ii % 1000 == 0:
            print(round(ii/len(twitter_data)*100,2))
            embeddings = model.encode(tweets)
            pred_prob = list(clf.predict_proba(embeddings)[:,1])
            all_pred+=pred_prob
            tweets = []
    # catching any leftovers
    embeddings = model.encode(tweets)
    pred_prob = list(clf.predict_proba(embeddings)[:,1])
    all_pred+=pred_prob
    twitter_data['hazard'] = all_pred#[dict_pred[t] if t in set(dict_pred.keys()) else np.nan for t in twitter_data[text_col].values]
    if 'id' not in twitter_data.columns:
        c = [col for col in twitter_data.columns if 'id' in col][0]
        twitter_data['id'] = twitter_data[c]
    twitter_data['id'] = twitter_data['id'].astype(str)
    twitter_data[['id','hazard']].to_csv(file[:-4]+'_hazards.csv',index=False)

if __name__ == "__main__":
   main(sys.argv[1:])
            
