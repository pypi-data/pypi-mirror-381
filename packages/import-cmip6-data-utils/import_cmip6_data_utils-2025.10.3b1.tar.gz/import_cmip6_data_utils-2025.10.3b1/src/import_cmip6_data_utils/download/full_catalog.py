#!/usr/bin/env python3

"""This script contains a function to download the full catalog filled with the search criteria by downloading one model.variant couple at a time.

To give a simple example : you wish to download the clt variable for GFDL-CM4.r1i1p1f1 and IPSL-CM6A-LR.r1i1p1f1, representing two source_id.member_id couples, for two experiments : piClim-aer and piClim-control.
Then, you will get in the end four netcdf files, one per entry.
Actually, the two clt variables for a different experiment are independent and thus are loaded into a different xarray Dataset.
Then there will be two netcdf files per couple : one per experiment, each entry is defined by its experiment_id.

Functions :
-----------

download_full_catalog : Downloads and saves the full catalog by splitting it into model.variant couples for which the variables that are regrouped by independent entries.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

##################################
### IMPORTATION OF THE MODULES ###
##################################

### DOWNLADING THE ENTRIES ###

import intake_esgf  # This gives us access to the ESGF catalog to make queries.

### HANDLING FILES FROM PYTHON ###

from shutil import rmtree  # This is imported to remove the raw data if asked.

from os.path import join  # It is used to joined two paths together.

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###

import pandas as pd  # This is to manage the product of the search

### PROJECT MODULES ###

## Generating the search criteria for each model.variant couple.

from import_cmip6_data_utils.download.one_couple import (
    download_couple_dictionary,  # It is imported to download and save a model.variant couple dictionary at a time.
)

## Reducing the keys of the CMIP6 dictionaries ##

from import_cmip6_data_utils.preprocessing.reduce_couple_dictionary_keys import (
    only_keep_wanted_facets_in_couple_dictionary,  # It is imported to reduce the information within the keys of a model.variant dictionary.
)

## Condensing the couple dictionary entries by regrouping the same entry variables into one dataset ##

from import_cmip6_data_utils.preprocessing.condense_dictionary import (
    condense_a_dictionary_of_different_entries,  # This is used to regroup the variables associated to the same entry in the same xarray Dataset within the dictionary.
)

## Saving the couple dictionary entries as netcdf files ##

from import_cmip6_data_utils.tools.save_and_load_netcdf import (
    save_dictionary_entries_to_nectdf,  # This is imported to save each entry of a CMIP6 dictionary to a netcdf file and returns its path.
    save_keys_vs_paths_dataframe,  # It is needed to generate and save a DataFrame linking the entry keys with the paths of the associated netcdf files.
)
##############################
#### DOWNLOAD_FULL_CATALOG ###
##############################


def download_full_catalog(
    full_catalog_models_and_variant_dataframe: pd.DataFrame,
    search_facets_dictionary: dict[str, list[str]],
    wanted_description_facets: list[str],
    defining_manually_output_keys: bool,
    add_measures: bool,
    do_climatology: bool,
    frequency_for_climatology: str,
    save_path: str,
    clear: bool,
    remove_raw_data: bool,
    verbose: bool = False,
):
    """Downloads and saves, as netcdf files, the full catalog by splitting it into model.variant couples.


    What we mean by entry is a set of facets that is independent of another set of facets in the full CMIP6 output dictionary.
    Different entries could be defined, for example, by a different experiment_id, grid_label or table_id for a given source_id and member_id couple.

    To give a simple example : you wish to download the clt variable for GFDL-CM4.r1i1p1f1 and IPSL-CM6A-LR.r1i1p1f1, representing two source_id.member_id couples, for two experiments : piClim-aer and piClim-control.
    Then, you will get in the end four netcdf files, one per entry.
    Actually, the two clt variables for a different experiment are independent and thus are loaded into a different xarray Dataset.
    Then there will be two netcdf files per couple : one per experiment, each entry is defined by its experiment_id.

    For each couple, the variables are regrouped by independent entries.
    The datasets produced for the entries of a given couple can be associated to simpler description keys than the ones of the full catalog.
    The climatology of each variable is optionally computed.

    Parameters
    ----------
    full_catalog_models_and_variant_dataframe : pd.DataFrame

        Dataframe of the selected models and variants couples from the full catalog.

    search_facets_dictionary : dict[str, list[str]]

        Search facets provided by the user.

    wanted_description_facets : list[str]

        List of the wanted description facets for the couple dictionary keys.

    add_measures : bool

        Bool defining if the measure variables need to be loaded for every variable.

    do_climatology : bool

        Bool defining if the climatologies are computed.

    frequency_for_climatology : str

        Frequency of the climatology : can be "day", "month" and "seasons", for more details see https://xcdat.readthedocs.io/en/latest/generated/xarray.Dataset.temporal.climatology.html.

    save_path : str

        Path leading to the folder in which the entries are stored.
        The preprocessed entries will be saved under a "/preprocessed" folder while the raw data under a "/CMIP6" folder.

    clear : bool, optional

        Bool defining whether we clear save_path or not.

    remove_raw_data : bool

        Bool defining if the raw data needs to be erased from disk or not.

    verbose : bool, optional

        Bool defining if the function needs to print information, by default False.

    """
    ### INITIALISATION ###

    ## Reset the catalog globally ##

    global catalog

    catalog = intake_esgf.ESGFCatalog()

    ## Define the number of models and variant couples ##

    number_of_entries = len(full_catalog_models_and_variant_dataframe)

    ## Generate the array of the name of the downloaded datasets  ##

    different_datasets_namelist = []

    ## Generate the paths associated to the different downloaded datasets ##

    paths_list = []

    ## Generate the path for the preprocessed data ##

    path_preprocessed_data = join(save_path, "preprocessed")

    ### GO THROUGH EACH MODEL.VARIANT COUPLE ###

    for couple_index in range(number_of_entries):
        ### DOWNLOAD ###

        catalog = intake_esgf.ESGFCatalog()

        catalog, downloaded_dictionary, downloaded_couple_name = (
            download_couple_dictionary(
                full_catalog_models_and_variant_dataframe=full_catalog_models_and_variant_dataframe,
                search_facets_dictionary=search_facets_dictionary,
                couple_index=couple_index,
                add_measures=add_measures,
                verbose=verbose,
            )
        )

        ### REDUCE THE DICT KEYS ###

        downloaded_dictionary = only_keep_wanted_facets_in_couple_dictionary(
            catalog=catalog,
            search_facets_dictionary=search_facets_dictionary,
            cmip6_dictionary=downloaded_dictionary,
            defining_manually_output_keys=defining_manually_output_keys,
            wanted_description_facets=wanted_description_facets,
            verbose=verbose,
        )

        ### CONDENSE THE DICT ###

        condensed_dictionary = condense_a_dictionary_of_different_entries(
            dictionary_of_different_entries=downloaded_dictionary,
            search_facets_dictionary=search_facets_dictionary,
            do_climatology=do_climatology,
            frequency_for_climatology=frequency_for_climatology,
            verbose=verbose,
        )

        ### SAVE THE CONTENT OF THE DICTIONARY AS A NETCDF FILE ###

        generated_paths_list = save_dictionary_entries_to_nectdf(
            cmip6_dictionary=condensed_dictionary,
            save_path=path_preprocessed_data,
            clear=clear,
            verbose=verbose,
        )

        ## Add the path to the list ##

        paths_list = paths_list + generated_paths_list

        ## Add the names of the entries to the namelist ##

        different_datasets_namelist = different_datasets_namelist + list(
            condensed_dictionary.keys()
        )

        # If wanted it closes the verbose display for this couple.
        if verbose:
            print("\n==============================\n")

    ### SAVE THE ASSOCIATED PATHS ###

    save_keys_vs_paths_dataframe(
        paths_list=paths_list,
        different_datasets_namelist=different_datasets_namelist,
        save_path=path_preprocessed_data,
        clear=clear,
        verbose=verbose,
    )

    ### IF ASKED REMOVING THE RAW DATA ###

    if remove_raw_data:
        ## Generate the path of the raw data ##

        full_path_raw_data = join(save_path, "CMIP6")

        # If wanted the user is informed of the removing.

        print("Removing the raw data located at {}".format(full_path_raw_data))

        ## Remove the raw data ##

        rmtree(full_path_raw_data)

    return
