import pygame

pygame.init()
displayGame = pygame.display.set_mode(size=(800, 600))
pygame.display.set_caption("mhh")
clock = pygame.time.Clock()
print(pygame.event.__doc__)
crashed=False
count=0
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        count+=1
        print(count)
        if event.type == pygame.quit():
            crashed=True
        print(event)
        
pygame.quit()

        
    