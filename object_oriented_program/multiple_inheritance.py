class person:
    name:str
    age:int

    def __init__(self,name,age):
     self.name=name
     self.age=age
    def person_info(self):
       print(f"name is : {self.name} , age is : {self.age}")

class empolyee:
   emp_id=int
   salary:int
   def __init__(self,emp_id,salary):
    self.emp_id=emp_id
    self.salary=salary
   def empolyee_info(self):
      print(f"empolyee details,emp_id : {self.emp_id}, salary :{self.salary}")

class manger(person,empolyee):
   department:str
   def __init__(self,name,age,eid,salary,department):
    person.__init__(self,age,name)
    empolyee.__init__(self,eid,salary)
    self.department=department
   def display_manager_info(self):
     self.person_info()
     self.empolyee_info()
     print(self.department)
manager_instance=manger(26,"arun",700,60000,"HHR")
manager_instance.display_manager_info()