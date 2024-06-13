def world_loader(worldMatrixGLOBAL, worldLoadDistance, refferenceX):
    worldMatrix = []
    refferenceX = int(refferenceX)
    for i in range(len(worldMatrixGLOBAL) - 1):
        if i > refferenceX - worldLoadDistance and i < refferenceX + worldLoadDistance:
            intermidateList = [worldMatrixGLOBAL[i], i]
            worldMatrix.append(intermidateList)
    return worldMatrix



def render_distance(self.y, worldLoadDistance, worldSizeY):
    global condition_met
    while time.time == 
    
        if self.y + worldLoadDistance <= worldSizeY:
            dd
        
        time.sleep(0.01)  # Adjust the sleep time as needed to balance CPU usage