class Student():
    
    nameofinstitute = 'sunbeam' #class variable
    
    @classmethod
    def change_institute_name(cls,in_institutename):
        cls.nameofinstitute=in_institutename
        
        
    def __init__(self,in_name,in_roll,in_sub):
        self.name=in_name
        self.rollnumber=in_roll
        self.sub=in_sub
    
    def display_instance(self):
        print(f'Name{self.name} Roll number {self.rollnumber} Subject {self.sub}')
    
    @staticmethod
    def display_fac():
        print('static method do not belong to class or object ref(1st par)')


def main():
    manjiri=Student("Manjiri","62","Python")
    print(type(manjiri))
    manjiri.display_instance()
    print(f"Purana institute : {manjiri.nameofinstitute}")
    Student.change_institute_name("no--it")
    print(f"naya institute : {manjiri.nameofinstitute}")
    
    Student.display_fac()
    manjiri.display_fac()   

main()