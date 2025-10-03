import requests
from dotenv import load_dotenv
import os

load_dotenv()

class HTTPayerClient:
    """
    Unified HTTPayer client for managing 402 responses and x402 payments.
    """

    def __init__(self,router_url=None,api_key=None):
        """
        :param router_url: URL of the hosted /pay endpoint.
        """
        self.router_url = router_url or os.getenv("X402_ROUTER_URL", "http://app.httpayer.com/pay")
        self.api_key = api_key or os.getenv('HTTPAYER_API_KEY')

        if not self.router_url or not self.api_key:
            missing = []
            if not self.router_url:
                missing.append("X402_ROUTER_URL")
            if not self.api_key:
                missing.append("HTTPAYER_API_KEY")
            raise ValueError(f"Missing configuration: {', '.join(missing)}")

    def pay_invoice(self, api_url=None, api_method="GET", api_payload={}):
        """
        Pay a 402 payment (using the router service).
        """
        return self._pay_via_router(api_url, api_method, api_payload)

    def _pay_via_router(self, api_url, api_method, api_payload=None, api_params=None, api_headers=None):
        """
        Call the hosted HTTPayer /pay endpoint to handle payment + retry.
        """
        if not self.router_url:
            raise ValueError("X402_ROUTER_URL not configured!")

        data = {
            "api_url": api_url,
            "method": api_method,
            "payload": api_payload or {},
        }
        if api_params:
            data["params"] = api_params
        if api_headers:
            data["headers"] = api_headers

        header = {'x-api-key': self.api_key}
        resp = requests.post(self.router_url, headers=header, json=data)
        return resp

    def request(self, method, url, **kwargs):
        """
        Automatically handle 402 Payment Required HTTP flow.
        """
        resp = requests.request(method, url, **kwargs)

        if resp.status_code == 402:
            api_payload = kwargs.get("json", {})
            api_params = kwargs.get("params", {})
            api_headers = kwargs.get("headers", {})
            resp = self._pay_via_router(url, method, api_payload, api_params, api_headers)

        return resp

