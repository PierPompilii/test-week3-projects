from lib.gratitudes import *

def test_gratitudes_Joy():
    gratitudes = Gratitudes()
    gratitudes.add("joy")
    Res = gratitudes.format()
    assert Res == "Be grateful for:joy"

def test_gratitudes_Joy_Happines():
    gratitudes = Gratitudes()
    gratitudes.add ("joy")
    gratitudes.add ("happines")
    res = gratitudes.format()
    assert res == "Be grateful for:joy, happines"
