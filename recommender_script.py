# %% [markdown]
# ### Anime recommender using cosine similarities on its properties like actors,directors and genres 
# https://towardsdatascience.com/how-to-build-from-scratch-a-content-based-movie-recommender-with-natural-language-processing-25ad400eb243

# %%
import pandas as pd
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# import numpy as np
# from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
pd.options.mode.chained_assignment = None  # default='warn'
df2=pd.read_csv('dataset/credits.csv')
df1= pd.read_csv("dataset/titles.csv")

# %%
# Group by 'title' and aggregate 'artist' using a lambda function to join multiple artists
grouped_df = df2.groupby('id')['name'].agg(lambda x: ', '.join(x)).reset_index()

# Reset index to get rid of hierarchical index and create a new DataFrame
new_df = pd.DataFrame(grouped_df)
# new_df.head()

# %%

df=df1.merge(new_df,on='id')
# df.head()

# %%
df=df.dropna()


# %%
# df['Key_words'] = " "

# for index, row in df.iterrows():
#     description = row['description']
#     # instantiating Rake, by default it uses english stopwords from NLTK
#     # and discards all puntuation characters as well
#     r = Rake()

#     # extracting the words by passing the text
#     r.extract_keywords_from_text(description)
    

#     # getting the dictionary whith key words as keys and their scores as values
#     key_words_dict_scores = r.get_word_degrees()
    
#     # assigning the key words to the new column for the corresponding movie
#     df.at[index, 'Key_words'] = list((key_words_dict_scores.keys()))

# %%
df.reset_index(drop=True, inplace=True) #now that index is good i can train again

# %%
df["bag_of_words"]=""

genre = ['genres']
# keyword= ['Key_words']
name=['name']
titles=['title','age_certification']
prod = ['production_countries']

for index, row in df.iterrows():
    words = ''
    for col in titles:
        words = words + ''.join(row[col])+' '
    for col in genre:
        row[col] = row[col].replace('[', '').replace(']', '').replace('\'', '')
        row[col] = row[col].replace(',', ' ')
        words = words + ''.join(row[col])+' '
    for col in name:
        row[col] = row[col].replace(',', ' ')
        words = words + ' '.join(row[col])+' '

    # for col in keyword:
    #     words = words + ' '.join(row[col])+ ' '
    # for col in prod:    
    #     row[col] = row[col].replace('[', '').replace(']', '').replace('\'', '')
    # for col in scores:
    #     words = words + str(int(row[col]))
    df.at[index,'bag_of_words'] = words.lower()
# df.head()

# %%

count = CountVectorizer()
count_matrix = count.fit_transform(df['bag_of_words'])

indices = pd.Series(df['title'])
# print(indices[:5]) 
#index to access to get recommendation
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# %%

def recommendation(Title, cosine_sim = cosine_sim):
    
    recommended_anime = []
    
    # gettin the index of the movie that matches the title
    idx = indices[indices == Title].index[0]

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    # getting the indexes of the 10 most similar movies
    top_5_indexes = list(score_series.iloc[1:6].index)
    
    # populating the list with the titles of the best 10 matching movies
    for i in top_5_indexes:
            recommended_anime.append(list(df.title)[i])
        
    return recommended_anime

# %%
print(type(recommendation('Your Lie in April')))
print(recommendation('Your Lie in April'))

# %%
# df[df.title=='Domestic Girlfriend']
# idx = indices[indices == 'Domestic Girlfriend'].index[0]
# print(idx)

# creating a Series with the similarity scores in descending order
# score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)


# %%
# df[df.title=='Dragon Ball']
# idx = indices[indices == 'Dragon Ball'].index[0]
# print(idx)

# creating a Series with the similarity scores in descending order
# score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
# print(score_series)

# %%
# df[df.title=='Domestic Girlfriend']

# %%
# print(recommendation('Domestic Girlfriend'))

# %%


# %%



