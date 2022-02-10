# Without str.strip().
def trim(s):
    if s:
        i = 0
        j = -1
        while s[i] == ' ' and i < len(s)-1:
            i += 1
        if s[i] == ' ' and i == len(s)-1:
            return ''
        while s[j] == ' ':
            j -= 1
        return (s[i:j+1] if j != -1 else s[i:])
    else:
        return s


# test:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
