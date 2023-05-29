#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from textblob import TextBlob

# Load the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\malli\Downloads\movie.csv")

# Define the start and end index for the range of reviews you want to select
start_index = 5
end_index = 15

# Select the range of reviews
selected_df = df.iloc[start_index:end_index].copy()

# Perform sentiment analysis on each selected review
for index, row in selected_df.iterrows():
    text = row['text']
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment >= 0.05:
        review = 'Positive'
    elif sentiment <= -0.05:
        review = 'Negative'
    else:
        review = 'Neutral'
    selected_df.loc[index, 'review'] = review

# Reset the index of the selected DataFrame
selected_df.reset_index(drop=True, inplace=True)

# Print the updated DataFrame with sentiment analysis results for the selected range
print(selected_df)


# In[ ]:





# In[ ]:




