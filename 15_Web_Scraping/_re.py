import re

result = dir(re)

#re modeule

str = "Text strings are used in many different ways. A text string is enclosed in double quotes, and can contain any combination of letters, numbers, spaces, and punctuation. It can contain a \n to indicate a newline or \b to indicate a backspace, but otherwise cannot contain tabs or other control characters. If you want a double quote mark inside a string, it has to be preceded by a backslash, to indicate it is not ending the string"

# https://www.w3schools.com/python/python_regex.asp
# https://docs.python.org/3/library/re.html

# result = re.findall("Python", str)
# result = len(result)

# result = re.split(" ", str)
# result = re.split("y", str)

# "/s" means blank space

# result = re.sub(" ", "_", str)
# result = re.sub("\s", ".", str)

# result = re.search("Python", str)

# result = result.span()

# result = re.findall("[xyz]",str) 
# result = re.findall("[a-z]",str) 

# result = re.findall("[^abc]",str) #Except "abc"

# result = re.findall("...",str) #3 chracter
# result = re.findall("Lo..m",str)

# result = re.findall("^a", str) #if start "a" string
# result = re.findall("^t", str)

# result = re.findall("t$", str)

# result = re.findall("tes+t", str)
# result = re.findall("tes?t", str)

# result = re.findall("[0-9]{2}",str)

# result = re.findall("\BText", str)


print(result)