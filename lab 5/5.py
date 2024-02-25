import re

# Test string
test_string = "a followed by anything b"

# Match pattern
b = re.match(r'a.*b$', test_string)

print(b)
    