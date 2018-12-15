import matplotlib.pyplot as plt

def very_low(power, alpha):
    if(0 <= power <= 4):
        membership_value = ((-1/4) * power) + 1
        if membership_value > alpha:
            membership_value = alpha
    else:
        membership_value = 0
    return membership_value

def low(power, alpha):
    if(3.75 <= power <= 6):
        membership_value = 1 - abs((power - (9.75/2)) / (6 - (9.75/2)))
        if membership_value > alpha:
            membership_value = alpha
    else:
        membership_value = 0
    return membership_value

def high(power, alpha):
    if(5.5 <= power <= 10):
        membership_value = 1 - abs((power - (15.5/2)) / (10 - (15.5/2)))
        if membership_value > alpha:
            membership_value = alpha
    else:
        membership_value = 0
    return membership_value

def very_high(power, alpha):
    if(9 <= power <= 13):
        membership_value = 1 - abs((power - (22/2)) / (13 - (22/2)))
        if membership_value > alpha:
            membership_value = alpha
    else:
        membership_value = 0
    return membership_value

# y1 = []
# y2 = []
# y3 = []
# y4 = []
# x1 = []
# plt.figure()
# for x in range(0, 14):
#     x1.append(x)
#     y1.append(very_low(x,x))
#     y2.append(low(x, x))
#     y3.append(high(x, x))
#     y4.append(very_high(x, x))

# plt.plot(x1, y1)
# plt.plot(x1, y2)
# plt.plot(x1, y3)
# plt.plot(x1, y4)
# plt.legend(('very-low', 'low', 'high', 'very-high'), loc='upper right')
# plt.savefig("power.png", bbox_inches='tight')
