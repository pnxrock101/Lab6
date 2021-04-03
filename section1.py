class Vehicle:
    type = 'Car'
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def getDeets(self):
        details =   f'Type:         :{Vehicle.type}\n'\
                    f'Year:         :{self.year}\n'\
                    f'Make:         :{self.make}\n'\
                    f'Model:        :{self.model}\n'\
                    f'Color:        :{self.color}\n'\
        return details

vehCar1 = Vehicle('Ford', 'Mustang', '1964', 'Red')
vehCar2 = Vehicle('Chevrolet', 'Camaro', '1969', 'Blue')
vehCar3 = Vehicle('Dodge', 'Charger', '1971', 'Black')
vehCar4 = Vehicle('Cadillac', 'Herse', '1953', 'Black')




class Beer:
    style = 'Stout'
    def __init__(self, brewery, location, name, rating):
        self.brewery = brewery
        self.location = location
        self.name = name
        self.rating = rating
    def getNotes(self):
        notes =     f'Brewery:          :{self.brewery}\n'\
                    f'Name:             :{self.name}\n'\
                    f'Style:            :{Beer.style}\n'\
                    f'Location:         :{self.location}\n'\
                    f'Rating:           :{self.rating}\n'\
        return notes

beerStout1 = Beer('Founders', 'Michigan', 'Breakfast Stout', '100')
beerStout2 = Beer('Atlantic', 'Maine', 'Cadillac Mountain Stout', '93')
beerStout3 = Beer('Deschutes', 'Oregon', 'Obsidian Stout', '94')
beerStout4 = Beer('Rogue', 'Oregon', 'Chocolate Stout', '93')




class Whiskey:
    style = 'Rye'
    def __init__(self, distillary, location, name, rating):
        self.distillary = distillary
        self.location = location
        self.name = name
        self.rating = rating
    def getInfo(self):
        info  =     f'Distillary:       :{self.distillary}\n'\
                    f'Name:             :{self.name}\n'\
                    f'Style:            :{Whiskey.style}\n'\
                    f'Location:         :{self.location}\n'\
                    f'Rating:           :{self.rating}\n'\
        return info

wskRye1 = Whiskey('WhistlePig Farm', 'Vermont', 'Straight Rye', '89')
wskRye2 = Whiskey('Jack Daniel', 'Tennessee', 'Tennessee Straight Rye', '84')
wskRye3 = Whiskey('Knob Creek', 'Kentucky', 'Kentucky Straight Rye', '85')
wskRye4 = Whiskey('Builleit', 'Kentucky', '95 Straight Rye', '86')



class Games:
    type = 'RPG'
    def __init__(self, developer, title, rating, time):
        self.developer = developer
        self.title = title
        self.rating = rating
        self.time = time
    def getGame(self):
        game  =     f'Developer:                :{self.developer}\n'\
                    f'Title:                    :{self.title}\n'\
                    f'Genre:                    :{Games.type}\n'\
                    f'Rating:                   :{self.rating}\n'\
                    f'Playthrough Time:         :{self.time}\n'\
        return game

gmRPG1 = Games('Blizzard', 'Diablo 3', '9 of 10', '84 Hrs')
gmRPG2 = Games('Bethesda', 'Fallout 4', '7 of 10', '80 Hrs')
gmRPG3 = Games('CD Projekt', 'Cyberpunk 2077', '7 of 10', '30 Hrs')
gmRPG4 = Games('Obsidian', 'The Outer Worlds', '9 of 10', '25 Hrs')
