# --------------
#Code starts here
def reverse(inp):
    rev = inp[::-1]
    return rev

def is_palindrome(number):
    input_str = str(number)

    input_rev = reverse(input_str)
    if input_rev == input_str:
        return True
    else:
        return False

def palindrome(num):
    palind = False

    while not palind:
        num += 1
        a = is_palindrome(num)
        if a==True:
            palind=True
            return num
        else:
            continue

a = palindrome(145)
print(a)



    



# --------------
#Code starts here
def a_scramble(str_1, str_2):
    list_1 = [i for i in str_1.lower()]
    list_2 = [i for i in str_2.lower()]

    if len(list_2)>len(list_1):
        return False
    else:
        match = False
        for i in list_2:
            if i in list_1:
                index_1 = list_1.index(i)
                del list_1[index_1]
                match= True
            else:
                match = False
                return False
        if match==True:
            return True

a_scramble("Tom Marvolo Riddle","Voldemort")


# --------------
#Code starts here
def check_fib(num):
    fib=[0,1] # first two fibonacci number

    if num<0:
        return False
    elif num<=1:
        return True
    else:
        while fib[-1]<num:
            for i in range(len(fib)-1, len(fib)):
                fib.append(fib[i] + fib[i-1])
    
    if num in fib:
        return True
    else:
        return False

print(check_fib(145))
print(check_fib(377))


# --------------
#Code starts here
def compress(word):
    list_1 = [i for i in word.lower()]
    list_count=[]
    last_char = None
    index = 0

    for i in list_1:
        count = 0
        if last_char==i:
            pass
        else:
            for j in range(index, len(list_1)):
                if i==list_1[j]:
                    count+=1
                    index+=1
                    if index >= len(list_1):
                        list_count.append(i)
                        list_count.append(str(count))
                else:
                    list_count.append(i)
                    list_count.append(str(count))
                    last_char = i
                    count=0
                    break

    return "".join(list_count)


print(compress('abbs'))
print(compress("xxcccdex"))



# --------------
#Code starts here
def k_distinct(string,k):
    list_1 = [i for i in string.lower()]
    list_2 = []

    for i in list_1:
        if i not in list_2:
            list_2.append(i)
        
    if k==len(list_2):
        return True
    else:
        return False

print(k_distinct('Messoptamia',8))
print(k_distinct('banana',4))


