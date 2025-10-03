import os
import requests
import sys

class LicenseValidator:
    def __init__(self):
        self.api_key = os.getenv("MCP_API_KEY")
        if os.getenv("DEBUG") == "true":
            print(f"API Key: {self.api_key}")
        self.validation_url = "http://host.docker.internal:3001/api/validate-license"
        
    def validate_license(self) -> bool:
        """Valide la licence auprès du backend Firstland"""
        if not self.api_key:
            print("API Key: Not Provided")
            sys.exit(1)
            return False
            
        try:
            response = requests.post(
                self.validation_url,
                json={
                    "api_key": self.api_key,
                    "tool_id": "financial-analyzer"
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get("valid", False)
            else:
                print(f"ERREUR: Validation échouée (HTTP {response.status_code})")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"ERREUR: Impossible de contacter le serveur de validation: {e}")
            return False
        except Exception as e:
            print(f"ERREUR: Validation inattendue: {e}")
            return False
