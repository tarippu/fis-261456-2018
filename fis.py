import matplotlib.pyplot as plt
import numpy as np

from rules import Rule, union
import brightness as br
import distance as dist
import power

if(__name__ == '__main__'):
    # main function goes here
    # brightness 0 - 5500 lux
    # distance 0 - 750 cm
    input_dist = float(input('Distance: '))
    input_brightness = float(input('Brightness: '))
    rule_output = []
    y = 0
    yx = 0
    
    rule1 = Rule(dist.very_far(input_dist), br.dark(input_brightness))
    rule_output.append(rule1.fuzzificate(1))
    rule2 = Rule(dist.very_far(input_dist), br.low_brightness(input_brightness))
    rule_output.append(rule2.fuzzificate(2))
    rule3 = Rule(dist.very_far(input_dist), br.medium_brightness(input_brightness))
    rule_output.append(rule3.fuzzificate(3))
    rule4 = Rule(dist.far(input_dist), br.dark(input_brightness))
    rule_output.append(rule4.fuzzificate(4))
    rule5 = Rule(dist.far(input_dist), br.low_brightness(input_brightness))
    rule_output.append(rule5.fuzzificate(5))
    rule6 = Rule(dist.far(input_dist), br.medium_brightness(input_brightness))
    rule_output.append(rule6.fuzzificate(6))
    rule7 = Rule(dist.not_far(input_dist), br.medium_brightness(input_brightness))
    rule_output.append(rule7.fuzzificate(7))
    rule8 = Rule(dist.not_far(input_dist), br.medium_brightness(input_brightness))
    rule_output.append(rule8.fuzzificate(8))
    rule9 = Rule(dist.not_far(input_dist), br.medium_brightness(input_brightness))
    rule_output.append(rule9.fuzzificate(9))
    rule10 = Rule(dist.close(input_dist), br.dark(input_brightness))
    rule_output.append(rule10.fuzzificate(10))
    rule11 = Rule(dist.close(input_dist), br.low_brightness(input_brightness))
    rule_output.append(rule11.fuzzificate(11))
    rule12 = Rule(dist.close(input_dist), br.medium_brightness(input_brightness))
    rule_output.append(rule12.fuzzificate(12))

    output = union(rule_output[0], rule_output[1])
    output = union(output, rule_output[2])
    output = union(output, rule_output[3])
    output = union(output, rule_output[4])
    output = union(output, rule_output[5])
    output = union(output, rule_output[6])
    output = union(output, rule_output[7])
    output = union(output, rule_output[8])
    output = union(output, rule_output[9])
    output = union(output, rule_output[10])
    output = union(output, rule_output[11])
    
    print("output: ", rule_output)

    for i in range(len(rule_output)):
        y += rule1.ranges[i] * output[i]
        yx += output[i]
    centroid = y / yx

    print("centroid: ", centroid)
    plt.figure(0)
    plt.plot(rule1.ranges, output)
    plt.savefig("output.png", bbox_inches='tight')
