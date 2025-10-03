class Stu:
    def _init_(self,name,grade,percent):   #method
        self.name = name   #attribute
        self.grade = grade #attribute
        sel.percent = percent

    def stu_details(self):
        print(f"{self.name} is in class {self.grade} & percent {self.percent}")