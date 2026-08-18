a = ''' Artificial intelligence is growing rapidly.
Machine learning is a part of AI.
It is used in healthcare, finance, and education.
It makes systems smarter and more efficient.'''
print(a)
#)Python indexing
#lef to right
print(a[2])
#right to lef
print(a[-3])

#for loop in python
#syntax   for variable_name in string :
    #do some thing
for i in a:
    print(i)
#check to type
type=type(a)
#check to length
len=len(a)
print(type)
print(len)
#check item in string
if "Artificial intelligence" in a:
    print("Yes, 'Artificial intelligence' is present.")


