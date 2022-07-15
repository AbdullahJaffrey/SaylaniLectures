def charcount(param):
    return len([i for i in param if i !=" "])


def spacecount(param1):
    return len([i for i in param1 if i ==" "])

def splitcount(param2):
    return len([i for i in param2.split(',')])

def totalcount1(param3):
    return len([i for i in param3.split(' ')])

def indexfinder(param4):
    return param4.find('Hello')

def wordfinder(string, wordfind):
#     string = input('Enter a line: ')
#     wordfind = input('Enter a word, you like to find: ')
      for i in string:
        if wordfind in string:
            return f" '{wordfind}' >> {True}"
        else:
            return f" '{wordfind}' >> {False}: Not found "
        
def splitcount(string1):
    return len([i for i in string1.split(',')])

def indexfinder(string, indexfind):
    for i in string:
        if indexfind in string:
            return f" '{indexfind} >> {string.find(indexfind)}'"
        else:
            return f" '{indexfind} >> Not found "
