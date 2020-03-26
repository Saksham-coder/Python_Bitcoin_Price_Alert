import requests
from datetime import datetime
import time

TICKER_API_URL = 'https://blockchain.info/ticker'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/bitcoin_price_update/n6JpNvUIxgXNd0oO9iVrB7Oi5-ovR73XzcT5gSFeD02'

BITCOIN_PRICE_THRESHOLD = 10000

# In this function , the API returns a JSON response, we can convert it to a Python object by calling the .json() function on the response.
def get_latest_crypto_price( url='https://blockchain.info/ticker'):
    response = requests.get(url)
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json['INR']['last'])
#if you print it you will get latest bitcoin price and you can select bitcoin or litecoin.
#print(get_latest_crypto_price())

#in this post_ifttt_webhook function payload will be sent to ifttt service and this will insert our desired event and finally it sends a HTTP POST request to the webhook URL.
def post_ifttt_webhook(event,value):
  data = {'value1': value}
  ifttt_event_url= 'https://maker.ifttt.com/trigger/bitcoin_price_update/with/key/n6JpNvUIxgXNd0oO9iVrB7Oi5-ovR73XzcT5gSFeD02'.format(event)
  requests.post(ifttt_event_url, json=data)

#It takes the bitcoin_history as an argument and formats it using some of the basic HTML tags allowed by Telegram, like <br>, <b>, <i>
def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        # Formats the date into a string: '24.02.2018 15:09'
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M') 
        price = bitcoin_price['price']
        # <b> (bold) tag creates bolded text
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)
        # Use a <br> (break) tag to create a new line
    return '<br>'.join(rows)

def main():
    bitcoin_history = []
    while True:
        price = get_latest_crypto_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})
        # Send an emergency notification
        if int(price) > BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)
        # Send a Telegram notification or it can also send notification in your preferred selected event.I have linked this to telegram and phone android sms notification.
        if len(bitcoin_history) == 5: 
            # Once we have 5 items in our bitcoin_history send an update
            post_ifttt_webhook('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            # Reset the history
            bitcoin_history = []
        # Sleep for 5 minutes 
        time.sleep(5 * 60)
        

if __name__ == '__main__':
    main()