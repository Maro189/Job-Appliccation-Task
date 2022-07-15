#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pacakages
import pandas as pd
import numpy as np

# opening file from folder location via pandas
df = pd.read_csv(r'G:\Python projects\Job project\Movie - Data Set for Cleaning - Sheet1.csv')

# renaming columns for better clarity
df = df.rename(columns = {'movie_title': 'Movie Title', 'num_critic_for_reviews': 'Number of Critic Reviews', 'duration': 'Duration (mins)',
                         'DIRECTOR_facebook_likes': 'Facebook Likes (Director)', 'actor_3_facebook_likes': 'Facebook Likes (Actor 3)', 
                          'ACTOR_1_facebook_likes': 'Facebook Likes (Actor 1)', 'gross': 'Gross profit ($)', 'Cast_Total_facebook_likes': 
                         'Facebook Likes (Cast Total)', 'budget': 'Budget ($)', 'title_year': 'Year Released', 'num_user_for_reviews': 
                          'Number of User Reviews', 'ACTOR_2_facebook_likes': 'Facebook Likes (Actor 2)', 'imdb_score': 'IMDB Score (/10)', 
                         'num_voted_users': 'Number of Votes', 'facenumber_in_poster': 'Faces on Poster'})

# dropping unnecessary columns
df = df.drop(columns = ['title_year.1'])
df

# removing unnecessary strings
df['Movie Title'] = df['Movie Title'].str.replace('?','')
df['Movie Title'] = df['Movie Title'].str.replace('ÿ','')
df['Facebook Likes (Director)'] = df['Facebook Likes (Director)'].str.replace('"475"', '475')
                                                  
# reordering columns for calirty
# defining cols as variable and printing variable to assist with column reordering 
# cols = list(df.columns.values)
# print(cols)
df = df.reindex(columns=['Movie Title','Year Released', 'Duration (mins)', 'Budget ($)', 'Gross profit ($)', 'IMDB Score (/10)', 
                        'Number of Critic Reviews', 'Number of User Reviews', 'Number of Votes', 'Facebook Likes (Actor 1)', 
                        'Facebook Likes (Actor 2)', 'Facebook Likes (Actor 3)', 'Facebook Likes (Director)', 'Facebook Likes (Cast Total)', 'Faces on Poster'])

df


# In[2]:


# saving clean dataset as csv to be accessed later
df.to_csv('Movie Dataset (clean).csv')


# In[ ]:




