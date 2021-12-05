from dataclasses import dataclass
from typing import List


@dataclass
class Number:
    number: int
    seen: bool = False


@dataclass
class Row:
    numbers: List[Number]
    bingo: bool = False

    @property
    def is_bingo(self):
        self.bingo = all(n.seen for n in self.numbers)
        return self.bingo

    def check_number(self, num: int):
        for my_num in self.numbers:
            if my_num.number == num:
                my_num.seen = True
                break

    @property
    def score(self):
        return sum(int(n.number) for n in self.numbers if not n.seen)


@dataclass
class Card:
    rows: List[Row]

    def check_number(self, num: int):
        # Check rows
        for row in self.rows:
            row.check_number(num)
            if row.is_bingo:
                return True
        # Check columns
        for col in range(5):
            if all(self.rows[row].numbers[col].seen for row in range(5)):
                return True

    @property
    def score(self):
        return sum(r.score for r in self.rows)


@dataclass
class Game:
    cards: List[Card]
    game_numbers: List[int]

    def play_game(self):
        results = []
        print(f"Playing game ... !")
        for number in self.game_numbers:
            for idx, card in enumerate(self.cards):
                bingo = card.check_number(number)
                if bingo:
                    self.cards.remove(card)
                    results.append(number * card.score)
                    break
        return results


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 01: A simple list of numbers
    with open("numbers") as f:
        list_of_numbers = f.readline()
        list_of_numbers = [int(n) for n in list_of_numbers.split(",")]

    with open("input") as f:
        list_of_cards = []
        raw_cards = f.read().split("\n\n")
        for card in raw_cards:
            list_of_rows = []
            rows = card.split("\n")
            for row in rows:
                row_to_add = Row([Number(int(n.strip())) for n in row.split()])
                list_of_rows.append(row_to_add)
            list_of_cards.append(Card(list_of_rows))

    game = Game(list_of_cards, list_of_numbers)
    results = game.play_game()
    print(results[0], results[-1])
