import re

txt = "jsbdbhdvabblfhdgdnabbb"

x = re.search("abb|abbb",txt)

print(x)