class Patient:
    def __init__(self,name,age,phone,disease,address):
        self.name=name
        self.age=age
        self.phone=phone
        self.disease=disease
        self.address=address
        
    def display_info(self):
       print(f"{self.name}, {self.age}, {self.phone}, {self.disease},{self.address}")
       
    def is_adult(self):
        return self.age>=18
       
            
    # def update_info(self,reference_from):
    #     # self.address=address
    #     self.reference_from=reference_from 
                
patient_1=Patient("hiamnsu",20,42325627,"nothing","bbsr") 
patient_2=Patient("tisu",16,55325627,"pain in knees","unknown") 
patient_3=Patient("tiku",26,89325627,"fever","baripada")  

patient_1.display_info()
patient_2.display_info()
patient_3.display_info()
    

a=patient_1.is_adult()
a1=patient_2.is_adult()
a3=patient_3.is_adult()


print(a1,a,a3) 


# patient_1.update_info("ctc","dr.dash")
# patient_2.update_info("bbsr","mrs.dash")
# patient_3.update_info("sam","mr.rohit")




