import os

from .auth import AzureTokenManager


class InputHandler:
    def __init__(self, environment):

        print(f"[Input Handler] Host: {environment.host} Partition: {environment.parsed_options.partition}  App ID: {environment.parsed_options.appid}")

        self.partition = environment.parsed_options.partition
        self.base_url = environment.host
        self.app_id = environment.parsed_options.appid
        
        # Detect if running in Azure Load Testing environment (production)
        self.is_azure_load_test_env = self._detect_azure_load_test_environment()
        
        self.header = self.prepare_headers()
    
    def _detect_azure_load_test_environment(self):
        """
        Detect if we're running in Azure Load Testing environment.
        
        Returns:
            bool: True if running in Azure Load Testing, False if local development
        """
        # Azure Load Testing sets specific environment variables
        azure_load_test_indicators = [
            'LOCUST_HOST',  # Set by Azure Load Testing
        ]
        
        # Check if any Azure Load Testing indicators are present
        for indicator in azure_load_test_indicators:
            if os.getenv(indicator):
                print(f"[Input Handler] Detected Azure Load Testing environment (indicator: {indicator})")
                return True
        
        print("[Input Handler] Detected local development environment")
        return False
    
    def prepare_headers(self):
        """
        Prepare headers for the HTTP client.
        Environment-aware authentication:
        - Local development (osdu_perf run local): Uses Azure CLI credentials
        - Azure Load Testing (osdu_perf run azure_load_test): Uses Managed Identity
        
        Returns:
            dict: Headers to be used in HTTP requests.
        """
        if self.is_azure_load_test_env:
            # Production: Use Managed Identity in Azure Load Testing
            print("[Input Handler] Using Managed Identity authentication (Production)")
            token_manager = AzureTokenManager(client_id=self.app_id, use_managed_identity=True)
        else:
            # Development: Use Azure CLI credentials locally
            print("[Input Handler] Using Azure CLI authentication (Development)")
            token_manager = AzureTokenManager(client_id=self.app_id, use_managed_identity=False)
            
        token = token_manager.get_access_token("https://management.azure.com/.default") 

        #token = self.client.get_access_token(scope=f"api://{self.app_id}/.default")
        headers = {
            "Content-Type": "application/json",
            "x-data-partition-id": self.partition,
            "x-correlation-id": self.app_id,
            "Authorization": f"Bearer {token}"
        }
        return headers
