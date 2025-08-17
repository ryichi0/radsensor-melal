from rest_framework import serializers
from .models import ContactMessage
import re

SQL_KEYWORDS = [
    "SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "CREATE", "TRUNCATE"
]

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'company', 'message']

    def validate(self, data):
        for field, value in data.items():
            # Skip the required check for the "message" field
            if field != "message":
                if not value or (isinstance(value, str) and not value.strip()):
                    raise serializers.ValidationError({
                        field: f"{field.replace('_', ' ').capitalize()} is required."
                    })

            # Check for SQL keywords (still applies to message)
            if isinstance(value, str):
                if any(re.search(rf"\b{kw}\b", value, re.IGNORECASE) for kw in SQL_KEYWORDS):
                    raise serializers.ValidationError({
                        field: "Invalid content detected."
                    })

        return data
