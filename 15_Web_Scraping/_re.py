import re

result = dir(re)

#re modeule

str = "Python is fun. Yes I'm sure it is Python."

# result = re.findall("Python", str)
# result = len(result)

# result = re.split(" ", str)
# result = re.split("y", str)

# "/s" means blank space
result = re.sub(" ", "_", str)
result = re.sub("\s", ".", str)

print(result)