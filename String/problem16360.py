# https://www.acmicpc.net/problem/16360
dic = {
    'a' : 'as', 'i' : 'ios', 'y' : 'ios',
    'l' : 'les', 'n' : 'anes', 'ne' : 'anes',
    'o' : 'os', 'r' : 'res', 't' : 'tas', 'u' : 'us',
    'v' : 'ves', 'w' : 'was'
}

for _ in range(int(input())) : 
    s = input()
    ans = s 
    for k in dic.keys() : 
        if s[-len(k):] == k : 
            ans = ans[:len(ans)-len(k)] + dic[k]
            break
    if s == ans : 
        ans = ans + 'us'
    print(ans)