from bug3_logic import find_max


def test_max_is_first():
    assert find_max([95, 85, 70, 60]) == 95


def test_max_is_middle():
    assert find_max([10, 30, 20]) == 30


def test_max_is_last():
    assert find_max([10, 20, 30]) == 30


def test_single_score():
    assert find_max([42]) == 42
