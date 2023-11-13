from lib.check_codeword import check_codework

def test_check_codeword_correct():
    result = check_codework("horse")
    assert result == "Correct! Come in."

def test_check_codeword_close():
    result = check_codework("hise")
    assert result == "Close, but nope."

def test_check_codeword_wrong():
    result = check_codework("zebra")
    assert result == "WRONG!"
