import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.classify import NaiveBayesClassifier
import pandas as pd
from textblob import TextBlob, classifiers
from nltk.corpus import stopwords



df = pd.read_csv('data/dataPa.csv')

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

# def remove_noise(tweet_tokens, stop_words = ()):
#
#     cleaned_tokens = []
#
#     for token, tag in pos_tag(tweet_tokens):
#         token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
#                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
#         token = re.sub("(@[A-Za-z0-9_]+)","", token)


def isService(service):
    if "receptionist" in service:
        return True


def isSecurity(wordSecurity):
    if "security" in wordSecurity.lower():
        return True

    if "camera" in wordSecurity.lower():
        return True

    if "body guard" in wordSecurity.lower():
        return True


def sentiment_result(value):
    if value == 0:
        return "Neutral"
    if value < 0:
        return "Negative"
    if value > 0:
        return "Positive"


for phrase in df['TextDataReview']:
    testimonial = TextBlob(phrase)
    print("Sentence :" + phrase)
    print("Polarity result: " + sentiment_result(testimonial.sentiment.polarity))
    print("Is it in security Field ? :" + str(isSecurity(phrase)) + "\n")





        # "if k == "True":
        #     print("Non-English word detected in the sentence")
        # else:
        #     print(create_word_features(testimonial.words))

# someA = TextBlob("It is beautiful at the parking lot but it is still a mess full of trashes and bad environment")
# print(sentiment_result(someA.sentiment.polarity))






# training = [
# ('I think there are a lot food court or restaurant nearby that just have much better menu than our school canteen.','negative'),
# ('It is not so great to fit in a small room without air','negative'),
# ('The Dark Knight Rises is the greatest superhero movie ever!','positive'),
# ('Fantastic Four should have never been made.','positive'),
# ('Wes Anderson is my favorite director!','positive'),
# ('Captain America 2 is pretty awesome.','positive'),
# ('The security guard did not know what they are doing despite taking a huge amount of salary ','negative'),
# ]
# testing = [
# ('Superman was never an interesting character.','pos'),
# ('Fantastic Mr Fox is an awesome film!','neg'),
# ('Dragonball Evolution is simply terrible!!','pos')
# ]
# classifier = classifiers.NaiveBayesClassifier(training)
# print (classifier.accuracy(testing))
#
#
# blob = TextBlob('the guard did not pay attention to anything beside sitting down and play phone', classifier=classifier)
# print (classifier.accuracy(blob))


# Money = TextBlob("")
# print(sentiment_result(Money.sentiment.polarity))
# print(Money.sentiment.polarity)



# print(" We got our polarity with result: " + str(testimonial.sentiment.polarity))
