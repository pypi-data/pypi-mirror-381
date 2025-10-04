# ./import_cmip6_data_utils/tools

## Description of the full subpackage

This subpackage is holding all the utilitary functions that may be used by several thematic submodules dealing with CMIP6 data. The different scripts present composing this subpackage are not interacting linearly together but are thought as independent.

## cmip6_dictionary_keys

### Description of the script

This script contains functions used to handle the keys of a CMIP6 dictionary.

### Functions

- **find_facet_index** : Finds the index associated to a specific facet in a provided dictionary key.

- **remove_facet_name_at_facet_index** :  Removes the facet name of the provided CMIP6 dictionary key at the given index.

- **extract_each_entry_dictionary_key_without_variable_names** : Extracts the entry keys in a given CMIP6 dictionary, without duplicates, by removing the different variables names.

### Inputs

These functions deal with **str** CMIP6 keys that are organised in terms of facets. One full key is organised like this :

```'mip_era.activity_drs.institution_id.source_id.experiment_id.member_id.table_id.variable_id.grid_label'```

They can be splitted under the form of a list :

```['mip_era','activity_drs','institution_id','source_id','experiment_id','member_id','table_id''variable_id','grid_label']```

For more details on the facets see : <http://goo.gl/v1drZl> (last visited 01/09/2025).

### Outputs

This script modifies the keys in-place or finds the index associated to a given facet name in a splitted key.

## csv_criteria

### Description of the script

This script contains functions used to read csv files and extracts the criteria to constrain the search of CMIP6 outputs.

### Functions

- **csv_to_dataframe** : Reads the provided csv file and generates a panda dataframe from it.

- **extract_search_facets** : Reads the provided csv file holding the search criteria and generates a dictionary of the search facets.

### Inputs

These functions are using provided csv files **str** paths to read them thanks to pandas.

### Outputs

The wanted outputs are **dictionaries** of search facets used to fill the catalog or **pandas DataFrame** used to filter the catalog.

## dataset

### Description of the script

This script contains functions dedicated to handle a CMIP6 xarray dataset.

### Functions

- **add_one_variable_to_dataset** : Adds a variable from a xarray DataArray to a xarray Dataset.

- **generate_climatology** : Generates a climatology of the variable of a xarray dataset based on the frequency given in input.

### Inputs

The inputs are **xarray Datasets**.

### Outputs

The outputs are still **xarray Datasets** but modified in-place or combined together.

## folders

### Description of the script

This script contains a function to create, remove and check the existence of given folders thanks to their paths.

### Functions

- **create_dir** : Creates a tree of folders and optionally empties it if it existed before.

### Inputs

This script receives a **str** path and a **str** filename.

### Outputs

The function creates the tree path associated to the input.

## save_and_load_netcdf

### Description of the script

This script is used to save (load) the downloaded CMIP6 data dictionaries into (from) netcdf files.

### Functions

- **save_dictionary_entries_to_nectdf** : Saves each entry of a CMIP6 dictionary to a netcdf file and returns its path.

- **save_keys_vs_paths_dataframe** : Saves the dataframe linking the entry keys with the paths of the associated netcdf files.

- **netcdf_to_dictionary** : Converts the generated netcdf files back to a dictionary of CMIP6 datasets.

- **extract_indices_associated_to_a_facet_in_keys_vs_paths** : Generates a dictionary associating facet names, searched for the given facet, to the row indices corresponding to these facets names in keys_vs_paths_table.

- **generate_cmip6_dictionary_of_entries_based_on_a_facet** : Loads CMIP6 data into a dictionary of dictionaries whose keys are the different facet names searched for a provided facet.

### Inputs

When the data is saved, the input is CMIP6 data, a **dictionary** of **xarray Datasets**.
When the data is loaded, the input is a **str** path.

### Outputs

When the data is saved, the output is the production of a **netcdf files** and of an associated **pandas Dataframe** that links the **str** CMIP6 dictionary keys with their **str** paths.
When the data is loaded with **netcdf_to_dictionary**, the output is the retrieved **dictionary** of **xarray Datasets**.

**generate_cmip6_dictionary_of_entries_based_on_a_facet** allows to load the data as a **dictionary of dictionaries** whose keys are based on a separating facet.

As an example, if your analysis is focusing on two different **experiment_id**, piClim-aer and piClim-control, you might want to know which entries are associated to the first experiment_id and the other to the other. By defining facet_for_independent_dictionaries as experiment_id you will get a dictionary per searched experiment.
