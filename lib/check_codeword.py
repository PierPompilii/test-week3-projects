def check_codework(codework):
    if codework == "horse":
        return "Correct! Come in."
    elif codework[0] == "h" and codework[-1] == "e":
        return "Close, but nope."
    else:
        return "WRONG!"