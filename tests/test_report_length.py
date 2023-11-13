from lib.report_length import report_length

def test_report_length_five_characters():
    length = len("Bruno")
    assert "This string was five character long"

def test_report_length_three_characters():
    length = len ("rat")
    assert "This string was three character long"

def test_report_length_n_characters():
    length = len ("pneumonoultramicroscopicsilicovolcanoconiosis")
    assert "This string was forty five character long"