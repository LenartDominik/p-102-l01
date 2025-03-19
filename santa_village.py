# village plan

class SantaVillage:
    def __init__(self, name, population, location, buildings):
        self.name = name
        self.population = population
        self.location = location
        self.buildings = buildings
    
    def __str__(self):
        return f"""<Village: {self.name}>
        <Population: {self.population}>
        <Location: {self.location}> """
    
    def increase_population(self):
        self.population += 1

class Building:
    def __init__(self, name, features):
        self.name = name
        self.features = features
        
class ToyFactory(Building):
    def __init__(self, name, features, equipment, relaxation_area):
        super().__init__(name, features)
        self.equipment = equipment
        self.relaxation_area = relaxation_area

    def produce_toys(self):
        return f'{self.name} is producing toys'

class ElfHouse(Building):
    def __init__(self, name, features, magic):
        super().__init__(name, features)
        self.magic = magic
        
class SantasHouse(Building):
    def __init__(self, name, features, properties):
        super().__init__(name, features)
        self.properties = properties
        
class ReindeerStable(Building):
    def __init__(self, name, features, hay, magic_food, trainings):
        super().__init__(name, features)
        self.hay = hay
        self.magic_food = magic_food
        self.trainings = trainings
        
class WorkShop(Building):
    def __init__(self, name, features, paintings, tools, baked_products):
        super().__init__(name, features)
        self.paintings = paintings
        self.tools = tools
        self.baked_products = baked_products
    
class ChristmasKitchen(Building):
    def __init__(self, name, features, specialities):
        super().__init__(name, features)
        self.specialities = specialities

    def cook(self):
        return f"{self.name} specializes in preparing: {', '.join(self.specialities)}."
    
class ChristmasPost(Building):
    def __init__(self, name, features, letters):
        super().__init__(name, features)
        self.letters = letters

class VillageMember:
    def __init__(self, name, age, skills, village):
        self.name = name
        self.age = age
        self.skills = skills
        village.increase_population()


# Citizens of the village and their activities        

class SantaClaus(VillageMember):
    def __init__(self, name, age, skills, village, profession):
        super().__init__(name, age, skills, village)
        self.profession = profession
    
    def reading_letters(self):
        return f'{self.name} is {self.age} years old and reads letters from children'
        
        
    def preparing_gifts(self):
        return f'{self.name} packs gifts'
    
    def delivering_gifts(self):
        return f'{self.name} delivers gifts to children'
        

class MrsClaus(VillageMember):
    def __init__(self, name, age, skills, village, baking):
        super().__init__(name, age, skills, village)
        self.baking = baking
        
    def baking_gingerbread(self):
        return f'{self.name} is baking gingerbread'

class PostmanElf(VillageMember):
    def __init__(self, name, age, skills, village, delivering):
        super().__init__(name, age, skills, village)
        self.delivering = delivering
    
    def sending_responses(self, responses):
        return f'{self.name} is sending responses {responses} to children letters.'


class MechanicElf(VillageMember):
    def __init__(self, name, age, skills, village, repairing):
        super().__init__(name, age, skills, village)
        self.repairing = repairing
    
    def sleigh_maintenance(self):
        return 'Maintenance of Santa sleigh'
        
class GuideElf(VillageMember):
    def __init__(self, name, age, skills, village, guiding):
        super().__init__(name, age, skills, village)
        self.guiding = guiding
        
    def guiding_tourists(self, stories):
        return f'Guiding tourists through the Father Christmas Village and telling magic {stories}'
        
        
class RudolfTheReindeer(VillageMember):
    def __init__(self, name, age, skills, village, flying):
        super().__init__(name, age, skills, village)
        self.flying = flying
    
class ArtistElf(VillageMember):
    def __init__(self, name, age, skills, village, painting):
        super().__init__(name, age, skills, village)
        self.painting = painting
        
    def creating_decorations(self, decorations):
        return f'Creating Christmas {decorations} and {self.painting} baubles for Christmas trees'
        
