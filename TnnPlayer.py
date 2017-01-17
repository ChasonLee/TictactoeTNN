# -*- coding: utf-8 -*-
__author__ = 'Chason'
import math
from TopologyNetwork import TopologyNetwork
class TnnPlayer:
    def __init__(self, ROW = 3, COL = 3, WIN_NUM = 3, tnn = None):
        self.ROW = ROW
        self.COL = COL
        self.WIN_NUM = WIN_NUM
        self.tnn = TopologyNetwork(ROW * COL * 2, ROW * COL)

    def HardCodeTnn(self):
        #Avoid conflict
        for i in range(self.ROW * self.COL):
            self.tnn.outputNodes[i].addInput(self.tnn.inputNodes[i * 2], -100)
            self.tnn.outputNodes[i].addInput(self.tnn.inputNodes[i * 2 + 1], -100)

        # Center occupy
        node = self.tnn.createHiddenNode(name="center occupy")
        node.addInput(self.tnn.inputNodes[self.ROW * self.COL - 1], -10)
        node.addInput(self.tnn.inputNodes[self.ROW * self.COL], -10)
        bias = self.tnn.createHiddenNode(1, name="bias")
        node.addInput(bias, 5)
        self.tnn.outputNodes[int(self.ROW * self.COL / 2)].addInput(node, 5)

        #Defence
        for i in range(self.ROW):
            for j in range(self.COL):
                for m, n in [(1, 1), (1, 0), (1, -1), (0, -1)]:
                    for inv in [1, -1]:
                        ti = i + inv * m
                        tj = j + inv * n
                        for k in range(1, max(self.ROW, self.COL)):
                            if  0 <= ti < self.ROW and 0 <= tj < self.COL:
                                node = self.tnn.createHiddenNode(name="src[%d, %d] def[%d, %d]*%d"%(i, j, ti, tj, k))
                                node.addInput(self.tnn.inputNodes[(ti * self.COL + tj) * 2 + 1], k * 2)
                                self.tnn.outputNodes[i * self.COL + j].addInput(node, 1)
                                ti = ti + inv * m
                                tj = tj + inv * n
                            else:
                                break