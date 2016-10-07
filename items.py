actions = {
    'set_hostname': {
        'command': 'hostnamectl set-hostname {}'.format(node.name),
        'unless': 'hostnamectl status --static | grep {}'.format(node.name),
    },
}
