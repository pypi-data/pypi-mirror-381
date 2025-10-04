#!/usr/bin/env python3

"""This script is used to save and load the downloaded CMIP6 data dictionaries.

save_dictionary_entries_to_nectdf : Saves each entry of a CMIP6 dictionary to a netcdf file and returns its path.

save_keys_vs_paths_dataframe : Saves the dataframe linking the entry keys with the paths of the associated netcdf files.

netcdf_to_dictionary : Converts the generated netcdf files back to a dictionary of CMIP6 datasets.

extract_indices_associated_to_a_facet_in_keys_vs_paths : Generates a dictionary associating facet names, searched for the given facet, to the row indices corresponding to these facets names in keys_vs_paths_table.

generate_cmip6_dictionary_of_entries_based_on_a_facet : Loads CMIP6 data into a dictionary of dictionaries whose keys are the different facet names searched for a provided facet.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license on github.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###

import xarray as xr  # It is imported manage the CMIP6 data.

import pandas as pd  # It is used to create and handle tables.

import numpy as np  # It is imported to work on the pandas arrays.

### HANDLE PATHS ###

from os.path import join  # This is to connect two paths.

### HOMEMADE LIBRARIES ###

## Import the package ##

## Creating a folder ##
from import_cmip6_data_utils.tools.folders import (
    create_dir,  # This function creates directories at the provided path and may clean them before.
)

## Handle CMIP6 keys ##
from import_cmip6_data_utils.tools.cmip6_dictionary_keys import (
    find_facet_index,  # It is used to find the index associated to a provided facet within a splitted CMIP6 key.
    remove_facet_name_at_facet_index,  # It is used to remove a facet present at the provided index in a CMIP6 key.
)

###################################
### DEFINITION OF THE FUNCTIONS ###
###################################

#########################################
### SAVE_DICTIONARY_ENTRIES_TO_NETCDF ###
#########################################


def save_dictionary_entries_to_nectdf(
    cmip6_dictionary: dict[str, xr.Dataset],
    save_path: str,
    clear: bool,
    verbose: bool = False,
) -> list[str]:
    """Saves each entry of a CMIP6 dictionary to a netcdf file and returns a list of their paths.

    Parameters
    ----------
    cmip6_dictionary : dict[str, xr.Dataset]

        Dictionary of the CMIP6 entries to save.

    save_path : str

        Path leading to the folder in which the entries will be stored.

    clear : bool, optional

        Whether we clear the path or not, by default True.

    verbose : bool, optional

        Bool defining if the function needs to print information, by default False.

    Returns
    -------
    generated_paths_list : list[str]

        List of the paths of the generated netcdf files.
    """

    ### INITIALISE THE PATH LIST ###

    generated_paths_list = []

    ### LOOP THROUGH THE ENTRIES OF THE DICTIONARY ##

    for ii, entry_key in enumerate(cmip6_dictionary.keys()):
        # If wanted it prints the entry that is being saved.

        if verbose:
            print("\nSaving {} in a netcdf file.\n".format(entry_key))

        ## Generate a filename with the key ##

        # Split the key into a list of keywords #

        splitted_key = entry_key.split(".")

        # Connect them with a "_" to make a filename that is not broken #

        full_name = "_".join(splitted_key)

        # Define the filename #

        filename = full_name + ".nc"

        ## Create the directory associated to the entry and keep its path ##

        saving_path_given_entry = create_dir(
            parent_path=save_path,
            name=full_name,
            clear=clear,
        )

        ## Generate the full path with the filename ##

        path_to_nc = saving_path_given_entry + "/" + filename

        ## Save the dataset linked to the entry ##

        cmip6_dictionary[entry_key].to_netcdf(path=path_to_nc)

        ## Add the path to the list of generated paths ##

        generated_paths_list.append(path_to_nc)

    return generated_paths_list


####################################
### SAVE_KEYS_VS_PATHS_DATAFRAME ###
####################################


def save_keys_vs_paths_dataframe(
    paths_list: list[str],
    different_datasets_namelist: list[str],
    save_path: str,
    clear: bool,
    verbose: bool = False,
):
    """Saves the dataframe linking the entry keys with the paths of the associated netcdf files.

    Parameters
    ----------
    paths_list : list[str]

         List of the paths of the generated netcdf files.

    different_datasets_namelist : list[str]

        List of the names of the entries that have been saved.

    save_path : str

        Path leading to the folder in which the entries are stored.

    clear : bool, optional

        Whether we clear the path or not, by default True.

    verbose : bool, optional

        Bool defining if the function needs to print information, by default False.
    """

    ### GENERATE THE PANDAS DATAFRAME ASSOCIATING KEYS WITH PATHS ###

    ## Create the pandas dataframe from a dictionnary ##

    # Define the table key vs path #

    keys_vs_paths_dictionary = {"key": different_datasets_namelist, "path": paths_list}

    # Define the dataframe #

    key_vs_paths_dataframe = pd.DataFrame(keys_vs_paths_dictionary)

    ## Save the pandas dataframe ##

    # Create the table folder to hold it #

    saving_path_table = create_dir(parent_path=save_path, name="table", clear=clear)

    # Save it #

    key_vs_paths_dataframe.to_pickle(saving_path_table + "/keys_vs_paths_table.pkl")

    # If wanted it prints that the table have been saved.
    if verbose:
        print("\nSaved the table of keys vs paths.\n")

    return


############################
### NETCDF_TO_DICTIONARY ###
############################


def netcdf_to_dictionary(save_path: str) -> dict[str, xr.Dataset]:
    """Converts the generated netcdf files back to a dictionary of CMIP6 datasets.

    This function uses the generated DataFrame of the entry keys versus the associated paths to recreate the full dictionary of the entries.

    Parameters
    ----------
    save_path : str

        Path leading to the folder in which the entries are stored.

    Returns
    -------
    cmip6_dictionary : dict[str, xr.Dataset]

        Dictionary of the different CMIP6 entries.
    """

    ### INITIALISE ###

    ## Generate the CMIP6 dictionary ##

    cmip6_dictionary = {}

    ## Retrieve the paths and keys from the keys vs paths DataFrame ##

    # Generate the full path of the .pkl file #

    full_pickle_file_path = join(save_path, "table/keys_vs_paths_table.pkl")

    # Load the dataframe #

    key_paths_table = pd.read_pickle(full_pickle_file_path)

    # Extract the keys #

    list_keys = key_paths_table["key"].to_list()

    # Extract the associated paths #

    paths = key_paths_table["path"].to_list()

    ### LOOP THROUGH THE KEYS OF THE ENTRIES ###

    for ii, key in enumerate(list_keys):
        ## Retrieve the path associated to the key ##

        path_to_nc = paths[ii]

        ## Load the netcdf file into the dictionary ##

        cmip6_dictionary[key] = xr.open_dataset(path_to_nc)

    return cmip6_dictionary


##############################################################
### EXTRACT_INDICES_ASSOCIATED_TO_A_FACET_IN_KEYS_VS_PATHS ###
##############################################################


def extract_indices_associated_to_a_facet_in_keys_vs_paths(
    facet_for_independent_dictionaries: str,
    keys_vs_paths_table: pd.DataFrame,
    search_facets_dictionary: dict[str, list[str]],
) -> dict[str, list[int]]:
    """Generates a dictionary associating facet names, searched for facet_for_independent_dictionaries, to the row indices corresponding to these facets names in keys_vs_paths_table.

    This is for the loading CMIP6 data into different dictionaries.
    The keys of the main dictionary are the different facet names linked to the chosen facet_for_independent_dictionaries.

    Parameters
    ----------
    facet_for_independent_dictionaries : str

        Chosen facet for loading the data into different dictionaries.

    keys_vs_paths_table : pd.DataFrame

        Pandas DataFrame associating the CMIP6 keys with the path of the associated netcdf files.

    search_facets_dictionary : dict[str, list[str]]

        Dictionary of the different search facets given in the csv file.

    Returns
    -------
    dict[str, list[int]]

        Dictionary associating each facet name linked to facet_for_independent_dictionaries with the list of the corresponding row indices in keys_vs_paths_table.
    """
    ### FIND INDEX OF THE FACET ###

    ## Extract a key from the table ##

    key_cmip6_dictionary = list(keys_vs_paths_table.key)[0]

    ## Find the index ##

    index_facet_for_independent_dictionaries = find_facet_index(
        key_cmip6_dictionary=key_cmip6_dictionary,
        search_facets_dictionary=search_facets_dictionary,
        facet_name=facet_for_independent_dictionaries,
    )

    ### LIST THE NAMES OF ASSOCIATED TO THE FACETS IN THE SEARCH CRITERIA ###

    ## Get the unique list of facet names asked in the search facets for the given facet ##

    unique_wanted_independent_facet_array = np.unique(
        search_facets_dictionary[facet_for_independent_dictionaries]
    )  # We take the unique list to remove duplicates.

    ## Convert the np.str array into a list[str] ##

    unique_wanted_independent_facet_array = [
        str(facet) for facet in unique_wanted_independent_facet_array
    ]

    ## Convert the array elements into str ##

    ### GENERATE THE ROW INDEX VS FACET NAME DICTIONARY ###

    ## Initialise the dictionary ##

    dictionary_row_index_associated_to_facet_name = {}

    ## Go through the searched names for the given facet ##

    for facet_name in unique_wanted_independent_facet_array:
        ## Create the list of indices corresponding to facet_name in the table ##

        # We go through the values of the keys splitted keys.
        # This allows us to find the keys that have the facet_name at the index_facet_for_independent_dictionaries index.
        # Thus, we associate them with the facet_name in the dictionary.

        row_index_for_searched_facet = [
            ii
            for ii, key in enumerate(keys_vs_paths_table.key.values)
            if key.split(".")[index_facet_for_independent_dictionaries] == facet_name
        ]

        ## Save the list of indices ##

        dictionary_row_index_associated_to_facet_name[facet_name] = (
            row_index_for_searched_facet
        )

    return dictionary_row_index_associated_to_facet_name


#############################################################
### GENERATE_CMIP6_DICTIONARY_OF_ENTRIES_BASED_ON_A_FACET ###
#############################################################


def generate_cmip6_dictionary_of_entries_based_on_a_facet(
    facet_for_independent_dictionaries: str,
    save_path: str,
    search_facets_dictionary: dict[str, list[str]],
) -> dict[str, dict[str, xr.Dataset]]:
    """Loads CMIP6 data into a dictionary of dictionaries whose keys are the different facet names searched for a provided facet.

    As an example, if your analysis is focusing on two different experiment_id, piClim-aer and piClim-control, you might want to know which entries are associated to the first experiment_id and the other to the other.
    By defining facet_for_independent_dictionaries as experiment_id you will get a dictionary per searched experiment.

    Parameters
    ----------
    facet_for_independent_dictionaries : str

        Facet separating the loaded data into different dictionaries. The keys of the main dictionary are the facet names searched for this facet.

    save_path : str

        Path leading to the folder in which the entries are stored.

    search_facets_dictionary : dict[str, list[str]]

        Dictionary of the different search facets given in the csv file.

    Returns
    -------
    cmip6_dictionary_based_on_given_facet : dict[str, dict[str, xr.Dataset]]

        Dictionary of dictionaries whose keys keys are the different facet names searched for facet_for_independent_dictionaries.

    Raises
    ------
    TypeError

        It is raised if facet_for_independent_dictionaries is None or not a str.
    """
    ### VERIFY THAT THE PROVIDED FACET HAS BEEN DEFINED ###

    if type(facet_for_independent_dictionaries) is not str:
        raise TypeError(
            "Please define facet_for_independent_dictionaries as a str input and check it is not 'None'"
        )

    ### INTIALISATION ###

    ## Initialise the dictionary ##

    cmip6_dictionary_based_on_given_facet = {}

    ## Define a permissive time coder for opening the dataset ##

    time_coder = xr.coders.CFDatetimeCoder(
        use_cftime=True,  # It allows for calendars that are not the Gregorian Calendar.
    )

    ## Open the table of CMIP6 keys and their paths through the provided save_path ##

    keys_vs_paths_table = pd.read_pickle(
        save_path + "/preprocessed/table/" + "keys_vs_paths_table.pkl"
    )

    ## Find the index at which is located facet_for_independent_dictionaries in the splitted CMIP6 keys ##

    one_cmip6_key = keys_vs_paths_table.key.values[0]

    index_facet_for_independent_dictionaries = find_facet_index(
        key_cmip6_dictionary=one_cmip6_key,
        search_facets_dictionary=search_facets_dictionary,
        facet_name=facet_for_independent_dictionaries,
    )

    ### SPLIT THE TABLE BASED ON FACET_FOR_INDEPENDENT_DICTIONARIES ###

    ## Retrieve the row indices list for each independent facet name of the provided facet ##

    dictionary_row_index_associated_to_facet_name = (
        extract_indices_associated_to_a_facet_in_keys_vs_paths(
            facet_for_independent_dictionaries=facet_for_independent_dictionaries,
            keys_vs_paths_table=keys_vs_paths_table,
        )
    )

    ### GENERATE THE FULL DICTIONARY ###

    ## Go through the facet names of the provided facet ##

    for facet_name in dictionary_row_index_associated_to_facet_name.keys():
        ## Generate the dictionary linked to a given facet name of the provided facet ##

        dictionary_of_datasets_linked_to_facet_name = {}

        ## Go through the table rows linked to facet_names ##

        for row_index in dictionary_row_index_associated_to_facet_name[facet_name]:
            ## Extract the path and the key ##

            # Path #

            row_path = keys_vs_paths_table.iloc[row_index].path

            # Key #

            row_key = keys_vs_paths_table.iloc[row_index].key

            ## Remove facet_name from the key as it is now an unnecessary information ##

            row_key_without_facet_name = remove_facet_name_at_facet_index(
                key=row_key,
                index_facet=index_facet_for_independent_dictionaries,
            )

            ## Add the Dataset associated to this row of the table to the dictionary ##

            dictionary_of_datasets_linked_to_facet_name[row_key_without_facet_name] = (
                xr.open_dataset(row_path, decode_times=time_coder)
            )

        ## Associate facet_name to its dictionary in the full CMIP6 dictionary ##

        cmip6_dictionary_based_on_given_facet[facet_name] = (
            dictionary_of_datasets_linked_to_facet_name
        )

    return cmip6_dictionary_based_on_given_facet


######################
### USED FOR TESTS ###
######################

if __name__ == "__main__":
    pass
