import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.cardgame1 = CardGame()
        self.card1 = Card("hearts", 1)
        self.card2 = Card("spades", 5)
        self.card3 = Card("clubs", 8)
    
    def test_check_for_ace__True(self):
        result = self.cardgame1.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_check_for_ace__False(self):
        result = self.cardgame1.check_for_ace(self.card2)
        self.assertEqual(False, result)
    
    def test_highest_card(self):
        highest_card = self.cardgame1.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, highest_card)

    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        total = self.cardgame1.cards_total(cards)
        self.assertEqual('You have a total of 14', total)