from src.day_one import TrebCalibrator


# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

def test_get_digit_from_line():

    line_one = "1abc2"
    line_two = "pqr3stu8vwx"
    treb = TrebCalibrator
    assert treb.get_digit_from_line(line_one) == "1"
    assert treb.get_digit_from_line(line_two) == "3"

