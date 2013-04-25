
import os, datetime, hashlib


def filename_generate(instance, old_filename, folder=''):
    extension = os.path.splitext(old_filename)[1]
    m = hashlib.md5()
    m.update(str(datetime.datetime.now()))
    m = m.hexdigest()
    return u'%s/%s/%s/%s/%s%s' % (folder, m[:2], m[2:4], m[4:6], m[6:], extension)


def item_image_border_filename_generate(instance, old_filename):
    return filename_generate(instance, old_filename, 'borders')

def item_image_filename_generate(instance, old_filename):
    return filename_generate(instance, old_filename, 'items')
