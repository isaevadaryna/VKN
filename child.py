class child:
    #name = "none"
    #surname = "none"
    #age = 0
    #year = 0
    def __init__(self, name, surname, year):
        self.name = str(name)
        self.surname = str(surname)
        self.age = 2022 - int(year)
        self.year = int(year)
    def set_age(self, year):
        self.age = 2022 - year
    def get_age(self):
        return(self.age)




