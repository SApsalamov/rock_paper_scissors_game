import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock Paper Scissors")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
rock_image = pygame.image.load(r"img\rock.png")
paper_image = pygame.image.load(r"img\paper.png")
scissors_image = pygame.image.load(r"img\scissors.png")


# Resize images
OBJECT_HEIGHT = 50
OBJECT_WIDTH = 50
rock_image = pygame.transform.scale(rock_image, (OBJECT_WIDTH, OBJECT_HEIGHT))
paper_image = pygame.transform.scale(paper_image, (OBJECT_WIDTH, OBJECT_HEIGHT))
scissors_image = pygame.transform.scale(scissors_image, (OBJECT_WIDTH, OBJECT_HEIGHT))

class GameObject:
    def __init__(self, image, initial_position):
        self.image = image
        self.position = initial_position
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # Keep objects within the boundaries of the screen
        if self.position[0] < 0 or self.position[0] > width - OBJECT_WIDTH:
            self.velocity[0] *= -1
        if self.position[1] < 0 or self.position[1] > height - OBJECT_HEIGHT:
            self.velocity[1] *= -1

    def draw(self):
        screen.blit(self.image, self.position)

    def transform(self, new_image):
        self.image = new_image

class CollisionHandler:
    def __init__(self):
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)

    def check_collisions(self):
        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                obj1 = self.objects[i]
                obj2 = self.objects[j]
                if self.distance(obj1.position, obj2.position) < OBJECT_HEIGHT:
                    self.handle_collision(obj1, obj2)

    def handle_collision(self, object1, object2):
        if object1.image == rock_image and object2.image == paper_image:
            object1.transform(paper_image)
        elif object1.image == paper_image and object2.image == scissors_image:
            object1.transform(scissors_image)
        elif object1.image == scissors_image and object2.image == rock_image:
            object1.transform(rock_image)
        elif object2.image == rock_image and object1.image == paper_image:
            object2.transform(paper_image)
        elif object2.image == paper_image and object1.image == scissors_image:
            object2.transform(scissors_image)
        elif object2.image == scissors_image and object1.image == rock_image:
            object2.transform(rock_image)

    def distance(self, pos1, pos2):
        return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

class Game:
    def __init__(self):
        self.collision_handler = CollisionHandler()
        self.create_objects()

    def create_objects(self):
        for _ in range(10):
            rock_object = GameObject(rock_image, [random.randint(0, width - OBJECT_WIDTH), random.randint(0, height - OBJECT_HEIGHT)])
            paper_object = GameObject(paper_image, [random.randint(0, width - OBJECT_WIDTH), random.randint(0, height - OBJECT_HEIGHT)])
            scissors_object = GameObject(scissors_image, [random.randint(0, width - OBJECT_WIDTH), random.randint(0, height - OBJECT_HEIGHT)])

            self.collision_handler.add_object(rock_object)
            self.collision_handler.add_object(paper_object)
            self.collision_handler.add_object(scissors_object)

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen
            screen.fill(WHITE)

            # Update and draw the GameObjects
            for object in self.collision_handler.objects:
                object.update()
                object.draw()

            # Check collisions
            self.collision_handler.check_collisions()

            pygame.display.flip()

        # Quit the game
        pygame.quit()

# Create a Game object and run the game
game = Game()
game.run()
