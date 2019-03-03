import imageio
import os
import datetime

root = os.getcwd()
target_extension = 'jpg'

root_contents = os.path.lisdir(root)
jpeg_files = []
for item in root_contents:
    try:
        fname, extension = item.split('.')
    except:
        continue
    if extension == target_extension: jpeg_files.append(item)

jpeg_files = [os.path.join(root, fname) for fname in jpeg_files]
images = []
for fname in jpeg_files:
    images.append(imageio.imread(fname))

date = str(datetime.datetime.now().date())
movie_name = date+'.gif'
movie_name = os.path.join(root, movie_name)
imageio.mimsave(movie_name, images)
print('DONE'))
