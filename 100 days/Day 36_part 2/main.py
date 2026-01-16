import requests
from bs4 import BeautifulSoup
import lxml

# 1. Product URL
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# 2. Headers (to avoid Amazon captcha)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=headers, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

price = None

# Amazon may show price in different elements
price_selectors = [
    "span.a-price > span.a-offscreen",   # most common
    "span#priceblock_ourprice",
    "span#priceblock_dealprice",
    "span#priceblock_saleprice",
]

for selector in price_selectors:
    element = soup.select_one(selector)
    if element:
        price_text = element.get_text().strip()
        # Remove currency symbol and commas, then convert to float
        price = float(price_text.replace("$", "").replace(",", ""))
        break

TARGET_PRICE = 90.0  # set your desired alert price
EMAIL_ADDRESS = "marvel123@gmail.com"
EMAIL_PASSWORD = "vcxn-ghtd-rtuc-tura"  # use app password, not normal password
RECEIVER_EMAIL = "marvel123@gmail.com"

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if price is not None:
    print(f"Current product price: ${price}")

    # Send email alert if price drops below target
    if price <= TARGET_PRICE:
        subject = "Amazon Price Alert 🚨"
        body = f"The price has dropped!

Current Price: ${price}
Target Price: ${TARGET_PRICE}

Product Link:
{URL}"

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            connection.send_message(msg)

        print("Email alert sent successfully!")
else:
    print("Price not found. Amazon may have returned a captcha or changed the page structure.")
