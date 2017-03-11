
def count_substring(text,substring):
    """count how many times substring occurs in string text"""
    
    ix = 0
    count = 0
    
    while ix < (len(text)-1):
        if text.find(substring,ix) != -1:
            ix = text.find(substring,ix)+1 #+len(substring) version with +len(substring) omits repeated occurences within the substring itself i.e.: 'aaa' in 'aaaaaa' and counts only 2 for this example not 4
            count += 1
        elif text.find(substring,ix) == -1:
            break
            
    
    return count
    

print(count_substring('Mississippi','is'))
print(count_substring('lala land','la'))
print(count_substring('tututututututu','tu'))
print(count_substring('aaaaaa','aaa'))
