import re

r = "(hi|hello|hey)[ ]*([a-z]*)"
print(re.match(r, "Hello Rosa", flags=re.IGNORECASE))
