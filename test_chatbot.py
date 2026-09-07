from chatbot import respond_to_query


def test_sustainable_picks_highest_score():
    answer = respond_to_query("Which coin is the most sustainable?")
    assert answer.startswith("Cardano")
    assert "8/10" in answer


def test_trending_lists_rising_coins():
    answer = respond_to_query("what is trending right now")
    assert "Bitcoin" in answer
    assert "Cardano" in answer
    assert "Ethereum" not in answer


def test_long_term_needs_rising_and_high_cap():
    answer = respond_to_query("anything good for long-term growth?")
    assert answer.startswith("Bitcoin")


def test_coin_name_gives_its_profile():
    answer = respond_to_query("tell me about ethereum")
    assert answer.startswith("Ethereum:")
    assert "stable" in answer


def test_unknown_question_points_to_help():
    answer = respond_to_query("what is the weather like")
    assert "help" in answer


def test_help_lists_the_coins():
    answer = respond_to_query("help")
    for coin in ("Bitcoin", "Ethereum", "Cardano"):
        assert coin in answer
