
import time
import smtplib

# Function to check the highest value of a symbol
def get_highest_value(symbol):
    # Replace this with your own logic to fetch the highest value of the symbol from an external data source
    # You can use APIs or any other method to retrieve the latest data
    highest_value=0

    if symbol=='btcusdt':
        highest_value = 30.0  # Placeholder value, replace with actual implementation
    return highest_value

# Function to send an email
def send_email(user_email, symbol, highest_value):
    # Replace this section with your own logic to send an email using your email service provider
    # Here's a basic example using smtplib
    subject = f"Highest value alert: {symbol}"
    message = f"The highest value of {symbol} is {highest_value}."
    from_address = "your_email@example.com"
    to_address = user_email

    # Connect to the SMTP server
    smtp_server = smtplib.SMTP("smtp.example.com", 587)  # Replace with your SMTP server details
    smtp_server.starttls()
    smtp_server.login("your_username", "your_password")  # Replace with your SMTP credentials

    # Compose and send the email
    email_body = f"Subject: {subject}\n\n{message}"
    smtp_server.sendmail(from_address, to_address, email_body)

    # Disconnect from the server
    smtp_server.quit()

# Example usage
user_email = "user@example.com"
symbols = ["btcusdt", "ethusdt"]
symbol_last_sent_time = {symbol: None for symbol in symbols}

while True:
    for symbol in symbols:
        highest_value = get_highest_value(symbol)

        # Check if the highest value exceeds a certain threshold
        if highest_value > 24.0 and (symbol_last_sent_time[symbol] is None or time.time() - symbol_last_sent_time[symbol] > 10):
            print(user_email, symbol, highest_value)
            symbol_last_sent_time[symbol] = time.time()

    # Wait for 1 second before checking again
    time.sleep(1)