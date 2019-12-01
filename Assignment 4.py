#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Question Number 1
info={"First_name":"Naveed",
      "Last_name":"Shah",
      "Age":22,
      "City":"Quetta"
    
}
print([info])
info["Qualification"]="Bs"
print([info])
info["Qualification"]="High acadmic level"
print([info])
del info["Qualification"]
print([info])


# In[22]:


#Question 2
Cities={"Quetta":{"Country Name":"Pakistan",
                  "Population":"1 million",
                  "Fact":"City of Clouds"
                 } ,
        "Karachi":{"Country Name":"Pakistan",
                  "Population":"15 million",
                  "Fact":"City of Lights"} ,
        "Lahore":{"Country Name":"Pakistan",
                  "Population":"11 million",
                  "Fact":"City of Dishes"        
        } 
    
}
print([Cities ["Quetta"]])
print([Cities["Karachi"]])
print([Cities["Lahore"]])


# In[37]:


#Question 3


list=[0]
for i in list:
    Age=int(input("Enter your age ? \n"))
    if Age>0 and Age <3:
        print("Ticket is free")
    elif Age>=3 and Age<=12:
        print("Ticket Cost is 10 $")
    else:
        print("Ticket Cost is 15 $")


# In[43]:


#Question 4
def favorite_book(title):
    book_name=title
    print("One of my favorite book is "+""+ book_name)


favorite_book("Emotional Intellegence")


# In[1]:


#Question 5

import random
Random=random.choice([1,2,3,4,5,6,7,8,9])
list1=[0,1,2]             
for a_list in list1:
    number=int(input("Guss the number we have in list betwwen 1 and 9 \n You Have only 3 chances \n"))
    if number == Random:
        print("Your Number Matched")
        break;
    else :
        print("\n Try Again \n")
        if number> Random:
            print("Put a smaller input than that you have entered \n")
        else:
            print("Put a Greater input than that you have entered \n")
        
      


# In[ ]:





# In[ ]:




