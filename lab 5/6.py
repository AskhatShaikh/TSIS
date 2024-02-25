import re

txt = "asjsdj.,.dfud,sd.vjhd kcb,d,nsds,jbv"

x = re.sub("[ ]|[,]|[.]" ,":",txt)

print(x)