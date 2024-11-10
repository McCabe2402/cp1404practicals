def extract_name_from_email(email):
    name_part = email.split('@')[0]
    name_part = name_part.replace('.', ' ')
    name = name_part.title()
    return name


def main():
    email_dict = {}

    email = input("Enter your email (or press Enter to finish): ").strip()

    while email:
        name = extract_name_from_email(email)
        email_dict[email] = name
        email = input("Enter your email (or press Enter to finish): ").strip()

    print("\nStored Emails and Names:")
    for email, name in email_dict.items():
        print(f"Email: {email} - Name: {name}")


if __name__ == "__main__":
    main()
