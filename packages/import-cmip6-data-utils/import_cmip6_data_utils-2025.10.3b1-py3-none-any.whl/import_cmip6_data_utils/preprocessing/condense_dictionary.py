#!/usr/bin/env python3

"""This script contains functions that allow to regroup variables from the same model entry into the same xarray dataset.

What we mean by entry is a set of facets that is independent of another set of facets in the full CMIP6 output dictionary.
Different entries could be defined, for example, by a different experiment_id, grid_label or table_id for a given source_id and member_id couple.

To give a simple example : if the clt and tas variables were loaded for GFDL-CM4.r1i1p1f1, a source_id.member_id couple, and for two experiments : piClim-aer and piClim-control, then intake-esgf generates a single dictionary with four xarray Datasets.
This script function will generate two xarray Datasets, one per entry. Actually, two variables for a different experiment are independent.

Optionally, the climatology of each variable can be computed according to the user-defined parameters and options.

Functions :

condense_same_entry_variables_into_one_dataset : Regroups the variables of a CMIP6 dictionary associated to the provided entry key in a xarray Dataset.

condense_a_dictionary_of_different_entries : Regroups the variables of a CMIP6 dictionary associated to different entries in a dictionary of xarray Dataset.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###

import xarray as xr  # This is imported to handle xarray objects.


### PROJECT MODULES ###

## Xarray datasets ##

from import_cmip6_data_utils.tools.dataset import (
    generate_climatology,  # This is to generate the climatology when condensing the dictionary.
    add_one_variable_to_dataset,  # It is to modify a dataset in-place by adding new variables.
)

## CMIP6 dictionary keys ##

from import_cmip6_data_utils.tools.cmip6_dictionary_keys import (
    extract_each_entry_dictionary_key_without_variable_names,  # It is imported to extract, in each model.variant couple dictionary, the independent entry keys without the variables.
)

###################################
### DEFINITION OF THE FUNCTIONS ###
###################################

######################################################
### CONDENSE_SAME_ENTRY_VARIABLES_INTO_ONE_DATASET ###
######################################################


def condense_same_entry_variables_into_one_dataset(
    dictionary_of_different_entries: dict[str, xr.Dataset],
    entry_splitted_key_with_star_variable: list[str],
    index_of_variable_id: int,
    provided_variable_id_list: list[str],
    do_climatology: bool,
    frequency_for_climatology: str = None,
) -> xr.Dataset:
    """Regroups the variables of a CMIP6 dictionary associated to the provided entry key in a xarray Dataset.

    What we mean by entry is a set of facets that is independent of another set of facets in the full CMIP6 output dictionary.
    Different entries could be defined, for example, by a different experiment_id, grid_label or table_id for a given source_id and member_id couple.

    To give a simple example : if the clt and tas variables were loaded for GFDL-CM4.r1i1p1f1, a source_id.member_id couple, and for two experiments : piClim-aer and piClim-control, then intake-esgf generates a single dictionary with four xarray Datasets.
    Then, if the provided key is the one associated to the piClim-control experiment, we will add the corresponding clt and tas into a single xarray Dataset and ignore the other variables.

    Parameters
    ----------
    dictionary_of_different_entries : dict[str, xr.Dataset]

        CMIP6 dictionary holding the different entries.

    entry_splitted_key_with_star_variable : list[str]

        Splitted key associated to the entry where the variable was replaced with a "*".

    index_of_variable_id : int

        Index at which the variable_id is located in the splitted keys.

    provided_variable_id_list : list[str]

        List of the variable_id provided by the user in their search.

    do_climatology : bool

        Bool describing if the climatology of the variable needs to be done before adding it.

    frequency_for_climatology : str, optional

        Frequency of the wanted climatology to provide if do_climatology is set to True, by default None. It can be "day", "month" or "season".

    Returns
    -------
    condensed_dataset : xr.Dataset

        Dataset where the different variables associated to the entry were regrouped.
    """

    ### CREATE THE DATASET ###

    ## Initialisation ##

    # Define the variable #

    variable_name = provided_variable_id_list[0]

    # Define that the dataset does not exist yet #

    modify_data = False

    # Copy the key without variable #

    entry_splitted_key_with_variable = entry_splitted_key_with_star_variable

    # Add the variable name #

    entry_splitted_key_with_variable[index_of_variable_id] = variable_name

    # Generate the key by joining the str list with "." #

    entry_key_with_variable = ".".join(entry_splitted_key_with_variable)

    # Retrieve the variable dataset #

    variable_dataset = dictionary_of_different_entries[entry_key_with_variable]

    ## Checking if the climatology needs to be done on the variable ##

    if do_climatology:
        # True : the climatology of the variable is computed #

        variable_dataset = generate_climatology(
            dataset=variable_dataset,
            variable_to_compute_climatology=variable_name,
            frequency=frequency_for_climatology,
        )

    ## Creation of the dataset ##

    condensed_dataset = add_one_variable_to_dataset(
        variable_name=variable_name,
        variable_dataset=variable_dataset,
        modify_data=modify_data,
    )

    ### FILL THE DATASET ###

    ## Set that now the dataset already exists ##

    modify_data = True

    ## Go through the rest of the variables ##

    for variable_name in provided_variable_id_list[1:]:
        # Copy the key without variable #

        entry_splitted_key_with_variable = entry_splitted_key_with_star_variable

        # Add the variable name #

        entry_splitted_key_with_variable[index_of_variable_id] = variable_name

        # Generate the key by joining the str list with "." #

        entry_key_with_variable = ".".join(entry_splitted_key_with_variable)

        # Retrieve the variable dataset #

        variable_dataset = dictionary_of_different_entries[entry_key_with_variable]

        ## Checking if the climatology needs to be done on the variable ##

        if do_climatology:
            # True : the climatology of the variable is computed #

            variable_dataset = generate_climatology(
                dataset=variable_dataset,
                variable_to_compute_climatology=variable_name,
                frequency=frequency_for_climatology,
            )

        ## Update the dataset ##

        condensed_dataset = add_one_variable_to_dataset(
            variable_name=variable_name,
            variable_dataset=variable_dataset,
            dataset=condensed_dataset,
            modify_data=modify_data,
        )

    return condensed_dataset


##################################################
### CONDENSE_A_DICTIONARY_OF_DIFFERENT ENTRIES ###
##################################################


def condense_a_dictionary_of_different_entries(
    dictionary_of_different_entries: dict[str, xr.Dataset],
    search_facets_dictionary: dict[str, list[str]],
    do_climatology: bool,
    frequency_for_climatology: str = None,
    verbose: bool = False,
) -> dict[str, xr.Dataset]:
    """Regroups the variables of a CMIP6 dictionary associated to different entries in a dictionary of xarray Dataset.

    What we mean by entry is a set of facets that is independent of another set of facets in the full CMIP6 output dictionary.
    Different entries could be defined, for example, by a different experiment_id, grid_label or table_id for a given source_id and member_id couple.

    To give a simple example : if the clt and tas variables were loaded for GFDL-CM4.r1i1p1f1, a source_id.member_id couple, and for two experiments : piClim-aer and piClim-control, then intake-esgf generates a single dictionary with four xarray Datasets.
    This function will generate two xarray Datasets, one per entry. Actually, two variables for a different experiment are independent.

    Parameters
    ----------

    dictionary_of_different_entries : xr.Dataset

        CMIP6 dictionary holding the different entries.

    search_facets_dictionary : dict[str, list[str]]

        Search facets provided by the user.

    do_climatology : bool

        Bool describing if the climatology of the variable needs to be done before adding it.

    frequency_for_climatology : str, optional

        Frequency of the wanted climatology to provide if do_climatology is set to True, by default None. It can be "day", "month" or "season".

    verbose : bool, optional

        Bool defining if the function needs to print information, by default False.

    Returns
    -------
    condensed_dictionary : dict[str, xr.Dataset]

        Dictionary of the different entries xr.Dataset where the variables have been regrouped.
    """

    ### INITIALISATION ###

    ## Initialise the dictionary ##

    condensed_dictionary = {}

    ## Retrieve the different entry keys ##

    (
        splitted_key_with_star_variable_for_each_entry,
        key_without_variable_for_each_entry,
        index_of_variable_id,
    ) = extract_each_entry_dictionary_key_without_variable_names(
        cmip6_dictionary=dictionary_of_different_entries,
        search_facets_dictionary=search_facets_dictionary,
    )

    ### LOOP THROUGH THE DIFFERENT ENTRIES ###

    for splitted_key_with_star_variable, key_without_variable in zip(
        splitted_key_with_star_variable_for_each_entry,
        key_without_variable_for_each_entry,
    ):
        # If wanted the key is printed

        if verbose:
            print(
                "\nRegrouping the variables of {} into a single dataset.\n".format(
                    key_without_variable,
                )
            )

        ## Regrouping the different variables in a xr.Dataset for the given key ##

        condensed_dictionary[key_without_variable] = (
            condense_same_entry_variables_into_one_dataset(
                dictionary_of_different_entries=dictionary_of_different_entries,
                entry_splitted_key_with_star_variable=splitted_key_with_star_variable,
                index_of_variable_id=index_of_variable_id,
                do_climatology=do_climatology,
                provided_variable_id_list=search_facets_dictionary["variable_id"],
                frequency_for_climatology=frequency_for_climatology,
            )
        )
    return condensed_dictionary


######################
### USED FOR TESTS ###
######################

if __name__ == "__main__":
    pass
