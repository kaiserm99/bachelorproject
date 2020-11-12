#!/usr/bin/env python3
"""
Bachelorproject
University of Freiburg
Foundations of Artificial Intelligence

Copyright 2020 by Adrian Emler
Author: Adrian Emler
email: emleradrian@gmail.com

Usage:
    To generate all models for a cnf file call in a shell:
        > python All_Models <file.cnf>
    It will print all possible models.
Note:
    The code is styled by PEP8 guidlines.
"""

import sys
import os
import subprocess
import shutil

tmp_model = 'tmp_model.model'
tmp_cnf = 'tmp.cnf'
tmp2_cnf = 'tmp_2.cnf'
DEVNULL = open(os.devnull, 'wb')


def main():
    """ Generates all possible models for a cnf file.
        To do so, it computes the following steps:
            1. Copy the file to an tmp file.
                So the original file will not be edited.
            2. Generate the model for tmp file.
            3. Invert the last model.
            4. Add the inverted model to the tmp file.
            5. Redo step 2-5 until it is unsatisfiable.
    """
    # check args and if file exists
    if len(sys.argv) != 2:
        print('usage: python All_Models <cnf_file>')
        return
    cnf_file = sys.argv[1]
    if not os.path.isfile(cnf_file):
        print('no such file', cnf_file)
        return

    # copy model to tmp.cnf
    shutil.copyfile(cnf_file, tmp_cnf)

    all_models = []
    model_line = True
    while model_line:
        # generate the next model
        err_msg = subprocess.Popen(
            ['minisat', tmp_cnf, tmp_model],
            stdin=DEVNULL, stdout=DEVNULL, stderr=subprocess.PIPE, shell=False)

        # Handle warnings and errors thrown from minisat.
        err_msg = err_msg.communicate()[1]
        if err_msg != b'':
            print(err_msg.decode('utf-8'))
            break

        # read the model from the tmp_model.model file
        model_line = read_model(tmp_model)
        if not(model_line is False):
            all_models.append(model_line)
            # generate a new constraint(clause) from the model
            new_constraint = invert_model(model_line)
            # append new constraint to the cnf file
            # and increase the clauses count
            add_constraint(tmp_cnf, new_constraint + '\n')

    # remove tmp files
    os.remove(tmp_model)
    os.remove(tmp_cnf)
    if not os.path.isfile(tmp2_cnf):
        os.remove(tmp2_cnf)

    print('All models:\n', all_models)


def read_model(file_name: str):
    """ Reads the model from the tmp_model file.

        Args:
            file_name: The file name of tmp_model.
        Returns:
            False if its unsatisfiable.
            Else the model as string
    """
    headline = ''
    model_line = ''
    with open(file_name, 'r') as file:
        headline = file.readline().rstrip()
        if headline == 'UNSAT':
            return False
        model_line = file.readline().rstrip()
    return model_line


def invert_model(model_line: str):
    """ Inverts a model.

        Args:
            model_line: The model as string.
        Returns:
            The inverted model as string.
    """
    model_line = model_line.split(' ')
    new_constraint = ''
    for c in model_line:
        if c[0] == '-':
            new_constraint += c[1] + ' '
        elif c[0] != '0':
            new_constraint += '-' + c[0] + ' '
    return new_constraint + '0'


def add_constraint(file_name: str, constraint: str):
    """ append a new constraint(clausel) at the end of a cnf file and
        increases the clausel counter of the cnf file.

        Args:
            file_name: The file name of a cnf file.
            constraint: The new clausel which should be appended.
    """
    shutil.copyfile(tmp_cnf, tmp2_cnf)

    with open(tmp2_cnf, 'r') as old_file:
        first_line = old_file.readline().rstrip()
        first_line = first_line.split(' ')
        # increase clauses count by 1
        first_line[-1] = str(int(first_line[-1]) + 1)
        with open(tmp_cnf, 'w') as file:
            file.write(' '.join(first_line) + '\n')
            line = old_file.readline()
            while line:
                file.write(line)
                line = old_file.readline()
            file.write(constraint + '\n')


if __name__ == '__main__':
    main()
