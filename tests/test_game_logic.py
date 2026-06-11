from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    is_in_range,
    check_guess,
    get_hint_message,
    update_score,
)


# --- check_guess --------------------------------------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- get_range_for_difficulty ------------------------------------------

def test_ranges_per_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    # Unknown difficulty falls back to the default range
    assert get_range_for_difficulty("???") == (1, 100)


# --- parse_guess --------------------------------------------------------

def test_parse_valid_integer():
    assert parse_guess("42") == (True, 42, None)


def test_parse_decimal_truncates():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7


def test_parse_empty_and_none():
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess(None) == (False, None, "Enter a guess.")


def test_parse_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."


# --- is_in_range --------------------------------------------------------

def test_is_in_range():
    assert is_in_range(1, 1, 20) is True
    assert is_in_range(20, 1, 20) is True
    assert is_in_range(0, 1, 20) is False
    assert is_in_range(21, 1, 20) is False


# --- get_hint_message (direction must NOT be inverted) ------------------

def test_hint_directions():
    assert get_hint_message("Too High") == "📉 Go LOWER!"
    assert get_hint_message("Too Low") == "📈 Go HIGHER!"
    assert get_hint_message("Win") == "🎉 Correct!"


# --- update_score -------------------------------------------------------

def test_first_try_win_scores_100():
    assert update_score(0, "Win", attempt_number=1) == 100


def test_later_win_scores_less():
    assert update_score(0, "Win", attempt_number=3) == 80


def test_win_points_floor_at_10():
    assert update_score(0, "Win", attempt_number=20) == 10


def test_wrong_guess_penalizes_5():
    assert update_score(50, "Too High", attempt_number=2) == 45
    assert update_score(50, "Too Low", attempt_number=2) == 45
