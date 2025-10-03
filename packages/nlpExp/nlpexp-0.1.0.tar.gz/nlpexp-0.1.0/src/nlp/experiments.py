def experiment_1():
    return '''from google.colab import userdata
import os
os.environ["KAGGLE_KEY"] = userdata.get('KAGGLE_KEY')
os.environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME')
!kaggle datasets download -d hammadjavaid/football-news-articles
!unzip "/content/football-news-articles.zip"
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
import numpy as np
import pandas as pd
import re
import nltk
import spacy
import string
pd.options.mode.chained_assignment = None
full_df = pd.read_csv("/content/allfootball.csv", nrows=5000)
df = full_df[["title"]]
df["title"] = df["title"].astype(str)
full_df.head()
"""Sentence Tokenization"""
import nltk
from nltk.tokenize import sent_tokenize
import pandas as pd
def tokenize_text(text):
return sent_tokenize(text)
df['sentences'] = df['title'].apply(tokenize_text)
print(df.head())
for index, row in df.head().iterrows():
print(f"Total sentences in entry {index}: {len(row['sentences'])}")
print("Sentences:")
print(np.array(row['sentences']))
print()
common_text = df['title']
import nltk
import numpy as np
import pandas as pd
default_st = nltk.sent_tokenize
def tokenize_text(text):
return default_st(text)
df['sentences'] = df['title'].apply(tokenize_text)
sample_sentences = df.iloc[0]['sentences']
print('Total sentences in sample_text:', len(sample_sentences))
print('Sample text sentences:')
print(np.array(sample_sentences))
punkt_st = nltk.tokenize.PunktSentenceTokenizer()
def tokenize_text(text):
return punkt_st.tokenize(text)
df['desccriptions'] = df['title'].apply(tokenize_text)
sample_sentences = df.iloc[0]['title']
print(np.array(sample_sentences))
"""Word Tokenization"""
from nltk.tokenize.toktok import ToktokTokenizer
tokenizer = ToktokTokenizer()
words = tokenizer.tokenize(sample_sentences)
np.array(words)
TOKEN_PATTERN = r'\w+'
regex_wt = nltk.RegexpTokenizer(pattern=TOKEN_PATTERN, gaps=False)
words = regex_wt.tokenize(sample_sentences)
np.array(words)
GAP_PATTERN = r'\s+'
regex_wt = nltk.RegexpTokenizer(pattern=GAP_PATTERN, gaps=True)
words = regex_wt.tokenize(sample_sentences)
np.array(words)
"""TEXT NORMALISATION
Lower Casing """
import pandas as pd
import string
df['text_lower'] = df['title'].str.lower()
df.head()
"""Removal of Punctuations"""
PUNCT_TO_REMOVE = string.punctuation
def remove_punctuation(text):
"""Custom function to remove the punctuation"""
return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))
df["text_wo_punct"] = df["text_lower"].apply(remove_punctuation)
df.drop(["text_lower"], axis=1, inplace=True)
df.head()
"""Removal of stopwords"""
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words_string = ", ".join(stop_words)
print(stop_words_string)
STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
"""custom function to remove the stopwords"""
return " ".join([word for word in str(text).split() if word not in STOPWORDS])
df["text_wo_stop"] = df["text_wo_punct"].apply(lambda text: remove_stopwords(text))
df.head()
"""Removal of Frequent words"""
from collections import Counter
cnt = Counter()
for text in df["text_wo_stop"].values:
for word in text.split():
cnt[word] += 1
cnt.most_common(10)
FREQWORDS = set([w for (w, wc) in cnt.most_common(10)])
def remove_freqwords(text):
"""custom function to remove the frequent words"""
return " ".join([word for word in str(text).split() if word not in FREQWORDS])
df["text_wo_stopfreq"] = df["text_wo_stop"].apply(lambda text: remove_freqwords(text))
df.head()
"""Stemming"""
from nltk.stem.porter import PorterStemmer
# Drop the two columns
# df.drop(["text_wo_stopfreq", "text_wo_stopfreqrare"], axis=1, inplace=True)
stemmer = PorterStemmer()
def stem_words(text):
return " ".join([stemmer.stem(word) for word in text.split()])
df["text_stemmed"] = df["title"].apply(lambda text: stem_words(text))
df.head()
from nltk.stem.snowball import SnowballStemmer
SnowballStemmer.languages
"""Lemmatization"""
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
def lemmatize_words(text):
return " ".join([lemmatizer.lemmatize(word) for word in text.split()])
df["text_lemmatized"] = df["title"].apply(lambda text: lemmatize_words(text))
df.head()
lemmatizer.lemmatize("running")
lemmatizer.lemmatize("running", "v")
print("Word is : stripes")
print("Lemma result for verb : ",lemmatizer.lemmatize("stripes", 'v'))
print("Lemma result for noun : ",lemmatizer.lemmatize("stripes", 'n'))
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
def lemmatize_words(text):
pos_tagged_text = nltk.pos_tag(text.split())
return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])
df["text_lemmatized"] = df["title"].apply(lambda text: lemmatize_words(text))
df.head()'''

def experiment_2():
    return '''from google.colab import userdata 
import os 
os.environ["KAGGLE_KEY"] = userdata.get('KAGGLE_KEY') 
os.environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME') 
import pandas as pd 
import numpy as np 
import re 
import nltk 
import matplotlib.pyplot as plt 
pd.options.display.max_colwidth = 200 
corpus_df=pd.read_csv("/content/samsum-train.csv", nrows=5000) 
corpus_df.head() 
corpus=np.array(corpus_df['summary']) 
print(corpus) 
from sklearn.feature_extraction.text import CountVectorizer 
cv = CountVectorizer(min_df=0., max_df=1.) 
cv_matrix = cv.fit_transform(corpus) 
cv_matrix 
print(cv_matrix) 
cv_matrix = cv_matrix.toarray() 
cv_matrix 
vocab = cv.get_feature_names_out() 
pd.DataFrame(cv_matrix, columns=vocab) 
bv = CountVectorizer(ngram_range=(2,2)) 
bv_matrix = bv.fit_transform(corpus) 
bv_matrix = bv_matrix.toarray() 
vocab = bv.get_feature_names_out() 
pd.DataFrame(bv_matrix, columns=vocab) 
from sklearn.feature_extraction.text import TfidfTransformer 
tt = TfidfTransformer(norm='l2', use_idf=True, smooth_idf=True) 
tt_matrix = tt.fit_transform(cv_matrix) 
tt_matrix = tt_matrix.toarray() 
vocab = cv.get_feature_names_out() 
pd.DataFrame(np.round(tt_matrix, 2), columns=vocab) 
from sklearn.feature_extraction.text import TfidfVectorizer 
tv = TfidfVectorizer(min_df=0., max_df=1., norm='l2', 
                     use_idf=True, smooth_idf=True) 
tv_matrix = tv.fit_transform(corpus) 
tv_matrix = tv_matrix.toarray() 
vocab = tv.get_feature_names_out() 
pd.DataFrame(np.round(tv_matrix, 2), columns=vocab)'''

def experiment_3():
    return '''from google.colab import userdata 
import os 
os.environ["KAGGLE_KEY"] = userdata.get('KAGGLE_KEY') 
os.environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME') 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import nltk 
nltk.download('punkt') 
corpus_df=pd.read_csv("/content/samsum-train.csv", nrows=5000) 
corpus_df.head() 
sentence=corpus_df['text'][0] 
nlp = spacy.load('en_core_web_sm') 
sentence_nlp = nlp(sentence) 
# POS tagging with Spacy 
spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in sentence_nlp] 
pd.DataFrame(spacy_pos_tagged, columns=['Word', 'POS tag', 'Tag type']).T 
nltk.download('averaged_perceptron_tagger') 
import nltk 
nltk_pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence)) 
pd.DataFrame(nltk_pos_tagged, columns=['Word', 'POS tag']).T 
from nltk.tag import RegexpTagger 
# define regex tag patterns 
patterns = [ 
        (r'.*ing$', 'VBG'),               # gerunds 
        (r'.*ed$', 'VBD'),                # simple past 
        (r'.*es$', 'VBZ'),                # 3rd singular present 
        (r'.*ould$', 'MD'),               # modals 
        (r'.*\'s$', 'NN$'),               # possessive nouns 
        (r'.*s$', 'NNS'),                 # plural nouns 
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers 
        (r'.*', 'NN')                     # nouns (default) ... 
] 
rt = RegexpTagger(patterns) 
rt.tag(nltk.word_tokenize(sentence)) 
 
nltk.download('treebank') 
 
from nltk.corpus import treebank 
data = treebank.tagged_sents() 
train_data = data[:3500] 
test_data = data[3500:] 
from nltk.tag import UnigramTagger 
from nltk.tag import BigramTagger 
from nltk.tag import TrigramTagger 
 
ut = UnigramTagger(train_data) 
bt = BigramTagger(train_data) 
tt = TrigramTagger(train_data) 
 
print(ut.tag(nltk.word_tokenize(sentence))) 
 
print(bt.tag(nltk.word_tokenize(sentence))) 
 
print(tt.tag(nltk.word_tokenize(sentence)))'''

def experiment_4():
    return '''import pandas as pd 
import numpy as np 
data_df = pd.read_csv("/content/BBC News Train.csv") 
data_df.head() 
data_df.dropna() 
data_df.isnull().sum() 
from sklearn.model_selection import train_test_split 
train_corpus, test_corpus, train_label_nums, test_label_nums, train_label_names, 
test_label_names = train_test_split(np.array(data_df['Text']), np.array(data_df['Category']), 
                                                       np.array(data_df['Category']), test_size=0.33) 
train_corpus.shape, test_corpus.shape 
nltk.download('punkt') 
from nltk.tokenize import word_tokenize 
tokenized_train = [word_tokenize(text) for text in train_corpus] 
tokenized_test = [word_tokenize(text) for text in test_corpus] 
import gensim 
w2v_num_features = 1000 
w2v_model = gensim.models.Word2Vec(tokenized_train, window=100, min_count=2, 
sample=1e-3, sg=1,workers=10) 
def document_vectorizer(corpus, model, num_features): 
    vocabulary = set(model.wv.index_to_key) 
    def average_word_vectors(words, model, vocabulary, num_features): 
        feature_vector = np.zeros((num_features,), dtype="float64") 
        nwords = 0. 
        for word in words: 
            if word in vocabulary: 
                nwords = nwords + 1. 
                word_vector = model.wv[word] 
                if len(word_vector) == num_features: 
                    feature_vector = np.add(feature_vector, word_vector) 
        if nwords: 
            feature_vector = np.divide(feature_vector, nwords) 
        return feature_vector 
    features = [average_word_vectors(tokenized_sentence, model, vocabulary, num_features) 
                    for tokenized_sentence in corpus] 
    return np.array(features) 
avg_wv_train_features = document_vectorizer(corpus=tokenized_train, model=w2v_model, 
                                                     num_features=w2v_num_features) 
avg_wv_test_features = document_vectorizer(corpus=tokenized_test, model=w2v_model, 
                                                    num_features=w2v_num_features) 
print('Word2Vec model:> Train features shape:', avg_wv_train_features.shape, 
      ' Test features shape:', avg_wv_test_features.shape) 
from sklearn.model_selection import cross_val_score 
from sklearn.linear_model import SGDClassifier 
svm = SGDClassifier(loss='hinge', penalty='l2', random_state=42, max_iter=500) 
svm.fit(avg_wv_train_features, train_label_names) 
svm_w2v_cv_scores = cross_val_score(svm, avg_wv_train_features, train_label_names) 
svm_w2v_cv_mean_score = np.mean(svm_w2v_cv_scores) 
svm_w2v_test_score = svm.score(avg_wv_test_features, test_label_names) '''

def experiment_5():
    return '''import pandas  as pd 
df = pd.read_csv("/content/samsum-train.csv") 
DOCUMENT = ' '.join(df['summary']) 
print(DOCUMENT) 
import re 
DOCUMENT = re.sub(r'\n|\r', ' ', DOCUMENT) 
DOCUMENT = re.sub(r' +', ' ', DOCUMENT) 
DOCUMENT = DOCUMENT.strip() 
!pip install gensim --upgrade 
import nltk 
nltk.download('punkt') 
sentences = nltk.sent_tokenize(DOCUMENT) 
len(sentences) 
import numpy as np 
import re 
nltk.download('stopwords') 
stop_words = nltk.corpus.stopwords.words('english') 
def normalize_document(doc): 
    # lower case and remove special characters\whitespaces 
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I|re.A) 
    doc = doc.lower() 
    doc = doc.strip() 
    # tokenize document 
    tokens = nltk.word_tokenize(doc) 
    # filter stopwords out of document 
    filtered_tokens = [token for token in tokens if token not in stop_words] 
    # re-create document from filtered tokens 
    doc = ' '.join(filtered_tokens) 
    return doc 
normalize_corpus = np.vectorize(normalize_document) 
norm_sentences = normalize_corpus(sentences) 
norm_sentences[:3]'''

def experiment_6():
    return '''import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
import nltk 
nltk.download('stopwords') 
nltk.download('punkt') 
# importing libraries 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
# Input text - to summarize 
text = """Here's a step-by-step breakdown of the Latent Dirichlet Allocation (LDA) 
algorithm and an implementation using the gensim library in Python: 
Compute the probability of the word given each topic (P(W|T)), which is the proportion of 
assignments to each topic over all documents containing the word. 
Reassign the word to a new topic based on these probabilities. 
Repeat the iterative process for several iterations until convergence """ 
# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 
freqTable = dict() 
for word in words: 
    word = word.lower() 
    if word in stopWords: 
        continue 
    if word in freqTable: 
        freqTable[word] += 1 
    else: 
        freqTable[word] = 1 
# Creating a dictionary to keep the score 
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 
for sentence in sentences: 
    for word, freq in freqTable.items(): 
        if word in sentence.lower(): 
            if sentence in sentenceValue: 
                sentenceValue[sentence] += freq 
            else: 
                sentenceValue[sentence] = freq 
sumValues = 0 
for sentence in sentenceValue: 
    sumValues += sentenceValue[sentence] 
# Average value of a sentence from the original text 
average = int(sumValues / len(sentenceValue)) 
# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
        summary += " " + sentence 
print(summary) 
import nltk 
from nltk.tokenize import sent_tokenize 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from gensim import corpora, models 
import numpy as np 
 
# Download NLTK resources 
nltk.download('punkt') 
nltk.download('stopwords') 
# Input text - to summarize 
text = """Here's a step-by-step breakdown of the Latent Semantic Analysis (LSA) algorithm: 
Latent Semantic Analysis (LSA), also known as Latent Semantic Indexing (LSI), is a 
technique in natural language processing used to analyze relationships between a set of  
documents or terms. Summarize the text by extracting important sentences based on their 
similarity scores. 
 
Let's implement LSA for automatic text summarization using the gensim library in 
Python.""" 
 
# Step 1: Tokenize the text into sentences 
sentences = sent_tokenize(text) 
 
# Step 2: Preprocess the text 
stop_words = set(stopwords.words('english')) 
preprocessed_sentences = [] 
for sentence in sentences: 
    # Tokenize words 
    words = word_tokenize(sentence) 
    # Convert to lowercase and remove stopwords 
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in 
stop_words] 
    preprocessed_sentences.append(words) 
 
# Step 3: Create a dictionary and corpus 
dictionary = corpora.Dictionary(preprocessed_sentences) 
corpus = [dictionary.doc2bow(sentence) for sentence in preprocessed_sentences] 
 
# Step 4: Apply SVD to reduce dimensionality 
lsa_model = models.LsiModel(corpus, id2word=dictionary, num_topics=2)  # We choose 2 
topics for simplicity 
 
# Step 5: Get the document-topic matrix 
document_topic_matrix = lsa_model[corpus] 
 
# Step 6: Compute similarity scores for sentences 
similarity_scores = [] 
for i, sentence in enumerate(sentences): 
    vec_bow = dictionary.doc2bow(preprocessed_sentences[i]) 
    vec_lsa = lsa_model[vec_bow] 
    # Compute similarity score as the length of the vector projection onto the first two topics 
    similarity_score = np.sqrt(np.sum(np.array([val[1] ** 2 for val in vec_lsa]) ** 2)) 
    similarity_scores.append((sentence, similarity_score)) 
 
# Step 7: Summarize the text based on similarity scores 
sorted_sentences = sorted(similarity_scores, key=lambda x: x[1], reverse=True) 
summary_length = min(3, len(sorted_sentences))  # Choose the top 3 sentences as summary 
summary = " ".join([sentence[0] for sentence in sorted_sentences[:summary_length]]) 
 
# Print the summary 
print("Summary:") 
print(summary)'''

def experiment_7():
    return '''import numpy as np 
 
def vectorize_terms(terms): 
    terms = [term.lower() for term in terms] 
    terms = [np.array(list(term)) for term in terms] 
    terms = [np.array([ord(char) for char in term]) 
                for term in terms] 
    return terms 
 
root = 'Believe' 
term1 = 'beleive' 
term2 = 'bargain' 
term3 = 'Elephant' 
 
terms = [root, term1, term2, term3] 
terms 
 
import pandas as pd 
 
# Character vectorization 
term_vectors = vectorize_terms(terms) 
 
# show vector representations 
vec_df = pd.DataFrame(term_vectors, index=terms) 
print(vec_df) 
root_term = root 
other_terms = [term1, term2, term3] 
root_term_vec = vec_df[vec_df.index == root_term].dropna(axis=1).values[0] 
other_term_vecs = [vec_df[vec_df.index == term].dropna(axis=1).values[0] 
                      for term in other_terms] 
 
def hamming_distance(u, v, norm=False): 
    if u.shape != v.shape: 
        raise ValueError('The vectors must have equal lengths.') 
    return (u != v).sum() if not norm else (u != v).mean() 
 
def manhattan_distance(u, v, norm=False): 
    if u.shape != v.shape: 
        raise ValueError('The vectors must have equal lengths.') 
    return abs(u - v).sum() if not norm else abs(u - v).mean() 
 
def euclidean_distance(u,v): 
    if u.shape != v.shape: 
        raise ValueError('The vectors must have equal lengths.') 
    distance = np.sqrt(np.sum(np.square(u - v))) 
    return distance 
 
def cosine_distance(u, v): 
    distance = 1.0 - (np.dot(u, v) / (np.sqrt(sum(np.square(u))) * np.sqrt(sum(np.square(v)))) 
                     ) 
    return distance'''

def experiment_8():
    return '''z!pip install SpeechRecognition 
import speech_recognition as sr 
sr.__version__ 
r = sr.Recognizer() 
harvard = sr.AudioFile("/content/harvard.wav") #read audio file 
with harvard as source: 
  audio = r.record(source) #record it 
type(audio) 
try: 
  text = r.recognize_google(audio) #recognise 
  print("Recognized Speech:",text) 
except sr.UnknownValueError: 
  print("Speech recognition could not understand audio") 
except sr.RequestError as e: 
  print("Could not request results from Google Speech Recognition service; {0}".format(e))'''

def experiment_9():
    return '''!pip install pydub 
 
from pydub import AudioSegment 
 
# Load audio file 
audio = AudioSegment.from_file("/content/harvard.wav") 
 
# Convert to MP3 format 
audio.export("output_audio.mp3", format="mp3") 
print("Audio file converted to MP3 format.") 
 
# Extract part of the audio 
start_time = 5000  # Start time in milliseconds (5 seconds) 
end_time = 10000   # End time in milliseconds (10 seconds) 
extracted_audio = audio[start_time:end_time] 
 
# Export extracted audio to WAV format 
extracted_audio.export("extracted_audio.wav", format="wav") 
print("Extracted audio saved as 'extracted_audio.wav'.") 
 
# Convert extracted audio to MP3 format 
extracted_audio.export("extracted_audio.mp3", format="mp3") 
print("Extracted Audio file converted to MP3 format.") 
 
# Adjust volume 
louder_audio = audio + 10  # Increase volume by 10 dB 
 
# Export louder audio to WAV format 
louder_audio.export("louder_audio.wav", format="wav") 
print("Louder audio saved as 'louder_audio.wav'.") 
 
# Convert louder audio to MP3 format 
louder_audio.export("louder_audio.mp3", format="mp3") 
print("Louder Audio file converted to MP3 format.")'''

def experiment_10():
    return '''import speech_recognition as sr  
def recognize_speech():  
# Initialize recognizer  
recognizer = sr.Recognizer()  
with sr.Microphone() as source:  
print("Listening...") 
# Adjust ambient noise for better recognition recognizer. 
adjust_for_ambient_noise(source)  
# Capture audio from the microphone  
audio_data = recognizer.listen(source) 
 print("Processing...")  
try: 
 # Use Google Web Speech API for speech recognition  
text = recognizer.recognize_google(audio_data)  
print("Recognized speech:", text)  
except sr.UnknownValueError:  
print("Sorry, I couldn't understand what you said.")  
except sr.RequestError as e:  
print("Error accessing Google Web Speech API:", e)  
if __name__ == "__main__":  
recognize_speech()'''

EXPERIMENTS = {
    1: experiment_1,
    2: experiment_2,
    3: experiment_3,
    4: experiment_4,
    5: experiment_5,
    6: experiment_6,
    7: experiment_7,
    8: experiment_8,
    9: experiment_9,
    10: experiment_10,
}
