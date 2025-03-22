import csv
from textblob import TextBlob

# Define the sentiment analysis function
def classify_review(review):
    # Analyze the sentiment of the review using TextBlob
    blob = TextBlob(review)
    # Sentiment score ranges from -1 (very negative) to 1 (very positive)
    sentiment = blob.sentiment.polarity
    # Consider positive if sentiment > 0, negative otherwise
    return 1 if sentiment > 0 else 0

# Function to read review text from a CSV file
def process_review_from_csv(csv_filename, row_index=0):
    with open(csv_filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header
        for idx, row in enumerate(reader):
            if idx == row_index:
                review_text = row[7]  # Assuming the review text is in the 8th column (index 7)
                print(f"Review: {review_text}")
                classification = classify_review(review_text)
                return classification

# Usage example
csv_filename = '/home/arsenal/ml/Internshala/food_recomndation_restaurant/filtered_reviews_philadelphia.csv'
classification = process_review_from_csv(csv_filename, row_index=0)
print(f"Review classification: {classification}")  # 1 (positive) or 0 (negative)