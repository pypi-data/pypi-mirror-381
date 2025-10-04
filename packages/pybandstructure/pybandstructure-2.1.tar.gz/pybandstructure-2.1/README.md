# Pybandstructure (version 2.1)

Band structure calculator for simple models.
Allows easy implementation of simple periodic Hamiltonians including tight binding or plane waves models.
Results can be analyzed to extract thermodynamical properties, density of states, and optical conductivity.
A submodule is devoted to the implementation of superlattice hamiltonians.

## Installation

The package can be installed from the Python Package Index as

    pip install pybandstructure

or downloaded from the [repository](https://gitlab.com/itorre/bandstructure-calculation).

## Documentation

Documentation is hosted by [Read the Docs](https://pybandstructure.readthedocs.io/en/latest/index.html).

## Examples

Please refer to the [repository](https://gitlab.com/itorre/bandstructure-calculation) for example notebooks illustrating the main features.

## New in version 2.1

- Compatible with Numpy version >= 1.24

- numpy.einsum() optimization default to 'greedy'

## License

The package is distributed under the GNU Lesser General Public License v3 (LGPLv3).

## Cite as

If you use Pybandstructure for your research please cite

P. Novelli, I. Torre, F.H.L. Koppens, F. Taddei, and M. Polini 

*"Optical and plasmonic properties of twisted bilayer graphene: 
Impact of interlayer tunneling asymmetry and ground-state charge inhomogeneity"* 

Phys. Rev. B __102__, 125403 (2020).