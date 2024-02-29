import pyautogui
from time import sleep
import keyboard  # You need to install this package


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_click_position():
    """
    Waits for the user to press Enter and then returns the current mouse position.
    """
    print("Move the mouse to the desired click position and press Enter.")
    keyboard.wait('enter')  # Wait for Enter key to be pressed
    return pyautogui.position()

def click_and_screenshot(interval=1, duration=10):
    """
    Clicks on a specific screen position and takes a screenshot every `interval` seconds for `duration` seconds.
    
    Args:
    - interval (int): How often to take screenshots (in seconds).
    - duration (int): How long the script should run (in seconds).
    """
    click_position = get_click_position()  # Get the click position from the user
    end_time = time.time() + duration
    while time.time() < end_time:
        # Move the mouse to the specified position and click.
        pyautogui.click(click_position)
        
        # Take a screenshot and save it with a timestamp.
        screenshot_filename = f"screenshot_{int(time.time())}.png"
        pyautogui.screenshot(screenshot_filename)
        print(f"Screenshot taken: {screenshot_filename}")
        
        # Wait for the specified interval before the next iteration.
        time.sleep(interval)






# Setup the Chrome WebDriver
options = webdriver.FirefoxOptions()
# Add any necessary options here. For example, you might want to run headless.
# options.add_argument('--headless')

# Initialize the WebDriver
driver = webdriver.Firefox(options=options)

# Function to take a screenshot and save it
def take_screenshot(driver, page_number):
    driver.save_screenshot(f'screenshot_{page_number}.png')

# Open the initial page
driver.get('url') # Replace with your target URL

# Wait for the page to load
wait = WebDriverWait(driver, 10)
selector="#___nextPage"
input("press enter to continue!")


# Loop through pages and take screenshots
page_number = 90

while True:
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))) # Replace with your actual selector
    # Take screenshot
    take_screenshot(driver, page_number)

    # Find the 'Next' button using its CSS selector
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, selector) # Replace with your actual selector
    except NoSuchElementException:
        print("No 'Next' button found. Exiting.")
        break
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))) # Replace with your actual selector

    # Click the 'Next' button
    next_button.click()

    # Increment the page number
    page_number += 1
    
    # Wait for the next page to load before taking another screenshot
    time.sleep(4) # You might need to adjust this delay

    # You can also wait for a specific element on the next page to ensure it has loaded
    # wait.until(EC.presence_of_element_located((By.ID, "someElementIdOnNextPage")))



# Close the WebDriver
driver.quit()

#book-title