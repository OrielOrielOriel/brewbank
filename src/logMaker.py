from abc import ABC, abstractmethod

from templates import *

class Log: 
    author = ""
    date = ""
    
    def __init__(self, author, date, prepstats, brewstats, drinkstats):
        self.author = author
        self.date = date
        self.stats = prepstats.stats | brewstats.stats | drinkstats.stats
        
    def __str__(self):
        ret = self.template.format(date=self.date, **self.stats)
        return ret
        
    def import_template(self, template_name):
        self.template = template_name

class Stats(ABC):
    def __init__(self, stats):
        self.stats = stats

    def __str__(self):
        ret = str(self.stats)
        return ret
    
    def __getitem__(self, key):
        ret = self.stats[key]
        return ret
    
class PrepStats(Stats):
    pass

class BrewStats(Stats):
    pass

class DrinkStats(Stats):
    pass