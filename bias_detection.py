from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import webbrowser
import os

# Automatically installs & sets up ChromeDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Open website
url = "https://example.com"  # Change this to any site
driver.get(url)

# Extract text
time.sleep(3)  # Wait for page load
page_text = driver.find_element(By.TAG_NAME, "body").text

# Generate output HTML
html_content = f"""
<html>
<head>
    <title>Web Scraping Output</title>
    <style>
        body {{ font-family: Arial; margin: 40px; background: #f4f4f4; }}
        .container {{ max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 10px; }}
        h1 {{ color: #333; }}
        pre {{ background: #eee; padding: 15px; border-radius: 5px; white-space: pre-wrap; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Web Scraping Result</h1>
        <h3>Extracted Text:</h3>
        <pre>{page_text}</pre>
    </div>
</body>
</html>
"""

# Save & open in browser
output_file = "output.html"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(html_content)
webbrowser.open("file://" + os.path.abspath(output_file))

# Close driver
driver.quit()
