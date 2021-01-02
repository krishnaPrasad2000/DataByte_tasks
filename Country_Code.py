import csv
final=[]
file='data_csv.csv'
country={}
value_1=0
value_2=0

with open(file,'r') as data:
    for line in csv.reader(data):
          country[line[0]]=line[1]
country.pop('Name')          
a=input('Enter the First Country Code: ')      
b=input('Enter the Second Country Code: ')  

for i in range(len(a)):
    value_1+=ord(a[i])    
    value_2+=ord(b[i])

for x in country:
    temp=0
    for i in range(len(country[x])):
       temp+=ord(country[x][i])
       if temp<value_2 and temp>value_1:
           final.append(x)
           
final.sort()
print(final)



