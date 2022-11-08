from tires.tires import Tires
class  Octoprime(Tires):
       def __init__(self,worn):
         self.__worn=worn 
       def needs_service(self):
         total=0 
         for i in self.__worn:
            total+=i
         if total>=3:
            return True
         return False
 