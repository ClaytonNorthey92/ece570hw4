import math
from matplotlib import pyplot

# rows
FMHZ_100 = 0
FMHZ_1000 = 1
K1 = 2
K2 = 3

#columns
C625_F = 0
C500_F = 1
CRG_6 = 2
CRG_59 = 3

DATA = [
	[0.02, 0.02, 0.069, 0.089],
	[0.067, 0.083, 0.224, 0.285],
	[0.6, 0.69, 2.1, 2.7],
	[0.0016, 0.0037, 0.0021, 0.0015]
]

FREQUENCY_RANGE = [f for f in range(1000, 100001)]

def _get_loss(k1, k2, f, d):
	return (k1 * math.sqrt(f) + k2 * f) * d

def _get_resistance(k1, k2, f):
	return 17.27 * (k1 * math.sqrt(f) + k2 * f)

def _get_kn(cable_id):
	return (DATA[K1][cable_id], DATA[K2][cable_id])

def _config_graph(position, title, ylabel):
	pyplot.subplot(position)
	pyplot.xscale('log')
	pyplot.title(title)
	pyplot.xlabel('MHz')
	pyplot.ylabel(ylabel)

def plot_loss(cable_id):
	k1, k2 = _get_kn(cable_id)
	d = .00328
	y_axis = [_get_loss(k1, k2, f, d) for f in FREQUENCY_RANGE]
	_config_graph('221', 'Loss Per Frequency', 'Loss')
	pyplot.plot(FREQUENCY_RANGE, y_axis)

def plot_resistance(cable_id):
	k1, k2 = _get_kn(cable_id)
	y_axis = [_get_resistance(k1, k2, f) for f in FREQUENCY_RANGE]
	_config_graph('222', 'Resistance Per Frequency', 'Resistance')
	pyplot.plot(FREQUENCY_RANGE, y_axis)

if __name__=='__main__':
	for cable in [C625_F, C500_F, CRG_6, CRG_59]:
		plot_loss(cable)
		plot_resistance(cable)
	pyplot.show()

