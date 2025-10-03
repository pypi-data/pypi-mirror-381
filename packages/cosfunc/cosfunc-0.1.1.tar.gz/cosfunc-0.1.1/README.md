# Cosfunc - Cosmological Functions

A Python package providing essential cosmological functions for astrophysics calculations.

## Features

- Hubble parameter calculations
- Cosmological distance functions
- Hydrogen number density
- Time-redshift derivatives
- Configurable cosmological parameters

## Installation

```bash
pip install cosfunc
```

## Usage

```python
from cosfunc import Set_Cosmology, H, n_H, dtdz

# Set cosmological parameters (optional, uses default if not set)
Set_Cosmology(h0=0.674, om_0=0.315)

# Calculate Hubble parameter at redshift z=7
hubble = H(7.0)
print(f"H(z=7) = {hubble}")

# Calculate hydrogen number density
density = n_H(0.5)  # overdensity delta = 0.5
print(f"n_H = {density}")

# Time derivative with respect to redshift
dt = dtdz(7.0)
print(f"dt/dz = {dt}")
```

## Functions

- `Set_Cosmology(h0, om_0)`: Set cosmological parameters
- `E(z)`: Dimensionless Hubble parameter
- `H(z)`: Hubble parameter at redshift z
- `n_H(delta)`: Hydrogen number density
- `dtdz(z)`: Time derivative with respect to redshift

## Default Parameters

- h = 0.674 (Hubble parameter)
- Ω_m = 0.315 (Matter density)
- Ω_b = 0.0224 / h² (Baryon density)

## License

MIT License
