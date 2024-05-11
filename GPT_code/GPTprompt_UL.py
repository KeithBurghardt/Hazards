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



#pre_prompt = 'Does the following story describe a hazard (something that could impose harm or other costs on the author of the story or on others)?\n'
pre_prompt = 'Does the story describe a hazard (something that could impose harm or other costs on the author of the story or on others)? Please answer "yes" or "no" and explain your thought process.\n'

stories = pd.read_csv('2014_labeled_data.csv')
responses={'summary':stories['summary'].values}
for model_engine in [ "gpt-3.5-turbo","gpt-4"]:
    print(model_engine)
    responses[model_engine] = []
    for text in stories['summary'].values:
        prompt = pre_prompt + text
        #try:
        response = np.nan
        if True:
            completion = client.chat.completions.create(model=model_engine,messages=[{"role": "user", "content": prompt}])
            response = completion.choices[0].message.content
            #completion = openai.ChatCompletion.create(model=model_engine,messages=[{"role": "user", "content": prompt}])
            #response = completion.choices[0].message["content"]
        responses[model_engine].append(response)
responses = pd.DataFrame(responses)
responses.to_csv('UL_responses.csv')

