#!/usr/bin/env python3

"""This script contains functions to prepare the download of the CMIP6 data.

Functions :
-----------

set_folder_to_save_raw_data : This function sets the path of the folder in which the data will be saved.

filtering_function : Filters the catalog to only keep model.variant couples that fits two optional conditions.

filter_catalog : This function wraps the filtering function of the intake-esgf catalog such that the filtering parameters are globally defined within this script.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""


##################################
### IMPORTATION OF THE MODULES ###
##################################

# ================ IMPORTATIONS ================ #

### LOAD AND NAVIGATE THROUGH THE DATA ###

import intake_esgf  # This package gives us access to the ESGF catalog to make queries.

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###

import pandas as pd  # It is imported to manage the product of the search.

### HANDLING PATHS ###

from os.path import join  # This is used to join two paths together.

### PROJECT MODULES ###

## Create directories and clean them ##

from import_cmip6_data_utils.tools.folders import (
    create_dir,  # It is used to create a cleaned directory in which the downloaded data will be stored.
)

###############################
#### SET_DOWNLOADING_FOLDER ###
###############################


def set_folder_to_save_raw_data(
    parent_path: str,
    download_folder_name: str,
    clear: bool = True,
    verbose: bool = False,
):
    """This function sets the path of the folder in which the data will be saved.

    Parameters
    ----------

    parent_path : str

        Parent path of the folder in which the data will be saved.

    download_folder_name : str

        Name of the folder in which the data will be saved.

    clear : bool, optional

        Bool defining we clear the tree or not, by default True.

    verbose : bool, optional

        Bool defining if the function needs to print information, by default False.
    """
    ### CREATE THE DIRECTORY ###

    download_path = create_dir(
        parent_path=parent_path,
        name=download_folder_name,
        clear=clear,
    )

    ### SET THE DOWNLOAD FOLDER PATH ###

    intake_esgf.conf.set(local_cache=download_path)

    ### SET THE PATH VARIABLES ###

    ## Write the full path of the raw data ##

    full_path_raw_data = join(download_path, "CMIP6")

    ## Write the full path of the preprocessed data ##

    full_path_preprocessed = join(download_path, "preprocessed")

    # If wanted prints the setting.

    if verbose:
        print(
            "\nThe folder in which the raw data will be downloaded is under the path {}.\n".format(
                full_path_raw_data
            )
        )

        print(
            "\nThe folder in which the preprocessed data will be saved is under the path {}.\n".format(
                full_path_preprocessed
            )
        )

    return download_path


###########################
#### FILTERING_FUNCTION ###
###########################


def filtering_function(
    grouped_outputs_by_model_and_variants: pd.DataFrame,
) -> bool:
    """Filters the catalog to only keep model.variant couples that fits two optional conditions.

    This function is fed to the intake-esgf catalog as an input.

    The first condition is that a given model.variant couple have the expected number of outputs.
    This condition is optional and is chosen by the user through a global parameter defined in the notebook.

    The second condition is that a part of a given model.variant couple outputs, organised into a pandas Dataframe, represent a subset of a provided filtering-criteria dataframe.
    To put it in another words, some facets associated to this specific entry of the catalog needs to correspond to the criteria imposed by a .csv file.
    This condition is optional and is chosen by the user through a global parameter defined in the notebook.

    For example, the user could provide for a .csv of model_id and variant_id and if the given couple is not in this list, this entry would be deleted.
    Another example is that a user would want to keep only the models associated with a specific institution for a specific variable.

    Note that the conditions criteria and the applicability conditions are defined globally.
    This is because intake-esgf do not allow for a filtering_function with more than the DataFrame as input.

    Parameters
    ----------
    grouped_model_entry : pd.DataFrame

        DataFrame of all the facets associated to a given model.variant couple.

    Returns
    -------
    bool

        Bool defining if the chosen conditions were met, it is always True if no condition was chosen.

    """
    ### INITIALISATION ###

    ## Retrieve global parameters defined in the main script ##

    # These parameters NEED to be defined in the main script

    global user_expected_outputs_number_per_model_variant, user_filtering_with_csv_file, user_filtering_criteria, user_filtering_by_number_of_outputs

    ### TEST :  NUMBER OF OUTPUTS ###

    ## We define the test result by setting it to True ##

    test_file_number = (
        True  # It is set to True to be ignored if the test is not wanted by the user.
    )

    ## The user required the first test ##

    if user_filtering_by_number_of_outputs:
        if (
            len(grouped_outputs_by_model_and_variants)
            == user_expected_outputs_number_per_model_variant
        ):
            ## Test succeeded ##

            test_file_number = True

        else:
            ## Test failed ##

            test_file_number = False

        ### TEST : FILTER THANKS TO A CSV FILE ###

        ## We define the test result by setting it to True ##

        test_csv_criteria = True  # It is set to True to be ignored if the test is not wanted by the user.

        ## The user required the second test ##

        if user_filtering_with_csv_file:
            ### TEST IF GROUPED_MODEL_ENTRY HOLDS A SUBSET OF USER_FILTERING_CRITERIA ###

            # If grouped_model_entry does hold a subset of user_filtering_criteria then
            # the merging of grouped_model_entry and filtering criteria with the following
            # options should preserve totally grouped_model_entry. The options are detailed
            # in the following paragraphs.
            #
            # The merge is realised "on" the columns of user_filtering_criteria as they are
            # what we want to identify within the columns of grouped_model_entry
            #
            # The "inner" option implies that we keep all the rows of grouped_model_entry
            # whose a subset of columns match the criteria in the filtering DataFrame.

            ## We realise the merging process described above ##

            filtered_grouped_model_model_and_variant = pd.merge(
                grouped_outputs_by_model_and_variants,
                user_filtering_criteria,
                how="inner",
                on=list(user_filtering_criteria.keys()),
            )

            ## We test if the filtered DataFrame is equal to the input DataFrame ##

            # We reset the index of the input or the test fails systematicaly #

            grouped_outputs_by_model_and_variants = (
                grouped_outputs_by_model_and_variants.reset_index(drop=True)
            )

            # Is the filtered entry equal to the input entry ? #

            test_csv_criteria = grouped_outputs_by_model_and_variants.equals(
                filtered_grouped_model_model_and_variant
            )

            ## The total result of the filtering is returned ##

            return test_file_number * test_csv_criteria

        ## The user did not require the second test ##

        else:
            ## The total result of the filtering is returned ##

            return test_file_number * test_csv_criteria


#######################
#### FILTER_CATALOG ###
#######################


def filter_catalog(
    catalog: intake_esgf.ESGFCatalog(),
    filtering_criteria: pd.DataFrame,
    expected_outputs_number_per_model_variant: int,
    filtering_with_csv_file: bool,
    filtering_by_number_of_outputs: bool,
):
    """This function wraps the filtering function of the intake-esgf catalog such that the filtering parameters are globally defined within this script.

    Indeed the conditions criteria and the applicability of the second condition are defined globally.
    This is because intake-esgf do not allow for a filtering_function with more than the DataFrame as input.
    Therefore, we define them in the notebook and then we define them globally in this script.

    Parameters
    ----------
    catalog : intake_esgf.ESGFCatalog

        Catalog that was filled by the full search criteria.

    filtering_criteria : pd.DataFrame

        Dataframe of the filtering facets extracted from the the filtering csv file.

    expected_outputs_number_per_model_variant : int

        Int number of expected outputs per model.variant couple.

    filtering_with_csv_file : bool

        Bool defining whether we filter the catalog with the filtering csv file criteria or not.

    filtering_by_file_number : bool

        Bool defining whether we filter the catalog by expected number of outputs per model.variant couple or not.

    Returns
    -------
    catalog : intake_esgf.ESGFCatalog

        Catalog that was filtered.
    """

    ### INITIALISATION ###

    ## Set the filtering parameters as global for the filtering function ##

    global user_expected_outputs_number_per_model_variant, user_filtering_with_csv_file, user_filtering_criteria, user_filtering_by_number_of_outputs

    ## Define them thanks to the parameters set in the import_cmip6_data notebook ##

    user_filtering_criteria = filtering_criteria

    user_expected_outputs_number_per_model_variant = (
        expected_outputs_number_per_model_variant
    )

    user_filtering_with_csv_file = filtering_with_csv_file

    user_filtering_by_number_of_outputs = filtering_by_number_of_outputs

    ### FILTER THE CATALOG ###

    catalog = catalog.remove_incomplete(filtering_function)

    return catalog


######################
### USED FOR TESTS ###
######################

if __name__ == "__main__":
    pass
