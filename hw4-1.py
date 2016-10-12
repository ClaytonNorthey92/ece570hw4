import math

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

def _get_loss(k1, k2, f, d):
	return (k1 * math.sqrt(f) + k2 * f)

def plot_loss(cable_id):
	k1 = DATA[K1][cable_id]
	k2 = DATA[K2][cable_id]
	f_Mhz = [f for f in range(100, 100001)]
	d = 1 #assuming this is one
	y_axis = [_get_loss(k1, k2, f, d) for f in f_Mhz]
	print(y_axis) 

if __name__=='__main__':
	for cable in [C625_F, C500_F, CRG_6, CRG_59]:
		plot_loss(cable)

