def remove_and_split(string , word):
    newstr = string.replace (word ,"")
    return newstr.strip()
 
a = "        Hassaan is a noob programer   " 
n = remove_and_split(a , "noob")
print(n)