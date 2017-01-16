# -*- coding: utf-8 -*-
__author__ = 'Chason'
from TopologyNetwork import TopologyNetwork
class TnnPlayer:
    def __init__(self, ROW = 3, COL = 3, WIN_NUM = 3, tnn = None):
        self.ROW = ROW
        self.COL = COL
        self.WIN_NUM = WIN_NUM
        self.tnn = TopologyNetwork(ROW * COL * 2, ROW * COL)

    def HardCodeTnn(self):
        # center occupy
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[1], 5)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[3], 5)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[5], 5)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[7], 5)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[11], 5)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[13], 5)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[15], 5)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[17], 5)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[8], -100)
        self.tnn.outputNodes[4].addInput(self.tnn.inputNodes[9], -100)
        node = self.tnn.createHiddenNode()
        node.addInput(self.tnn.inputNodes[8], -10)

