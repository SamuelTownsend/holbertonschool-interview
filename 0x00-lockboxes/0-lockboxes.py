#!/usr/bin/python3
''' Module woks to see if a set of boxes can all be opened '''
def canUnlockAll(boxes):
    ''' Will return true if all boxes can be opened. If not it wil return false '''
    avKeys = [0]
    # Loop through availableKeys adding new keys as we go
    for x in avKeys:
        for key in boxes[x]:
            # Append key if it is within boxes range and not yet obtained
            if key not in avKeys and key < len(boxes):
                avKeys.append(key)
    
    x = 0
    while x < len(boxes):
        if x not in avKeys:
            return False
        x += 1
