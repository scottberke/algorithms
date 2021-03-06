# O(n!) where n is string
def string_perms(string, res, base=''):
    if not string:
        res.append(base)
    for i in range(len(string)):
        string_perms(string[:i] + string[i+1:], res, base + string[i])
    return res



# def string_perms(string, res, l, base=''):
#     if len(base) == l:
#         res.append(base)
#     for i in range(len(string)):
#         string_perms(string[:i] + string[i+1:], res, l, base + string[i])
#     return res
