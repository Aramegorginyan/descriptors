import re

class StringValue:
    def __set_name__(self,owner,name):
        self.name = "_" + name

    def __get__(self,instance,owner):
        return getattr(instance, self.name)
    
    def __set__(self,instance,value):
        result = value.strip()
        if not isinstance(result,str) or not result.isalpha():
            raise TypeError("The value must be a string and contain only letters.")
        setattr(instance, self.name, result)

class Email:
    def __set_name__(self,owner,email):
        self.email = "_" + email

    def __get__(self,instance,owner):
        return getattr(instance, self.email)
    
    def __set__(self,instance,value):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        filtered_chars = [char for char in value if char in ('@', '.')]

        if not bool(pattern.search(value)) or len(filtered_chars) > 2:
            raise TypeError("Invalid email")
        setattr(instance, self.email, value)

class Password:
    def __set_name__(self,owner,password):
        self.password = "_" + password

    def __get__(self,instance,owner):
        return getattr(instance, self.password)
    
    def __set__(self,instance,value):
        special_chars = {'!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'}

        if 8 <= len(value) <= 20:
            has_uppercase = any(char.isupper() for char in value)
            has_digit = any(char.isdigit() for char in value)
            has_special_char = any(char in special_chars for char in value)

            if has_uppercase and has_digit and has_special_char:
                setattr(instance,self.password,value)
            else:
                raise TypeError("Password must contain at least 1 special char, 1 uppercase letter and number")
        else:
            raise TypeError("Password must be longer than 8 chars and lower than 20 chars")
        
class IntegerValue:
    def __set_name__(self,owner,age):
        self.age = "_" + age

    def __get__(self,instance,owner):
        return getattr(instance, self.age)
    
    def __set__(self,instance,value):
        if value < 0 or not isinstance(value,int):
            raise ValueError("??")
        setattr(instance,self.age,value)

class User:
    first_name = StringValue()
    last_name = StringValue()
    age = IntegerValue()
    email = Email()
    password = Password()
    
    def __init__(self,first_name,last_name,age,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password

u = User("Arame","Gorginyan",0,"ramekgorg@gmail.com","Qwezxc123:")
print(u.first_name)
print(u.last_name)
print(u.age)
print(u.email)
print(u.password)