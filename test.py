# -*- coding: utf-8 -*-
__author__ = 'Chason'
# import pickle
# from EvolutionNeuralNetwork import *
#
# f = open("EnnPlayer.data")
# load_player = pickle.load(f)
# f.close()
#
# load_player.enn.show_structure()

# from TopologyNetwork import TopologyNetwork
# from TopologyNode import Node
# tnn = TopologyNetwork(18, 9)
# node = tnn.createHiddenNode()
# node.addInput(tnn.inputNodes[0], 0.3)
#
# tnn.showStructure()
from TnnPlayer import TnnPlayer
from GameBoard import GameBoard
tp = TnnPlayer()
tp.HardCodeTnn()
tp.tnn.inputNodes[2].value = 0
tp.tnn.forwardPropagation()
tp.tnn.showStructure()
gb = GameBoard()
gb.Move(tp.tnn.maxOutput(),1)
gb.ShowBoard()