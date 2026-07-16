"""
Filter() :- it is an in built function which is used to extract the only required values from the collection
syntax:
      var_name=filter(function_name,collection)
      print(datatype(var_name))
      OR
      print(data_type(filter(function_name,collection)))
"""
#extract only even numbers from the range 2 to 6
print(list(filter(lambda a: a%2==0,range(2,6))))

#write a program to extract all the string data item from the tuple
x = (2,'supriya',5+2j,'s',True)
print(tuple(filter(lambda a: type(a)==str,x)))

#write a program to extract all the string data item from the tuple only if it is stating with lowercase charecter and ending with uppercase
data = ('supriyA',33,4+4j,'S','pramodA')
result=filter(lambda x: isinstance(x,str) and x[0].islower() and x[-1].isupper(),data)
print(tuple(result))    

#write a program to find the square of all the even numbers from the given list only if it is an integer
a = [10,20,'hello',5+6j,85,90,37,90.00]
result = map(lambda x:x**2,filter(lambda y:type(y)==int and y%2==0,a))
print(list(result))

#write a program to extract all the collection data or values present in a list which has an even length
data = [[10,20],30+5j,'hello',(1,2,3),'True',True]
result = filter(lambda x:type(x) in (int,str,list,tuple) and len(x)%2==0,data)
print(list(result))

"""
reduce() :- it is an inbuilt function which is used to prform the operation in b/w the values @ elemnts present inside the colection
syntax:
       from functool import reduce
       var_name=reduce(func_name,collection)
       print(var_name)
"""
from functools import reduce
add = lambda s,i:s+i
out = reduce(add,[1,2,3,4,5,6])
print(out)

#write a program to find maximum number in collection
print(reduce(lambda a,b:a if a>b else b,[10,30,40,70]))