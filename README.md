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
The hazard detection model trained on ~1000 tweets with known hazards

