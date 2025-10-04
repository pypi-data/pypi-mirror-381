# ./import_cmip6_data_utils/download

## Description of the full subpackage

This subpackage is dedicated to the downloading of the CMIP6 data through the **full_catalog** script. It is constructed linearly following this order :

- **prepare** is dedicated to preparing the download by setting the folder in which the data is saved, with **set_folder_to_save_raw_data**, and filtering the catalog, with **filter_catalog**.

- **one_couple** is used to download one model.variant couple from the catalog at a time.

- **download_full_catalog** is the main function of the whole **import_cmip6_data_module**. It uses functions from the **preprocessing** and **tools** subpackages.

## prepare

### Description of the script

This script contains functions to prepare the download of the CMIP6 data.

### Functions

**set_folder_to_save_raw_data** : This function sets the path of the folder in which the data will be saved.

**filtering_function** : Filters the catalog to only keep model.variant couples that fits two conditions.

**filter_catalog** : This function wraps the filtering function of the intake-esgf catalog such that the filtering parameters are globally defined within this script.

### Inputs

This script receives the **str** path of the folder in which the data will be saved.
It also takes as inputs the filtering parameters defined globally in the *import_cmip6_data* notebook.

### Outputs

It creates the folder in which the downloaded data will be saved.
It also gives the filtered catalog intake_esgf catalog.

## one_couple

### Description of the script

This script contains functions to download one model.variant couple from the catalog at a time.

An example of model.variant couple would be GFDL-CM4.r1i1p1f1. This script downloads all the wanted facets set in the csv file but restrain the search to this couple.

### Functions

**generate_search_criteria_for_given_couple** : Generates the search criteria for a given couple by adding its source_id and member_id to the search facets.

**download_couple_dictionary** : Downloads the raw searched data associated to a given model.variant couple from the full catalog.

### Inputs

This script takes as an input the full **dictionary** of search criteria and the **pandas DataFrame** of found results produced by the intake-esgf catalog.

### Outputs

The script downloads the data and loads the **CMIP6 data dictionary** associated to the search for one given model.variant couple.

## full_catalog

### Description of the script

This script contains a function to download the full catalog filled with the search criteria by downloading one model.variant couple at a time.

### Functions

**download_full_catalog** : Downloads and saves, as netcdf files, the full catalog by splitting it into model.variant couples. For each couple, the variables are regrouped by independent entries.

What we mean by **entry** is a set of facets that is independent of another set of facets in the full CMIP6 output dictionary. Different entries could be defined, for example, by a different **experiment_id**, **grid_label** or **table_id** for a given **source_id** and **member_id** couple.

To give a simple example : you wish to download the **clt** variable for GFDL-CM4.r1i1p1f1 and IPSL-CM6A-LR.r1i1p1f1, representing two source_id.member_id couples, for two experiments : **piClim-aer** and **piClim-control**. Then, you will get in the end four **netcdf** files, one per entry. Actually, the two **clt** variables for a different experiment are independent and thus are loaded into a different **xarray Dataset**. Then there will be two netcdf files per couple : one per experiment, each entry is defined by its **experiment_id**.

The datasets produced for the entries of a given couple can be associated to simpler description keys than the ones of the full catalog. The climatology of each variable is optionally computed.

### Inputs

It receives all the user criteria and options defined in the *import_cmip6_data* notebook by the user.
The script also takes as an input the filled intake-esgf catalog.

### Outputs

It downloads the full catalog and save several netcdf files for each model.variant couple. Each file is associated to a **xarray.Dataset** defined for a given entry from the catalog. The climatology of the variables of the dataset can be computed if the user asks so.
