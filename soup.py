import random

class Soup:
    def __init__ (self, size):
        self.soup = []
        self.positions = ['horizontal', 'vertical', 'diagonal']
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.show_words = False
        self.size = size

        for i in range(size):
            self.soup.append([])
            for j in range(size):
                self.soup[i].append('*')

    def remove_letter (self, x, y):
        self.soup[y][x] = '*'

    def generate (self, words_arr):
        for word_index, word in enumerate(words_arr):
            word = word.upper()
            position = random.choice(self.positions)
            reverse = random.choice([True, False])

            if reverse == True:
                word = word[::-1]

            letter_positions = []

            if position == 'horizontal':
                x = random.randrange(0, len(self.soup) - len(word) - 1)
                y = random.randrange(0, len(self.soup) - 1)

                for index, char in enumerate(word):
                    if self.soup[y][x + index] == '*':
                        self.soup[y][x + index] = char
                        letter_positions.append({ 'x': x + index, 'y': y })
                    else:
                        for position in letter_positions:
                            self.remove_letter(position['x'], position['y'])
                        words_arr.append(word)
                        break
            elif position == 'vertical':
                x = random.randrange(0, len(self.soup) - 1)
                y = random.randrange(0, len(self.soup) - len(word) - 1)

                for index, char in enumerate(word):
                    if self.soup[y + index][x] == '*':
                        self.soup[y + index][x] = char
                        letter_positions.append({ 'x': x, 'y': y + index })
                    else:
                        for position in letter_positions:
                            self.remove_letter(position['x'], position['y'])
                        words_arr.append(word)
                        break
            elif position == 'diagonal':
                x = random.randrange(0, len(self.soup) - len(word) - 1)
                y = random.randrange(0, len(self.soup) - len(word) - 1)

                for index, char in enumerate(word):
                    if self.soup[y + index][x + index] == '*':
                        self.soup[y + index][x + index] = char
                        letter_positions.append({ 'x': x + index, 'y': y + index })
                    else:
                        for position in letter_positions:
                            self.remove_letter(position['x'], position['y'])
                        words_arr.append(word)
                        break

        self.randomize()

    def randomize (self):
        for yindex, row in enumerate(self.soup):
            for xindex, letter in enumerate(row):
                if letter == '*':
                    letter = random.choice(self.letters)
                    self.soup[yindex][xindex] = letter
