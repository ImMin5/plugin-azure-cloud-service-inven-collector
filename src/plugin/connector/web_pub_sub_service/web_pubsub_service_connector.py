import logging

from plugin.connector.base import AzureBaseConnector

_LOGGER = logging.getLogger("spaceone")


class WebPubSubServiceConnector(AzureBaseConnector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_connect(kwargs.get('secret_data'))

    def list_by_subscription(self):
        return self.web_pubsub_service_client.web_pub_sub.list_by_subscription()

    def list_hubs(self, resource_group_name, resource_name):
        return self.web_pubsub_service_client.web_pub_sub_hubs.list(resource_group_name=resource_group_name,
                                                                    resource_name=resource_name)

    def list_keys(self, resource_group_name, resource_name):
        return self.web_pubsub_service_client.web_pub_sub.list_keys(resource_group_name=resource_group_name,
                                                                    resource_name=resource_name)