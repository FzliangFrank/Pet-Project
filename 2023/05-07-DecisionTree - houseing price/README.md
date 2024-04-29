# What is this? 

A experiment using decision tree to predict housing price given a dataset. 

# Mindful of Decision Tree

# Machine Learnning in General

## NA valud Remove
- First thing you need to consider is missing value. This is where the hardwork comes in. With NA valud consider follow: 
    - NA or NULL? 
    - Rows or Column 
    - Impute? 
    - Is value missing or because they actually meaning something. 
    - in extreme case you will need to consider each column attributes. 

## Categorical Vriables
- Categorical Variables:
    What is considered good category
    What is considered bad category
Three strategies:
- 1. Drop 
- 2. Ordinal transform OrdinalEncoder.fit_transform()
- 3. 