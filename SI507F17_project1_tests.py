## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class Testing_Cards_proj1(unittest.TestCase):
    #Card related tests
    
    def test_make_sure_default_is_2_of_diamonds(self):
        c = Card()
        self.assertEqual(c.suit,'Diamonds')
        self.assertEqual(c.rank,2)
    def test_make_sure_class_card_takes_proper_arguments_to_make_proper_card(self):
        #suit_names =  ["Diamonds","Clubs","Hearts","Spades"]        
        a = Card(2,12) #Queen of Hearts
        self.assertEqual(a.suit,'Hearts')
        self.assertEqual(a.rank,'Queen')   
        self.assertEqual(a.rank_num,12)
        
        b = Card(1,1) #Ace of clubs
        self.assertEqual(b.suit,'Clubs')
        self.assertEqual(b.rank,'Ace')   
        self.assertEqual(b.rank_num,1)
        
        c = Card(0,11) #Jack of Diamonds
        self.assertEqual(c.suit,'Diamonds')
        self.assertEqual(c.rank,'Jack')   
        self.assertEqual(c.rank_num,11)        

        d = Card(3,13) #King of Spades
        self.assertEqual(d.suit,'Spades')
        self.assertEqual(d.rank,'King')   
        self.assertEqual(d.rank_num,13)
        
        e = Card(3,5) #5 of Spades
        self.assertEqual(e.suit,'Spades')
        self.assertEqual(e.rank,5)   
        self.assertEqual(e.rank_num,5)
        
    def test_string_method_of_Card(self):
        test_card = Card(3,1) #should be an ace of spades
        self.assertEqual(test_card.__str__(),'Ace of Spades')                               #THIS ONE FUCKIN FAILS!!!!!!!!!!!!!!!!!

class Testing_Deck_proj1(unittest.TestCase):
    #Deck related Tests
    
    def test_checks_to_see_if_class_deck_actually_creates_52_cards(self):
        test_deck = Deck()
        self.assertEqual(len(test_deck.cards), 52)
    def test_if_deck_str_contains_certain_cards(self):
        test_deck = Deck()
        self.assertTrue('Ace of Diamonds' in test_deck.__str__())                           #THIS ONE FUCKIN FAILS!!!!!!!!!!!!!!!!!
    def test_what_happens_when_you_tryto_pop_off_all_the_damn_cards(self):
        test_deck = Deck()
        for i in range(52):
            test_deck.pop_card()
        self.assertEqual(len(test_deck.cards),0)
    def test_check_if_shuffle_method_of_Deck_shuffles_cards(self):
        test_deck = Deck()
        test_deck_shuffled = test_deck.shuffle()
        self.assertFalse(test_deck is test_deck_shuffled)
    def test_check_if_replace_card_method_of_class_deck_works(self):
        test_deck = Deck()
        second_deck = Deck()
        a = test_deck.pop_card()
        test_deck.replace_card(a)
        second_deck.replace_card(a)
        self.assertEqual(len(test_deck.cards), 52) #makes sure function replaces the card
        self.assertEqual(len(second_deck.cards), 52) #makes sure function doesn't replace cards that already exists
    def test_check_if_sort_cards_method_of_class_deck_works(self):
        some_deck = Deck()
        cards_for_testing = [Card(2,5),Card(1,5),Card(0,5),Card(3,5)]
        cards_ordered = [Card(0,5),Card(1,5),Card(2,5),Card(3,5)]
        for i in range(52):
            some_deck.pop_card()
        for i in cards_for_testing:
            some_deck.replace_card(i)
        some_deck.sort_cards()
        self.assertEqual(len(some_deck.cards),4)                                            #THIS ONE FUCKIN FAILS!!!!!!!!!!!!!!!!!

        
class Testing_playWarGames_function_proj1(unittest.TestCase):
    #play_war_game related tests
    
    def test_checks_if_playwargame_function_returns_tuple_of_str_and_two_ints(self):
        result = play_war_game(True)
        self.assertTrue(type(result), tuple)
        #Check the contents of the tuple
        self.assertTrue(type(result[0]), str)
        self.assertTrue(type(result[1]), int)
        self.assertTrue(type(result[2]), int)


unittest.main(verbosity=2)