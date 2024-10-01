from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Make sure to download the correct WebDriver version
driver.get("https://www.humanbenchmark.com/tests/typing")

# Wait for the page to load
time.sleep(3)

# Find the element that holds the text to type
text_element = driver.find_element(By.CLASS_NAME, "challenge-text")
text_to_type = text_element.text

# Find the input field where text should be entered
input_field = driver.find_element(By.TAG_NAME, "input")

# Function to simulate typing with adjustable speed
def type_like_human(text, input_field, delay=0.05):
    for char in text:
        input_field.send_keys(char)
        time.sleep(delay)

# Start typing
type_like_human(text_to_type, input_field)

# You can wait and close the browser
time.sleep(10)  # Give time to observe the result
driver.quit()

