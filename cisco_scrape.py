import os
import smtplib
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the ChromeDriver location from an environment variable
chromedriver_loc = os.environ.get('CHROMEDRIVER_LOC')
if not chromedriver_loc:
    raise ValueError("CHROMEDRIVER_LOC environment variable not set.")

s = Service(chromedriver_loc)
driver = webdriver.Chrome(service=s)

# Navigate to the Cisco publication listing page
driver.get("https://sec.cloudapps.cisco.com/security/center/publicationListing.x")

# Wait for the element to be clickable, then click
try:
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/cdc-template/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/table/tbody[2]/tr[1]/td/table/tbody/tr[1]/td[1]/div/span[4]/a"))
    )
    element.click()
except Exception as e:
    print(f"Error: {e}")
    driver.quit()
    exit()

# Wait for the page to load completely
time.sleep(10)  # You can replace this with another WebDriverWait if needed

# Extract the product name
product_name = driver.find_element(By.XPATH, "/html/body/cdc-template/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]").text
print(f"Product Name: {product_name}")

# Extract the reporting date
reporting_date = driver.find_element(By.XPATH, "/html/body/cdc-template/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]").text
print(f"Reporting Date: {reporting_date}")

# Extract the version number
version_number = driver.find_element(By.XPATH, "/html/body/cdc-template/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div[1]").text
print(f"Version Number: {version_number}")

# Extract all Cisco Bug IDs and their associated links
bug_ids_elements = driver.find_elements(By.CSS_SELECTOR, "div.ddtsList div.bugDiv a")
bug_ids = [(bug.text, bug.get_attribute("href")) for bug in bug_ids_elements]
# Print the Bug IDs and their links
for bug_id, link in bug_ids:
    print(f"Bug ID: {bug_id}, Link: {link}")

# Extract the CVSS score
cvss_score = driver.find_element(By.XPATH, "/html/body/cdc-template/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[7]/div[2]/div/input").get_attribute("value")
print(f"CVSS Score: {cvss_score}")

subject = 'Cisco Security Advisory'
# Format the email content
email_content = f"""Subject: {subject} \n\n
Product Name: {product_name}
Reporting Date: {reporting_date}
Version Number: {version_number}
CVSS Score: {cvss_score}

Bug IDs and Links:
"""

for bug_id, link in bug_ids:
    email_content += f"{bug_id}: {link}\n"

# Retrieve email credentials and recipient from environment variables
sender_mail = os.environ.get('SENDER_MAIL')
sender_mail_password = os.environ.get('SENDER_MAIL_PASSWORD')
receiver_mail = os.environ.get('RECEIVER_MAIL')

# Check if the environment variables are loaded correctly
if not sender_mail or not sender_mail_password or not receiver_mail:
    raise ValueError("Email credentials or receiver email are not set in the environment variables.")

# Set up the SMTP server and send the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    # Log in to the email account
    server.login(sender_mail, sender_mail_password)

    # Send the email
    server.sendmail(sender_mail, receiver_mail, email_content)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    # Close the SMTP server
    server.quit()

# Close the browser
driver.quit()
