"""
Jethro Ronald Lee
DS 2000
Homework 6
March 25, 2022
sentiment.py
"""

import matplotlib.pyplot as plt

REDDIT = "reddit.txt"

POS_COLOR = "forestgreen"
NEG_COLOR = "darkred"
NEUTRAL_COLOR = "yellow"

POS_LABEL = "Positive Comment"
NEG_LABEL = "Negative Comment"
NEUTRAL_LABEL = "Neutral Comment"

# Lists of calm/positive words and negative/worried words that are used to
# analyze the sentiment of a Reddit comment
POSITIVE = ["good", "happy", "relieved", "relief", "glad", "finally", "normal", 
            "excited", "proud", "well", "healthy", "lol", "great", "amazing", 
            "celebrate", "optimistic", "bliss", "soothing", "calm"]
NEGATIVE = ["bad", "angry", "frustrated", "stressed", "stress", "stupid", 
            "scared", "scary", "scaring", "hate", "hated", "annoying", 
            "annoyed", "tired", "disappointed", "lol", "afraid", "complain", 
            "pain", "trouble","concern", "concerns", "worry", "worries", 
            "crazy", "unfortunately", "concerning", "blood", "tough"]

def sentiment_score(comment, pos, neg):
    """
    Function: sentiment_score
    Parameters: comment (a string), list of positive words (strings), list of 
    negative words (strings)
    Returns: sentiment score (float between -1 and 1)
    """
    score = 0
    words = comment.split()
    
    for word in words:
        if word in pos:
            score += 1
        if word in neg:
            score -= 1
    
    return score / len(words)

def read_comments(filename):
    """
    Function: read_comments
    Parameter: filename, string
    Returns: list of strings, one per every 5th line in the file
    """
    comments = []
    
    with open(filename, "r", encoding = "utf-8") as infile:
        while True:
            community = infile.readline()
            username = infile.readline()
            points = infile.readline()
            timestamp = infile.readline()
            comment = infile.readline()
            blank_line = infile.readline()
            if not community:
                break
            comments.append(comment)
            
    return comments

def clean_string(input_st):
    """
    Function: clean_string
    Parameter: input string, a string
    Returns: cleaned up version of a string that is all lowercase and contains 
    no punctuation/numbers
    """
    output_str = ""
    
    for letter in input_st:
        if letter.isalpha() or letter == " ":
            output_str += letter.lower()
     
    return output_str

def categorize_scores(lst):
    """
    Function: categorize_scores
    Parameters: a list of sentiment scores (floats)
    Returns: A dict, where each key (str) indicates whether the values they 
    align w/ are scores for a certain sentiment or indices of the scores in the
    inputted list. The values are scores (floats) or indices (ints).
    """
    sent_dct = {"pos_ind": [], "pos_scores": [], "neg_ind": [], 
                "neg_scores": [], "neutral_ind": [], "neutral_scores": []}
 
    for i in range(len(lst)):
        if lst[i] > 0:
            sent_dct["pos_ind"].append(i)
            sent_dct["pos_scores"].append(lst[i])
        elif lst[i] < 0:
             sent_dct["neg_ind"].append(i)
             sent_dct["neg_scores"].append(lst[i])
        else:
             sent_dct["neutral_ind"].append(i)
             sent_dct["neutral_scores"].append(lst[i])
            
    return sent_dct

def plot_comment_data(sent_dct):
    """
    Function: plot_comment_data
    Parameter: A dict, where each key (str) indicates whether the values they  
    align w/ are certain sentiment scores or indices. The values are scores 
    (floats) or indices (ints).
    Returns: Nothing, just generates a plot (x-pos = indices, y-pos = scores)
    """     
    
    plt.scatter(sent_dct["pos_ind"], sent_dct["pos_scores"], color = POS_COLOR, 
                label = POS_LABEL)
    plt.scatter(sent_dct["neg_ind"], sent_dct["neg_scores"], color = NEG_COLOR, 
                label = NEG_LABEL)
    plt.scatter(sent_dct["neutral_ind"], sent_dct["neutral_scores"], 
                color = NEUTRAL_COLOR, label = NEUTRAL_LABEL)
    plt.title("Sentiment Scores for Comments in the NEU Subreddit About COVID")
    plt.xlabel("Comments From Oldest to Newest")
    plt.ylabel("Sentiment Score")
    plt.legend() 

def main():
    
    scores = []
    
    # Gathers the data in the file and saves the comments into a separate list
    comments = read_comments(REDDIT)
    
    # Cleans up every comment to remove punctuation and numbers and makes them  
    # all lowercase. Each comment is given a sentiment score.
    for comment in comments:
        clean = clean_string(comment)
        score = sentiment_score(clean, POSITIVE, NEGATIVE)
        scores.append(score)

    # Calculates and prints out the average sentiment score of all the comments
    avg_score = sum(scores) / len(scores)
    print("Average sentiment score of all comments:", avg_score)
    
    # Generates a plot that depicts the sentiment of each comment from oldest
    # to newest. The plot contains a title, axis labels, and a legend.
    scores.reverse()
    plot_dct = categorize_scores(scores)
    plot_comment_data(plot_dct)
   
main()