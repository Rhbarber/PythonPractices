from pydactyl import PterodactylClient

api = PterodactylClient('debug', 'anything')

[i for i in dir(api.client.servers) if not i.startswith('_')]
# ['account', 'backups', 'databases', 'files', 'get_server', 'get_server_utilization', 'list_permissions', 'list_servers', 'network', 'schedules', 'send_console_command', 'send_power_action', 'servers', 'settings', 'startup', 'users']
[i for i in dir(api.client.servers.settings) if not i.startswith('_')]
# ['reinstall_server', 'rename_server']
print(api.client.servers.settings.rename_server.__doc__)
# Renames the server.
#        Args:
#            server_id(str): Server identifier (abbreviated UUID)
#            name(str): New name for the server
