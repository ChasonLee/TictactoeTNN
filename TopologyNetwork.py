# -*- coding: utf-8 -*-
__author__ = 'Chason'
from TopologyNode import Node

class TopologyNetwork:
    def __init__(self, inputNum, outputNum):
        self.inputNum = inputNum
        self.outputNum = outputNum
        self.hiddenNum = 0
        self.inputNodes = [Node(i) for i in range(inputNum)]
        self.outputNodes = [Node(i) for i in range(outputNum)]
        self.hiddenNodes = []
        self.beatFlag = False

    def forwardPropagation(self):
        for node in self.hiddenNodes:
            if node.getInputNum() > 0:
                node.activation(self.beatFlag)
        for node in self.outputNodes:
            if node.getInputNum() > 0:
                node.activation(self.beatFlag)
        self.beatFlag = not self.beatFlag

    def maxOutput(self):
        maxvalue = -2
        res = None
        for i, node in enumerate(self.outputNodes):
            if maxvalue < node.value:
                maxvalue = node.value
                res = i
        return res

    def createHiddenNode(self, value = 0, name = ""):
        node = Node(self.hiddenNum, self.beatFlag, value=value, name=name)
        self.hiddenNodes.append(node)
        self.hiddenNum += 1
        return node

    def showStructure(self):
        print "/******************************************************************************************\\"

        print "|\tinput nodes:\t"
        for node in self.inputNodes:
            print "\t", node.value,
            if node.id % 6 == 5:
                print
        print

        for node in self.hiddenNodes:
            print "|\thidden node%d(%s):\t%f"%(node.id, node.name, node.value)

        print
        for node in self.hiddenNodes:
            if node.getInputNum() > 0:
                print "|\t%d neurons connected to hidden node%d(%s):"%(node.getInputNum(), node.id, node.name)
                for i, inputNode in enumerate(node.inputs):
                    if inputNode.flag == None:
                        print "|\t\tinput node%d,\ttheta: %f" % (inputNode.id, node.thetas[i])
                    else:
                        print "|\t\thidden node%d(%s),\ttheta: %f"%(inputNode.id, inputNode.name, node.thetas[i])
        for node in self.outputNodes:
            if node.getInputNum() > 0:
                print "|\t%d neurons connected to output node%d:"%(node.getInputNum(), node.id)
                for i, inputNode in enumerate(node.inputs):
                    if inputNode.flag == None:
                        print "|\t\tinput node%d,\ttheta: %f" % (inputNode.id, node.thetas[i])
                    else:
                        print "|\t\thidden node%d(%s),\ttheta: %f"%(inputNode.id, inputNode.name, node.thetas[i])


        print "\n|\toutput nodes:\t"
        for node in self.outputNodes:
            print "\t%.6f"%node.value,
            if node.id % 3 == 2:
                print

        print "\******************************************************************************************/"