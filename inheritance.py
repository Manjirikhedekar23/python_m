class Person():
    def __init__(self,in_name,in_place,):
        self.name=in_name
        self.place=in_place
    
    def display_attributes(self):
        print(f"Name : {self.name}")
        print(f"Place : {self.place}")

class Sister(Person):
      def __init__(self,in_name,in_place,in_examsub):
        super().__init__(in_name,in_place)
        self.exam_subjects = []
        self.exam_subjects.append(in_examsub)
    
      def display_attributes(self):
        super().display_attributes()
        print(f"Exam subjects : {self.exam_subjects}")
    
      def add_skill(self,rcv_examsub):
        self.exam_subjects.append(rcv_examsub)
                
def main():
    boi1=Person("Avicii","Stockholm")
    boi1.display_attributes()
   
    boi2=Sister("Alison Wonderland","Australia","Electro")
    boi2.add_skill("Dubstep")
    boi2.display_attributes()
    
main()


# class Person:
#     def __init__(self,name,res) -> None:
#         self.name=name
#         self.res=res
    
#     def disp_attr(self):
#         print("Name: ", self.name)
#         print("Residence:", self.res)
    
# class Sister(Person):
#     def __init__(self,name,res,ex_sub) -> None:
#         super().__init__(name,res)
#         self.ex_sub=ex_sub
    
#     def disp_attr(self):
#         super().disp_attr()
#         print("Exam Subs: " ,self.ex_sub)
    
# def main():
#     s=Sister("abc","pqr","xyz")
#     s.disp_attr()

# main()