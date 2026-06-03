import re
import os


def create_sample_input():
    sample_text = """
Hello team,

Please reach out to the following people for the project:
- Project Lead: avinash.kamella@gmail.com
- HR Contact: hr.codealpha@company.org
- Tech Support: support@codealpha.tech
- Client Email: john.doe@clientcorp.in
- Invalid entry: notanemail@
- Also invalid: @missingusername.com
- Another valid one: intern2024@yahoo.co.in
- Manager: ramesh_kumar@infosys.com
- Random text with email: contact us at hello@world.net for more info.
- Duplicate test: avinash.kamella@gmail.com

Regards,
CodeAlpha Team
services@codealpha.tech
"""

    with open("input.txt", "w") as f:
        f.write(sample_text)

    print("Sample input.txt created.")


def extract_emails(filename):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return []

    with open(filename, "r") as f:
        content = f.read()

    emails = re.findall(pattern, content)
    return sorted(set(emails))


def save_emails(emails, filename):
    with open(filename, "w") as f:
        f.write("Extracted Email Addresses\n")
        f.write("-" * 30 + "\n")

        for email in emails:
            f.write(email + "\n")

        f.write("-" * 30 + "\n")
        f.write(f"Total: {len(emails)}\n")

    print(f"Emails saved to '{filename}'")


def display_results(emails):
    print("\nExtracted Email Addresses\n")

    if not emails:
        print("No valid emails found.")
        return

    for i, email in enumerate(emails, start=1):
        print(f"{i}. {email}")

    print(f"\nTotal unique emails: {len(emails)}")


def main():
    print("Email Extractor")

    choice = input(
        "Enter 1 to use sample file or 2 to provide your own file: "
    ).strip()

    if choice == "1":
        create_sample_input()
        input_file = "input.txt"
    elif choice == "2":
        input_file = input("Enter file path: ").strip()
    else:
        print("Invalid choice. Using sample file.")
        create_sample_input()
        input_file = "input.txt"

    emails = extract_emails(input_file)

    display_results(emails)

    if emails:
        save_choice = input(
            "\nSave extracted emails to a file? (y/n): "
        ).strip().lower()

        if save_choice == "y":
            save_emails(emails, "extracted_emails.txt")


if __name__ == "__main__":
    main()
