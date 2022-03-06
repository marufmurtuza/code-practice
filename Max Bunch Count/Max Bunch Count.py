class Bunch:
    def __init__(self,source):
        self.source = source
    
    def max_bunch_find(self):
        max_value = 0
    
        for i in range(len(self.source)):
            is_max = self.source.count(i)
            
            if is_max > max_value: 
                max_value = is_max
                
                
        print(max_value)

source =  [1, 2, 2, 3, 4, 4, 4]

value = Bunch(source)

value.max_bunch_find()