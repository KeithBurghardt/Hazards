# Hazards
## What this model does
Model returns a CSV file of the post ID and the hazard probability for each of theses posts. 

## How to run
```
python hazard_detection.py <filename>
```

## Requirements.txt
Lists the required libraries:

- pandas==2.0.2
- sklearn==1.2.2
- matplotlib==3.7.1
- scipy==1.10.1
- sentence_transformers==2.2.2
- numpy==1.24.4

## finalized_model_SVM.sav
The hazard detection model trained on ~1300 tweets with known hazards. This is a multilingual model (it works for any major language).

## Hazard_guidelines.docx
These are the questions asked to annotators. We have 3 annotators per tweet (all tweets were in English and chosen among a random set of tweets containing hazard (threat) words).

## collect_tweets_threats.py
This code collects the tweets containing threat words for annotations. The threat words come from a threat dictionary (https://www.michelegelfand.com/threat-dictionary), which only contains English words. The equivalent for non-English words has yet to be developed, but could be a translation of these words to a different language (although some words lose their threat meaning in a different language, and alternatively, other words that describe threats or hazards in another language may not exist in this corpus).

## threats.csv
All English words collected as of late 2022 from https://www.michelegelfand.com/threat-dictionary.

Hazard corpus reference:

Choi, Virginia K. and Shrestha, Snehesh and Pan, Xinyue and Gelfand, Michele J. (2022). When danger strikes: A linguistic tool for tracking America’s collective response to threats Proceedings of the National Academy of Sciences:119(4):e2113891119, doi: 10.1073/pnas.2113891119.
