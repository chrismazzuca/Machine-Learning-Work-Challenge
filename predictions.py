from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = pd.read_csv("Employment Data/job_skills.csv", index_col=0)
print(data.head(0))
# data.fillna('', inplace=True)
# vectorizer = TfidfVectorizer(stop_words='english', max_df=0.95, strip_accents='ascii', lowercase=True)
# X = vectorizer.fit_transform(data.loc[:,'Responsibilities'].values)