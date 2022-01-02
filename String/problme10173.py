# https://www.acmicpc.net/problem/10173

while True : 
    string =  input()
    if string == 'EOI' : break
    print("Found" if "nemo" in string.lower() else "Missing")