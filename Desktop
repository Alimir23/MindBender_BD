import re


counts = dict()


with open('/home/field/Desktop/Shakespeare.txt') as f:
    File = f.read().split()

    for items in File:
        
        items = items.lower()
        
        items = ''.join(re.findall
                        ('[a-zA-Z0-9@\s]+',items))
        
        if items in counts:
            counts[items] += 1
        else:
            counts[items] = 1
print(counts)        