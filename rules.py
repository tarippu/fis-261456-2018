import numpy as np

import distance as dist
import brightness as br

from graph import draw_graph

class Rule(object):
    def __init__(self, distance, brightness):
        self.distance_membership = distance
        self.brightness_membership = brightness

rule1 = Rule(dist.very_far(), br.dark())
rule2 = Rule(dist.very_far(), br.low_brightness())
rule3 = Rule(dist.very_far(), br.medium_brightness)
rule4 = Rule(dist.far(), br.dark())
rule5 = Rule(dist.far(), br.low_brightness)
rule6 = Rule(dist.far(), br.medium_brightness())
rule7 = Rule(dist.not_far(), br.medium_brightness())
rule8 = Rule(dist.not_far(), br.medium_brightness())
rule9 = Rule(dist.not_far(), br.medium_brightness())
rule10 = Rule(dist.close(), br.dark())
rule11 = Rule(dist.close(), br.low_brightness())
rule12 = Rule(dist.close(), br.medium_brightness())
