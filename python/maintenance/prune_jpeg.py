import os

prune_extensions = set(['jpeg','jpg','png'])

contents = os.listdir()
root = os.getcwd()
contents = [os.path.join(root, c) for c in contents]
purge_files = []
for item in contents:
    if not os.path.isfile(item): continue
    path, fname = os.path.split(item)
    fname = fname.split('.')
    if len(fname) != 3: continue
    if fname[2] not in prune_extensions: continue
    purge_files.append(item)
for item in purge_files:
    os.remove(item)
