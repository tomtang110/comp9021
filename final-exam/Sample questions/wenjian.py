import re
with open('word_search_1.txt') as file1:
    a = []
    ab = re.compile(r'\w+')
    for each in file1:
        abc = ab.findall(each)
        ac = ''.join(abc)
        a.append(ac)
print(a)





