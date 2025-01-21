# Install necessary libraries
!pip install sumy

from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lsa import LsaSummarizer
import csv

# Step 1: Import a list of URLs from a text file
with open('urls.txt') as f:
    urls = [line.strip() for line in f]

results = []

# Step 2: Analyze the content of each URL and generate meta descriptions
for url in urls:
    parser = HtmlParser.from_url(url, Tokenizer("english"))
    stemmer = Stemmer("english")
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words("english")
    description = summarizer(parser.document, 3)
    description = " ".join([sentence._text for sentence in description])
    if len(description) > 155:
        description = description[:152] + '...'
    results.append({
        'url': url,
        'description': description
    })

# Step 4: Export the results to a CSV file
with open('results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['url','description'])
    writer.writeheader()
    writer.writerows(results)