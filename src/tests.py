import unittest
from datetime import date

from logMaker import DrinkStats, Log, Stats, PrepStats, BrewStats, DrinkStats
from templates import *

AUTHOR = "Marie Curie"
DATE = date.today()
TEMPLATE = ImmersionV60
PREPSTATS = {    
    "coffee_bean": "Turkish Bean",
    "brew_tool": "Hario Switch",
    "grinder": "Fellow Ode",
    "grind_size": 2.3,
    "coffee_amount": 15.1,
    "water_temperature": 100,
    }
BREWSTATS = {
    "bloom_water_amount": 36.4,
    "bloom_duration": 34,
    "total_water": 246.7,
    "steep_duration": 120,
    "draw_down_duration": 90,
}
DRINKSTATS = {
    "flavour_notes": "Nutty, light bitterness",
    "overall_score": 5.6,
    "aroma_quantity": "high",
    "aroma_quality": "low",
    "acidity_quantity": "high",
    "acidity_quality": "low",
    "sweetness_quantity": "high",
    "sweetness_quality": "low",
    "body_quantity": "high",
    "body_quality": "low",
    "finish_quantity": "high",
    "finish_quality": "low",
    "notes": "Kinda sucked lol"
}
STATS = PREPSTATS | BREWSTATS | DRINKSTATS 

class TestLog(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.prepstats = PrepStats(stats=PREPSTATS)
        self.brewstats = BrewStats(stats=BREWSTATS)
        self.drinkstats = DrinkStats(stats=DRINKSTATS)
        self.stats = Stats(stats=STATS)
        self.log = Log(
            author=AUTHOR, 
            date=DATE, 
            prepstats=self.prepstats, 
            brewstats=self.brewstats, 
            drinkstats=self.drinkstats
        )
    
    def test_author(self):
        """Whether author is correctly set."""
        self.assertEqual(self.log.author, AUTHOR)
        
    def test_date_is_set(self):
        """Whether the date is set correctly"""
        self.assertEqual(self.log.date, DATE)
        
    def test_date_prints_correctly(self):
        """Whether date prints correctly"""
        self.assertEqual(str(self.log.date), str(DATE))
        
    def test_stats(self):
        """Tests that stats are set correctly"""
        self.assertSequenceEqual(self.log.stats, STATS)
        
    def test_template_import(self):
        """Tests that template is imported correctly"""
        self.log.import_template(TEMPLATE)
        self.assertEqual(self.log.template, TEMPLATE)
        
    def test_log_print(self):
        """Tests that the log prints correctly"""
        test_case = TEMPLATE.format(date=DATE, **STATS)
        
        self.log.import_template(TEMPLATE)
        self.assertEqual(str(self.log), test_case)

class TestStats(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.stats = Stats(stats=STATS)
        
    def test_stats_are_set(self):
        """Tests that stats input is stats output"""
        self.assertEqual(self.stats.stats, STATS)
        
    def test_stats_print(self):
        """Tests that stats prints dictionary"""
        self.assertEqual(str(self.stats), str(STATS))
        
    def test_susbscript(self):
        """Tests subscript functionality"""
        key = "bloom_duration"
        self.assertEqual(self.stats[key], STATS[key])
        
class TestPrepStats(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.prepstats = PrepStats(stats=PREPSTATS)
        
    def test_stats_are_set(self):
        """Tests that stats input is stats output"""
        self.assertEqual(self.prepstats.stats, PREPSTATS)
    
        
if __name__ == "__main__":
    unittest.main()