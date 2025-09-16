from seasons import date_in_words
from seasons import parse_date
from datetime import date
def test_date_in_words():
    assert date_in_words(date(1995,1,1)) == "Fifteen million, nine hundred ninety-four thousand eighty minutes"
    assert date_in_words(date(2000,1,1)) == "Thirteen million, three hundred sixty-four thousand, six hundred forty minutes"

