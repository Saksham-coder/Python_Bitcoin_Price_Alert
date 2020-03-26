Bitcoin Price Alert script.
[PYTHON]

Using the popular automation website IFTTT, create IFTTT applets,using Coinmarketcap API.

We’re going to create two IFTTT applets:

One for emergency notification when Bitcoin price falls under a certain threshold; and another for regular Telegram updates on the Bitcoin price.

Both will be triggered by our Python app which will consume the data from the Coinmarketcap API.

In our case, the trigger will be a webhook service provided by IFTTT. You can think of webhooks as “user-defined HTTP callbacks".

Our Python app will make an HTTP request to the webhook URL which will trigger an action. Now, this is the fun part—the action could be almost anything
 you want. IFTTT offers a multitude of actions(as i mentioned in the desc) like sending an email, updating a Google Spreadsheet and even calling your phone.

To use IFTTT you’ll first need to set up a new account and install their mobile app (if you want to receive phone notifications from your Python app).

Sending a Test IFTTT Notification Now we can move onto the IFTTT side of things. To use IFTTT you’ll first need to set up a new account and install their
 mobile app (if you want to receive phone notifications from your Python app). Once you set that up, we’re going to create a new IFTTT applet for testing 
purposes.

To see the documentation on how to use the IFTTT webhooks go to this page and click on the “Documentation” button in the top right corner.
 The documentation page contains the webhook URL and it looks like this:

https://maker.ifttt.com/trigger/{event}/with/key/{your-IFTTT-key}

You’ll need to substitute the {event} part with whatever name you gave, when you created the applet. The {your-IFTTT-key} part is already populated 
with your IFTTT key.

Creating IFTTT Applets

We need to create two new IFTTT applets: one for emergency Bitcoin price notifications and one for regular updates.

Emergency bitcoin price notification applet:
1.Choose the “webhooks” service and select the “Receive a web request” trigger
2.Name the event bitcoin_price_emergency
3.For the action select the “Notifications” service and select the “Send a rich notification from the IFTTT app” action
4.Give it a title, like “Bitcoin price emergency!”
5.Set the message to Bitcoin price is at ${{Value1}}. Buy or sell now! (we’ll return to the {{Value1}} part later on)
6.Create the action and finish setting up the applet

....

Regular price updates applet:

1.Again choose the “webhooks” service and select the “Receive a web request” trigger
2.Name the event bitcoin_price_update
3.For the action select the “Telegram” service and select the “Send message” action
4.Set the message text to: Latest bitcoin prices: {{Value1}}
5.Create the action and finish with the applet

Note: When creating this applet you will have to authorize the IFTTT Telegram bot.

in the main function. It will consist of a while True loop since we want our app to run forever. In the loop we will call the Coinmarketcap API to get the latest 
Bitcoin price and record the current date and time.

Based on the current price we will decide if we want to send an emergency notification. For our regular Telegram updates we will also append the current price
and date to a bitcoin_history list. Once the list reaches a certain number of items (e.g. 5) we will format the items, send the update to Telegram, and reset the
history for future updates.

[IMPORTANT]

An important thing is to avoid sending out requests too frequently, for two reasons:
-The Coinmarketcap API states that they update the data only once every 5 minutes, so there’s no point in reloading the latest pricing info more
 frequently than that.
-If your app sends too many requests to the Coinmarketcap API your IP might get banned or temporarily suspended. That is why we need to “go to sleep” 
(stop the execution of the loop) for at least 5 minutes before we get new data.