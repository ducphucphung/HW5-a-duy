#Bài 2:
def symbol(n):
    dict1={')':'(', ']':'[', '}':'{'}
    list1=[ ]
    stt=True
    for i in n:
        if dict1.get(i) is not None and len(list1)!=0 and list1[-1]==dict1[i]:
            list1.pop()
        else:
            list1.append(i)
    return len(list1)==0
n=input("Nhập một chuỗi kí tự:")
print(symbol(n))
    
