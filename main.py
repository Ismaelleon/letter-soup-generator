import pygame
from soup import Soup

pygame.init()


print('Soup Generator')
soup_size = int(input('Insert your soup size: '))
soup_words = input('Insert the words for your soup: ')

soup = Soup(soup_size)
soup.generate(soup_words.split(','))

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Letter soup')

def render ():
    pygame.display.update()
    window.fill((255, 255, 255))
    col_size = window.get_size()[0] / soup.size

    font = pygame.font.SysFont(None, int(col_size))
    for yindex, row in enumerate(soup.soup):
        for xindex, col in enumerate(row):
            letter = font.render(col, True, (0, 0, 0))
            letter_size = font.size(col)

            x = (xindex * col_size) + (col_size / 2) - letter_size[0] / 2
            y = (yindex * col_size) + (col_size / 2) - letter_size[1] / 2
            window.blit(letter, (x, y))

    pygame.image.save(window, "soup.png")
    print('Soup saved on file soup.png')

render()
