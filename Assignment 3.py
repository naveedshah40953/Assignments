#!/usr/bin/env python
# coding: utf-8

# In[1]:



test_list = [ 1, 6, 3, 5, 3, 4 ] 
  
print("Checking if 4 exists in list ( using loop ) : ") 
  
# Checking if 4 exists in list  
# using loop 
for i in test_list: 
    if(i == 4) : 
        print ("Element Exists") 
  
print("Checking if 4 exists in list ( using in ) : ") 


# In[2]:


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


# In[3]:


my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))


# In[17]:


lst = [ 3, 6, 9, 12, 3, 30, 15, 9, 45, 36, 12, 12]
dupItems = []
uniqItems = {}
for x in lst:
   if x not in uniqItems:
      uniqItems[x] = 1
   else:
      if uniqItems[x] == 1:
         dupItems.append(x)
      uniqItems[x] += 1
print(dupItems)


# In[5]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)


# In[16]:


print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. power");
choice = int(input("Enter your choice: "));
if (choice>=1 and choice<=4):
    print("Enter two numbers: ");
    num1 = int(input());
    num2 = int(input());
    if choice == 1:
    	res = num1 + num2;
    	print("Result = ", res);
    elif choice == 2:
    	res = num1 - num2;
    	print("Result = ", res);
    elif choice == 3:
    	res = num1 * num2;
    	print("Result = ", res);
    elif choice == 4:
        res = num1 ** num2;
        print ("Resulty =",res)
    else:
    	res = num1 / num2;
        print("Result = ", res);
else:
    print("Wrong input..!!");


# In[ ]:





# In[ ]:




