#!/usr/bin/env python3

import os.path
import os
import sys
import subprocess

from cgecore.utils.loaders_mixin import LoadersMixin




class Config():

    ENV_VAR_FILENAME = "environment_variables.md"
    
    DEFAULT_VALS = {
       
        "min_cov": 0.6,
        "threshold": 0.9,
        
       
    }

    def __init__(self, args):

        # Directoy of config.py substracted the last dir 'cge'
        self.plasmidfinder_root = os.path.dirname(os.path.realpath(__file__))[:-3]
        self.env_var_file = "{}{}".format(self.plasmidfinder_root,
                                          Config.ENV_VAR_FILENAME)
        
        Config.set_default_and_env_vals(args, self.env_var_file)


    

    @staticmethod
    def set_default_and_env_vals(args, env_def_filepath):

        known_envs = LoadersMixin.load_md_table_after_keyword(
            env_def_filepath, "## Environment Variables Table")

        # Set flag values defined in environment variables
        for var, entries in known_envs.items():

            try:
                cli_val = getattr(args, entries[0])
                # Flags set by user will not be None, default vals will be None
                if(cli_val is not None):
                    continue

                var_val = os.environ.get(var, None)
                if(var_val is not None):
                    setattr(args, entries[0], var_val)

            except AttributeError:
                sys.exit("ERROR: A flag set in the Environment Variables Table"
                         " in the README file did not match any valid flags in"
                         " PlasmidFinder. Flag not recognized: {}."
                         .format(entries[0]))

        Config._set_default_values(args)

    @staticmethod
    def _set_default_values(args):
        for flag, def_val in Config.DEFAULT_VALS.items():
            val = getattr(args, flag)
            if(val is None):
                setattr(args, flag, def_val)
