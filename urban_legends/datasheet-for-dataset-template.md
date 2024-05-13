# Datasheet for dataset Urban Legends

Questions from the [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) paper, v7.

Jump to section:

- [Motivation](#motivation)
- [Composition](#composition)
- [Collection process](#collection-process)
- [Preprocessing/cleaning/labeling](#preprocessingcleaninglabeling)
- [Uses](#uses)
- [Distribution](#distribution)
- [Maintenance](#maintenance)

## Motivation


### For what purpose was the dataset created? 

These data were collected to understand how hazards are shared within urban legends.

### Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?

Anonymized.

### Who funded the creation of the dataset? 

Anonymized

### Any other comments?
N/A
## Composition


### What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?

These contain several different urban legends, some of which are different examples of the same urban legend mofit, such as the vanishing hitchhiker.

### How many instances are there in total (of each type, if appropriate)?
- 996 urban legends from SNOPES 2022
- 255 urban legends from the Encyclopedia of Urban Legends
- 280 urban legends from SNOPES 2014

### Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?

These data contain all instances within the Encyclopedia and all instances with "fact-check" within SNOPES. This is likely a biased subsample of urban legends that possibly exist, especially when these legends are mostly in English.

### What data does each instance consist of? 

The raw data are text with a title, possibly a broad claim, and an example legend (if it exists).

### Is there a label or target associated with each instance?

N/A

### Is any information missing from individual instances?

In SNOPES data, example legends may not exist. Instead broad claims are recorded instead.

### Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)?

SNOPES urban legends that fall under the same title/url are examples of the same broad motif.

### Are there recommended data splits (e.g., training, development/validation, testing)?

N/A
### Are there any errors, sources of noise, or redundancies in the dataset?

N/A
### Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?

Cf. Fessler et al., 2014 for hazards associated with the 2014 SNOPES urban legends.

### Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)?

N/A

### Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?

Urban legends may cause anxiety depending on the type.

### Does the dataset relate to people? 

No.
### Does the dataset identify any subpopulations (e.g., by age, gender)?
N/A
### Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?

N/A
### Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?

N/A
### Any other comments?
N/A
## Collection process


### How was the data associated with each instance acquired?

Data were scraped by hand within the URL or book.

### What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?

We use human scraping. 

### If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?
These collections are complete.

### Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?

Undergraduate research assistant students performed the collection.

### Over what timeframe was the data collected?

Data were collected in late 2022 over the course of approximately 2 months.

### Were any ethical review processes conducted (e.g., by an institutional review board)?
N/A
### Does the dataset relate to people?

No.
### Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?
N/A
### Were the individuals in question notified about the data collection?

N/A
### Did the individuals in question consent to the collection and use of their data?

N/A

### If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?

N/A

### Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted?

N/A
### Any other comments?
N/A
## Preprocessing/cleaning/labeling


### Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?

No.

### Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?

Data is raw.

### Is the software used to preprocess/clean/label the instances available?

N/A
### Any other comments?
N/A
## Uses


### Has the dataset been used for any tasks already?

No.

### Is there a repository that links to any or all papers or systems that use the dataset?

Anonymized.

### What (other) tasks could the dataset be used for?
These data will be useful for any future analysis of urban legends.
### Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

No.
### Are there tasks for which the dataset should not be used?

N/A
### Any other comments?
N/A
## Distribution

### Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created? 

These data are freely available.

### How will the dataset will be distributed (e.g., tarball on website, API, GitHub)?

All data are in a XLSX file on this repository.

### When will the dataset be distributed?
Data are available now.
### Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?

There is no copytight or ToU.

### Have any third parties imposed IP-based or other restrictions on the data associated with the instances?

No.

### Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?

No.

### Any other comments?
N/A
## Maintenance


### Who is supporting/hosting/maintaining the dataset?
Anonymized.
### How can the owner/curator/manager of the dataset be contacted (e.g., email address)?
Anonymized.
### Is there an erratum?

No. These data are static.
### Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)?

No.
### If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?

N/A
### Will older versions of the dataset continue to be supported/hosted/maintained?

N/A
### If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?

Yes, any new data can be forked from this repository.

### Any other comments?
N/A
