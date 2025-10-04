# ./import_cmip6_data_utils/preprocessing

## Description of the full subpackage

This subpackage is dedicated to condensing raw intake-esgf catalog outputs into more compact and readable dictionaries. It is used by the **load** subpackage.

- **condense_dictionary**, is dedicated to regrouping variables from the same model entry within a CMIP6 dictionary into the same xarray dataset. Its main function is **condense_a_dictionary_of_different_entries** that needs **condense_same_entry_variables_into_one_dataset** to handle one entry at a time.

- **reduce_couple_dictionary_keys**, is used to reduce the dictionary description keys to what the user wants. Its main function is **only_keep_wanted_facets_in_couple_dictionary** while the other functions are utilitary functions used to achieve the goal of the script.

## condense_dictionary

### Description of the script

This script contains functions that allow to regroup variables from the same model entry into the same xarray dataset.

What we mean by **entry** is a set of facets that is independent of another set of facets in the full CMIP6 output dictionary. Different entries could be defined, for example, by a different **experiment_id**, **grid_label** or **table_id** for a given **source_id** and **member_id** couple.

To give a simple example : if the **clt** and **tas** variables were loaded for GFDL-CM4.r1i1p1f1, a **source_id.member_id couple**, and for two experiments : **piClim-aer** and **piClim-control**, then intake-esgf generates a single dictionary with **four xarray Datasets**. This **condensing_dictionary** script, will generate **two xarray Datasets**, one per entry, into a dictionary. Actually, two variables for a different experiment are independent.

Optionally, the climatology of each variable can be computed according to the user-defined parameters and options.

### Functions

**condense_same_entry_variables_into_one_dataset** : Regroups the variables of a CMIP6 dictionary associated to the provided entry key in a xarray Dataset.

**condense_a_dictionary_of_different_entries** : Regroups the variables of a CMIP6 dictionary associated to different entries in a dictionary of xarray Dataset.

### Inputs

The inputs of this script are CMIP6 data **dictionaries**. They are composed of **xarray Datasets** of variables associated to different catalog entries.-

### Outputs

The outputs are condensed CMIP6 data **dictionaries**. All the variables associated to the same entries have been regrouped into a single dataset, reducing the number of **str** keys of the dictionary.

## reduce_couple_dictionary_keys

### Description of the script

This script contains functions to edit the dictionary keys of a CMIP6 dictionary associated to a model.variant couple.

The default option, when <g>**defining_manually_output_keys**</g> is set to <r>**False**</r>, implies that, only the facets that are **different between the variables of a single given model.variant couple** are kept. What's more, the **source_id**, **member_id** and **variable_id** are always preserved. As a result, if the search facets are

```{"variable_id" : "clt", "experiment_id" : ["piClim-aer","piClim-control"], "table_id" : ["Amon"]}```

then

```CMIP6.RFMIP.NOAA-GFDL.GFDL-CM4.piClim-aer.r1i1p1f1.Amon.rsdscs.gr1```

becomes

```GFDL-CM4.piClim-aer.r1i1p1f1.rsdscs```.

This is the case because for the **clt variables** in the dictionary of GFDL-CM4.r1i1p1f1, **only the experiment_id is different**. The **table_id** would not change between two **clt** variables of the two different experiments. Same for the rest of the facets.

### Functions

**define_facets_to_ignore_for_couple** : Defines the facets that will be ignored for a given model_variant couple dictionary keys.

**find_index_of_kept_facets** : Finds the index of the facets to be kept in the splitted full catalog facets.

**only_keep_wanted_facets_in_key** : Modifies a key to keep only the wanted facets within it.

**only_keep_wanted_facets_in_couple_dictionary** : Modifies the keys of a model.variant couple dictionary according to the wanted description facets.

### Inputs

These functions deal with **str** CMIP6 keys that are organised in terms of facets. One full key is organised like this :

```'mip_era.activity_drs.institution_id.source_id.experiment_id.member_id.table_id.variable_id.grid_label'```

They can be splitted under the form of a list :

```['mip_era','activity_drs','institution_id','source_id','experiment_id','member_id','table_id''variable_id','grid_label']```

For more details on the facets see : <http://goo.gl/v1drZl> (last visited 01/09/2025).

### Outputs

The outputs are **str** CMIP6 keys that have been deprived of the facets not wanted by the user.
