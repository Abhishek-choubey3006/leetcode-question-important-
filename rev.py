# nalindome

from collections import Counter


def palindrome(x):
    return (str(x)==str(x)[::-1])

# print(palindrome(121))

def Monotype(arr):
    increasing = decreasing = True
    for i in range(len(arr)):
        if arr[i]>arr[i-1]:
            decreasing = False
        elif arr[i]<arr[i-1]:
            increasing = True
        
    return increasing or decreasing

# arr = [0]
# print(Monotype(arr))

def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sums = nums[i] + nums[j]
            if sums == target:
                return i , j


# nums = [1,2,3,4,5,6,7,8]
# target = 5
# print(twosum(nums,target))

def concat(nums):
    z = []
    for i in range(1,len(nums)+1):
        z.append(i)
    return nums + z
# nums = [1,2,3,4,5,6,7,8,9]
# print(concat(nums))

def power(x,n):
    if n == 0:
        return 0
    if n==1:
        return x
    elif n<0:
        x = 1//x
        n = -n
    
    else:
        res = 1
        while n>0:
            if n%2==1:
                res *= x

            n *= n
            x //= 2
        return res
    
# print(pow(2,3))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=0
        b =1
        for i in range(0,n):
            print(a)
            c = a+b
            a=b
            b=c
            
# print(fib(5))

# reverse

def reverse(n):
    l = n.split()
    # l1 = l[::-1]
    z = []
    for i in range(len(l)):
        z.append(l[::-1])
    return z

# print(reverse("Abhishek is good Boy"))

def rev(n):
    l = n.split()
    l1 = l[::-1]
    return " ".join(l1)

# print(rev("Abhishek is good Boy"))


# maximum product of three number in the array

def maxx(nums):
    nums.sort()
    l = nums[-1] * nums[-2] * nums[-3]
    m = nums[0] * nums[1] * nums[-1]
    return max(l,m)
# nums = [1,3,4,5,2,6,7,3]
# print(max(nums))

def perfectsquqre(num):
    n=0
    while (n*n)<=num:
        n += 1
        sqrt = n-1
    
        if (sqrt*sqrt) == num:
            return sqrt
        

# print(perfectsquqre(16))


# running sum 1D Array

def runningsum(arr):
    z = 0
    for i in arr:
        z += i

    return z
# arr = [1,2,3,4,5,6]
# print(runningsum(arr))
        

 

def lastWord(s):
    return len(s.split()[-1])

# s1 = " Good Mornig Abhishek"
# print(lastWord(s1))


def addDigit(num):
    while num>9:
        sum = 0
        while num:
            sum += num%10
            num = num//10
        num = sum
    return num

# print(addDigit(38))

def remove1(nums,val):
    if len(nums)==0:
        return
    else:
        for val in nums:
            nums.remove(val)

        return nums
nums = [5,5,1,2,3,4,5,6,7,89,8,7,6,2,1]
val = 4
# print(remove1(nums,val))

def dublicate(num):
    i = len(nums)-1
    while i>0:
        if num[i]==num[i-1]:
            return num.pop(i)
            
        i = i-1
# nums = [5,5,1,2,3,4,5,6,7,89,8,7,6,2,2,1]
# print(dublicate(nums))


def s(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1,len(list)):
            if list[min]>list[j]:
                min = j
            list[i] , list[min]=list[min],list[i]
            
    return list



# list = [2,5,3,6,3,78,4,9,5,89,43,2]
# print(s(list))

    
# sort color -- Bubble Sort

def sortcolor(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
               
    return list


def sortcolor2(list):
    low = 0
    mid = 0
    high = len(list)-1
    while mid <= high:
        if list[mid] == 0:
            list[low],list[mid]=list[mid],list[low]
            low +=1
            mid +=1
        elif list[mid]==1:
            mid +=1
        else:
            list[mid],list[high] = list[high],list[mid]

            high -=1
    return list


l = [2,0,2,1,1,0]
# print(sortcolor2(l))

def reverse3(s):
    l = s.split()[::-1]
    print(" ".join(l))
    a = []
    for i in l:
        a.append(i[::-1])
    return " ".join(a)

str = "welcome to codeing section"
# section codeing to welcome
# noitces gniedoc ot emoclew


# to find middle of the linked list
def middle(self,head):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# remove value from the list
def remove(num,val):
    while val in num:
        num.remove(val)
    return num
l = [1,2,3,4,5,5]
val = 3
# print(remove(l,val))

# remove dublicate from the list

def dublicate(num):
    i = len(num)-1
    while i>0:
        if num[i]==num[i-1]:

            num.pop(i)
        i =i-1
    return num
# print(dublicate(l))

    
def deletemiddleoflinkedlist(head):
    prev = slow = fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head
# solution is done in the linkedlist section




       
def movezeros(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[j] == 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        if nums[j] != 0:
            j+=1
    return nums

list = [1,2,0,3,6,0,4,8,0,3,8,0]
# print(movezeros(list))

        


s = "abcd"
t = "abcde"
def differnce(t,s):
    sum_t = sum_s = 0
    for c in t:
        sum_t += ord(c)
    for c in s:
        sum_s += ord(c)
    # return chr(sum_t - sum_s)
    # 1.hashmap
    # count_t = Counter(t)
    # count_s = Counter(s)
    # for c in count_t:
    #     if c not in count_s:
    #         return c
    #     if count_s[c] < count_t[c]:
    #         return c

    # 2. Ascii value
    # sum_s = sum_t = 0
    # for c in s:
    #     sum_s += ord(c)
    # for c in t:
    #     sum_t += ord(c)
    # return chr(sum_t-sum_s)
    # 3.bitwise manipulation
    # res = 0
    # for c in s:
    #     res = res^ord(c)
    # for c in t:
    #     res = res^ord(c)
    # return chr(res) 
# print(differnce(t,s))

def powerfour(n):
    if n==1:
        return True
    elif n<=0 or n%4 != 0:
        return False
    else:
        return powerfour(n//4)
# print(powerfour(64))
    
def powerthree(n):
    if n == 1:
        return True
    elif n<=0 or n%3 != 0:
        return False
    else:
        return powerthree(n//3)
# print(powerthree(10))
    
def powertwo(n):
    if n == 1:
        return True
    elif n<=0 or n%2 != 0:
        return False
    else:
        return powertwo(n//2)
# print(powertwo(403))


def topower(n,exp):
    if exp == 0:
        return n
    
    else:
        return n ** exp
# print(topower(2,6))

# rotate the array
def rotateArray(arr,k):
    k = k%len(arr)
    l = 0
    r = len(arr)-1
    while l<r:
        arr[l],arr[r]= arr[r],arr[l]
        l+=1
        r-=1
    l = 0
    r = k-1
    while l<r:
        arr[l],arr[r]= arr[r],arr[l]
        l+=1
        r-=1
    l = k 
    r = len(arr)-1
    while l<r:
        arr[l],arr[r]= arr[r],arr[l]
        l+=1
        r-=1
    return arr

arr = [1,2,3,4,5,6,7,2]
k = 2
# print(rotateArray(arr,k))


# delete middle node
class Node:
    def __init__(self,value):

        self.value = value
        self.next = None
class ll:
    def __init__(self):
        self.head = None
        self.tail = None

    
    

    def printing(self):
        if self.head is None:
            print("it is null")
        else:
            while self.head is not None:
                print(self.head.value,end="-->")
                self.head = self.head.next
        


        
    def push(self,value):
        noe = Node(value)
        noe.next = self.head
        self.head = noe

    def remove(self):
        prev = slow = fast = self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return self.head
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    
    def removeNnodelast(self,n):
        if self.head is None:
            return "Emtpy"
        slow = fast = self.head
        for i in range(n):
            fast = fast.next
            if not fast:
                return self.head.next
            
        while fast.next:
            
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head
    
    def retrunlastnode(self,n):
        fast=slow = self.head
        for i in range(n):
            fast = fast.next
        if not fast:
            return self.head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow.value


    def removedublicate(self):
        cur = self.head
        while cur:
            while cur.next.value == cur.value:
                cur.next = cur.next.next
            cur= cur.next
        return self.head



l = ll()
l.push(1)
l.push(2)
l.push(3)
l.push(21)
l.push(31)
l.push(41)
l.push(51)
l.push(4)
l.push(1)
# print(l.retrunlastnode(1))
# l.reverse()/
# l.removeNnodelast(4)
# print(l.removedublicate())
# print(l.printing())

def dublicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
# print(dublicate(arr))


class stack:
    update = ''
    def __init__(self):
        
        self.list = []

    def isempty(self):
        return self.list == []
    
    def push(self,value):
        return self.list.append(value)

    def pop(self):
        return self.list.pop()
    def get(self):
        return self.list
   
    def reverse_string(self,s):
        for i in range(len(s)):
            self.push(s[i])

        while not(len(self.get())==0):
            self.update += self.pop()
        return self.update

            
s ="Abhishek"
s1 = stack()
# print(s1.reverse_string(s))



# / tribonacci series

def tribonacci(n):
    a=0
    b=0
    c=1
    for i in range(0,n+1):
        d = a+b+c
        a=b
        b=c
        c = d
    return a
# print(tribonacci(5),end="-->")
arr = [1,2,1]
def findublicate(arr):
    i = len(arr)-1
    while i>0:
        if arr[i]==arr[i-1]:
            arr.remove(i)
        i-=1
    return arr
# print(findublicate(arr))



def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        a = b 
        b = c
    return a
# print(fibonacci(8))

def search2d(nums,target):
    for i in range(len(nums)):
       
        if nums[i]== target:
            return True
        
    return False
   
    
nums = [1,2,34,5,6,7]
target = 32
# print(search2d(nums,target))


# leetcode find the differnce of the string 
def diff(s,t):
    S = T = 0
    for i in s:
        S = S + ord(i)
    for i in t:
        T= T + ord(i)
    return chr(S-T)

s = "abced"
t = "abcd"
# print(diff(s,t))



