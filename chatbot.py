"""GreenCoin Guide: a rule based chatbot about cryptocurrencies.

The bot matches keywords in the question against a small set of rules and
answers from the data in crypto_db.py. There is no language model behind it.
"""

from crypto_db import crypto_db

HELP = (
    "I can answer questions about the coins I know: "
    + ", ".join(crypto_db)
    + ".\n"
    "Try asking about:\n"
    "  - which coin is most sustainable\n"
    "  - which coins are trending or rising\n"
    "  - what looks good for long-term growth\n"
    "  - a coin by name, for example 'tell me about Cardano'\n"
    "Type 'exit' to quit."
)


def most_sustainable():
    coin = max(crypto_db, key=lambda c: crypto_db[c]["sustainability_score"])
    score = crypto_db[coin]["sustainability_score"]
    return f"{coin} is the greenest choice, with a sustainability score of {score}/10."


def rising_coins():
    rising = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
    if not rising:
        return "None of the coins I know are rising at the moment."
    return "Coins on the rise: " + ", ".join(rising) + "."


def long_term_picks():
    picks = [
        c for c, info in crypto_db.items()
        if info["price_trend"] == "rising" and info["market_cap"] == "high"
    ]
    if not picks:
        return "Nothing I know of is both rising and large enough to call a long-term pick."
    return (
        ", ".join(picks)
        + " looks like a long-term option: the price is rising and the market cap is high."
    )


def describe(coin):
    info = crypto_db[coin]
    return (
        f"{coin}: price trend {info['price_trend']}, market cap {info['market_cap']}, "
        f"energy use {info['energy_use']}, sustainability {info['sustainability_score']}/10."
    )


def respond_to_query(user_query):
    """Return the bot's answer to one question as a string."""
    query = user_query.lower()

    if "help" in query or query.strip() == "":
        return HELP

    for coin in crypto_db:
        if coin.lower() in query:
            return describe(coin)

    if "sustainab" in query or "green" in query or "eco" in query:
        return most_sustainable()

    if "trend" in query or "rising" in query or "going up" in query:
        return rising_coins()

    if "long-term" in query or "long term" in query or "growth" in query:
        return long_term_picks()

    return "I do not have a rule for that yet. Type 'help' to see what I can answer."


def main():
    print("GreenCoin Guide. Type 'help' for what I can answer, 'exit' to quit.")
    while True:
        try:
            question = input("\nAsk GreenCoin: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if question.strip().lower() in ("exit", "quit"):
            print("Goodbye.")
            break
        print(respond_to_query(question))


if __name__ == "__main__":
    main()
