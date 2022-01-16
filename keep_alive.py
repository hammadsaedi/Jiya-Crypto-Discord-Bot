from flask import Flask
from threading import Thread

app = Flask('crypto bot')

@app.route('/', methods=['GET'])
def home():
  res = """
  <h2 style="font-weight: 400;"><strong>Crypto Currency Trading Group Help Discord Bot</strong></h2>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong>Submitted by:</strong></p>
<p style="font-weight: 400;">Hammad Saeedi                     FA21-BCS-023</p>
<p style="font-weight: 400;">Fasiha Arshad                         FA21-BCS-020</p>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong>Submitted to:</strong></p>
<p style="font-weight: 400;">Mr. Umar Iqbal</p>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong>Source Code:</strong></p>
<ul>
<li style="font-weight: 400;"><strong>Replit:</strong></li>
</ul>
<p style="font-weight: 400;"><strong><a href="https://replit.com/@fasad/Discord-Bot" data-saferedirecturl="https://www.google.com/url?q=https://replit.com/@fasad/Discord-Bot&amp;source=gmail&amp;ust=1642407796629000&amp;usg=AOvVaw0WwJbFtTDISwpm6xXBoz83">https://replit.com/@fasad/Discord-Bot</a> </strong></p>
<p style="font-weight: 400;"><em> </em></p>
<p style="font-weight: 400;"><strong><u>Bot</u></strong></p>
<p style="font-weight: 400;"><strong>Discord:</strong></p>
<p style="font-weight: 400;">Discord is an instant messaging and digital distribution platform. Users communicate with voice calls, video calls, text messaging, media and files in private chats or as part of communities called "servers".</p>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong>Crypto Currencies:</strong></p>
<p style="font-weight: 400;">Cryptocurrency is digital money that is secured by blockchain technology. Cryptocurrency investing can take many forms, ranging from buying cryptocurrency directly to investing in crypto funds and companies. You can buy cryptocurrency using a crypto exchange or through certain broker-dealers.</p>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong>Real Time Price Fetching:</strong></p>
<p style="font-weight: 400;">System is built to fetch real time crypto currency prices in python script, for this purpose coin market cap API is used. Price is then sent to Discord server upon user request, for this purpose Discord API is being used.</p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong><u>Tool and Technologies</u></strong></p>
<p style="font-weight: 400;"><strong>Python:</strong></p>
<p style="font-weight: 400;">Python is an interpreted high-level general-purpose programming language. Whole scripting is supposed to be done in Python 3.10.</p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong>Discord:</strong></p>
<p style="font-weight: 400;">Discord is an instant messaging and digital distribution platform. Users communicate with voice calls, video calls, text messaging, media and files in private chats or as part of communities called "servers".</p>
<ul>
<li style="font-weight: 400;"><strong>Discord API:</strong></li>
</ul>
<p style="font-weight: 400;">Discord Developers options provide facility to develop a bot. It issues access tokens to interact within the script.</p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong>Repl.it:</strong></p>
<p style="font-weight: 400;">Replit, formerly Repl.it, is a San Francisco-based start-up and an online IDE. Its name comes from the acronym REPL, which stands for "read–evaluate–print loop".</p>
<ul>
<li style="font-weight: 400;"><strong>IDE:</strong></li>
</ul>
<p style="font-weight: 400;">Repl.it IDE is Cloud Based which provides a powerful Versions Control and Team Collaboration Environment.</p>
<ul>
<li style="font-weight: 400;"><strong>Data Base:</strong></li>
</ul>
<p style="font-weight: 400;">It provides a powerful and easily accessible Database. Project data is supposed to be stored within this Database.</p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong>Coin Market Cap:</strong></p>
<p style="font-weight: 400;">Coin Market Cap is the world's most-referenced price-tracking website for crypto assets in the rapidly growing cryptocurrency space.</p>
<ul>
<li style="font-weight: 400;"><strong>Coin Market Cap API:</strong></li>
</ul>
<p style="font-weight: 400;">Coin Market Cap Developer Python API is used to fetch real time crypto currency price in console. It is used for individual prices which depend upon United States Dollars. Data is updated after 60 seconds.</p>
<p style="font-weight: 400;"><strong> </strong></p>
<p style="font-weight: 400;"><strong>Binance:</strong></p>
<p style="font-weight: 400;">Binance is an online exchange where users can trade cryptocurrencies. It supports most commonly traded cryptocurrencies. Binance provides a crypto wallet for traders to store their electronic funds. The exchange also has supporting services for users to earn interest or transact using cryptocurrencies.</p>
<ul>
<li style="font-weight: 400;"><strong>Binance API:</strong></li>
</ul>
<p style="font-weight: 400;">Binance Developer Python API is used to fetch real time crypto currency price in the console. It is used for fetching prices depending upon trading pairs such as ETHBTC. Data is updated in milliseconds.</p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong>Python Requests:</strong></p>
<p style="font-weight: 400;">Requests is a HTTP library for the Python programming language. The goal of the project is to make HTTP requests simpler and more human-friendly. It will be used to fetch Data from the API.</p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong>JSON:</strong></p>
<p style="font-weight: 400;">JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays. It is a common data format with diverse uses in electronic data interchange, including that of web applications with servers. Data will be fetched in JSON format from Coin Market Cap API.</p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong>Flask:</strong></p>
<p style="font-weight: 400;">Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. Flask is used to set up server which run 24/7 with the help of <a href="http://replit.com/" data-saferedirecturl="https://www.google.com/url?q=http://replit.com&amp;source=gmail&amp;ust=1642407796629000&amp;usg=AOvVaw1EnoznXkKuQ1yWRYtpRZ33">replit.com</a></p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong>HTML:</strong></p>
<p style="font-weight: 400;">The Hyper Text Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript. Some tags of HTML are used to make good interaction with web server built by Flask.</p>
<p style="font-weight: 400;"> </p>
<p style="font-weight: 400;"><strong>Uptime Robot:</strong></p>
<p style="font-weight: 400;">Uptime Robot is a free tool used to monitor websites. It monitors websites every 5 minutes and alerts you if your sites are down. It will be used to double check the status of the bot.</p>
"""
  return res

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()