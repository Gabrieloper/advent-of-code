from day_2 import evaluate_num, parse_file_ids


def test_evaluate_nums():
    assert evaluate_num(11) == 11
    assert evaluate_num(22) == 22
    assert evaluate_num(99) == 99
    assert evaluate_num(1010) == 1010
    assert evaluate_num(1188511885) == 1188511885
    assert evaluate_num(222222) == 222222
    assert evaluate_num(446446) == 446446
    assert evaluate_num(446446) == 446446
    assert evaluate_num(38593859) == 38593859


def test_parse_file_ids():
    assert parse_file_ids("11-22") == 33
    assert parse_file_ids("95-115") == 99
    assert parse_file_ids("998-1012") == 1010
    assert parse_file_ids("1188511880-1188511890") == 1188511885
    assert parse_file_ids("222220-222224") == 222222
    assert parse_file_ids("1698522-1698528") == 0
    assert parse_file_ids("446443-446449") == 446446
    assert parse_file_ids("38593856-38593862") == 38593859
