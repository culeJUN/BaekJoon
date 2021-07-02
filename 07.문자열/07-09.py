def two(i, s) :
    if s[i] + s[i + 1] in word :
        return 1
    else :
        return 0

def three(i, s) :
    if s[i] + s[i + 1] + s[i + 2] in word :
        return 1
    else :
        return 0

s = input()
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
i = 0

while True :    
    if i + 2 < len(s) :
        if three(i,s) :
            count += 1
            i += 3
        elif two(i, s) :
            count += 1
            i += 2
        else :
            count += 1
            i += 1

    elif i + 1 < len(s) :
        if two(i, s) :
            count += 1
            i += 2
        else :
            count += 1
            i += 1

    else :
        count += 1
        i += 1

    if i == len(s) :
        print(count)
        break


