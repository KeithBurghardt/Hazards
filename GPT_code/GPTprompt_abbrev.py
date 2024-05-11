import os
import openai
import pandas as pd
import numpy as np

def get_summary(text):
    pre_prompt = 'Please summarize the following text: '
    summary = []
    for ii,ex in enumerate(text):
        if ii % 10 == 0:
            print(round(ii/len(text)*100,2))
        prompt = pre_prompt + ex
        response = np.nan
        try:
            # max tokens <= 128
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": prompt}],max_tokens = 128)
            response = completion.choices[0].message["content"]
        except:
            pass
        summary.append(response)
    for ii,res in enumerate(summary):
        if type(res) is not str:
            if np.isnan(res):
                try:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": prompt}])
                    response = completion.choices[0].message["content"]
                    summary[ii] = response
                except:
                    continue

    return summary

openai.organization = ""
openai.api_key = ""
model_engine = "gpt-4"#
model_engine = "gpt-3.5-turbo-0301"#"text-davinci-003"


unlabeled_data_SNOPES = pd.read_excel('Urban Legend Data_ 2022 Snopes, Encyclopedia & 2014.xlsx',sheet_name='992 SNOPES LEGENDS')
unlabeled_data_Enc = pd.read_excel('Urban Legend Data_ 2022 Snopes, Encyclopedia & 2014.xlsx',sheet_name='255 Encyclopedia Of Urban Legen')
unlabeled_data_Enc = unlabeled_data_Enc[['NARRATIVE MYTH/Legend Title ','LEGEND TEXT ']]
text_SNOPES = unlabeled_data_SNOPES['LEGEND TEXT '].values.astype(str)
text_enc = unlabeled_data_Enc['LEGEND TEXT '].values.astype(str)

outfile = 'unlabeled_SNOPES.csv'

if not os.path.exists(outfile):
    unlabeled_data_SNOPES['summary'] = get_summary(text_SNOPES)
    unlabeled_data_SNOPES.to_csv(outfile,index=False)
outfile = 'unlabeled_Enc.csv'
if not os.path.exists(outfile):
    unlabeled_data_Enc['summary'] = get_summary(text_enc)
    unlabeled_data_Enc.to_csv(outfile,index=False)


outfile = '2014_labeled_data.csv'
if not os.path.exists(outfile):
    data = pd.read_csv('urbanlegend_dataset_CODER#S.csv')
    data.columns = ['number','hazard','hazard_aspect','hazard_central','hazard_severe','hazard_overcome','benefit','benefit_aspect','benefit_central','benefit_severe','benefit_obtain','coder']
    cleaned_data = data[['number','hazard','hazard_severe','benefit','benefit_severe']].replace('Y',1).replace('N',0).replace('S',1).replace('M',0)
    cleaned_data['hazard_severe'] = cleaned_data['hazard_severe'].fillna(0)
    cleaned_data['benefit_severe'] = cleaned_data['benefit_severe'].fillna(0)
    cleaned_data = cleaned_data.dropna()
    labeled_data = pd.read_excel('Urban Legend Data_ 2022 Snopes, Encyclopedia & 2014.xlsx',sheet_name='2014 Data')
    text = labeled_data['Example'].values
    # summarize 'example' to be under 128 tokens
    #pre_prompt = 'Please summarize the following text: '
    
    labeled_data['summary'] = get_summary(text)
    labeled_data.to_csv(outfile,index=False)
