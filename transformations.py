import numpy as np

def transl(x, y, z):
    transform = np.eye(4)
    transform[0,3] = x
    transform[1,3] = y
    transform[2,3] = z

    return transform

def rotx(roll):
    rotation = np.eye(3)
    rotation = np.eye(3)
    rotation[1][1] = np.cos(roll)
    rotation[1][2] = -1 * np.sin(roll)
    rotation[2][1] = np.sin(roll)
    rotation[2][2] = np.cos(roll)

    return rotation

def roty(pitch):
    rotation = np.eye(3)
    rotation[0][0] = np.cos(pitch)
    rotation[0][2] = np.sin(pitch)
    rotation[2][0] = -1 * np.sin(pitch)
    rotation[2][2] = np.cos(pitch)

    return rotation

def rotz(yaw):
    rotation = np.eye(3)
    rotation[0][0] = np.cos(yaw)
    rotation[0][1] = -1 * np.sin(yaw)
    rotation[1][0] = np.sin(yaw)
    rotation[1][1] = np.cos(yaw)

    return rotation


def rpy2tr(roll, pitch, yaw):
    rotation_z = rotz(yaw)
    rotation_y = roty(pitch)
    rotation_x = rotx(roll)

    rotation = rotation_z @ rotation_y @ rotation_x

    transformation = np.eye(4)
    transformation[:3, :3] = rotation

    return transformation

def tr2rpy(transformation):
    rotation = transformation[:3, :3]

    roll = np.arctan2(rotation[2, 1], rotation[2, 2])
    pitch = np.arctan2(-rotation[2, 0], np.sqrt(rotation[2, 1]**2 + rotation[2, 2]**2))
    yaw = np.arctan2(rotation[1, 0], rotation[0, 0])

    return roll, pitch, yaw