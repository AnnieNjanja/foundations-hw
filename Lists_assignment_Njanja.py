#!/usr/bin/env python
# coding: utf-8

# In[106]:


# The Blartle campaign received four donations:
# One of $45
# One of $78
# One of $230
# One of $2
# Save these in a variable named 'donations'
donations = [45, 78, 230, 2]


# In[107]:


# I forgot how many donations it was. Can you count them?
len(donations)


# In[108]:


# I'm the campaign manager for the Blartle campaign! How
# much money did we raise in total?

print(sum(donations),"$")


# In[109]:


# What were the largest and smallest donations?
# Print the sentences,
# "The largest donation was ____"
# "The minimum donation was ____"

print("The largest donation was", "$", max(donations))
print("The minimum donation was", "$", min(donations))


# In[110]:


# Why is it, for example, max(donations) and not donations.max()?
# What's the difference between the two?


# In[111]:


# Print out ONLY the first donation
print(donations[0])


# In[112]:


# When do we use [], when do we use (), when do we use {}?
# Why do we sometimes use some, and sometimes use others?

#() applies where functions like print are involved
#[] is for lists and indexing the list
#{} are easier to use when printing statements, they are better to use than print() especially where integers are involved


# In[113]:


# We need to write thank-you letters! Print out the
# sentences "Thank you for your donation of $____"
# for each of the donations

for donation in donations:
    print("Thank you for your donation of", "$", donation)


# In[114]:


# I'm the campaign manager again, and I want to make MORE MONEY.
# In each of the thank-you letters, also print whether 
# it was above or below the average donation
# you probably want to save the average donation in 
# a variable called 'average'

average = (sum(donations) / len(donations))
for donation in donations:
    if donation > average:
        print("Thank you for your donation of", "$", donation,",""your donation was above the average.")
    else: 
        print("Thank you for your donation of", "$", donation,"," "your donation was below the average.")
        


# In[ ]:





# In[121]:


# I still want more money, but we need to be more detailed if we
# are going to get it. Print out the thank-you letters one more
# time, but this time say something like "it was $4 above the average
# donation" or "It was $30 below the average donation"

for donation in donations:
    difference = (abs(donation - average))
      print("Thank you for your donation of", "$", donation, "your donation was", difference,"above the average.")
else: 
    print("Thank you for your donation of", "$", donation,"your donation was", difference,"below the average.")
        

