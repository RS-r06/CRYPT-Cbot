# GreenCoin Guide

A terminal chatbot that answers beginner questions about cryptocurrencies and
suggests coins by price trend and energy use.

The bot is rule based. It matches keywords in your question against a small
set of rules and looks the answer up in a local dataset. There is no machine
learning behind it.

## Who it is for

Beginners who want a simple starting point on which coins are rising and which
use less energy. The coin data is a small fixed sample, not live market data,
so it is not financial advice.

## How to run it

```bash
python chatbot.py
```

Python only, nothing to install. Type `help` to see what it answers and
`exit` to quit. A session looks like this:

```
Ask GreenCoin: which coin is most sustainable?
Cardano is the greenest choice, with a sustainability score of 8/10.

Ask GreenCoin: what is trending
Coins on the rise: Bitcoin, Cardano.

Ask GreenCoin: tell me about Cardano
Cardano: price trend rising, market cap medium, energy use low, sustainability 8/10.

Ask GreenCoin: what is the weather
I do not have a rule for that yet. Type 'help' to see what I can answer.
```

To run the tests:

```bash
pip install pytest
pytest
```

## What I built

- A keyword matcher that picks one rule per question
- Rules for the greenest coin, rising coins, long term picks and a
  description of one coin by name
- A coin dataset in `crypto_db.py` with price trend, market cap, energy use
  and a sustainability score
- Six pytest tests: one for each rule, the help text and the fallback answer

## What I learned

[FILL IN: two or three sentences in your own words. For example: where keyword
matching breaks (try "which coin uses the least power?"), why a question can
only hit one rule, or how returning strings instead of printing made the bot
testable.]

## Author

Rehumile Sechele, rehumiles@gmail.com
