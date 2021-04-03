##Child classes

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
                    f'Rating:           :{self.rating}'
        return notes
    def shortNote(self):
        shNote =    f'Brewery:          :{self.brewery}\n'\
                    f'Name:             :{self.name}'
        return shNote

class ipaBeer(Beer):
    style = 'IPA'
    def getIPANotes(self):
        notes =     f'Style:            :{ipaBeer.style}\n'\
                    f'Brewery:          :{self.brewery}\n'\
                    f'Name:             :{self.name}\n'\
                    f'Location:         :{self.location}\n'\
                    f'Rating:           :{self.rating}'
        return notes
    def shortIPANote(self):
        shNote =    f'Style:            :{ipaBeer.style}\n'\
                    f'Brewery:          :{self.brewery}\n'\
                    f'Name:             :{self.name}'
        return shNote

beerIPA1 = ipaBeer('Intuition', 'Florida', 'I 10', '86')
beerIPA2 = ipaBeer('Six Point', 'New York', 'Resin', '92')
beerIPA3 = ipaBeer('Funky Budda', 'Florida', 'Hopgun', '86')
beerIPA4 = ipaBeer('Green Room', 'Florida', 'Double Overhead', '91')



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
                    f'Rating:           :{self.rating}'
        return info
    def shortInfo(self):
        shrtIn =    f'Distillary:       :{self.distillary}\n'\
                    f'Name:             :{self.name}'
        return shrtIn

class bourbWsky(Whiskey):
    style = 'Bourbon'
    def getBourbInfo(self):
        infoBour  = f'Style:            :{bourbWsky.style}\n'\
                    f'Distillary:       :{self.distillary}\n'\
                    f'Name:             :{self.name}\n'\
                    f'Location:         :{self.location}\n'\
                    f'Rating:           :{self.rating}'
        return infoBour
    def shortBourInfo(self):
        shrtBourIn = f'Style:            :{bourbWsky.style}\n'\
                     f'Distillary:       :{self.distillary}\n'\
                     f'Name:             :{self.name}'
        return shrtBourIn

bourbon1 = bourbWsky('Buffalo Trace', 'Kentucky', 'McAfees Benchmark No 8', '75')
bourbon2 = bourbWsky('Four Roses', 'Kentucky', 'Small Batch Kentucky Straight', '87')
bourbon3 = bourbWsky('Evan Williams', 'Kentucky', 'Single Barrel 2003 Vintage', '93')
bourbon4 = bourbWsky('Makers Mark', 'Kentucky', 'Kentucky Straight Bourbon Whiskey', '89')
