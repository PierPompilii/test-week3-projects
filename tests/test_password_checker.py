from lib.password_checker import *

def password_checker_is_true():
    passwordchecker = PasswordChecker()
    passwordchecker.check("abcdefgh")
    assert True

def password_checker_not_True():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check ("abcde")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
