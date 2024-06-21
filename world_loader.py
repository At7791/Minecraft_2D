def world_loader(worldMatrixGLOBAL, worldLoadDistance, refferenceX):
    worldMatrix = []
    refferenceX = int(refferenceX)
    for i in range(len(worldMatrixGLOBAL) - 1):
        if i > refferenceX - worldLoadDistance and i < refferenceX + worldLoadDistance:
            intermidateList = [worldMatrixGLOBAL[i], i]
            worldMatrix.append(intermidateList)
    return worldMatrix
