from lib.string_builder import *

def test_string_empty():
    stringbuilder = StringBuilder()
    assert stringbuilder.output() == ""

def test_string_builder():
    stringbuilder = StringBuilder()
    stringbuilder.add ("house")
    assert stringbuilder.size() == 5
    assert stringbuilder.output() == "house"

def test_string_builder_more():
    stringbuilder = StringBuilder()
    stringbuilder.add ("house")
    stringbuilder.add(" ")
    stringbuilder.add ("of")
    stringbuilder.add(" ")
    stringbuilder.add ("dragon")
    assert stringbuilder.size () == 15
    assert stringbuilder.output() == "house of dragon"


