#!python
print("content-type: text/html; charset=utf-8\n")

#Positionary formatting
#By using {}, we can format varible and its value.
#we directly use {} and then we put value later in order with .format('value', value....)
print("To {}. sint {} qui {} officia.{}".format('KYU', 32, 'KYU', 32))

#Named Placeholders
#with this approach, we strengthen understanding of data type and efficency in use
print("To {name}. sint {age:d} qui {name} officia.{age:d}".format(name='KYU', age=32))
