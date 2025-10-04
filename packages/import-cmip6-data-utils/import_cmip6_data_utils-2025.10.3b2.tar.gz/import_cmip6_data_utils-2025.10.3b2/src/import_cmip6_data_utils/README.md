# ./import_cmip6_data_utils

# Description of the package

This package is used in order to download CMIP6 data thanks to an input *.csv* file, filled with the criteria for the search. It is decomposed into several sub-packages. In order to use it easily, you may check the **raw notebook associated to it**. It is maintained in this [repository](https://gricad-gitlab.univ-grenoble-alpes.fr/gibonil/import_cmip6_data).

### Description of the subpackages

- **tools** : This subpackage is holding all the utilitary functions that may be used by several thematic subpackages dealing with CMIP6 data.

- **preprocessing** : This subpackage is dedicated to condensing raw intake-esgf catalog outputs into more compact and readable dictionaries.

- **download** : This subpackage is dedicated to the downloading of the CMIP6 data through the **full_catalog** script.

### Interaction between the subpackages

- **tools** : This subpackage is used by both **preprocessing** and **download**.

- **preprocessing** : This subpackage is used by **download** for processing the raw CMIP6 data.

- **download** : This subpackage uses most of the functions developed within the package as the **full_catalog** script is the main routine of the notebook.
