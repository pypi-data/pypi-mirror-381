#!/usr/bin/env python3

"""This script contains functions used to handle the keys of a CMIP6 dictionary.

These functions deal with **str** CMIP6 keys that are organised in terms of facets. One full key is organised like this :

'mip_era.activity_drs.institution_id.source_id.experiment_id.member_id.table_id.variable_id.grid_label'

They can be splitted under the form of a list :

['mip_era','activity_drs','institution_id','source_id','experiment_id','member_id','table_id''variable_id','grid_label']

For more details on the facets see : <http://goo.gl/v1drZl> (last visited 01/09/2025).

Functions :

find_facet_index : Finds the index associated to a specific facet in a provided dictionary key.

remove_facet_name_at_facet_index : Removes the facet name of the provided CMIP6 dictionary key at the given index.

extract_each_entry_dictionary_key_without_variable_names : Extracts the entry keys in a given CMIP6 dictionary, without duplicates, by removing the different variables names.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###

import numpy as np  # It is to handle numpy arrays and the associated tools.

import xarray as xr  # This is imported to handle xarray objects.

### TYPE HINTS FOR FUNCTIONS ###

from numpy.typing import NDArray  # It is used for type hinting for the numpy library.

###################################
### DEFINITION OF THE FUNCTIONS ###
###################################

########################
### FIND_FACET_INDEX ###
########################


def find_facet_index(
    key_cmip6_dictionary: str,
    search_facets_dictionary: dict[str, list[str]],
    facet_name: str,
) -> np.int64:
    """Finds the index associated to a specific facet in a provided splitted dictionary key.

    It uses the provided search facets and looks for a given facet, for example variable_id, in a splitted key of a dowloaded cmip6 dictionary.
    As a result, the function provides the index associated to the variable_id facet in all the keys of the dictionary.

    Parameters
    ----------
    key_cmip6_dictionary : str

        A key from a dictionary of CMIP6 datasets.

    search_facets_dictionary : dict[str, list[str]]

        Search facets provided by the user, used to find the index of facet_name in the dictionary key.

    facet_name : str

        Facet_name whose associated index is searched by the function.

    Returns
    -------
    index_of_facet : np.int64

        Index associated to facet_name in the CMIP6 dictionary.
    """

    ### RETRIEVE THE LIST OF FACETS PROVIDED FOR FACET_NAME ###

    provided_list_for_facet_name = search_facets_dictionary[
        facet_name
    ]  # For example if facet_name is "variable_id", the list could hold "clt".

    ### FINDING THE INDEX ASSOCIATED TO FACET_NAME ###

    ## Using the list to find the corresponding index in the provided key ##

    index_of_facet = np.where(
        np.isin(key_cmip6_dictionary.split("."), provided_list_for_facet_name)
    )[0][0]

    return index_of_facet


########################################
### REMOVE_FACET_NAME_AT_FACET_INDEX ###
########################################


def remove_facet_name_at_facet_index(
    key: str,
    index_facet: int,
) -> str:
    """Removes the facet name of the provided CMIP6 dictionary key at the given index.


    Parameters
    ----------
    key : str

        CMIP6 description key that is organised in the following way :

        'mip_era.activity_drs.institution_id.source_id.experiment_id.member_id.table_id.variable_id.grid_label'

        Note that the provided key can be missing facets.

    index_facet : int

        Index at which the facet needs to be removed from the key.

    Returns
    -------
    key_without_facet_at_index : str

        Key without facet at the given index.
    """

    ### SPLIT THE KEY ###
    key_splitted = key.split(".")

    ### REMOVE THE FACET AT THE PROVIDED INDEX ###

    key_splitted.pop(index_facet)

    ### REFORM THE KEY ###

    key_without_facet_at_index = ".".join(key_splitted)

    return key_without_facet_at_index


################################################################
### EXTRACT_EACH_ENTRY_DICTIONARY_KEY_WITHOUT_VARIABLE_NAMES ###
################################################################


def extract_each_entry_dictionary_key_without_variable_names(
    cmip6_dictionary: dict[str, xr.Dataset],
    search_facets_dictionary: dict[str, list[str]],
) -> tuple[list[str], list[str], int]:
    """Extracts the entry keys in a given CMIP6 dictionary, without duplicates, by removing the different variables names, under two different forms.

    For example if a given dictionary of the "GFDL-CM4" model for the "r1i1p1f1" variant holds two experiments 'piClim-aer" and "piClim-control", then we will retrieve two entries.
    Indeed, there will be one entry per independent set of facets, which are here determined by the experiments.
    The function extracts the entry keys into two numpy array : one array holding the full entry key splitted with a "*" where the variable is and one array with the variable removed.

    To go on with the example, if the dictionary only holds the "clt" variable, the "piClim-control" key would be : CMIP6.RFMIP.NOAA-GFDL.GFDL-CM4.piClim-aer.r1i1p1f1.Amon.clt.gr1.

    This key will be transformed in two different outputs :

    1) ["CMIP6","RFMIP","NOAA-GFDL","GFDL-CM4","piClim-aer","r1i1p1f1","Amon","*","gr1"]
    2) CMIP6.RFMIP.NOAA-GFDL.GFDL-CM4.piClim-aer.r1i1p1f1.Amon.gr1

    Parameters
    ----------
    cmip6_dictionary : dict[str, xr.Dataset]

        CMIP6 Dictionary holding the different entries.

    search_facets_dictionary : dict[str, list[str]]

        Dictionary of the search facets provided by the user to identify where the variables are in the key.

    Returns
    -------
    tuple[list[str], list[str], int]

    splitted_keys_with_star_variable_unique : list[str]

        A list of str holding the entry keys splitted with a "*" where the variable is, without duplicates.

    keys_without_variable_unique : list[str]

        A list of str holding the entry keys with the variables removed, without duplicates.

    index_of_variable_id : int

        Index at which the variable_id is located in the splitted keys.

    """

    ### INITIALISATION ###

    ## Extract the list of the keys ##

    list_keys = list(cmip6_dictionary.keys())

    ## Get the number of keys ##

    number_of_keys = len(list_keys)

    ## Generate the output array with the known number of keys ###

    splitted_keys_with_star_variable = np.empty(
        number_of_keys,
        dtype=object,  # We use dtype = object otherwise the string values get truncated.
    )

    keys_without_variable = np.empty(
        number_of_keys,
        dtype=object,  # We use dtype = object otherwise the string values get truncated.
    )

    ## Find the index at which the variable_id is located in the splitted keys.

    index_of_variable_id = find_facet_index(
        key_cmip6_dictionary=list_keys[0],
        search_facets_dictionary=search_facets_dictionary,
        facet_name="variable_id",
    )

    ### LOOP OVER THE DICTIONARY KEYS ###

    for ii, key in enumerate(list_keys):
        ## Split the keys where there is a "." ##

        splitted_key = key.split(".")

        ## Copy the splitted key ##

        splitted_key_with_star_variable = splitted_key

        ## Remove the variable and replace it with a * ##

        splitted_key_with_star_variable[index_of_variable_id] = "*"

        ## Save it into the output numpy arrays ##

        splitted_keys_with_star_variable[ii] = splitted_key_with_star_variable

        ## Generate the key without the variable ##

        # Copy the splitted key #

        splitted_key_without_variable = splitted_key_with_star_variable.copy()

        # Remove the variable #

        splitted_key_without_variable.remove("*")

        # Reconstruct the full key and save it #

        keys_without_variable[ii] = ".".join(splitted_key_without_variable)

    ### REMOVE THE DUPLICATES ###

    ## Generate the unique arrays of splitted keys and keys without variables ##

    splitted_keys_with_star_variable_unique = np.unique(
        splitted_keys_with_star_variable
    )

    keys_without_variable_unique = np.unique(keys_without_variable)

    ## Convert these array of np.str into list[str] ##

    splitted_keys_with_star_variable_unique = [
        str(splitted_key_with_star_variable)
        for splitted_key_with_star_variable in splitted_keys_with_star_variable_unique
    ]

    keys_without_variable_unique = [
        str(key_without_variable)
        for key_without_variable in keys_without_variable_unique
    ]

    return (
        splitted_keys_with_star_variable_unique,
        keys_without_variable_unique,
        index_of_variable_id,
    )


######################
### USED FOR TESTS ###
######################

if __name__ == "__main__":
    pass
