import datetime

class AuditLogDescriptor:
    def __init__(self, name):
        self.name = name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        previous_value = instance.__dict__.get(self.name)
        instance.__dict__[self.name] = value
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{self.name} {previous_value} {value} {current_time}")
        
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class NumericRange:
    def __init__(self, name, min_value, max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Attribute value must be numeric")
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Attribute value must be between {self.min_value} and {self.max_value}.")
        instance.__dict__[self.name] = value

class StringFormat:
    def __init__(self, name, format_rules):
        self.name = name
        self.format_rules = format_rules
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Attribute value must be a string.")
        if not all(rule in value for rule in self.format_rules):
            raise ValueError(f"Attribute value must match format rules: {self.format_rules}.")
        instance.__dict__[self.name] = value

class MyClass:
    numeric_attribute = NumericRange("numeric_attribute", 0, 100)
    string_attribute = StringFormat("string_attribute", ["prefix", "suffix"])
    audit_attribute = AuditLogDescriptor("audit_attribute")

obj = MyClass()
obj.numeric_attribute = 50
print(obj.numeric_attribute)
obj.numeric_attribute = 150