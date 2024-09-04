
# Vulnerability Reporter

This script automates the process of scraping security advisories from Cisco's website and sending the extracted information via email. It uses Selenium for web scraping and `smtplib` for sending emails.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)

## Prerequisites

Before you can use this script, ensure that you have the following installed on your system:

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your version of Chrome)
- pip (Python package installer)

You will also need the following Python packages:

- `selenium`
- `requests`
- `python-dotenv`

## Installation

1. **Clone the Repository or Download the Script**:

   ```bash
   git clone https://github.com/skitkat/vuln_reporter.git
   cd vuln_reporter
   ```

2. **Install the Required Python Packages**:

   Install the necessary packages by running:

   ```bash
   pip install selenium python-dotenv requests
   ```

3. **Download ChromeDriver**:

   - Download ChromeDriver from the official website: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).
   - Ensure the version of ChromeDriver matches your version of Google Chrome.
   - Extract the `chromedriver` executable to a known location.

## Setup

1. **Create a `.env` File Inside the Same Folder**:

   In the project root directory, create a file named `.env` with the following content:

   ```plaintext
   CHROMEDRIVER_LOC="C:/path/to/your/chromedriver.exe"
   SENDER_MAIL="your-email@gmail.com"
   SENDER_MAIL_PASSWORD="your-email-password"
   RECEIVER_MAIL="recipient-email@example.com"
   ```

   - Replace `C:/path/to/your/chromedriver.exe` with the actual path to your `chromedriver` executable.
   - Replace `your-email@gmail.com` with your sender email address.
   - Replace `your-email-password` with your email account's password (consider using an app-specific password if using Gmail).
   - Replace `recipient-email@example.com` with the recipient's email address.

2. **Verify Environment Variables**:

   Make sure all environment variables are correctly set in the `.env` file. These will be loaded automatically by the script using the `python-dotenv` package.

## Usage

1. **Run the Script**:

   Execute the script by running:

   ```bash
   python cisco_scrape.py
   ```

   The script will:
   - Navigate to the Cisco publication listing page.
   - Extract relevant information such as product name, reporting date, version number, and bug IDs.
   - Send the extracted information via email to the specified recipient.

2. **Check the Output**:

   - The script will print the extracted information in the terminal/console.
   - If the email is sent successfully, a confirmation message will be printed.
   - The browser window will close automatically after execution.

