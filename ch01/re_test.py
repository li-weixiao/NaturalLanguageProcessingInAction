import re

r = "(hi|hello|hey)[ ]*([a-z]*)"
print(re.match(r, "Hello Rosa", flags=re.IGNORECASE))

re_greeting = re.compile(r, flags=re.IGNORECASE)

my_names = set(['rosa', 'rose'])
curt_names = set(['you', 'u'])
greeter_name = ''
match = re_greeting.match("hello rosa") # match = re_greeting.match(input())

if match:
    at_name = match.groups()[-1]
    if at_name in curt_names:
        print("Good one.")
    elif at_name.lower() in my_names:
        print("Hi {}, How are you?".format(greeter_name))



from collections import Counter

print(Counter("Hello boy and gril, Hello everyone".split()))
