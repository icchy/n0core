try:
    from n0core.lib.n0mq import N0MQ
    from n0core.config import config
except:
    import sys
    sys.path.append('../../')
    from n0core.lib.n0mq import N0MQ
    from n0core.config import config


n0mq = N0MQ(config['pulsar']['service_url'])
consumer = n0mq.subscribe(config['pulsar']['scheduler_topic'])

MAP_CREATE = {
    'VM': create_VM,
    'Volume': create_Volume,
    'Network': create_Network,
    'Port': create_Port,
}

MAP_ATTACH = {
    'Volume': attach_Volume,
    'Network': attach_Network,
    'Port': attach_Port,
}


def create_VM(obj):
    vm = obj.VM


def create_Volume(obj):
    volume = obj.Volume


def create_Network(obj):
    network = obj.Network


def create_Port(obj):
    port = obj.Port


def attach_Volume(obj):
    volume = obj.Volume


def attach_Network(obj):
    network = obj.Network


def attach_Port(obj):
    port = obj.Port



@consumer.on('Request')
def on_request(message):
    obj = message.data.object
    data_name = obj.WhichOneof('data')

    # check db
    for relation in obj.relations:
        _data_name = relation.object.WhichOneOf('data')
        FUNCMAP[data_name](obj)

    FUNCMAP[data_name](obj)



def main():
    n0mq.listen()


if __name__ == '__main__':
    main()
