import logging

from spaceone.inventory.libs.connector import AzureConnector
from spaceone.inventory.error.custom import *

__all__ = ['MySQLServerConnector']
_LOGGER = logging.getLogger(__name__)


class MySQLServerConnector(AzureConnector):

    def __init__(self, secret_data=None, **kwargs):
        super().__init__(**kwargs)

        self.set_connect(secret_data)

    def list_servers(self):
        return self.mysql_client.servers.list()

    def list_firewall_rules_by_server(self, resource_group_name, server_name):
        return self.mysql_client.firewall_rules.list_by_server(resource_group_name=resource_group_name, server_name=server_name)

    def list_server_parameters(self, resource_group_name, server_name):
        return self.mysql_client.server_parameters._list_update_configurations_initial(resource_group_name=resource_group_name, server_name=server_name, value=[])
