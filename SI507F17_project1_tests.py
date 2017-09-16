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
    
    #The class Card should always have 3 class variables: suit_names, rank_levels, and faces
    def test_if_class_variables_exist_in_class_cards(self):
        c = Card()
        self.assertIsNotNone(c.suit_names)
        self.assertIsNotNone(c.rank_levels)
        self.assertIsNotNone(c.faces)
        
    #suit_names should contain a list of strings that represent suits: Diamonds, Clubs, Hearts, Spades
    def test_if_variable_suit_names_has_a_list_of_strings_representing_suits(self):
        c = Card()
        suit_list = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        self.assertIsInstance(c.suit_names, list)
        for each_item in c.suit_names:
            self.assertIn(each_item,suit_list)
        
    #rank_levels should contain a list of integers, 1-13
    def test_if_variable_suit_names_has_a_list_of_strings_representing_suits(self):
        c = Card()
        int_range = []
        for i in range(13):
            int_range.append(i+1)
        self.assertIsInstance(c.rank_levels, list)
        for each_item in c.rank_levels:
            self.assertIn(each_item,int_range)
    '''
    faces should contain a dictionary whose keys are numbers and whose values are strings. It should have the following key-value pairs:
		* 1:"Ace"
		* 11:"Jack"
		* 12:"Queen"
		* 13:"King"
    '''
    def test_if_class_variable_faces_contain_a_dictionary_where_kisnumber_and_visstrings(self):
        c = Card()
        target_dict = {1:"Ace",11:"Jack",12:"Queen",13:"King"}
        self.assertTrue(type(c.faces),dict)
        self.assertEqual(c.faces,target_dict)    

    '''
    The class Card's constructor should accept a number representing a suit and a number representing a rank. You can assume that no one should ever put in a number that is an invalid suit (less than zero or greater than 3) or an invalid rank (less than zero or greater than 13). The default value for a suit in the Card constructor (variable name *suit*) is 0, for Diamonds, and the default value for the rank in the Card constructor (variable name *rank*) is 2.
    '''
    def test_if_default_is_2_of_diamonds(self):
        c = Card()
        self.assertEqual(c.suit,'Diamonds')
        self.assertEqual(c.rank,2)
    def test_if_class_card_takes_proper_arguments_to_make_proper_card(self):
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
    
    # The Card class has a string method, which should return a string e.g. "Ace of Spades" or "3 of Clubs", etc.
    def test_string_method_of_Card(self):
        suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
        for i in range(12):
            if i == 0:
                for j in range(3):
                    self.assertEqual(str(Card(j,i+1)),"Ace of {}".format(suit_names[j]))
            elif i==10:
                for j in range(3):
                    self.assertEqual(str(Card(j,i+1)),"Jack of {}".format(suit_names[j]))
            elif i==11:
                for j in range(3):
                    self.assertEqual(str(Card(j,i+1)),"Queen of {}".format(suit_names[j]))
            elif i==12:
                for j in range(3):
                    self.assertEqual(str(Card(j,i+1)),"King of {}".format(suit_names[j]))
            else:
                for j in range(3):
                    self.assertEqual(str(Card(j,i+1)),"{} of {}".format(i+1,suit_names[j]))
                    
class Testing_Deck_proj1(unittest.TestCase):
    #Deck related Tests
    
    
    #The class Deck's constructor does not accept input, and you can assume this will always be handled correctly by a programmer using this code.
    def test_if_class_Deck_does_not_accept_input(self):
        self.assertRaises(TypeError, lambda: Deck("a"))
    
    
    #The Deck constructor builds a list of cards -- all the cards that would be included in a 52-card deck: rank 1-13 of each of the four suits.
    #The Deck constructor creates one instance variable: self.cards, which should hold a list of Card objects when a Deck instance is created.
    def test_if_class_deck_actually_creates_52_cards(self):
        test_deck = Deck()
        self.assertEqual(len(test_deck.cards), 52)
    
    #The Deck string method should return a multi-line string with one line for each printed representation of a card in the deck. So a complete deck should have a 52-line string of strings like "Ace of Diamonds", "Two of Diamonds", etc.
    #THIS ONE FUCKIN FAILS, probably because it's related to the issue found in test_string_method_of_Card !!!!!!!!!!!!!!!!!
    def test_if_class_deck_str_contains_certain_cards(self):
        test_deck = Deck()
        list_of_cards = []
        suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
        for suit_type in range(3):
            for card_number in range(12):
                if card_number == 0:
                    list_of_cards.append('Ace of {}'.format(suit_names[suit_type]))
                elif card_number == 10:
                    list_of_cards.append('Jack of {}'.format(suit_names[suit_type]))
                elif card_number == 11:
                    list_of_cards.append('Queen of {}'.format(suit_names[suit_type]))
                elif card_number == 12:
                    list_of_cards.append('King of {}'.format(suit_names[suit_type]))
                else:
                    list_of_cards.append('{} of {}'.format(card_number+1,suit_names[suit_type]))
        for card_string in list_of_cards:
            self.assertIn(card_string, test_deck.__str__())                           
    
    #Deck has a method pop_card which accepts an integer as input and has a default value such that the Deck will pop off the last (top) card of the deck, as if you're taking off the top card in a card game. When pop_card is invoked on a Deck instance, the last card in the deck is removed from the deck. You should be able to "pop" all of the cards off of the deck until the deck is empty (its self.cards list is the empty list). 
    def test_if_pop_cards_method_of_Deck_gets_rid_of_cards(self):
        test_deck = Deck()
        for i in range(52):
            test_deck.pop_card()
        self.assertEqual(len(test_deck.cards),0)
        
    #Deck has a method shuffle which accepts no external input and shuffles the self.cards list in the Deck at that time so that it has a random order.
    def test_if_shuffle_method_of_Deck_shuffles_cards(self):
        test_deck = Deck()
        test_deck_shuffled = test_deck.shuffle()
        self.assertFalse(test_deck is test_deck_shuffled)
    
    #Deck has a method replace_card which accepts a Card instance as input. If the card instance input into the method is NOT already in the deck, it is added back to the deck. If it IS already in the deck, nothing changes about the Deck (a deck should not have any duplicate cards as a result of calling this method).
    def test_if_replace_card_method_of_class_deck_works(self):
        test_deck = Deck()
        second_deck = Deck()
        a = test_deck.pop_card()
        test_deck.replace_card(a)
        second_deck.replace_card(a)
        self.assertEqual(len(test_deck.cards), 52) #makes sure function replaces the card
        self.assertEqual(len(second_deck.cards), 52) #makes sure function doesn't replace cards that already exists
    
    #Deck has a method sort_cards which should organize the cards remaining in the deck into an order such that they are in ascending order by suit: Diamonds, then Clubs, then Hearts, then Spades.
    #THIS ONE FUCKIN FAILS!!!!!!!!!!!!!!!!!
    def test_if_sort_cards_method_of_class_deck_sorts_cards_by_suit(self):
        some_deck = Deck()
        cards_for_testing = [Card(2,5),Card(1,5),Card(0,5),Card(3,5)]
        cards_ordered = [Card(0,5),Card(1,5),Card(2,5),Card(3,5)]
        for i in range(52):
            some_deck.pop_card()
        for i in cards_for_testing:
            some_deck.replace_card(i)
        some_deck.sort_cards()
        self.assertEqual(len(some_deck.cards),4)                                            

    #Deck has a method deal_hand which takes a required input hand_size, an integer representing the number of cars in the hand. It should return a list of Card objects that make up the hand dealt....
    def test_if_Deck_method_deal_hand_returns_a_list(self):
        some_deck = Deck()
        hand_size = 3
        some_deck.deal_hand(hand_size)
        self.assertIsInstance(some_deck.deal_hand(hand_size),list)

    #A hand should be able to be dealt up to the full size of the current deck (e.g. if 3 cards have been removed from the deck and not replaced, it should be impossible to deal a 52-card hand, but if no cards have been removed, it should be possible)
    #THIS ONE FUCKIN FAILS!!!!!!!!!!!!!!!!! it looks like it's popping too many cards at a certain point 
    def test_if_Deck_method_deal_hand_deals_upto_fullsize_of_current_deck(self):
        for i in range(51):
            some_deck = Deck()
            self.assertEqual(len(some_deck.deal_hand(i+1)),i+1)
            
class Testing_playWarGames_function_proj1(unittest.TestCase):
    #play_war_game related tests
    
    #The play_war_game function should initialize two Deck instances, representing Player 1 and Player 2, inside its function scope and simulate a variation on the card game of War (http://www.bicyclecards.com/how-to-play/war/). This happens with no external input. There are 3 possible outcomes: the Player1 score is larger than the Player2 score and Player1 wins, the Player2 score is larger than the Player1 score and Player2 wins, or the two scores are the same and there is a tie.
    
    #The play_war_game function should always return a tuple of a string and two integers, where the string is either "Player1", "Player2", or "Tie", and the integers represent the Player1 score and the Player2 score, respectively.
    def test_if_playwargame_function_returns_tuple_of_str_and_two_ints(self):
        result = play_war_game(True)
        self.assertTrue(type(result), tuple)
        #Check the contents of the tuple
        self.assertTrue(type(result[0]), str)
        self.assertTrue(type(result[1]), int)
        self.assertTrue(type(result[2]), int)
        
class Testing_show_song_function_proj1(unittest.TestCase):
    #show_song() related tests
    
    #The show_song function takes a string as input to use as a search term for songs on iTunes. Its default value is "Winner", but you should be able to search for any search term with this function.
    def test_if_show_song_function_searches_any_string(self):
        resulting_song = show_song("Caravan Palace")
        self.assertEqual("something",str(resulting_song))
    #The show_song function invokes a function from the helper_functions file (which you do NOT have to test!), that gets data from the iTunes Search API based on this search term. It creates a list of Song objects, using the Song class definition from the helper_functions file. 

	#The show_song function should return a single instance of class Song (whose definition you can see in helper_functions.py, but which you do NOT have to test).
    def test_if_show_song_returns_a_single_instance_of_class_Song(self):
        result = show_song()
        self.assertEqual(type(result),helper_functions.Song)
    
if __name__=='__main__':
    unittest.main(verbosity=2)