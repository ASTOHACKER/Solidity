class Employee:
    #create method
    def detail(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.depart = department
    def showdata(self):
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))
        print("depart = {}".format(self.depart))


    def __del__(self):
        print("Call destructor")\
#create object

obj1 = Employee()
obj1.detail("narudom",20000,"Dev")

obj2 = Employee()
obj2.detail("narudom1",200001,"program")

obj1.showdata()
obj2.showdata()

#https://www.youtube.com/watch?v=YXNwADEE3EU&list=PLltVQYLz1BMBGWAaxQYa42rdxfeOlVBwn&index=1
#46:09


