import re

text = "Hi there you here exa_mple@example.com some more text email@email.de"

# Find emails in text

pattern = re.compile("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

# Find URLs in text

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

# Find IP addresses in text

pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

matches = pattern.findall(text)

print(matches)

################ Meta Characters ################

# [] A set of characters
# \ Signals a special sequence (can also be used to escape special characters)
# . Any character (except newline character)
# ^ Starts with
# $ Ends with
# * Zero or more occurrences
# + One or more occurrences
# {} Exactly the specified number of occurrences
# | Either or
# () Capture and group

################ Special Sequences ################

# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string

################ Sets ################

# [arn] Returns a match where one of the specified characters (a, r, or n) are present
# [a-n] Returns a match for any lower case character, alphabetically between a and n
# [^arn] Returns a match for any character EXCEPT a, r, and n
# [0123] Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9] Returns a match for any digit between 0 and 9
# [0-5][0-9] Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z] Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+] In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
