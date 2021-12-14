
stored_emails = []

def clean(address):
    # removing + up to @ in email address
    plus_index = address.find('+')
    if plus_index != -1:
        at_index = address.find('@')
        address = address[:plus_index] + address[at_index:]

    # removing . before the @
    at_index = address.find('@')
    before_at = ""
    i = 0
    while i < at_index:
        if address[i] != '.':
            before_at = before_at + address[i]
        i += 1

    cleaned = before_at + address[at_index:]

    # make lowercase
    cleaned = cleaned.lower()
    return cleaned

def stored_email(cleaned):
    if cleaned not in stored_emails:
        stored_emails.append(cleaned)
        print(f"{cleaned} has been stored")
    else:
        print(f"{cleaned} is already stored")

def main():
    cleaned = clean('rainey.schafer+book@gmail.com')
    stored_email(cleaned)
    cleaned = clean('rainey+book@gmail.com')
    stored_email(cleaned)
    cleaned = clean('rainey+books@gmail.com')
    stored_email(cleaned)

main()