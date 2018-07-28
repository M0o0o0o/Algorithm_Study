while True : 
    a, b = map(int,input().split())
    if a + b == 0 :
        break
    result = 'factor'
    if a > b  :
        result = 'multiple'
        a, b = b, a
    
    index = 2 
    while True : 
        buf = a * index
        index += 1
        if buf == b : 
            break;
        elif buf > b  :
            result = 'neither'
            break
    print(result)
# 첫 번째 숫자가 두 번째 숫자의 약수이다. factor 
# 첫 번째 숫자가 두 번째 숫자의 배수이다. multiple
# 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다. neither
    


