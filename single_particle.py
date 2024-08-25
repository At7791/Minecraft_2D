from random import uniform
class Single_Particle():
    blockParticleProportions = 0.25
    def __init__(self, particle_ID, duration, position_vector, velocity_vector, blockType) -> None:
        self.ID = particle_ID
        self.duration = duration
        self.end = False
        self.x, self.y = position_vector
        self.velocityX, self.velocityY = velocity_vector
        self.cycle = 0
        self.cycle_texture = 0

        if particle_ID == "block_particle":
            self.positionOnBlockTexture = (uniform(0, 1 - self.__class__.blockParticleProportions), uniform(0, 1 - self.__class__.blockParticleProportions), self.__class__.blockParticleProportions, self.__class__.blockParticleProportions)
            self.blockType = blockType

    def update(self, data: list) -> None:
        path, number_of_textures, size, color, gravity, drag, phase_duration = data
        # counts down the particle duration which acts like a timer

        duration_decrement = False
        if phase_duration == None:
            duration_decrement = True
        else:
            # updates the texture cycle
            self.cycle += 1
            if self.cycle >= phase_duration:
                self.cycle = 0
                self.cycle_texture += 1
            
            if self.cycle_texture >= number_of_textures:
                self.cycle_texture = 0
                duration_decrement = True

        # declares itself finished with 'self.end'
        if self.duration <= 0:
            self.end = True
            return
        
        if duration_decrement:
            self.duration -= 1
        
        if phase_duration != None and self.duration <= 0:
            self.end = True
            return

        # applies physics to the particles
        self.velocityX += gravity[0]
        self.velocityY += gravity[1]

        self.velocityX -= self.velocityX * drag
        self.velocityY -= self.velocityY * drag

        self.x += self.velocityX
        self.y += self.velocityY