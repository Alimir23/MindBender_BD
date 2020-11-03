import re
from pydoop import hdfs



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
            
counts = sorted(counts.items(), key = 
             lambda kv:(kv[1], kv[0]))

print(counts)

with open('listfile.txt', 'w') as f:
    for listitem in counts:
        f.write("  ".join(str(s) for s in listitem) + '\n')


hdfs_path = "hdfs://localhost:9000/SPtext/PythonResult.txt"
hdfs.put("listfile.txt", hdfs_path)