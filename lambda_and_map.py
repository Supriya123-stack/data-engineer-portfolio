"""lamda function :-it is a function which is used to perform small opertion in python by using lamda key
   syntax
    1.   var_nam = lambda args:expression
         print(var_nam)
         or
         print((lambda args:expression)(values))
    2.  syntax to write if else expression  in lamda
        
        var_name = lamba args:TSB if contion else FSB
        print(var_name)
        or
        print((lambda args:TSB if condition else FBS))

"""

#find squr and cube room of a number
a = lambda c:[c**2,c**3]
print(a(2))

#number is odd or even
a = lambda x:"EVEN" if x%2==0 else "ODD"
print(a(67))

"""
   MAP() function :- it is a built in function that applys another function on each item of one or more collection
   -> it will considerd a collection and it applyes same functionality to each and every value s.present insde the collection(list,set,tuple,dict)
   -> map return a map object adress to get the proper result we should convert it into list,tuple etc
   syntax:
         var_name= map(function_name,collection)
         print(var_name)

"""
#ex: sqr_root of collection
sqr = lambda a:a**2
sqr_var = map(sqr,[1,2,3,4])
print(list(sqr_var))

# OR

sqr_var = map(lambda a:a**2,[1,2,3,4])
print(list(sqr_var))

#OR

print(list(map(lambda a:a**2 ,[1,2,3,4])))

#write a program factorial  of all the integer present inside the tuple
def fact(n):
    if n<1 or n==0:
        return 1
    return n*fact(n-1)
print(tuple(map(fact,[1,2,3,4,5])))

#write a program to apply square on each and every element present inside a collection without using map()
c = eval(input("enter the collection:"))
b =[]
n= 0
for i in c:
    n = i**2
    b.append(n)
print(b)    

#write a program to apply square on each and every elemnet if it is even number in the collection using map()
def sqr(a):
    if a%2==0:
        return a**2
ab =map(sqr,[1,2,3,4,5,6])
print(list(ab))   

#write to find the cube of number in which range are enterd by the use starting and ending o/p in dict formate.
start = int(input("enter the starting value:"))
end = int(input("enter the ending value:"))
x = range(start,end)
print(dict(map(lambda a:(a,a**2),x)))

#write a program i/p: "program on map function" o/p:{'program':'margorp','on':'no','map':'pam','function':'noitcnuf'}
s = "program on map function".split()
print(dict(map(lambda i:(i,i[::-1]),s)))




