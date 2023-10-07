import re
# Define regex patterns for common spammy words and phrases
spam_patterns = [
    r"buy now",
    r"free[\s\d]*",
    r"discount[\s\d]*",
    r"limited time offer",
    r"click here",
    r"winner",
    r"lottery",
    r"money back",
]
# Function to classify an email as spam or not
def classify_email(email_content):
    # Convert email content to lowercase for case-insensitive matching
    email_content = email_content.lower()
    # Check if any spam patterns match in the email content
    for pattern in spam_patterns:
        if re.search(pattern, email_content):
            return "Spam"

    return "Not Spam"
# Example usage
if __name__ == "__main__":
    # Sample email content
    email_content = input("enter email content to check for spam:\n  ")
    print()
    print()
    classification = classify_email(email_content)
    print("Email Classification:", classification)
