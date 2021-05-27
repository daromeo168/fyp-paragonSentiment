import tokenize

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.classify import NaiveBayesClassifier
import pandas as pd
from textblob import TextBlob, classifiers
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, session
from collections import Counter
import gspread
from oauth2client.service_account import ServiceAccountCredentials


import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)



scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('googleDriveCredential/DataFYP-f9b4cc069a54.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('CSV-to-Google-Sheet')

sheetid = '1-axN2JfkmJc18DsmIW120PMZ6on-omMVUaRHdH6qHjM'


df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheetid}/export?format=csv')

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

def balancingScore(value, object):
    badSentiment = ["expensive", "dirty", "pricey", "issue"]

    for negativeSentiment in badSentiment:
        for verbinG in object.words:#tokenizing
            if negativeSentiment == verbinG:
                value = value - 0.05
                if "not" + negativeSentiment:
                    value = value + 0.1

    if value == 0:
        return "Neutral " + str(value)

    if value < 0:
        return "Negative " + str(value)

    if value > 0:
        return "Positive " + str(value)
secure_sent = 0
def isSecurity(wordSecurity):
    parkingBox = ["car", "parking", "moto", "motocycle", "bike", "park", "parking lot", "guard", "bodyguard", "security", "camera", "vehicle", "Loss and found", "found"]

    for gem in parkingBox:
        if gem in wordSecurity.lower():
            return True
tuition_sent = 0
def isTuition(bitPrice):
    feeBox = ["school price", "tuition", "school payment","school" + "fee" ]
    for dols in feeBox:
        if dols in bitPrice.lower():
            return True
cant_sent = 0
def ratingCanteen(numbs):
    if numbs == "1":
        value = -0.9

        return value
    if numbs == "2":
        value = -0.4

        return value
    if numbs == "3":
        value = 0.0

        return value
    if numbs == "4":
        value = 0.4

        return value
    if numbs == "5":
        value = 0.9

        return value
env_sent = 0
def isEnvironment(facilitiy):

    facilBoxy = ["hall", "library", "classroom", "clean", "dirty", "atmosphere", "air", "hot", "cold", "conference", "toilet", "garden", "scenary", "computerhall", "environment"]
    for sameSame in facilBoxy:
        if sameSame in facilitiy.lower():
            return True
service_sent = 0
def isService(service):

    serviceBox = ["receptionist ", "behavior", "service", "borrowing", "reserving"]

    for something in serviceBox:
        if something in service.lower():
            return True

#
# def isSecurity(wordSecurity):
#     if "security" in wordSecurity.lower():
#         return True
#
#     if "camera" in wordSecurity.lower():
#         return True
#
#     if "body guard" in wordSecurity.lower():
#         return True


def sentiment_result(value):

    if value == 0:
        return "Neutral"
    if value < 0:
        return "Negative"
    if value > 0:
        return "Positive"

negative_point = 0
Neutral_point = 0
positive_point = 0



for phrase in df['TextDataReview']:
    manjiGang = TextBlob(phrase)
    poleRate = ["1", "2", "3", "4", "5"]

    word = 0
    for ratingSession in poleRate:
        # Supporting the Pole
        if phrase == ratingSession:
            print("Sentiment Point: " + str(ratingCanteen(phrase)))
            print("Sentence: Poll review for canteen => :" + phrase)
            print("Polarity result: " + sentiment_result(ratingCanteen(phrase)))
            print("\n")
            cant_sent += 1
            if sentiment_result(ratingCanteen(phrase)) == "Positive":
                positive_point += 1
            if sentiment_result(ratingCanteen(phrase)) == "Negative":
                negative_point += 1
            if sentiment_result(ratingCanteen(phrase)) == "Neutral":
                Neutral_point += 1



    # Regular data
    if phrase != "1":
        if phrase != "2":
            if phrase != "3":
                if phrase != "4":
                    if phrase != "5":
                        print("Sentiment point:  " + str(manjiGang.sentiment.polarity))
                        print("Sentence :" + phrase)
                        print("Polarity result: " + sentiment_result(manjiGang.sentiment.polarity))
                        print("\n")
                        if sentiment_result(manjiGang.sentiment.polarity) == "Positive":
                            positive_point += 1
                        #     pos neg neu of each cate guidance
                        #     if isService(phrase) == True:
                        #         pos_service_sent += 1
                        #
                        #     if isTuition(phrase) == True:
                        #         pos_tuition_sent += 1
                        #
                        #     if isSecurity(phrase) == True:
                        #         pos_secure_sent += 1
                        #
                        #     if isEnvironment(phrase) == True:
                        #         pos_env_sent += 1
                        if sentiment_result(manjiGang.sentiment.polarity) == "Negative":
                            negative_point += 1
                        if sentiment_result(manjiGang.sentiment.polarity) == "Neutral":
                            Neutral_point += 1

                        if isService(phrase) == True:
                            service_sent += 1

                        if isTuition(phrase) == True:
                            tuition_sent += 1

                        if isSecurity(phrase) == True:
                            secure_sent += 1

                        if isEnvironment(phrase) == True:
                            env_sent += 1




print("Service ========> " + str(service_sent))
print("tuition ========> " + str(tuition_sent))
print("Security ========> " + str(secure_sent))
print("Environment ========> " + str(env_sent))
print("canteen ========> " + str(cant_sent))

print(service_sent + tuition_sent + secure_sent + env_sent + cant_sent)

total_sen = 0

for something in df['TextDataReview']:
    total_sen+=1

print(total_sen)


word_COUNT = []
superior = ['the', 'is', 'i', 'to', 'for', 'and', 'it', 'good', 'it', 'or','for']



all_words = Counter(' '.join(df['TextDataReview']).lower().split()).most_common(20)



print(all_words)
print(all_words[9:10])








@app.route("/")
def hello():
    return render_template('index.html', total_sen=total_sen, neg_p=negative_point, pos_p=positive_point, neut_p=Neutral_point)

# RUNING SERVER ON LOCAL HOST ##
if __name__ == '__main__':
    app.run(debug=True)












        # "if k == "True":
        #     print("Non-English word detected in the sentence")
        # else:
        #     print(create_word_features(testimonial.words))




# someA = TextBlob("room is not dirty but omygood")
# print(balancingScore(someA.sentiment.polarity, someA))
#
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
