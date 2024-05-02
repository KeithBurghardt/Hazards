import os
import openai
import pandas as pd
import numpy as np

openai.organization = ""
openai.api_key = ""
model_engine = "gpt-4"#
#model_engine = "gpt-3.5-turbo-0301"#"text-davinci-003"

n = 1

annotations = pd.read_csv('annotations.csv')# from GT data
unique_text = annotations['text'].drop_duplicates().values

responses = {t:np.nan for t in unique_text}
# social conservative
pre_prompt = 'Does the tweet describe a hazard (something that could impose harm or other costs on the author of the tweet or on others)? Please answer "yes" or "no" and explain your thought process.'

for ii,text in enumerate(unique_text):
    if ii % 10 == 0:
        print(round(ii/len(unique_text)*100,1))
    prompt = pre_prompt + text
    # Generate a response
    try:
        completion = openai.ChatCompletion.create(model=model_engine,messages=[{"role": "user", "content": prompt}])
        response = completion.choices[0].message["content"]
        responses[text] = response
        print(response)
    except:
        continue

for ii,text in enumerate(unique_text):
    if type(responses[text]) is not str:
        if np.isnan(responses[text]):
            try:
                completion = openai.ChatCompletion.create(model=model_engine,messages=[{"role": "user", "content": prompt}])
                response = completion.choices[0].message["content"]
                responses[text] = response
            except:
                continue

t = list(responses.keys())
res = [responses[k] for k in responses.keys()]
#pd.DataFrame([[t,r] for t,r in zip(t,res)],columns=['text','responses']).to_csv('gpt35_responses_threat_'+str(n)+'_soc.csv',index=False)
#annotations['gpt35_response'] = [responses[t] for t in annotations['text'].values]
#annotations['gpt35_hazard'] = [responses[t].split(',')[0].split('.')[0] if type(responses[t]) is str else np.nan for t in annotations['text'].values]
#annotations.to_csv('annotations_responses_sampled_tweets.csv',index=False)

pd.DataFrame([[t,r] for t,r in zip(t,res)],columns=['text','responses']).to_csv('gpt35_cons_qualtrics-prompt_responses.csv',index=False)
#pd.DataFrame([[t,r] for t,r in zip(t,res)],columns=['text','responses']).to_csv('gpt35_lib_responses.csv',index=False)

