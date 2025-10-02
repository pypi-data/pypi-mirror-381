"""
HTTP client for Catastro JSON APIs.
Based on client.go from alejndr0/go-catastro
"""
import requests
from typing import Dict, Optional, Any


class CatastroHttpClient:
    """HTTP client for JSON-based Catastro APIs."""
    
    BASE_URL = "http://ovc.catastro.meh.es/"
    
    def __init__(self):
        self.session = requests.Session()
        # Set User-Agent header because the server returns a 403 without it
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        })
    
    def get_json(self, url: str, query_params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Make GET request to Catastro JSON API endpoint.
        
        Args:
            url: Endpoint URL path (relative to BASE_URL)
            query_params: Query parameters dict
            
        Returns:
            JSON response as dict
            
        Raises:
            requests.RequestException: For HTTP errors
            CatastroApiError: For API errors
        """
        if query_params is None:
            query_params = {}
            
        # Filter out empty values
        filtered_params = {k: v for k, v in query_params.items() if v != ""}
        
        full_url = self.BASE_URL + url
        
        response = self.session.get(full_url, params=filtered_params)
        response.raise_for_status()
        
        data = response.json()
        
        # Check for API errors
        self._check_api_error(data)
        
        return data
    
    def _check_api_error(self, data: Dict[str, Any]) -> None:
        """
        Check if API response contains errors and raise exception if so.
        
        Args:
            data: JSON response data
            
        Raises:
            CatastroApiError: If API returned an error
        """
        # The error checking logic varies by endpoint, but typically looks for cuerr != 0
        # This is a simplified version - specific endpoints may need custom error checking
        
        # Try to find error control structure in various response formats
        control = None
        error_list = None
        
        # Different endpoints have different response structures
        for result_key in data.keys():
            if isinstance(data[result_key], dict):
                result_data = data[result_key]
                if "control" in result_data:
                    control = result_data["control"]
                if "lerr" in result_data:
                    # lerr can contain an "err" array
                    lerr = result_data["lerr"]
                    if isinstance(lerr, dict) and "err" in lerr:
                        error_list = lerr["err"]
                    else:
                        error_list = lerr
                # Some responses use "ErrorList" instead of "lerr"
                if "ErrorList" in result_data:
                    error_list = result_data["ErrorList"]
        
        if control and "cuerr" in control and control["cuerr"] != 0:
            error_msg = "API returned error"
            if error_list and len(error_list) > 0:
                # Check if error_list[0] is a dictionary with error details
                if isinstance(error_list[0], dict):
                    if "des" in error_list[0]:
                        error_msg = error_list[0]["des"]
                    elif "desc" in error_list[0]:
                        error_msg = error_list[0]["desc"]
                else:
                    # error_list[0] might be a simple value (like an error code)
                    error_msg = f"API error: {error_list[0]}"
            elif "cuerr" in control:
                error_msg = f"API error code: {control['cuerr']}"
            raise CatastroApiError(error_msg)


class CatastroApiError(Exception):
    """Exception raised for Catastro API errors."""
    pass