#!/usr/bin/env python3

"""This script contains functions dedicated to handle a CMIP6 xarray dataset.
Functions :

add_one_variable_to_dataset : Adds a variable from a xarray DataArray to a xarray Dataset.

generate_climatology : Generates a climatology of the variable of a xarray dataset based on the frequency given in input.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###

import xarray as xr  # This is to handle xarray objects.

import xcdat as xc  # It is imported to generate the climatologies.

###################################
### DEFINITION OF THE FUNCTIONS ###
###################################

###################################
### ADD_ONE_VARIABLE_TO_DATESET ###
###################################


def add_one_variable_to_dataset(
    variable_name: str,
    variable_dataset: xr.Dataset,
    dataset: xr.Dataset = None,
    modify_data: bool = False,
) -> xr.Dataset:
    """Adds a variable from a xarray DataArray to a xarray Dataset.

    Parameters
    ----------
    variable_name : str

        Name of the variable to add to the output Dataset.

    variable_dataset : xr.Dataset

        DataArray that needs to be added to a Dataset or turned into a Dataset.

    dataset : xr.Dataset, optional

        Dataset that, if provided, gets modified in place, by default None.

    modify_data : bool, optional

        Defines whether we modify a provided input dataset in-place, by default False.

    Returns
    -------
    dataset : xr.Dataset

        The input dataset that has been modified in-place or created.
    """
    ### ADDING THE VARIABLE TO THE DATASET ###

    ## Checking wether we need to modify the dataset or not ##

    if not modify_data:  # If modify_data is false initializes the dataset.
        dataset = variable_dataset

    else:  # If modify_data is true fills the provided one.
        dataset = dataset.assign(variable_dataset)

    return dataset


############################
### GENERATE_CLIMATOLOGY ###
############################


def generate_climatology(
    dataset: xr.Dataset,
    variable_to_compute_climatology: str,
    frequency: str,
) -> xr.Dataset:
    """Generates a climatology of the variable of a xarray dataset based on the frequency given in input.

    Parameters
    ----------
    dataset : xr.Dataset

        Input dataset holding the variable on which the climatology is computed.

    variable_to_compute_climatology : str

        The name of the variable on which to compute the climatology.

    frequency : str

        Frequency of the climatology : can be "day", "month" and "seasons", for more details see https://xcdat.readthedocs.io/en/latest/generated/xarray.Dataset.temporal.climatology.html.

    Returns
    -------
    dataset_with_climatology_of_variable : xr.Dataset

        Input dataset with the climatology computed for the given variable.
    """

    ### COMPUTING THE CLIMATOLOGY ###

    dataset_with_climatology_of_variable = dataset.temporal.climatology(
        data_var=variable_to_compute_climatology,
        freq=frequency,
    )

    return dataset_with_climatology_of_variable


######################
### USED FOR TESTS ###
######################

if __name__ == "__main__":
    pass
