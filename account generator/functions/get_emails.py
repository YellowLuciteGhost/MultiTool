def get_emails():
    with open('email.txt', 'r') as f:
        emails = [line.strip() for line in f]
    return emails