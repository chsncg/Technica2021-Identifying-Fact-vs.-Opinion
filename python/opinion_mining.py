from sentiment_analysis import sentiment_scores
import string

# dictionaries of opinion based and fact based words
opinion_words = {"least": -1, "greatest": -1, "best": -1, "worst": -1, "bigoted": -3, "conceited": -3, "highly": -2,
                 "aggressive": -2, "opinion": -2, "convinced": -1, "woefully": -3, "aplenty": -2, "despair": -2,
                 "righteous": -2, "bad": -3, "anger": -1, "blah": -4, "believed": -4, "believe": -4, "most": -2,
                 "good": -3, "disappointing": -4, "dubious": -4, "critically": -3, "presumably": -2, "noteworthy": -2,
                 "important": -3, "contempt": -3, "extreme": -3, "strained": -3, "blistering": -3, "claim": -2,
                 "favored": -2, "meaningful": -3, "behest": -3, "big": -2, "biggest": -2}

fact_words = {"testimony": 3, "information": 3, "declined": 2, "documents": 2, "before": 1, "during": 1,
              "former": 1, "later": 1, "politically": 3, "political": 3, "legally": 4, "legal": 4, "attorney": 3,
              "issued": 2, "evidence": 5, "investigator": 1, "investigators": 1, "present": 2, "received": 2,
              "results": 2, "result": 2, "informed": 3, "files": 1, "file": 1, "court": 2, "noted": 3, "official": 2,
              "officials": 2, "policy": 2, "records": 2, "record": 2, "sanction": 2, "sanctions": 2,
              "document": 2, "current": 3, "case": 1}


def mining(term):
    if term in opinion_words.keys():
        return opinion_words[term]
    elif term in fact_words.keys():
        return fact_words[term]
    else:
        return 0

def analyze_score(score):
    if score >= 10:
        return "fact-based"
    elif score <= -10:
        return "opinion-based"
    else:
        return "inconclusive"

def punctuation_removal(file):
    for line in file:
        for char in line:
            all_list = [char for char in line if char not in string.punctuation]

    clean_str = ''.join(all_list)

    return clean_str

def article_mine(article, analysis, source_score):
    for word in article.split():
        source_score += mining(word)

    analysis = analyze_score(source_score)

    print("This article is {}".format(analysis))

    if analysis == "opinion-based":
        sentiment_scores(article)

if __name__ == "__main__":

# ask user if they would like to input a CSV file or input text
    option = int(input("Press 1 if you want to submit a text file or press 2 to type your input: "))
    source_score = 0
    analysis = ''

    if option == 1:
        filename = input("Enter your text file name with the extension: ")

        with open(filename, 'r') as file:
            article = punctuation_removal(file)
        article_mine(article, analysis, source_score)

    elif option == 2:
        text = input("Enter text input to analyze: ")
        article = punctuation_removal(text)
        article_mine(article, analysis, source_score)

    else:
        option = input("Please enter a valid input: ")






