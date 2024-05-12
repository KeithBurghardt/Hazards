- extract_tweets_threat.py: our code to collect tweets that contain words from the threat dictionary. This dictionary is here: - https://www.michelegelfand.com/threat-dictionary
- Hazard guidelines: text annotators use to detect if a hazard exists 
- AnonymousAnnotations.csv: annotations for each post by each annotator. We include an anonymized annotator ID along with basic demographics to determine whether demographics affect what is annotated as a hazard. We also include severe hazards and benefit annotations, which we do not analyze in our study.
- TweetGT.csv: the mean of annotator labels for each post based on AnonymousAnnotations.csv. We also include severe hazards and benefit annotations, which we do not analyze in our study.
- urbanlegend_dataset_CODER#S.csv: 2014 SNOPES text annotated by each of 7 annotators from Fessler et al., 2014:

Fessler, D. M., Pisor, A. C., & Navarrete, C. D. (2014). Negatively-biased credulity and the cultural evolution of beliefs. PloS one, 9(4), e95167.
