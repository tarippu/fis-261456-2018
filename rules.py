import numpy as np

import distance as dist
import brightness as br
import power

from graph import draw_graph

class Rule(object):
    def __init__(self, distance, brightness):
        self.distance_membership = distance
        self.ranges = np.arange(0, 14, 1)
        self.brightness_membership = brightness

    def fuzzificate(self, rule_no):
        alpha_cut = min(self.distance_membership, self.brightness_membership)

        ranges = self.ranges
        y = []

        if(rule_no == 1):
            for i in range(len(ranges)):
                y.append(round(power.very_high(ranges[i], alpha_cut), 2))
        elif(rule_no == 2):
            for i in range(len(ranges)):
                y.append(round(power.very_high(ranges[i], alpha_cut), 2))
        elif(rule_no == 3):
            for i in range(len(ranges)):
                y.append(round(power.high(ranges[i], alpha_cut), 2))
        elif(rule_no == 4):
            for i in range(len(ranges)):
                y.append(round(power.high(ranges[i], alpha_cut), 2))
        elif(rule_no == 5):
            for i in range(len(ranges)):
                y.append(round(power.low(ranges[i], alpha_cut), 2))
        elif(rule_no == 6):
            for i in range(len(ranges)):
                y.append(round(power.low(ranges[i], alpha_cut), 2))
        elif(rule_no == 7):
            for i in range(len(ranges)):
                y.append(round(power.low(ranges[i], alpha_cut), 2))
        elif(rule_no == 8):
            for i in range(len(ranges)):
                y.append(round(power.low(ranges[i], alpha_cut), 2))
        elif(rule_no == 9):
            for i in range(len(ranges)):
                y.append(round(power.very_low(ranges[i], alpha_cut), 2))
        elif(rule_no == 10):
            for i in range(len(ranges)):
                y.append(round(power.low(ranges[i], alpha_cut), 2))
        elif(rule_no == 11):
            for i in range(len(ranges)):
                y.append(round(power.very_low(ranges[i], alpha_cut), 2))
        elif(rule_no == 12):
            for i in range(len(ranges)):
                y.append(round(power.very_low(ranges[i], alpha_cut), 2))

        draw_graph(ranges, y, 'rule' + str(rule_no), rule_no)
        return y
