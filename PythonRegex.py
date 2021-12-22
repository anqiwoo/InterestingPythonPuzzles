import re
s = 'xyyy xyy xy x'
print(re.findall('xy?', s))
print(re.findall('xy*', s))
print(re.findall('xy+', s))

'''
Takeaway:
? means zero or one occurrences of the preceding character.
* means zero or more occurrences of the preceding character.
+ means one or more occurrences of the preceding character.

Three Regex are all greedy: they grab as many as they can lay their hands on.
'''
