class student:
    def __init__(self,full_name,Age,state):
        self.name=full_name
        self.age=Age
        self.state=state
        
s1=student("Jon snow",22,"Winterfell")
s2=student("Arya stark",18,"Winterfell")
s3=student("Sansa stark",20,"Winterfell")
s4=student("Bran stark",16,"Winterfell")
s5=student("Rob stark",25,"Winterfell")
s6=student("Rickon stark",10,"Winterfell")
s7=student("Theon greyjoy",22,"Iron Islands")
print(s1.name,s1.age,s1.state)      
print(s2.age,s2.name,s2.state)
print(s3.state,s3.name,s3.age)
print(s4.name,s4.age,s4.state)
print(s5.age,s5.name,s5.state)
print(s6.state,s6.name,s6.age)
print(s7.name,s7.age,s7.state)