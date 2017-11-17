
sysdir='/sys/class/infiniband/mlx4_0/ports/1/counters/'

def counter_data_handler(name):
	# print sysdir + '/' + name
	try: 
		f = open(sysdir + '/' + name )
	except IOError:
		return 0

	for l in f:
		line = l.split()

	f.close()
	return int(line[0])


def metric_init(params):
    global descriptors, sysdir

    if 'sysdir' in params:
        sysdir = params['sysdir']

    r1 = {'name': 'port_rcv_data',
        'call_back': counter_data_handler,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'bytes',
        'slope': 'positive',
        'format': '%u',
        'description': 'IB receive data',
        'groups': 'ibnetwork'}
    r2 = {'name': 'port_rcv_packets',
        'call_back': counter_data_handler,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'bytes',
        'slope': 'positive',
        'format': '%u',
        'description': 'IB receive packets',
        'groups': 'ibnetwork'}
    r3 = {'name': 'port_rcv_errors',
        'call_back': counter_data_handler,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'bytes',
        'slope': 'positive',
        'format': '%u',
        'description': 'IB receive errors',
        'groups': 'ibnetwork'}
    t1 = {'name': 'port_xmit_data',
        'call_back': counter_data_handler,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'bytes',
        'slope': 'positive',
        'format': '%u',
        'description': 'IB transmit data',
        'groups': 'ibnetwork'}
    t2 = {'name': 'port_xmit_packets',
        'call_back': counter_data_handler,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'bytes',
        'slope': 'positive',
        'format': '%u',
        'description': 'IB transmit packets',
        'groups': 'ibnetwork'}
    t3 = {'name': 'port_xmit_errors',
        'call_back': counter_data_handler,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'bytes',
        'slope': 'positive',
        'format': '%u',
        'description': 'IB transmit errors',
        'groups': 'ibnetwork'}



    descriptors = [r1,r2,r3,t1,t2,t3]

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

