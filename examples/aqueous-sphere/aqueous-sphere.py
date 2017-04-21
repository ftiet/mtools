import numpy as np
import matplotlib.pyplot as plt
from mtools.post_process import calc_charge_density
from mtools.post_process import calc_number_density

resnames = ['Na', 'Cl', 'HOH']
coord_file = 'run/prod.gro'
trj_file = 'run/prod.trr'
top_file = 'run/prod.top'
bin_width = 0.02
area = 4*np.pi*1.018**2 
dim = 2
box_range = [0.0, 4.0]
data_path = 'data/'
geometry = 'sphere'
sphere_center = 4.0

#calc_number_density(coord_file, trj_file, bin_width, area,
#    dim, box_range, data_path, geometry, sphere_center)
#
#fig = plt.figure(figsize=(5, 3))
#
#for res in [x.strip() for x in  open('data/resnames.txt', 'r')]:
#    if res == 'grC':
#        continue
#    else:
#        data = np.loadtxt('{}/{}-number-density.txt'.format(data_path, res))
#        if res == 'HOH':
#            plt.plot([x-0.682 for x in data[:, 0]],
#                [x/20 for x in data[:, 1]], '-', label='Water/20')
#        else:
#            plt.plot([x-0.682 for x in data[:, 0]], data[:, 1], '-', label=res)
#
#plt.legend(loc=0)
#plt.ylabel(r'Ion Number Densities $\left(\mathsf{\frac{molecule}{nm^3}}\right)$')
#plt.set_xlabel('Distance from Surface, $nm$')
#fig.savefig('img/number_density.pdf')

calc_charge_density(coord_file, trj_file, top_file, bin_width, area,
    dim, box_range, data_path, geometry, sphere_center)

fig, ax = plt.subplots(figsize=(5, 3))

data = np.loadtxt('{}/charge-density.txt'.format(data_path))
ax.plot([x for x in data[:, 0]], data[:, 1], '-')

ax.set_ylabel(r'Charge Density $\left(\mathsf{\frac{e^-}{nm^3}}\right)$')
ax.set_xlabel('Distance from Surface, $nm$')
fig.savefig('img/charge-density.pdf')
