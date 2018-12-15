import matplotlib.pyplot as plt

# brightness unit in lux
def dark(brightness, alpha):
    membership_value = 0
    if(0 <= brightness <= 20):
        membership_value = ((-1/20) * brightness) + 1
        if(membership_value > alpha):
            membership_value = alpha
    else:
        membership_value = 0
    return membership_value

def low_brightness(brightness, alpha):
    membership_value = 0
    if(18 <= brightness <= 400):
        membership_value = 1 - abs((brightness - 209) / 191)
        if(membership_value > alpha):
            membership_value = alpha
    else:
        membership_value = 0
    return membership_value

def medium_brightness(brightness, alpha):
    membership_value = 0
    if(375 <= brightness <= 900):
        membership_value = 1 - abs((brightness - 637.5) / 262.5)
        if(membership_value > alpha):
            membership_value = alpha
    else:
        membership_value = 0
    return membership_value

def high_brightness(brightness, alpha):
    membership_value = 0
    if(800 <= brightness <= 5000):
        membership_value = 1 - abs((brightness - 2900) / 2100)
        if(membership_value > alpha):
            membership_value = alpha
    else:
        membership_value = 0
    return membership_value

# x1 = []
# y1 = []
# y2 = []
# y3 = []
# y4 = []

# plt.figure()
# for x in range(0, 5500):
#     y1.append(dark(x, x))
#     y2.append(low_brightness(x, x))
#     y3.append(medium_brightness(x, x))
#     y4.append(high_brightness(x, x))
#     x1.append(x)

# plt.plot(x1, y1)
# plt.plot(x1, y2)
# plt.plot(x1, y3)
# plt.plot(x1, y4)
# plt.legend(('dark', 'low-brightness', 'medium-brightness', 'high-brightness'), loc='upper right')
# plt.savefig("brightness-membership.png", bbox_inches='tight')
