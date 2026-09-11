import numpy as np
from link import Link

class Robot:
    def __init__(self):
        self._links=[]
        self._link_names=[]

    def init_link(self, link_list):
        self._lin