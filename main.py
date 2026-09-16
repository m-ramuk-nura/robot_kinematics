from visualization import *
from transformations import *
import numpy as np
from robot import *


def main():
    robot = Robot()

    # DH parameters:
    # [a, alpha, d, theta, joint_type]
    dh_parameters = np.array([
        [0.0,  0.0,  0.30, 0.0, "revolute"],
        [0.40, 0.0,  0.0,  0.0, "revolute"],
        [0.30, 0.0,  0.0, 0.0, "revolute"],
        [0.20, 0.0,  0.0, 0.0, "revolute"],
        [0.10, 0.0,  0.0, 0.0, "revolute"],
        [0.10, 0.0,  0.0, 0.0, "revolute"]
    ], dtype=object)

    robot.init_dh(dh_parameters)

    # Joint angles in radians
    q = np.array([
        0.0,
        np.pi / 4,
        0.0,
        0.0,
        0.0,
        0.0
    ])

    # Forward kinematics
    transformation = robot.forward_kinematics(q)

    print("End-effector transformation:")
    print(transformation)

    # Position
    position = transformation[:3, 3]

    print("\nEnd-effector position:")
    print("x =", position[0])
    print("y =", position[1])
    print("z =", position[2])


if __name__ == "__main__":
    main()