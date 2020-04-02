import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2


# Load the dataset with pandas, and preprocess the data
data = pd.read_csv("Employment Data/job_skills.csv", index_col=0)
data.fillna('', inplace=True)
data['Category id'] = data['Category'].factorize()[0]
labels = data['Category id']
categories = dict(data[['Category', 'Category id']].drop_duplicates().values)

# Create a tf-idf vectorizer, and fit it to the "Responsibilities" column
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2), strip_accents='ascii', lowercase=True)
features = vectorizer.fit_transform(data.Responsibilities).toarray()

# For each category, store the 3 most common unigrams and bigrams
with open("results.txt", "w") as file:
    for category, responsibility in sorted(categories.items()):
        indices = np.argsort(chi2(features, labels == responsibility)[0])
        feature_names = np.array(vectorizer.get_feature_names())[indices]
        unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
        bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
        file.write(category + '\n')
        file.write("  3 Most Common Unigrams: {}\n".format(', '.join(unigrams[-3:])))
        file.write("  3 Most Common Bigrams: {}\n\n".format(', '.join(bigrams[-3:])))