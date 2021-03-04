class Restaurant:
    def __init__(self, res_name, cuisine_type):
        self.res_name = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def des_res(self):
        print('Restaurant:', self.res_name, 'Cuisine Type:', self.cuisine_type)
        
    def open_res(self):
        print('The restaurant is open.')
        
    def inc_number_served(self, ns):
        self.number_served += ns