class lake():
    name = "none"
    continent = "none"
    area = 0.0
    depth = 0.0
    def init(self, name, continent, area, depth):
        self.name = name
        self.continent = continent
        self.area = area
        self.depth = depth
    def del_name(self, name):
        self.name = str(name)
    def change_area(self,area):
        self.area = float(area)
    def change_depth(self,depth):
        self.depth = float(depth)

r = lake()
r.init("Гурон", "Північна Америка", 0.0, 0.0)
r.del_name("Гурон")
print(r.name)
print(r.continent)
r.change_area(59.6)
print(r.area)
r.change_depth(230)
print(r.depth)






