#!/usr/bin/env python3

"""This script contains functions to edit the dictionary keys of a CMIP6 dictionary associated to a model.variant couple.

Its main function is only_keep_wanted_facets_in_couple_dictionary whose goal is to reduce the facets contained in the given CMIP6 dictionary keys.

---
DEFAULT OPTION

The default option, when defining_manually_output_keys is set to False, implies that, only the facets that are different between the variables of a single given model.variant couple are kept.
What's more, the source_id, member_id and variable_id are always preserved. As a result, if the search facets are

{"variable_id" : "clt", "experiment_id" : ["piClim-aer","piClim-control"], "table_id" : ["Amon"]}

then

CMIP6.RFMIP.NOAA-GFDL.GFDL-CM4.piClim-aer.r1i1p1f1.Amon.rsdscs.gr1

becomes

GFDL-CM4.piClim-aer.r1i1p1f1.rsdscs.

This is the case because for the clt variables in the dictionary of GFDL-CM4.r1i1p1f1, only the experiment_id is different.
The table_id would not change between two clt variables of the two different experiments.
Same for the rest of the facets.

---
MANUAL OPTION


Functions :
-----------

define_facets_to_ignore_for_couple : Defines the facets that will be ignored for a given model_variant couple dictionary keys.

find_index_of_kept_facets : Finds the index of the facets to be kept in the splitted full catalog facets.

only_keep_wanted_facets_in_key : Modifies a key to keep only the wanted facets within it.

only_keep_wanted_facets_in_couple_dictionary : Modifies the keys of a model.variant couple dictionary according to the wanted description facets.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

### DOWNLADING THE ENTRIES ###

import intake_esgf  # This gives us access to the ESGF catalog to make queries.

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###

import numpy as np  # It is imported to work on the pandas arrays.

import xarray as xr  # This package is used to handle xarrays.

### TYPE HINTS ###

from numpy.typing import NDArray

###############################################
#### ONLY_FACETS_TO_IGNORE_FOR_COUPLE_ENTRY ###
###############################################


def define_facets_to_ignore_for_couple(
    filled_catalog_for_given_couple: intake_esgf.ESGFCatalog,
    search_facets_dictionary: dict[str, list[str]],
    defining_manually_output_keys: bool,
    wanted_description_facets: list[str],
) -> NDArray:
    """Defines the facets that will be ignored for a given model.variant couple dictionary keys.

    Parameters
    ----------

    filled_catalog_for_given_couple : intake_esgf.ESGFCatalog

        Intake-esgf catalog filled with the provided search criteria and the source_id and member_id of the couple.

    search_facets_dictionary : dict[str, list[str]]

        Search facets provided by the user.

    defining_manually_output_keys : bool

        Bool defining if the output keys are kept according to the default method of defined by wanted_description_facets.

    wanted_description_facets : list[str]

        List of the wanted description facets for the couple dictionary keys.

    Returns
    -------
    facets_to_ignore : list[str]

        List of the facets to be ignored for the coupel dictionary keys.

    Raises
    ------
    TypeError
        If wanted_description_facets is not defined.
    """

    ### DEFINING THE ORIGINAL FULL LIST OF FACETS ###

    full_used_facets = filled_catalog_for_given_couple.project.master_id_facets()

    ### TEST WHETHER THE USER DEFINES THE OUTPUT KEYS MANUALLY OR NOT ###

    if not (defining_manually_output_keys):
        ### DEFAULT MODE FOR OUTPUT KEYS ###

        # This default mode signifies that we keep all the keys that are different
        # for a single couple (source_id | member_id) search and add the source_id,
        # member_id and variable_id.

        ## Generate the wanted_description keys ##

        minimal_keys_for_entry = filled_catalog_for_given_couple._minimal_key_format()

        ## Generate the wanted_description keys ##
        wanted_description_facets = np.unique(
            minimal_keys_for_entry + ["source_id", "member_id", "variable_id"]
        )

    else:
        ### THE USER DEFINES THE KEYS MANUALLY ###

        ## Test if the user provided them or not ##

        if wanted_description_facets is None:
            raise TypeError(
                "'None' value provided for wanted_description_facets.\nPlease define it as an input."
            )

        ## Generate the wanted_description keys ##

        minimal_keys_for_entry = filled_catalog_for_given_couple._minimal_key_format()

        ## Generate the wanted_description keys ##
        wanted_description_facets = np.unique(
            minimal_keys_for_entry + wanted_description_facets
        )

    ### GENERATE THE FACETS TO IGNORE BASED ON THE WANTED DESCRIPTION KEYS ###

    ## Remove the wanted description facets from the full list of used facets ##

    facets_to_ignore = np.setdiff1d(full_used_facets, wanted_description_facets)

    ## Transform the facets to ignore from an array of np.str to a list[str] ##

    facets_to_ignore = [str(facet_to_ignore) for facet_to_ignore in facets_to_ignore]

    return facets_to_ignore


##################################
#### FIND_INDEX_OF_KEPT_FACETS ###
##################################


def find_index_of_kept_facets(
    facets_to_ignore: list[str],
    full_catalog_facets: list[str],
) -> list[int]:
    """Finds the index of the facets to be kept in the list of the full catalog facets.

    Parameters
    ----------
    facets_to_ignore : list[str]

        List of the facets to be ignored within the full catalog facets.

    full_catalog_facets : list[str]

        Ordered list of the full catalog facets used to describe an entry key the CMIP6 dictionary.

    Returns
    -------
    index_of_kept_facets : list[int]

        List of the index of the facets that will be kept.
    """

    ### GENERATES THE LIST OF THE INDEX OF KEPT FACETS ###

    index_of_kept_facets = [
        ii
        for ii, facet in enumerate(full_catalog_facets)
        if facet not in facets_to_ignore
    ]

    return index_of_kept_facets


#######################################
#### ONLY_KEEP_WANTED_FACETS_IN_KEY ###
#######################################


def only_keep_wanted_facets_in_key(
    full_key: str,
    index_of_kept_facets: list[int],
) -> str:
    """Modifies a key to keep only the wanted facets within it.

    Parameters
    ----------
    full_key : str

        Full key to be reduced.

    index_of_kept_facets : list[int]

        List of the index of the facets to keep in the splitted key.

    Returns
    -------
    key_with_wanted_facets : str

        Key reduced to the wanted facets.

    """
    full_key_splitted = full_key.split(".")

    new_key_splitted = [full_key_splitted[index] for index in index_of_kept_facets]

    key_with_wanted_facets = ".".join(new_key_splitted)

    return key_with_wanted_facets


#####################################################
#### ONLY_KEEP_WANTED_FACETS_IN_COUPLE_DICTIONARY ###
#####################################################


def only_keep_wanted_facets_in_couple_dictionary(
    catalog: intake_esgf.ESGFCatalog,
    cmip6_dictionary: dict[str, xr.Dataset],
    search_facets_dictionary: dict[str, list[str]],
    defining_manually_output_keys: bool,
    wanted_description_facets: list[str],
    verbose: bool = False,
) -> dict[str, xr.Dataset]:
    """Modifies the keys of a model.variant couple dictionary according to the wanted description facets.

    Originally we download dictionaries for a given couple with the full description keys :

    'mip_era.activity_drs.institution_id.source_id.experiment_id.member_id.table_id.variable_id.grid_label'

    This function reduces it for the given couple according to two possible modes.

    Default method : This signifies that the function keeps all the keys that are different
        for a single couple (source_id | member_id) search and adds the source_id and member_id to the description key.

    Manual method : It is the user that provides the wanted description facets.


    Parameters
    ----------

    catalog: intake_esgf.ESGFCatalog,

        Catalog that was filled by the search for the given model.variant couple.

    cmip6_dictionary : dict[str, xr.Dataset]

        CMIP6 dictionary holding the different entries.

    search_facets_dictionary : dict[str, list[str]]

        Search facets provided by the user.

    defining_manually_output_keys : bool

        Bool defining if the output keys are kept according to the default method of defined by wanted_description_facets.

    wanted_description_facets : list[str]

        List of the wanted description facets for the couple dictionary keys.

    verbose : bool, optional

        Bool defining if the function needs to print information, by default False.

    Returns
    -------
    updated_dictionary : dict[str, xr.Dataset]

        Model.variant couple dictionary with the keys reduced according to the wanted facets.
    """

    ### INITIALISATION ###

    ## Extract the full catalog facets description list ##

    full_catalog_facets = catalog.project.master_id_facets()

    ## Find the facets to ignore for the given couple ##

    facets_to_ignore = define_facets_to_ignore_for_couple(
        filled_catalog_for_given_couple=catalog,
        search_facets_dictionary=search_facets_dictionary,
        defining_manually_output_keys=defining_manually_output_keys,
        wanted_description_facets=wanted_description_facets,
    )

    ## Find the index of the facets to keep ##

    index_of_kept_facets = find_index_of_kept_facets(
        facets_to_ignore=facets_to_ignore,
        full_catalog_facets=full_catalog_facets,
    )

    ## Initialise the updated dictionary ##

    updated_dictionary = {}

    ### LOOP THROUGH THE KEYS ###

    # If wanted the first edited key is printed

    if verbose:
        show_first_key = True

    else:
        show_first_key = False

    for key in cmip6_dictionary.keys():
        ## Editing the key by keeping the wanted facets only ##

        key_with_wanted_facets = only_keep_wanted_facets_in_key(
            full_key=key,
            index_of_kept_facets=index_of_kept_facets,
        )

        # If wanted the first edited key is printed

        if show_first_key:
            print(
                "\nUpdating the key {} into {}.\n".format(key, key_with_wanted_facets)
            )

            show_first_key = False

        ## Setting this key to the updated dictionary ##

        updated_dictionary[key_with_wanted_facets] = cmip6_dictionary[key]

    return updated_dictionary
