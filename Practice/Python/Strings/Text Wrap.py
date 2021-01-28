def wrap(string, max_width):
    lines = int(len(string)) / int(max_width)
    
    if lines.is_integer():
        lines = lines
        
    else:
        lines = int(lines) + 1

    i = 0
    MW = max_width
    
    for _ in range(lines-1):
        print(string[i:MW])
        i += max_width
        MW += max_width

    return string[i:MW]


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
