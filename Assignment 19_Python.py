#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Thing:
    pass
print(Thing) 
("""class'__main__.Thing'""")
example = Thing()
print(example)


# In[14]:


class Thing2:
    letters = 'abc'
    
print(Thing2.letters)


# In[15]:


class Thing3:
    def __init__(self):
        self.letters = 'xyz'


# In[39]:


print(Thing3.letters)


# In[40]:


something = Thing3()
print(something.letters)


# In[41]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
hydrogen = Element('Hydrogen', 'H', 1)


# In[19]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


# In[42]:


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}


# In[43]:


hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])


# In[44]:


hydrogen.name


# In[45]:


hydrogen = Element(**el_dict)
hydrogen.name


# In[46]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))
hydrogen = Element(**el_dict)
hydrogen.dump()


# In[47]:


print(hydrogen)


# In[48]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))

hydrogen = Element(**el_dict)
print(hydrogen)


# In[49]:


class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property    
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
hydrogen = Element('Hydrogen', 'H', 1)


# In[50]:


hydrogen.name


# In[51]:


hydrogen.symbol


# In[52]:


hydrogen.number


# In[53]:


class Bear:
    def eats(self):
        return 'berries'
    
class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'
    
b = Bear()
r = Rabbit()
o = Octothorpe()


# In[54]:


print(b.eats())


# In[55]:


print(r.eats())


# In[56]:


print(o.eats())


# In[57]:


class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'
    
class SmartPhone:
    def does(self):
        return 'ring'
    
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
        
    def does(self):
        return '''I have many attachments:
        My laser, to %s.
        My claw, to %s.
        My smartphone, to %s.''' % (self.laser.does(),self.claw.does(),self.smartphone.does() )


# In[58]:


robbie = Robot()


# In[59]:


print( robbie.does())


# In[ ]:




