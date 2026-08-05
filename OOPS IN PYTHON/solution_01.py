# create astudent class that takes name and marksof 3 subjectsas arguments in constructor.thencreate amethod to print the avergae
   
   
class student:
    def __init__(self,name,marks):
        self.name=name
        self.mark=marks
        
    def get_avg(self):
        total = 0
        for val in self.mark:
            total += val
        avg = total / len(self.mark) if self.mark else 0
        print("Hi I am", self.name, "my avg mark is", avg)


s1 = student("Jonny Dep", [87, 67, 93])
s1.get_avg()
               
    