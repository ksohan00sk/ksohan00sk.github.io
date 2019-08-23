import string
fhand = open('saga.txt')
counts = dict()
print('sam dsuza')
for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
           if word not in counts:
                counts[word] = 1
           else:
                counts[word] += 1     
