import matplotlib.pyplot as plt
import numpy as np

from rules import Rule
import brightness as br
import distance as dist
import power

def union(x, y):
    output = []

    for i in range(len(x)):
        a = max(x[i], y[i])
        output.append(a)
    return output

if(__name__ == '__main__'):
    # main function goes here
    # brightness 0 - 5500 lux
    # distance 0 - 750 cm
    input_dist = float(input('Distance: '))
    input_brightness = float(input('Brightness: '))
    
    rule1 = Rule(dist.very_far(input_dist), br.dark(input_brightness))
    rule1.fuzzificate(1)
    rule2 = Rule(dist.very_far(input_dist), br.low_brightness(input_brightness))
    rule2.fuzzificate(2)
    rule3 = Rule(dist.very_far(input_dist), br.medium_brightness(input_brightness))
    rule3.fuzzificate(3)
    rule4 = Rule(dist.far(input_dist), br.dark(input_brightness))
    rule4.fuzzificate(4)
    rule5 = Rule(dist.far(input_dist), br.low_brightness(input_brightness))
    rule5.fuzzificate(5)
    rule6 = Rule(dist.far(input_dist), br.medium_brightness(input_brightness))
    rule6.fuzzificate(6)
    rule7 = Rule(dist.not_far(input_dist), br.medium_brightness(input_brightness))
    rule7.fuzzificate(7)
    rule8 = Rule(dist.not_far(input_dist), br.medium_brightness(input_brightness))
    rule8.fuzzificate(8)
    rule9 = Rule(dist.not_far(input_dist), br.medium_brightness(input_brightness))
    rule9.fuzzificate(9)
    rule10 = Rule(dist.close(input_dist), br.dark(input_brightness))
    rule10.fuzzificate(10)
    rule11 = Rule(dist.close(input_dist), br.low_brightness(input_brightness))
    rule11.fuzzificate(11)
    rule12 = Rule(dist.close(input_dist), br.medium_brightness(input_brightness))
    rule12.fuzzificate(12)