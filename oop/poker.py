"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialze Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Return a string representation of the card.

        "{value} of {suit}"
        "2 of hearts" or "Q of spades"

        """
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    dict_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}

    def __init__(self):
        """Initialize Hand."""
        self.cards = []

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suite.
        """
        if len(self.cards) >= 5:
            return False
        for cardd in self.cards:
            if cardd.value == card.value and cardd.suit == card.suit:
                return False
        if card not in self.cards and (card.value in self.values and card.suit in self.suits):
            return True
        return False

    def add_card(self, card: Card):
        """
        Add a card to hand.

        Before adding a card, you would have to check if it can be added.
        """
        if self.can_add_card(card):
            self.cards.append(card)

    def can_remove_card(self, card: Card):
        """
        Check if a card can be removed from hand.

        The only consideration should be that the card is already being held.
        """
        if card in self.cards:
            return True
        return False

    def remove_card(self, card: Card):
        """
        Remove a card from hand.

        Before removing the card, you would have to check if it can be removed.
        """
        if self.can_remove_card(card):
            self.cards.remove(card)

    def get_cards(self):
        """Return a list of cards as objects."""
        for card in self.cards:
            if card.value in self.dict_values.keys():
                card.value = self.dict_values[card.value]
        ccards = sorted(self.cards, key = lambda cards : cards.value,reverse = False)
        return ccards

    def is_straight(self):
        """
        Determine if the hand is a straight.

        A straight hand will have all cards in the order of value.
        Sorting will help you here as the order will vary.

        Examples:
        4 5 6 7 8
        K J 10 Q A

        For the sake of simplicity - A 2 3 4 5 will not be tested.
        You can always consider A to be the highest ranked card.
        """
        if len(self.get_cards()) == 5:
            lowest = None
            for card in self.get_cards():
                if lowest == None:
                    lowest = card.value
                else:
                    if card.value != lowest + 1:
                        return False
                    else:
                        lowest = card.value
            return True
        return False

    def is_flush(self):
        """
        Determine if the hand is a flush.

        In a flush hand all cards are the same suit. Their number value is not important here.
        """
        if len(self.get_cards()) == 5:
            lastsuit = None
            for card in self.get_cards():
                if lastsuit == None:
                    lastsuit = card.suit
                else:
                    if lastsuit != card.suit:
                        return False
            return True
        return False

    def is_straight_flush(self):
        """
        Determine if the hand is a straight flush.

        Such a hand is both straight and flush at the same time.

        """
        if self.is_flush() and self.is_straight():
            return True
        return False

    def is_full_house(self):
        """
        Determine if the hand is a full house.

        A house will have three cards of one value, and two cards of a second value.
        For example:
        2 2 2 6 6
        K J K J K
        """
        c1_checkval = None
        c1_amount = 0
        for card in self.get_cards():
            if c1_checkval == None:
                c1_checkval = card.value
                c1_amount += 1
            else:
                if card.value == c1_checkval:
                    c1_amount += 1
        c2_checkval = None
        c2_amount = 0
        for card in self.get_cards():
            if card.value != c1_checkval:
                if c2_checkval == None:
                    c2_checkval = card.value
                    c2_amount += 1
                else:
                    if card.value == c2_checkval:
                        c2_amount += 1
        if c1_amount == 3 and c2_amount == 2 or c2_amount == 3 and c1_amount == 2:
            return True
        return False

    def is_four_of_a_kind(self):
        """
        Determine if there are four cards of the same value in hand.

        For example:
        2 2 K 2 2
        9 4 4 4 4

        """
        cards = self.get_cards()
        count = {}
        for card in cards:
            if card.value not in count:
                count[card.value] = 0
            count[card.value] += 1
        if len(count) == 2 and set(count.values()) == set([1,4]):
            return True
        return False
            

    def is_three_of_a_kind(self):
        """
        Determine if there are three cards of the same value in hand.

        For Example:
        Q 4 Q Q 7
        5 5 1 5 2

        """
        cards = self.get_cards()
        count = {}
        for card in cards:
            if card.value not in count:
                count[card.value] = 0
            count[card.value] += 1
        if 3 in list(count.values()):
            return True
        return False

    def is_pair(self):
        """
        Determine if there are two kinds of the same value in hand.

        For example:
        5 A 2 K A
        8 7 6 6 5

        """
        cards = self.get_cards()
        count = {}
        for card in cards:
            if card.value not in count:
                count[card.value] = 0
            count[card.value] += 1
        if 2 in list(count.values()):
            return True
        return False

    def get_hand_type(self):
        """
        Return a string representation of the hand.

        Return None (or nothing), if there are less than five cards in hand.

        "straight flush" - Both a straight and a flush
        "flush" - The cards are all of the same suit
        "straight" - The cards can be ordered
        "full house" - Three cards are of the same value while the other two also share a value.
        "four of a kind" - Four cards are of the same value
        "three of a kind" - Three cards are of the same value
        "pair" - Two cards are of the same value
        "high card" - None of the above

        """
        if len(self.get_cards()) < 5:
            return None
        if self.is_straight_flush() == True:
            return "straight flush"
        elif self.is_straight() == True:
            return "straight"
        elif self.is_flush() == True:
            return "flush"
        elif self.is_four_of_a_kind() == True:
            return "four of a kind"
        elif self.is_full_house() == True:
            return "full house"
        elif self.is_three_of_a_kind() == True:
            return "three of a kind"
        elif self.is_pair() == True:
            return "pair"
        return "high card"
        

    def __repr__(self):
        """
        Return a string representation of the hand.

        I got a {type} with cards: {card list}
        I got a straight with cards: 2 of diamonds, 4 of spades, 5 of clubs, 3 of diamonds, 6 of hearts

        If a hand type cannot be yet determined, return a list of cards as so:

        I'm holding {cards}
        I'm holding 2 of diamonds, 4 of spades.

        Order of the cards is not important.
        """
        if self.get_hand_type() != None:
            return f"I got a {self.get_hand_type()} with cards: {self.get_cards()}."
        return f"I'm holding {self.get_cards()}."
        raise NotImplementedError


if __name__ == "__main__":
    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "spades"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "hearts")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "straight"

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "flush"

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "four of a kind"
