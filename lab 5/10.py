import re

def camel_to_snake(camel_case):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()

# Test the function
camel_string = "camelCaseString"
snake_string = camel_to_snake(camel_string)
print("Camel case:", camel_string)
print("Snake case:", snake_string)
