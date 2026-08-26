# class Patient:
#     def __init__(self,name,age,phone,disease,address):
#         self.name=name
#         self.age=age
#         self.phone=phone
#         self.disease=disease
#         self.address=address
        
#     def display_info(self):
#        print(f"{self.name}, {self.age}, {self.phone}, {self.disease},{self.address}")
       
#     def is_adult(self):
#         return self.age>=18
       
            
#     # def update_info(self,reference_from):
#     #     # self.address=address
#     #     self.reference_from=reference_from 
                
# patient_1=Patient("hiamnsu",20,42325627,"nothing","bbsr") 
# patient_2=Patient("tisu",16,55325627,"pain in knees","unknown") 
# patient_3=Patient("tiku",26,89325627,"fever","baripada")  

# patient_1.display_info()
# patient_2.display_info()
# patient_3.display_info()
    

# a=patient_1.is_adult()
# a1=patient_2.is_adult()
# a3=patient_3.is_adult()


# print(a1,a,a3) 


# # patient_1.update_info("ctc","dr.dash")
# # patient_2.update_info("bbsr","mrs.dash")
# # patient_3.update_info("sam","mr.rohit")
   
class Doctor():
    def __init__(self,name,specialization,experience):
        self.name=name
        self.specialization=specialization
        self.experience=experience
        
    def display_info(self):
        print(f"{self.name},{self.specialization},{self.experience}")    
        
    def is_experienced(self):
         return self.experience>=5
     
    def can_handle_emergency(self):
        return self.specialization == "emergency"
             

doctor_1=Doctor("dr.ramesh","orthopedic",6)
doctor_2=Doctor("dr.jatin","cardiology",3)
doctor_3=Doctor("dr.narendra","opd",2)

doctor_1.display_info()
doctor_2.display_info()
doctor_3.display_info()

a1=doctor_1.is_experienced()
a2=doctor_2.is_experienced()
a3=doctor_3.is_experienced()

a4=doctor_1.can_handle_emergency()
a5=doctor_2.can_handle_emergency()
a6=doctor_3.can_handle_emergency()

print(a1,a2,a3)

print("can they handle emergency situation","doctor1:",a4,
      "doctor2:",a5,"doctor3:",a6)

