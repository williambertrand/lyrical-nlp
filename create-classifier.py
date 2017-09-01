from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from nltk.corpus import stopwords

# Load the list of (english) stop-words from nltk
stop_words = stopwords.words("english")
