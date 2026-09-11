import numpy as np
from link import Link

class Robot:
    def __str__(self):
        string = f"Robot Links\n"
        string += f"Link Name\ta\talpha\td\ttheta\tJoint Type\n"
        string += f"---\t---\t---\t---\t---\t---\n"
        for link in self._links:
            string += f"{link.name}\t{link.a}\t{link.alpha}\t{link.d}\t"
            string += f"{link.theta}\t{link.joint_type}\n"
        return ""

    def __repr__(self):
        string = "Robot()"
        return string

    def __init__(self):
        self.links=[]
        self.link_names=[]

    def init_link(self, link_list):
        for link in link_list:
            try:
                assert(isinstance(link, Link))
                self.links.append(link)
                self.link_names.append(link.name)

            except AssertionError:
                raise TypeError("All elements in link_list must be instances of the Link class.")


    def init_dh(dh_parameters):
        dof = dh_parameters.shape[0]
        try:
            assert(dh_parameters.shape[1] == 4)
        except:
            raise("DH Parameters Table not correct")
        
        for i in range(dof):
            name = f"Link_{i}"
            a = dh_parameters[i, 0]
            alpha = dh_parameters[i, 1]
            d = dh_parameters[i, 2]
            theta = dh_parameters[i, 3]
            link = Link(name=name, alpha=alpha, a=a, d=d, theta=theta,  joint_type = joint_type)
            self.links.append(link)
            self.link_names.append(link.name)