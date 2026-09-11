import numpy as np


class Link:
    def __init__(self, name='', alpha=0, a=0, d=0, theta=0, joint_type='revolute', inertia_matrix=None, cog=None, mass=0):

        self.name = name
        self.alpha = alpha
        self.a = a
        self.d = d
        self.theta = theta
        self.joint_type = joint_type
        self.inertia_matrix = (
            np.zeros((3, 3)) if inertia_matrix is None else inertia_matrix
        )
        self.cog = np.zeros(3) if cog is None else cog
        self.mass = mass

    def __str__(self):
        string = f"{self.name}\n"
        string += "Parameter\tValue\n"
        string += "---\t\t---\n"
        string += f"joint\t\t{self.joint_type}\n"
        string += f"alpha\t\t{self.alpha}\n"
        string += f"a\t\t{self.a}\n"
        string += f"d\t\t{self.d}\n"
        string += f"theta\t\t{self.theta}\n"

        return string

    def __repr__(self):
        return (
            f"Link(name={self.name}, alpha={self.alpha}, "
            f"a={self.a}, d={self.d}, theta={self.theta})"
        )

    def transform(self, q):
        alpha = self.alpha
        a = self.a

        if self.joint_type == 'revolute':
            theta = q
            d = self.d
        else:
            theta = self.theta
            d = q

        transformation = np.array([
            [np.cos(theta), -np.sin(theta), 0, a],
            [
                np.sin(theta) * np.cos(alpha),
                np.cos(theta) * np.cos(alpha),
                -np.sin(alpha),
                -np.sin(alpha) * d
            ],
            [
                np.sin(theta) * np.sin(alpha),
                np.cos(theta) * np.sin(alpha),
                np.cos(alpha),
                np.cos(alpha) * d
            ],
            [0, 0, 0, 1]
        ])

        return transformation