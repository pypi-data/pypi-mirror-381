#!/usr/bin/env python3

"""This script contains a function to create, remove and check the existence of given folders thanks to their paths.

Functions :
-----------

create_dir : Creates a tree of folders and optionally empties it if it existed before.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.

"""


##################################
### IMPORTATION OF THE MODULES ###
##################################

import os  # It is imported to handle path's management

import shutil  # This is for removing a folder tree


#############################################
### DEFINITION OF THE SPECIFIC EXCEPTIONS ###
#############################################


class FileExistsError(Exception):
    """Raise when the path already exists and isn't a regular file or folder"""


###################################
### DEFINITION OF THE FUNCTIONS ###
###################################

##################
### CREATE_DIR ###
##################


def create_dir(parent_path: str, name: str, clear: bool = True) -> str:
    """Creates a tree that leads to a folder and optionally empties it if it existed before.

    Parameters
    ----------
    parent_path : str

        Parent path of the tree or folder.

    name : str

        Name of the folder to create or path that leads to the folder to create.

    clear : bool, optional

        Bool defining we clear the tree or not, by default True.

    Returns
    -------
    path : str

        Path to the created folder.

    Raises
    ------
    FileExistsError

        This error is raised when the generated path already exists and is not a regular file or folder.
    """

    ### CREATE THE FULL PATH ###

    path = os.path.join(parent_path, name)

    ### CLEARING PROCEDURE IF THE PATH/SYMLINK ALREADY EXISTS ###

    ## Test if we need to clear and if the path/symlink already exists ##

    if clear and os.path.lexists(path):
        ## If it is a path or a symlink we remove it ##

        if os.path.isfile(path) or os.path.islink(path):
            shutil.rmtree(path)

        ## If it is a path we remove all the tree ##

        elif os.path.isdir(path):
            shutil.rmtree(path)

        ## If we do not know what this is ##

        else:
            raise FileExistsError(
                "Path already exists and isn't a regular file or folder"
            )

    ### MAKE THE DIRECTORY ###

    os.makedirs(path, exist_ok=True)  # if it exists : no error is sent

    return path


######################
### USED FOR TESTS ###
######################

if __name__ == "__main__":
    pass
