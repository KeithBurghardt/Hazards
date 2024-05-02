import os
import openai
import pandas as pd
import numpy as np
import networkx as nx

from openai import OpenAI


openai_api_key = ""
client = OpenAI(
    api_key=openai_api_key,
)

annotations = pd.read_csv('annotations.csv')# from GT data
unique_text = annotations['text'].drop_duplicates().values
responses={'text':unique_text}
# social conservative
pre_prompt = 'Does the tweet describe a hazard (something that could impose harm or other costs on the author of the tweet or on others)? Please answer "yes" or "no" and explain your thought process.\n'

for model_engine in [ "gpt-3.5-turbo","gpt-4"]:
    print(model_engine)
    responses[model_engine] = []
    for ii,text in enumerate(unique_text):
        if ii % 100 == 0:
            print(round(ii/len(unique_text)*100,2))
        prompt = pre_prompt + text
        response = np.nan
        if True:
            completion = client.chat.completions.create(model=model_engine,messages=[{"role": "user", "content": prompt}])
            response = completion.choices[0].message.content
        responses[model_engine].append(response)
responses = pd.DataFrame(responses)
responses.to_csv('tweet_responses.csv')
