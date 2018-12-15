import matplotlib.pyplot as plt

def draw_graph(x, y, rule_name, idx):
    plt.figure(idx)
    plt.plot(x, y)
    plt.savefig(rule_name, bbox_inches='tight')
