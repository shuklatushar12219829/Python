import re
txt="Hello World worllld"
x=re.findall("l{1,3}",txt)
print(x)

txt="He.llo.World"
x=re.search("\.",txt)#lost the importance of meta character
print(x)