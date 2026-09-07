# The coin data the bot answers from.
#
# price_trend: "rising", "stable" or "falling"
# market_cap:  "high", "medium" or "low"
# energy_use:  "high", "medium" or "low"
# sustainability_score: 0 to 10, higher is greener

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3,
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6,
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8,
    },
}
