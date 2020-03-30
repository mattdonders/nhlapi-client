import logging
import requests


class APIEndpoint(Model):
    def __init__(self, api, endpoint=None, cls=None):
        self.api = api
        self.endpoint = endpoint
        self._cls = cls

    def get(
        self,
        endpoint=None,
        resource_id=None,
        resource_cls=None,
        json_key=None,
        single_resource=False,
        **kwargs
    ):

        endpoint = endpoint or self.endpoint

        if not resource_cls:
            resource_cls = self._cls

        try:
            response = self.api.execute(endpoint)
            # logging.info("Finalized Request URL: %s", response.url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            logging.error("HTTP Error: %s", errh)
            raise
        except requests.exceptions.ConnectionError as errc:
            logging.error("Connection Error: %s", errc)
            raise
        except requests.exceptions.Timeout as errt:
            logging.error("Timeout Error: %s", errt)
            raise
        except requests.exceptions.RequestException as err:
            logging.error("Uncaught Exception: %s", err)
            raise

        return resource_cls.parse(response.json())

        # if json_key:
        #     response = response.json()
        #     response = response[json_key]

        # if single_resource:
        #     return resource_cls.parse(response[0])

        # return [resource_cls.parse(resource) for resource in response]
