class Employee():
    department_name="Electronics"
    
    @classmethod
    def get_department_name(cls,in_dep):
        cls.department_name=in_dep
        
           
    def __init__(self,in_id,in_sal,in_mgrid):
        self.emp_id=in_id
        self.emp_salary=in_sal
        self.mgr_id=in_mgrid
    
    def display_instances(self):
        print(f"Employee id {self.emp_id} Employee's Salaray {self.emp_salary} Manager's' id {self.mgr_id}")
    
    def set_emp_salary(self,newsal):
        self.emp_salary=newsal
        
    def get_emp_salary(self):
        print(f"The new promoted salary is {self.emp_salary}")
    
    
        
        
        
        
def main():
    emp1=Employee("33","4000","1")
    emp1.display_instances()
    emp1.set_emp_salary("2000")
    emp1.get_emp_salary()
    
    
main()
    
