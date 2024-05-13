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

## GPT_code
This contains all code to have GPT annotate tweets or urban legends, as well as summarize all urban legends to under 128 tokens.
## ground_truth_data
This contains all code and guidelines for collection and annotation of ground truth X posts, along with the annotated posts and urban legend annotations from Fessler et al., 2014. We also share a datasheet that describes the data.

## hazard_detection
This contains the trained model and the code to predict hazards in JSONL files.
## israel-hamas_war
This contains the coordinated network extracted from our analysis of X posts related to the Hamas-Israel war in an edgelist format. The nodes represent hashed usernames. 
## training_code
This contains the Jupyter notebook used to train the models

## urban_legends
This contains all urban legends collected, including those from Fessler et al., 2014. We also share a datasheet that describes the data.

References:

Fessler DMT, Pisor AC, Navarrete CD (2014) Negatively-Biased Credulity and the Cultural Evolution of Beliefs. PLoS ONE 9(4): e95167. doi:10.1371/journal.pone.0095167
