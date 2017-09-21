def mirror_string(text):
    
    """mirrors string argument"""
    copy = text  # create a copy of the original text
    ix = len(text)-1
  
    while ix >= 0:
        copy += text[ix]
        ix -= 1
    return copy
  
words = """blaze fire rain wood torment pain massacre list of words no chance but must win"""

print(mirror_string('a')) 
