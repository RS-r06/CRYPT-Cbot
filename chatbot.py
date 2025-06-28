from crypto_db import crypto_db

def respond_to_query(user_query):
    query = user_query.lower()

    if "sustainable" in query:
        coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"{coin} is the greenest choice 🌱 with a sustainability score of {crypto_db[coin]['sustainability_score']*10}/10.")
    
    elif "trending" in query or "rising" in query:
        rising = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
        print(f"📈 Coins on the rise: {', '.join(rising)}")
    
    elif "long-term" in query or "growth" in query:
        for coin, info in crypto_db.items():
            if info["price_trend"] == "rising" and info["market_cap"] == "high":
                print(f"{coin} looks like a great long-term play 🚀")

    else:
        print("I’m still training my circuits 🤖 Try asking about trends or sustainability.")

# Example run
while True:
    question = input("\nAsk CryptoBot: ")
    if question.lower() in ["exit", "quit"]:
        print("Goodbye! 🌟")
        break
    respond_to_query(question)