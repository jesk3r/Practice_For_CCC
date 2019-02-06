
# coding: utf-8

# In[120]:


squre = [input("Enter numbers: ").split(), input("Enter numbers: ").split(),input("Enter numbers: ").split() ,input("Enter numbers: ").split()]



# In[121]:


suml = lambda a,b,c : int(a[b][c]) + int(a[b][c+1]) + int(a[b][c+2]) + int(a[b][c+3])

sumd = lambda a,b,c : int(a[b][c]) +  int(a[b+1][c]) +  int(a[b+2][c]) +  int(a[b+3][c]) 


# In[122]:


r1 = suml(s,1,0)

sidesum = []
botsum = []


for i in range(0,4):
    sidesum.append(suml(squre,i,0))


for i in range(0,4):
    botsum.append(sumd(squre,0,i))


if sidesum == botsum:
    print("magic")
else:
    print("not magic")

