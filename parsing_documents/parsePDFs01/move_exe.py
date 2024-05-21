import os, sys


init_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
exe_dir = os.path.join(init_dir, "dist")

if len(os.listdir(exe_dir)) != 0:
    for i in os.listdir(exe_dir):
        os.replace(os.path.join(exe_dir, i), os.path.join(init_dir, i))