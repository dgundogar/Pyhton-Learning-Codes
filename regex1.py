import re

def is_valid(cc):
    
    if re.match('[4-6]\d{3}(-?)\d{4}\\1\d{4}\\1\d{4}$',cc)and not re.search('(\d)-?\\1-?\\1-?\\1',cc):
        return True
    else: return False

for _ in range (int(input())):
    cc=input()
    if is_valid(cc)==True:
        print("Valid")
    else:
        print("Invalid")