import random


class Cards:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __eq__(self, other):
        return (self.value == other.value) or (self.color == other.color)

    def __str__(self):
        return f"{self.color} {self.value}"


class Deck:
    COLORS = ['красный', "зеленый", "желтый", "синий"]
    VALUES = range(5)

    def __init__(self):
        self.cards = [Cards(i, j) for i in self.COLORS for j in self.VALUES]
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        return None


class Play:
    def __init__(self, name, bot=False):
        self.name = name
        self.hand = []
        self.bot = bot

    def draw(self, deck, count=1):
        for _ in range(count):
            card = deck.draw()
            if card:
                self.hand.append(card)

    def pl(self, ind, top_card):
        if 0 <= ind < len(self.hand):
            make_card = self.hand[ind]
            if make_card.__eq__(top_card):
                return self.hand.pop(ind)
        return None

    def show_cards(self):
        return ", ".join(f"Карта №{p}. {t}" for p, t in enumerate(self.hand))

    def __len__(self):
        return len(self.hand)

    def bot_move(self, top_card, deck):
        for i, n in enumerate(self.hand):
            if n == top_card:
                return self.hand.pop(i)
        self.draw(deck, 1)
        return None


class Game:
    def __init__(self):
        self.deck = Deck()
        self.play = Play('ИГРОК')
        self.bot = Play('БОТ', bot=True)
        self.players = [self.play, self.bot]
        for u in self.players:
            u.draw(self.deck, 5)
        self.top_card = self.deck.draw()
        self.scores = {self.play.name: 0, self.bot.name: 0}

    def calculate_score(self, winner, loser):
        # Очки = количество карт оставшихся у проигравшего
        points = len(loser.hand)
        self.scores[winner.name] += points
        print(f"{winner.name} получает {points} очков! Текущий счет: {self.scores}")

    def start(self):
        print('Игра началась!')
        res = random.randint(0, 1)
        while len(self.play) > 0 and len(self.bot) > 0:
            cur = self.players[res]
            if cur.bot:
                print('Ход БОТА.')
            else:
                print('Ход ИГРОКА.')

            if cur.bot:
                print('Карты БОТА: ***')
                played = cur.bot_move(self.top_card, self.deck)
                if played:
                    print(f'БОТ кинул: {played}')
                    self.top_card = played
                else:
                    print('БОТ взял карту!')
            else:
                print(f'ВАШИ карты: {self.play.show_cards()}')
                can_play = any(w == self.top_card for w in self.play.hand)
                if not can_play and not self.deck.cards:
                    print(f'Карты кончились, вы проиграли :(')
                    self.calculate_score(self.bot, self.play)
                    return
                num = input("Введите номер карты или БЕРУ: ")
                if num == "БЕРУ":
                    self.play.draw(self.deck, 1)
                    continue
                if num.isdigit():
                    ans = self.play.pl(int(num), self.top_card)
                    if ans:
                        self.top_card = ans
                    else:
                        print(f'Мы не можем пойти с этой карты!')

            res = 1 - res

        if len(self.bot) == 0:
            print('БОТ выиграл!')
            self.calculate_score(self.bot, self.play)
        else:
            print("ВЫ выиграли!")
            self.calculate_score(self.play, self.bot)


if __name__ == '__main__':
    game = Game()
    game.start()
