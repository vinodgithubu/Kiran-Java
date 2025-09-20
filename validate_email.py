import re

def is_valid_email(email: str) -> bool:
    try:
        # Simple regex for email validation
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
    except Exception as e:
        print(f"Error validating email '{email}': {e}")
        return False

# Example usage
if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "invalid-email",
        "user.name@domain.co",
        "user@.com",
        "user@domain"
    ]
    for email in test_emails:
        try:
            result = is_valid_email(email)
            print(f"{email}: {'Valid' if result else 'Invalid'}")
        except Exception as e:
            print(f"Exception occurred for '{email}': {e}")