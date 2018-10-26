# Z-A-Selector
Charge (Z) / Atomic mass (A) Selector ... For charged ions


The mass of atoms is given in units of 1/12 of C12 atom: see: https://en.wikipedia.org/wiki/Atomic_mass.
The charge state gives ionization values (here: loss of electrons) from neutral - to -full ionization. The maximum
electron number is given by the elements characterisitics depending on the number of protons in the atomic core 
(see: https://en.wikipedia.org/wiki/Periodic_table). 
Hence, Z>0 for electron loss and Z<0 for electron capture. 

For moving ions, the charge to mass number (Z/A) can be determined by a Thomson Spectrometer (static B and E field), that deflects
the ions according to Z/A and in velocity. (https://en.wikipedia.org/wiki/Mass-to-charge_ratio).

This little program gives for a given Z/A number up to the 4.th period of the periodic table, the matching elements within
an uncertainty. Naturally, the uncertainty if choosen to big leads to multiple matches.

Values Z/A are asked in decimals (0.xyd), uncertainty in the same notation (absolute error!).
Some frequent isotopes (https://en.wikipedia.org/wiki/Isotope) are implemented too.

