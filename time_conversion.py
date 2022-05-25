s = "07:05:45PM"

if 'AM' in s:
    s = s.replace('AM', '')
    s = s.split(':')
    if s[0] == '12':
        s[0] = '00'
    s = ':'.join(s)
elif 'PM' in s:
    s = s.replace('PM', '')
    s = s.split(':')
    if s[0] != '12':
        s[0] = str(int(s[0]) + 12)
    s = ':'.join(s)
        
print(s)