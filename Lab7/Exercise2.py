import pygame

def next():
    global songs
    songs = songs[1:] + [songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

def rev(s):
    s.reverse()
    return s

def prev():
    global songs
    rev(songs)
    songs= songs[1:] + [songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

pygame.init()
screen= pygame.display.set_mode((500,500))

songs=['OST.mp3', 'последняя любовь моргенштерн.mp3', 'Ghetto Dogs - Алмата.mp3']

blue=(0,0,225)
for i in songs:
    pygame.mixer.music.load(i)
    pygame.mixer.music.play(0)

play=False
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = not play
                    if play: pygame.mixer.music.pause()
                    else: pygame.mixer.music.unpause()
            
            
                elif event.key == pygame.K_RIGHT:
                    play= not play
                    if play: next()

                elif event.key == pygame.K_LEFT:
                    play= not play
                    if play: prev()
    
    screen.fill(blue)   
    pygame.display.flip()