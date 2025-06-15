from typing import Dict, Any
from passlib.hash import argon2

class Hasher:
    @staticmethod
    def get_password_hash(password: str) -> str:
        return argon2.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return argon2.verify(plain_password, hashed_password)
    
    @staticmethod
    def validate_passwords(password: str, confirm_password: str) -> Dict[str, Any]:
        """
        Validate passwords match and meet basic requirements
        
        Args:
            password (str): Password to validate
            confirm_password (str): Password confirmation
        
        Returns:
            Dict containing validation status and potential errors
        """
        validation_result = {
            "is_valid": True,
            "errors": []
        }
        
        # Check password match
        if password != confirm_password:
            validation_result["is_valid"] = False
            validation_result["errors"].append("Passwords do not match")
        
        # Optional: Add more password complexity checks
        if len(password) < 4:
            validation_result["is_valid"] = False
            validation_result["errors"].append("Password must be at least 4 characters long")
        
        return validation_result

