from tires.tires import Tires
class Carrigan(Tires):
   def __init__(self,worn):
         self.__worn=worn 
   def needs_service(self):
          for i in self.__worn:
             if i>=0.9:
                return True 
          return False
 