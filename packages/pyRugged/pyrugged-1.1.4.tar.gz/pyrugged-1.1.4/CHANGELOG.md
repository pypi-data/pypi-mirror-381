# PyRugged Changelog

## 1.1.4 (2025-10-03)

- Add Python 3.14-RC support (3.11 to 3.14-rc versions)

## 1.1.3 (2025-09-26)

- Minor fix: filter altitudes to avoid inconsistent shape in point_at_altitude_vec
- CI pipeline: build, test & publish on PyPI both Python 3.11 and 3.13 versions

## 1.1.2 (2025-08-11)

- Update dependency to orekit-jcc 13.1.0

## 1.1.1 (2025-07-30)

- Migrate setup.cfg to pyproject.toml 
- Published to [The Python Package Index](https://pypi.org/project/pyRugged/) (PyPI)

## 1.1.0 ASGARD rework (2025-07-10)

- Use orekit-jcc bindings
- Add gitlab-ci 
- DEM intersection vectorization
- Cythonize some functions
- SAR vectorization
- Fix indexes in DEM Tiles out of bound at antemeridian
- Update scipy version using cubic_legacy method.
- Clean tutorials 
- Update to orekit 13.0.3

## 1.0.4 Add multi altitudes in direct location

- Use input list of altitude in direct location
- Cython optimisations

## 1.0.3 Fix transform LOS array

- Fix transform los array in sinusoidal rotation

## 1.0.2 Optimisation

- Temporary version for optimisations 

## 1.0.1 Sinusoidal Transform

- Add Sinusoidal Rotation

## 1.0.0 First Release 

- PyRugged coded in python3 with support of OREKIT 11.1 and Hipparchus 2.0 JCC bindings
- SAR location 
