###Numeric
#int 
var=10



#float
var=3.14
print(type(var))


#complex
var=10+5j    #Real+imaginary
print(type(var))


###Text

#str
var="first bit solution"
var='first bit solution'
print(type(var))

var= """ This is my first line 
           my name is harshada"""
print(type(var))

###sequential
# list
var=[10,20,30,40,]

# tuple
var=(10,20,30,40)
var=10,20,30,40

#rang
var=range(1,100)

## settype
#set
var={10,20,30,40}

# frozemset
var=frozenset({ 10,20,30,40})

###Mapping

#dict
var={'id':10 ,'name':'harshada','sal':100000}
print(type(var))

###other
#bool
var=True
print(type(var))

#None type
var=None
print(type(var))

