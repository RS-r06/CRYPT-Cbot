# GreenCoin Guide

A terminal chatbot that answers beginner questions about cryptocurrencies and
suggests coins based on two things: price trend and energy use.

The bot is rule based. It matches keywords in what you type against a small set
of rules and looks the answer up in a local dataset. There is no machine
learning model behind it.

## What it does

- Reads a typed question and picks the rule that matches it
- Looks up coins in a local dataset of price trend, market cap, energy use and
  a sustainability score
- Recommends coins for growth, for sustainability, or describes one coin by name
- Answers in conversation until you type `exit`

## Built with

Python only. The coin data sits in `crypto_db.py`. Nothing to install.

## How to run it

```bash
python chatbot.py
```

A session looks like this:

```
Ask GreenCoin: which coin is most sustainable?
Cardano is the greenest choice, with a sustainability score of 8/10.

Ask GreenCoin: what is trending
Coins on the rise: Bitcoin, Cardano.

Ask GreenCoin: anything for long-term growth
Bitcoin looks like a long-term option: the price is rising and the market cap is high.

Ask GreenCoin: tell me about Cardano
Cardano: price trend rising, market cap medium, energy use low, sustainability 8/10.

Ask GreenCoin: what is the weather
I do not have a rule for that yet. Type 'help' to see what I can answer.
```

## Tests

```bash
pip install pytest
pytest
```

Six tests cover each rule and the fallback for a question the bot has no rule
for.

## What I learned

Keyword matching breaks as soon as a question does not contain the word the
rule expects. "Which coin uses the least power?" gets the fallback answer even
though the data can answer it, because the rule looks for "sustainable",
"green" or "eco". Each new phrasing needs a new keyword, which does not scale.
The other limit is that a question can only hit one rule, so "sustainable coins
that are rising" answers the sustainability half and ignores the rest.

The first version printed its answers straight from the matching function.
Making it return a string instead is what made the tests possible.

## Author

Rehumile Masego Sechele, rehumiles@gmail.com
