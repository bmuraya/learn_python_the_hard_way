formatter = "{} {} {} {}"

print (formatter.format ("one", "two", "three", "four"))
print (formatter.format (True, False, False, True))
print (formatter.format(formatter, formatter, formatter, formatter))
print (formatter.format(
    "try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))