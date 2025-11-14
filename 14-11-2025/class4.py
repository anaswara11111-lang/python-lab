class Me:
    def __init__(self,name,age,hobby):
        self.name=name
        self.age=age
        self.hobby=hobby
    def display(self):
        print("My name is",self.name,". Iam",self.age,"year old",". My hobbies are",self.hobby,".")
m1=Me("Anaswara",21,"Watching movies,Reading")
m1.display()
