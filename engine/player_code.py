from entity_code import EntityClass
from hitbox_code import Hitboxes
from math import floor, ceil

class PlayerClass(EntityClass):
    def __init__(self, StartWorld):
        self.type = "player"
        super().__init__(self.type)
        self.hitbox = Hitboxes(0.6, 1.8)
        self.x, self.y = float(StartWorld), float(5)
        self.count = 0
        self.isSprinting = False
        self.isCrouching = False

        self.blockTargetedX, self.blockTargetedY = 0, 0
        self.lastBlockTargetedX, self.lastBlockTargetedY = None, None
        self.targetedBlockNatrue = None
        
        self.mining = False
        self.minableTargeted = False
        self.breakTimer = None
        self.breakBlock = False
        self.breakProgress = 0

    # Updates the variable cycling used to display the player sprites
    def updateCycle(self):
        if self.velocityX != 0:
            if self.isSprinting == True:
                if self.cycle >= 20:
                    self.cycle = 0
                else:
                    self.cycle += 2
            else:
                if self.cycle >= 20:
                    self.cycle = 0
                else:
                    self.cycle += 1
        else:
            self.cycle = 0

    def miningDuration(self, blockHardness):
        if blockHardness == 0:
            return 0
        
        speedMultiplier = 1
        blockDamage = speedMultiplier / blockHardness
        blockDamage /= 30
        
        # print(blockDamage, ceil(1 / blockDamage))
        if blockDamage > 1:
            return 0
        return ceil(1 / blockDamage)

    def blockInteractions(self, blocksID, convert):

        self.minableTargeted = False
        if convert.is_block_in_world((self.blockTargetedX, self.blockTargetedY)):
            self.targetedBlockNatrue = convert.blockNature((self.blockTargetedX, self.blockTargetedY))
            if self.targetedBlockNatrue != "air":
                self.minableTargeted = True

        if self.mining:
            # Initialize the timer for the block to break
            if self.breakTimer == None:
                if self.minableTargeted:
                    self.numberOfTicks = self.miningDuration(blocksID[self.targetedBlockNatrue][1])
                    if self.numberOfTicks == 0: # instant mine
                        self.breakBlock = True
                    else:
                        self.breakTimer = 0
                        self.breakProgress = 0
            # A block is already beeing broken
            else:
                # The player switched to another block
                if self.lastBlockTargetedX != self.blockTargetedX or self.lastBlockTargetedY != self.blockTargetedY:
                    self.breakTimer = None
                # The block broke in this tick
                elif self.breakTimer >= self.numberOfTicks and self.numberOfTicks >= 0:
                    self.breakTimer = None
                    self.breakBlock = True
                    self.breakProgress = 0
                # The block continues to be broken
                else:
                    self.breakTimer += 1
                    if self.numberOfTicks > 0:
                        self.breakProgress = floor(10 * (self.breakTimer / self.numberOfTicks))
                        if self.breakProgress == 10:
                            self.breakProgress = 9
                    else:
                        self.breakProgress = 0
        else:
            self.breakTimer = None

        self.lastBlockTargetedX = self.blockTargetedX
        self.lastBlockTargetedY = self.blockTargetedY

    def updatesPhysics(self, events, calibrationFPS, convert):
        super().updatesPhysics(calibrationFPS, convert)
        self.count += 1

        # applies the effect to the player movement of the key presses
        if events.forwardKeyPressed == True:
            self.accelerationX = 0.1
        elif events.backwardKeyPressed == True:
            self.accelerationX = -0.1
        else:
            self.accelerationX = 0
                
        if events.jumpKeyPressed == True and self.onGround == True:
            self.velocityY = 0.53

        # Makes the player sprint, crouch or walk normally
        if events.crouchKeyPressed == True:
            self.accelerationX *= 0.3
            self.hitbox.update(self.x, self.y)
            self.isSprinting = False
            self.isCrouching = True
        elif events.sprintKeyPressed == True:
            self.accelerationX *= 1.3
            if self.velocityX != 0:
                self.isSprinting = True
            self.isCrouching = False
        else:
            self.isSprinting = False
            self.isCrouching = False
        
        # handels blockinteraction
        self.blockTargetedX, self.blockTargetedY = convert.XYinWorld(events.mouseX, events.mouseY, True)

        if events.clickingLeft == True:
            self.mining = True
        else:
            self.mining = False

        # Debug keys
        if events.debugTrigger1 == True:
            self.count = 0

    def getPlayerCoordinates(self):
        return (self.x, self.y)