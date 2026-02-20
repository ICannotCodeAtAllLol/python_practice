def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    if n < 1:
        return "Argument must be an integer greater than 0."
    l = []
    for i in range(1, n+1):
        l.append(i)
    return " ".join(map(str, l))


number_pattern(1)