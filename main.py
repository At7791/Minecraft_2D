import time

from display import Display
from world_generator import world_generator
from world_generator import rendering
from entity_code import EntityClass
from player_code import PlayerClass
from event_controler import Events 
from world import World
from converter import Converter
from game_data_loader import load_file, save_to_file
from particles import Particles

active_texture_pack = "minecraft_regular_versionfile"

# Block data gets loaded
blocksID = load_file("assets/game_data/block_data.json")

# World creation and generation
sizeX, sizeY = 200, 50
StartWorld = -0
HeightBedrockLeft1 = 2
HeightStoneLeft1 = 20
HeightDirtLeft1 = 30

world = World("assets\local_data\worlds/test_world")

worldLoadRadius = 2
RenderDistance = worldLoadRadius + 5
loadedWorld = {}
loadedWorld = world.loader(loadedWorld, worldLoadRadius, StartWorld)

# Class initialisations
entities = {"player": []}
player = PlayerClass(StartWorld)
entities["player"].append(player)
EntityClass.worldMatrix = loadedWorld
particles = Particles(load_file("assets/game_data/particle_data.json"))

dis = Display(load_file("assets\game_data\settings\display_settings.json"), blocksID, entities, particles.particles_data)

events = Events()
convert = Converter(worldLoadRadius, world.chunkWidth, loadedWorld, dis.zoom, dis.windowSizeX, dis.windowSizeY, entities["player"][0])


# Variables used in the time management
TPS = 20
FPS = 60

durationTick = 1 / TPS
durationFrame = 1 / FPS

ticks = 0

measuredFPS = 0
measuredTPS = 0
waitLoops = 0

currentTime = time.time()
previousTickTime = currentTime
previousFrameTime = currentTime

numberOfFrames = 0
numberOfTicks = 0
preivousSecond = currentTime

accumulatorTicks = 0
elapsedTimeTicks = 0

accumulatorFrames = 0
elapsedTimeFrames = 0

count = 0

running = True

while running:
    # Time calculations
    count += 1
    currentTime = time.time()

    elapsedTimeTicks = currentTime - previousTickTime
    elapsedTimeFrames = currentTime - previousFrameTime

    previousFrameTime = currentTime
    previousTickTime = currentTime

    accumulatorTicks += elapsedTimeTicks
    accumulatorFrames += elapsedTimeFrames

    # Game Tick Loop (20 times per second)
    while accumulatorTicks >= durationTick:
        # world loading chunks
        loadedWorld = world.loader(loadedWorld, worldLoadRadius, int(player.getPlayerCoordinates()[0]))

        # updates converter
        convert.loadedWorld = loadedWorld

        # Entity Updates (except player)
        for entityType in entities.keys():
            for entity in entities[entityType]:
                entity.updateCycle()

                if entityType != "player":
                    entity.updatesPhysics(deltaTime * TPS, convert)

        accumulatorTicks -= durationTick
        numberOfTicks += 1
        ticks += 1

    # Frames and Player physics Loop (as many times per second as there are FPS)
    while accumulatorFrames >= durationFrame:
        deltaTime = accumulatorFrames
        
        # Events
        events.eventsMain()

        # Player and Entity Class updates
        EntityClass.loadedWorld = loadedWorld
        EntityClass.worldLoadRadius = worldLoadRadius
        player.updatesPhysics(events, deltaTime * TPS, convert)

        # Breaking blocks as the player
        player.blockInteractions(blocksID, convert)

        if player.breakBlock == True:
            loadedWorld[convert.chunk_X(player.blockTargetedX)][convert.in_chunk_X(player.blockTargetedX)][convert.to_block_Y(player.blockTargetedY)] = "air"
            player.breakBlock = False

        # Particle Updates
        if events.debugTrigger1:
            particles.new_particles("block_particle", 100, 0.3 * FPS,(dis.XYinWorld(events.mouseX, events.mouseY)), ((-0.1, 0.1), (-0.1, 0.1)), (0, 0), "deepslate") # (-1, 0)
            # print(loadedWorld)
            for chunkX in loadedWorld.keys():
                print(f"Chunk number: {chunkX}")
                for slice in loadedWorld[chunkX]:
                    print(slice)

        particles.update()

        # Display Updates
        dis.displayMain(loadedWorld, entities, particles, convert)
        dis.displayOverlay(events, measuredFPS, measuredTPS, waitLoops, convert)
        dis.displayUpdate()

        # Exit game
        if events.exitGame:
            world.save(loadedWorld)
            running = False
        
        accumulatorFrames -= durationFrame
        numberOfFrames += 1

    # Displays the number of measured FPS and TPS (DEBUG)
    if time.time() - preivousSecond >= 1:
        measuredFPS = numberOfFrames
        measuredTPS = numberOfTicks
        waitLoops = count
        numberOfFrames = 0
        numberOfTicks = 0
        count = 0
        preivousSecond = time.time()
    time.sleep(0.001)
    
dis.close()
quit()
