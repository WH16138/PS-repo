import re
input()
s = input()
cnt = 0
if not re.search('[!@#$%^&*()-+]',s):cnt+=1
if not re.search('[a-z]',s):cnt+=1
if not re.search('[A-Z]',s):cnt+=1
if not re.search('[0-9]',s):cnt+=1 
print(max(6-len(s),cnt))