#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Question 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
        
        


# In[2]:


#Question 2
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('My Name is Naveed')


# In[5]:


#Questin 3
def fun():  
# list of numbers 
    list1 = [10, 21, 4, 45, 66, 93] 
  
    # iterating each number in list 
    for num in list1: 
      
    # checking condition 
        if num % 2 == 0: 
               print(num, end = " ")
                
fun()                


# In[6]:


#Question 4
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza')) 


# In[7]:


#Question 5
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))


# In[ ]:




