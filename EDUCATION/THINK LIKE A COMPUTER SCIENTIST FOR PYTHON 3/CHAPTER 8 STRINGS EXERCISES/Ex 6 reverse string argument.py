def reverse_string(text):
    
    """reverses string argument"""
    copy = ""# create an empty string
    ix = len(text)-1
  
    while ix >= 0:
        copy += text[ix]
        ix -= 1
    return copy
  
words = """blaze fire rain wood torment pain massacre list of words no chance but must win"""

print(reverse_string(words)) 
