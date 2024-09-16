from random import uniform, randint
from single_particle import Single_Particle 

class Particles():
    def __init__(self, particles_data) -> None:
        self.particles_data = particles_data
        self.active_particles = {}
        self.finished_particles = {}

        for particle_type in self.particles_data.keys():
            self.active_particles[particle_type] = []
            self.finished_particles[particle_type] = []

    def new_particles(self, particle_ID: str, number_of_particles: int, duration: int, position_vector: tuple, velocity_vector: tuple = (0, 0), delta: tuple = (0, 0), blockType = None) -> None:
        position_vector_initial = position_vector
        velocity_vector_initial = velocity_vector
        for i in range(number_of_particles):
            # set particle position
            if position_vector_initial[0] <= position_vector_initial[0] + delta[0]:
                x = uniform(position_vector_initial[0], position_vector_initial[0] + delta[0])
            else:
                x = uniform(position_vector_initial[0] + delta[0], position_vector_initial[0])

            if position_vector_initial[1] <= position_vector_initial[1] + delta[1]:
                y = uniform(position_vector_initial[1], position_vector_initial[1] + delta[1])
            else:
                y = uniform(position_vector_initial[1] + delta[1], position_vector_initial[1])
            position_vector = (x, y)

            # set particle velocity in case it is random
            velocityX, velocityY = velocity_vector_initial
            if type(velocityX) == tuple:
                velocityX = uniform(velocityX[0], velocityX[1])
            if type(velocityY) == tuple:
                velocityY = uniform(velocityY[0], velocityY[1])
            velocity_vector = (velocityX, velocityY)

            # creates the particle
            particle = Single_Particle(particle_ID, duration, position_vector, velocity_vector, blockType)

            # adds the new particle to the list of active particles
            self.active_particles[particle_ID].append(particle)

    def update(self) -> None:
        for particle_type in self.active_particles.keys():
            for particle in self.active_particles[particle_type]:
                # updates the every individual particle
                particle.update(self.particles_data[particle_type])

        # deletes every particle that is finished
        for particle_type in self.active_particles.keys():
            for particle in self.active_particles[particle_type]:
                if particle.end:
                    del self.active_particles[particle_type][self.active_particles[particle_type].index(particle)]

    def get_defined_particles_ID(self) -> list:
        particle_IDs = []
        for particle_ID in self.particles_data.keys():
            particle_IDs.append(particle_ID)
        return particle_IDs
    
    def get_defined_particles_data(self) -> list:
        return self.particles_data
    
    def get_defined_particle_data(self, particle_ID: str) -> list:
        particle_present = False
        for IDs in self.particles_data.keys():
            if IDs == particle_ID:
                particle_present = True

        if not particle_present:
            raise ValueError(f"The particle with the particle ID: '{particle_ID}' is not defined")
        
        return self.particles_data[particle_ID]
    
    def clear_all_particles(self) -> None:
        for particle_type in self.active_particles.keys():
            self.active_particles[particle_type] = []

    def clear_particle_type(self, particle_ID: str) -> None:
        self.active_particles[particle_ID] = []