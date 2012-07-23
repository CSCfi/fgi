import os, os.path

urdir='/var/spool/nordugrid/usagerecords/urs'
sessiondir='/export/home/sessiondir'

def ur_count(name):
	return len([name for name in os.listdir(urdir) if os.path.isfile(urdir + '/' + name)])

def sesdir_count(name):
	return len([name for name in os.listdir(sessiondir) if os.path.isdir(sessiondir + '/' + name)])


def metric_init(params):
    global descriptors, sysdir

    if 'urdir' in params:
        urdir = params['urdir']
    if 'sessiondir' in params:
	sessiondir = params['sessiondir']

    ur = {'name': 'ur_count',
        'call_back': ur_count,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'bytes',
        'slope': 'both',
        'format': '%u',
        'description': 'UR records unsent',
        'groups': 'arc-sanity'}
    ses = {'name': 'sessiondir_count',
        'call_back': sesdir_count,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'bytes',
        'slope': 'both',
        'format': '%u',
        'description': 'Sessiondirs present',
        'groups': 'arc-sanity'}


    descriptors = [ur,ses]

    return descriptors

def metric_cleanup():
    '''Clean up the metric module.'''
    pass

#This code is for debugging and unit testing
if __name__ == '__main__':
    metric_init({})
    for d in descriptors:
        v = d['call_back'](d['name'])
        print 'value for %s is %u' % (d['name'],  v)

