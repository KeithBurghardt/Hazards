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
## collect_tweets_threats.py
This code collects the tweets containing threat words for annotations. The threat words come from a threat dictionary (https://www.michelegelfand.com/threat-dictionary), which only contains English words. The equivalent for non-English words has yet to be developed, but could be a translation of these words to a different language (although some words lose their threat meaning in a different language, and alternatively, other words that describe threats or hazards in another language may not exist in this corpus).

## Hazard_guidelines.docx
These are the questions asked to annotators. We have 3 annotators per tweet (all tweets were in English and chosen among a random set of tweets containing hazard (threat) words).

## annotations.csv
Ground truth annotations of extracted posts that contain at least one hazard word as discussed in Choi et al., 2022.

## NegativelyBiasedCredulityPred.ipynb

How the model is trained, as well as data exploration. X posts are listed in this GitHub, while the urban legends from from Fessler et al., 2014.

## finalized_model_SVM.sav
The hazard detection model trained on ~1300 tweets with known hazards. This is a multilingual model (it works for any major language).

## hazard_detection.py
Code to annotate text via their hazard probability.


## threats.csv
All English words collected as of late 2022 from https://www.michelegelfand.com/threat-dictionary (Choi et al., 2022).


References:

Choi, Virginia K. and Shrestha, Snehesh and Pan, Xinyue and Gelfand, Michele J. (2022). When danger strikes: A linguistic tool for tracking America’s collective response to threats Proceedings of the National Academy of Sciences:119(4):e2113891119, doi: 10.1073/pnas.2113891119.

Fessler DMT, Pisor AC, Navarrete CD (2014) Negatively-Biased Credulity and the Cultural Evolution of Beliefs. PLoS ONE 9(4): e95167. doi:10.1371/journal.pone.0095167
