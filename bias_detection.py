from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from textblob import TextBlob
import time

# Setup Selenium WebDriver (Make sure to update the path to chromedriver)
service = Service("/path/to/chromedriver")  # Change this to the correct path
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no browser window)
driver = webdriver.Chrome(service=service, options=options)

# Function to extract text from a webpage
def get_webpage_text(url):
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    return driver.find_element(By.TAG_NAME, "body").text

# Function to analyze bias using TextBlob
def analyze_bias(text):
    analysis = TextBlob(text)
    subjectivity = analysis.sentiment.subjectivity  # High subjectivity indicates potential bias
    return subjectivity

# Test with a news website
url = "https://www.bbc.com/news"
print(f"Extracting text from: {url}")
text = get_webpage_text(url)
bias_score = analyze_bias(text)

print(f"Bias Score (0 = Objective, 1 = Highly Biased): {bias_score}")

# Close the browser
driver.quit()
