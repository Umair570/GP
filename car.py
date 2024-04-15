class Cars:
    def __init__(self,colour,model):  
        self.col=colour   
                          
        self.mod=model
    def car(self):
        return f"{self.col} is driving and its model is {self.mod}"

car1=Cars("Red",2021)    
print(car1.car())    
car2=Cars("Black",2024)        
print(car2.car())