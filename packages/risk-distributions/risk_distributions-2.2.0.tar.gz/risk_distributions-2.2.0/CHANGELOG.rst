**2.2.0 - 10/02/25**

 - Allow user to pass incomplete parameter sets to EnsembleDistribution (filled with zeros)
 - Backfill some unit tests

**2.1.6 - 08/01/25**

 - Use vivarium_dependencies for common setup constraints

**2.1.5 - 07/25/25**

 - Feature: Support new environment creation via 'make build-env'

**2.1.4 - 07/16/25**

 - Support pinning of vivarium_build_utils; pin vivarium_build_utils>=1.1.0,<2.0.0
 
**2.1.3 - 01/30/24**

  - Get python versions from python_versions.json

**2.1.2 - 12/3/24**

 - Fix mutable state bugs in pd Series and Dataframes

**2.1.1 - 11/26/24**

 - Fix bug in MirroredGamma and MirroredGumbel CDFs.
 - Update Deploy to Python 3.11

**2.1.0 - 11/07/24**

 - Drop support for Python 3.9
 - Modernize type hinting

**2.0.17 - 09/17/24**

- Pin Sphinx below 8.0

**2.0.16 - 01/29/24**

 - Fix broken readthedocs build

**2.0.15 - 01/09/24**

 - Update PyPI to 2FA with trusted publisher

**2.0.14 - 10/19/23**

 - Implement setuptools-scm
 - Drop support for Python 3.7-3.8; add support for 3.11

**2.0.13 - 09/26/23**

 - Increment version number

**2.0.12 - 09/26/23**

 - Address Pandas 2.1 FutureWarnings

**2.0.11 - 12/27/22**

 - Update PR template
 - Modify codeowners
 - Update CI and setup to build python 3.7-3.10

**2.0.10 - 07/01/22**

 - Add CODEOWNERS
 - Fix autodoc warnings

**2.0.9 - 05/05/22**

 - Update black dependency in CI

**2.0.8 - 02/15/22**

 - Autoformat code with black and isort.
 - Add black and isort checks to CI.

**2.0.7 - 02/12/22**

 - Modernize CI.
 - Add PR template.
 - Update to BSD 3-clause license.
 - Squash warnings in doc building
 - Fix remote doc builds.

**2.0.6 - 08/31/21**

 - Add credentials to repository 
 
**2.0.5 - 08/31/21**

 - Set python deployment version to 3.8 
 
**2.0.4 - 08/31/21**

 - Implement quantile (ppf) function for EnsembleDistribution using 2 pr
 - CI changes
 - Update authors and maintainers

**2.0.3 - 09/08/20**

 - Correction to the Beta distribution wrapper.
 - supress RuntimeWarning around dist calculation
 - Update authors and maintainers

**2.0.2 - 11/18/19**

 - Fix set logic in data frame formatting.

**2.0.1 - 03/12/19**

 - Add API documentation.
 - Add cdf to all distributions.
 - Bugfix to handle case where computable is empty for ppf, pdf, and cdf.

**2.0.0 - 02/13/19**

 - Full rewrite of risk distributions.
 - Separation of input data handling from parameter calculation.
 - Improved interactive usability.

**1.0.1 - 11/07/18**

 - Clean up separated distributions.
 - Allow for only mean and standard deviation or pre-calculated parameters.

**1.0.0 - 10/29/18**

 - Initial Release

