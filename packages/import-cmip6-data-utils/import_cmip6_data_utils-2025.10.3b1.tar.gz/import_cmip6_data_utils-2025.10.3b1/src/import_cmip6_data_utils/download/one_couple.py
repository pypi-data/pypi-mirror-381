#!/usr/bin/env python3

"""This script contains functions to download one model.variant couple from the catalog at a time.

An example of model.variant couple would be GFDL-CM4.r1i1p1f1.
This script downloads all the wanted facets set in the csv file but restrain the search to this couple.

Functions :
-----------

generate_search_criteria_for_given_couple : Generates the search criteria for a given couple by adding its source_id and member_id to the search facets.

download_couple_dictionary : Downloads the raw searched data associated to a given model.variant couple from the full catalog.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

### DOWNLADING THE ENTRIES ###

import intake_esgf  # This gives us access to the ESGF catalog to make queries.

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###

import pandas as pd  # This is to manage the product of the search
import xarray as xr  # This package is used to handle xarrays.

### HANDLE THE OUTPUTS OF JUPYTER CELLS ###

from IPython.display import (
    clear_output,
)  # It is to clear the output of a Jupyter cell from intake-esgf information.

### EXCEPTIONS OF INTAKE-ESGF ###

import intake_esgf.exceptions as intake_exception  # This is imported to raise intake-esgf specific exceptions

##################################################
#### GENERATE_SEARCH_CRITERIA_FOR_GIVEN_COUPLE ###
##################################################


def generate_search_criteria_for_given_couple(
    search_facets_dictionary: dict[str, list[str]],
    full_catalog_models_and_variant_dataframe: pd.DataFrame,
    couple_index: int,
) -> tuple[dict[str, str], str]:
    """Generates the search criteria for a given model.variant couple by adding its source_id and member_id to the search facets.

    Parameters
    ----------
    search_facets_dictionary : dict[str, list[str]]

        Search facets provided by the user.

    full_catalog_models_and_variant_dataframe : pd.DataFrame

        Dataframe of the selected models and variants couples from the full catalog.

    couple_index : int

        Index of the couple for which the function generates the search criteria.

    Returns
    -------
    tuple[dict[str, str], str]

    search_criteria_given_couple : dict[str, str]

        Original search criteria dictionary with the source_id and member_id of the wanted couple.

    couple_name : str

        Name of the model.variant couple.
    """
    ### COPYING THE ORIGINAL SEARCH CRITERIAS DICTIONARY ###

    search_criteria_given_couple = search_facets_dictionary.copy()

    ## Get the row information ##

    # Source_id #

    source_id_to_download = full_catalog_models_and_variant_dataframe.iloc[
        couple_index
    ].source_id

    # Member_id #

    member_id_to_download = full_catalog_models_and_variant_dataframe.iloc[
        couple_index
    ].member_id

    ## Update the search criterias ##

    # Source_id #

    search_criteria_given_couple["source_id"] = source_id_to_download

    # Member_id #

    search_criteria_given_couple["member_id"] = member_id_to_download

    ## Generate the model.variant couple name ##

    couple_name = source_id_to_download + "." + member_id_to_download

    return search_criteria_given_couple, couple_name


###################################
#### DOWNLOAD_COUPLE_DICTIONARY ###
###################################


def download_couple_dictionary(
    full_catalog_models_and_variant_dataframe: pd.DataFrame,
    search_facets_dictionary: dict[str, list[str]],
    couple_index: int,
    add_measures: bool,
    verbose: bool = False,
) -> tuple[dict[str, xr.DataArray], str]:
    """Downloads the raw searched data associated to a given model.variant couple from the full catalog.

    Parameters
    ----------
    full_catalog_models_and_variant_dataframe : pd.DataFrame

        Dataframe of the selected models and variants couples from the full catalog.

    search_facets_dictionary : dict[str, list[str]]

        Search facets provided by the user.

    couple_index : int

        Index of the couple for which the function generates the search criteria.

    add_measures : bool

        Bool defining if the measure variables need to be loaded for every variable.

    verbose : bool, optional

        Bool defining if the function needs to print information, by default False.

    Returns
    -------
    tuple[intake_esgf.ESGFCatalog, dict[str, xr.DataArray], str]

    catalog : intake_esgf.ESGFCatalog

    Catalog that was filled by the search for the given model.variant couple

    downloaded_couple_dictionary

    Dictionary of the Datasets the downloaded entries for this given model.variant couple.

    couple_name : str

    Name of the model.variant couple.

    Raises
    ------
    breaking_exception

        An intake-esgf exception caught if something in the search or download goes wrong.


    """
    ### INITIALISATION ###

    ## Generate the associated search criterias ##

    search_criteria_given_couple, couple_name = (
        generate_search_criteria_for_given_couple(
            search_facets_dictionary=search_facets_dictionary,
            full_catalog_models_and_variant_dataframe=full_catalog_models_and_variant_dataframe,
            couple_index=couple_index,
        )
    )

    ## Generate the single model's output name ##

    print("\nLoading {} ...\n".format(couple_name))

    try:
        ## Reset the catalog ##

        global catalog

        ## Initialise the catalog ##

        catalog = intake_esgf.ESGFCatalog()

        ## Apply the search criterias ##

        catalog.search(
            **search_criteria_given_couple,
        )

        ## Downloading the output... ##

        downloaded_couple_dictionary = catalog.to_dataset_dict(
            add_measures=add_measures,
            minimal_keys=False,
        )

        ## Remove the facets to be ignored ##

        clear_output(wait=False)

    except intake_exception.IntakeESGFException as breaking_exception:
        raise breaking_exception

    if verbose:
        print("\n==============================\n")

        print(
            "\nDownloaded model.variant couple {}/{} : {}\n".format(
                couple_index + 1,
                len(full_catalog_models_and_variant_dataframe),
                couple_name,
            )
        )

    return (
        catalog,
        downloaded_couple_dictionary,
        couple_name,
    )
