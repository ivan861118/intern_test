inputString1 = "junyiacademy"
inputString2 = "flipped class room is important"

def reverseAll(x):
    return(x[::-1])

    
def reverseEach(x):
    target = ""
    array=x.split(" ")
    for i in range(0,len(array)):
        array[i] = reverseAll(array[i])
        target+=array[i]
        target+=" "
    
    return target

a1 = reverseAll(inputString1)
#print(a1)

a2 = reverseEach(inputString2)
print(a2)