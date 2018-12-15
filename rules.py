import matplotlib.pyplot as plt
import numpy as np

import brightness as br
import distance as dist
import power

from graph import draw_graph

def union(x, y):
    output = []

    for i in range(len(x)):
        a = max(x[i], y[i])
        output.append(a)
    return output

class Rule(object):
    def __init__(self, distance, brightness):
        self.distance_membership = distance
        self.ranges = np.arange(0, 14, 1)
        self.brightness_membership = brightness

    def fuzzificate(self, rule_no):
        alpha_cut = min(self.distance_membership, self.brightness_membership)
        ranges = self.ranges
        rule_outs = []

        if(rule_no == 1):
            y1 = []
            for i in range(len(ranges)):
                y1.append(round(power.very_high(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y1, 'rule' + str(1), 1)
            return y1
        elif(rule_no == 2):
            y2 = []
            for i in range(len(ranges)):
                y2.append(round(power.very_high(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y2, 'rule' + str(2), 2)
            return y2
        elif(rule_no == 3):
            y3 = []
            for i in range(len(ranges)):
                y3.append(round(power.high(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y3, 'rule' + str(3), 3)
            return y3
        elif(rule_no == 4):
            y4 = []
            for i in range(len(ranges)):
                y4.append(round(power.high(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y4, 'rule' + str(4), 4)
            return y4
        elif(rule_no == 5):
            y5 = []
            for i in range(len(ranges)):
                y5.append(round(power.low(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y5, 'rule' + str(5), 5)
            return y5
        elif(rule_no == 6):
            y6 = []
            for i in range(len(ranges)):
                y6.append(round(power.low(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y6, 'rule' + str(6), 6)
            return y6
        elif(rule_no == 7):
            y7 = []
            for i in range(len(ranges)):
                y7.append(round(power.low(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y7, 'rule' + str(7), 7)
            return y7
        elif(rule_no == 8):
            y8 = []
            for i in range(len(ranges)):
                y8.append(round(power.low(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y8, 'rule' + str(8), 8)
            return y8
        elif(rule_no == 9):
            y9 = []
            for i in range(len(ranges)):
                y9.append(round(power.very_low(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y9, 'rule' + str(9), 9)
            return y9
        elif(rule_no == 10):
            y10 = []
            for i in range(len(ranges)):
                y10.append(round(power.low(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y10, 'rule' + str(10), 10)
            return y10
        elif(rule_no == 11):
            y11 = []
            for i in range(len(ranges)):
                y11.append(round(power.very_low(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y11, 'rule' + str(11), 11)
            return y11
        elif(rule_no == 12):
            y12 = []
            for i in range(len(ranges)):
                y12.append(round(power.very_low(ranges[i], alpha_cut), 2))
            draw_graph(ranges, y12, 'rule' + str(12), 12)
            return y12
        
