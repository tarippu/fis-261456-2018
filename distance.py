import matplotlib.pyplot as plt

# brightness unit in cm
def very_far(distance):
    membership_value = 0
    if(400 <= distance <= 700):
        membership_value = 1 - abs((distance - 550) / 150)
    else:
        membership_value = 0
    return membership_value

def far(distance):
    membership_value = 0
    if(180 <= distance <= 420):
        membership_value = 1 - abs((distance - 300) / 120)
    else:
        membership_value = 0
    return membership_value

def not_far(distance):
    membership_value = 0
    if(80 <= distance <= 200):
        membership_value = 1 - abs((distance - 140) / 60)#
    else:
        membership_value = 0
    return membership_value

def close(distance):
    membership_value = 0
    if(0 <= distance <= 100):
        membership_value = ((-1/100) * distance) + 1
    else:
        membership_value = 0
    return membership_value

# x1 = []
# y1 = []
# y2 = []
# y3 = []
# y4 = []

# plt.figure()
# for x in range(0, 800):
#     y1.append(very_far(x, x))
#     y2.append(far(x, x))
#     y3.append(not_far(x, x))
#     y4.append(close(x, x))
#     x1.append(x)

# plt.plot(x1, y1)
# plt.plot(x1, y2)
# plt.plot(x1, y3)
# plt.plot(x1, y4)
# plt.legend(('very-far', 'far', 'not-far', 'close'), loc='upper right')
# plt.savefig("distance-membership.png", bbox_inches='tight')