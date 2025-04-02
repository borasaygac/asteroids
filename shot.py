from circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, x, y, radius):
          super().__init__(x, y, radius)

    def draw(self, screen):
         return super().draw(screen)
    
    def update(self, dt):
         return super().update(dt)