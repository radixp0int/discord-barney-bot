import discord
import os
from dotenv import load_dotenv
import pandas_datareader as web
import random

client = discord.Client()

load_dotenv()

TOKEN = os.getenv('TOKEN')

quotes = [
    "Haaaaave you met Ted?",
    "Think of me as Yoda. Only instead of being little and green, I wear suits and I'm awesome. I'm your bro. I'm Broda.",
    "Whenever I’m sad, I stop being sad and be awesome instead.",
    "I realized that I’m searching, searching for what I really want in life. And you know what? I have absolutely no idea what that is.",
    "A lie is just a great story that someone ruined with the truth.",
    "The three-day rule is a childish, manipulative mind game. But yeah, you wait three days.",
    "Every Halloween, I bring a spare costume, in case I strike out with the hottest girl at the party. That way, I have a second chance to make a first impression.",
    "I finally found the one, Marshall. Her name is Bacon.",
    "Believe it or not, I was not always as awesome as I am today."
]


def get_stock_price(ticker):
    data = web.DataReader(ticker, "yahoo")
    return data['Close'].iloc[-1]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$barney':
        await message.channel.send(f"{quotes[random.randint(0, len(quotes) - 1)]}")

    if message.content.startswith("$price"):
        if len(message.content.split(' ')) == 2:
            ticker = message.content.split(" ")[1]
            price = "{:,.2f}".format(get_stock_price(ticker))
            await message.channel.send(f"Stock price of {ticker} is ${price}!")


@client.event
async def on_connect():
    print("Bot connected to the server!")


client.run(TOKEN)
