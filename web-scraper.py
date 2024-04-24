import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from statistics import mean

# Parses an amazon reviews page and performs a sentiment analysis on the reviews.  Then calculates the mean sentiment and gives it a rating out of 5.
# Am aware that you can just extract the rating out of 5 from the review data itself but this is just a fun exercise :) 

# Function to parse Amazon reviews page and extract text reviews.
def get_reviews(url):
	reviews = []
    # Send a GET request to the webpage
	headers = {
    "accept-language": "en-GB,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
}
	response = requests.get(url,headers=headers)
    
    # Check if the request was successful (status code 200)
	if response.status_code == 200:
        	# Parse the HTML content of the webpage
		soup = BeautifulSoup(response.text, 'html.parser')
		headings = soup.find_all('h1')
		review_elements = soup.select("div.review")        
        	# Print out the text content of each <h1> tag
		for review in review_elements:
			reviews.append(review.select_one("span.review-text").text)
		return reviews
	else:
		print(response.status_code)
		print("Failed to retrieve webpage")

def get_sentiments(reviews):
	sentiments = []
	for review in reviews:
		blob = TextBlob(review)
		sentiment = blob.sentiment.polarity
		sentiments.append(sentiment)
	print(mean(sentiments) * 2.5 + 2.5)

url = "https://www.amazon.co.uk/product-reviews/B08MFDT65P/ref=zg_bs_c_boost_d_sccl_2_cr/259-7320068-1582701?pd_rd_w=2Ozyt&content-id=amzn1.sym.3f9daf0e-df48-4e4c-9b03-d5dd85519204&pf_rd_p=3f9daf0e-df48-4e4c-9b03-d5dd85519204&pf_rd_r=FZ7G6PDM5SR4BZ7CASN8&pd_rd_wg=AZvco&pd_rd_r=b55e0cf7-bb44-431a-aecd-dedaf53f39f4&pd_rd_i=B08MFDT65P"

reviews = get_reviews(url)
get_sentiments(reviews)
