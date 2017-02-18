def eval(x):
    if x=='thousand':
        return 't'
    elif x=='hundred':
        return 'h'
    elif x=='and':
        return ''
    else:
        if x[0]== 'z':
            return '0'
        elif x[0]=='o':
            return '1'
        elif x[0]=='t':
            if x[1]=='w':
                return '2'
            else:
                return '3'
        elif x[0]=='f':
            if x[1]=='o':
                return '4'
            else:
                return '5'
        elif x[0]=='s':
            if x[1]=='i':
                return '6'
            else:
                return '7'
        elif x[0]=='e':
            return '8'
        else:
            return '9'

f=open('/Users/megan/Code/code-golf-spring-2017/inputs/6.txt','r')
o = open('/Users/megan/Code/code-golf-spring-2017/answers/6.txt', 'w')
for line in f:
    res = ''
    sep = line.split()
    print sep
    for val in sep:
        v = val.split('-')
        if len(v)>1:
            res += eval(v[0])
            res += eval(v[1])
        else:
            res += eval(v[0])
    o.write(res + '\n')
