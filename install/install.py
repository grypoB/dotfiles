import sys
import os
from subprocess import call
import subprocess
import re

if __name__ == "__main__":

    script_parent = os.path.dirname(os.path.realpath(__file__))
    script_gparent = os.path.dirname(script_parent)
    find_res = subprocess.Popen('find '+script_gparent, shell=True, stdout=subprocess.PIPE)
    repo_items = find_res.stdout.readlines()
    home_folder = os.getenv("HOME")

    for item in repo_items:
        item = item.strip()
        
        item_name = os.path.basename(item)
        if not ( re.search('\.git/',item) or re.search('\.gitignore$',item) or re.search('install', item) ):

            if os.path.isfile(item):

                new_item_parent = (os.path.dirname(item)).replace(script_gparent,home_folder)
                symlink_path = os.path.join(new_item_parent,item_name)

                if not os.path.exists(new_item_parent):
                    os.makedirs(new_item_parent)
                if os.path.isfile(symlink_path):
                    if not os.path.islink(symlink_path):
                        print symlink_path + ' already exists'
                    else:
                        os.remove(symlink_path)
                        os.symlink(item, symlink_path)
                else:
                    os.symlink(item, symlink_path)
