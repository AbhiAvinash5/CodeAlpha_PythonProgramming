"""
TASK 3: Task Automation with Python Scripts
Sub-task: Extract all email addresses from a .txt file and save them to another file.
CodeAlpha Python Programming Internship
Author: Avinash Kamella
"""

import re       # Regular Expressions — for pattern matching
import os       # For file path operations

# ─── Sample Input File Creator ───────────────────────────────────────────────
# This function creates a sample input.txt so you can test immediately
# In real use, you'd already have your own .txt file

def create_sample_input():
    """Creates a sample input.txt file with mixed content and emails."""
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
    - Duplicate test: avinash.kamella@gmail.com (should appear only once)

    Regards,
    CodeAlpha Team
    services@codealpha.tech
    """

    with open("input.txt", "w") as f:
        f.write(sample_text)

    print("  📄 Sample 'input.txt' created for testing!")

# ─── Core: Extract Emails using Regex ────────────────────────────────────────

def extract_emails(input_filename):
    """
    Reads a .txt file and extracts all valid email addresses using regex.

    What is Regex?
    → Regular Expression is a pattern that describes what text to search for.
    → Think of it like a 'search filter' that finds specific patterns in text.

    Returns a list of unique emails found.
    """

    # ── The Regex Pattern ──────────────────────────────────────────────────
    # r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    #
    # Breaking it down piece by piece:
    # [a-zA-Z0-9._%+-]+  → username part: letters, digits, dots, _, %, +, -
    #                       (the + means "one or more of these characters")
    # @                  → the literal @ symbol
    # [a-zA-Z0-9.-]+     → domain name: letters, digits, dots, hyphens
    # \.                 → a literal dot (backslash escapes the dot)
    # [a-zA-Z]{2,}       → extension: at least 2 letters (com, in, org, tech...)
    # ──────────────────────────────────────────────────────────────────────

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Check if the input file exists
    if not os.path.exists(input_filename):
        print(f"  ⚠  File '{input_filename}' not found!")
        return []

    # Read the entire file content
    with open(input_filename, "r") as f:
        content = f.read()

    # re.findall() → scans the entire text and returns ALL matches as a list
    all_emails = re.findall(email_pattern, content)

    # Remove duplicates using a set, then convert back to a sorted list
    # set() automatically removes duplicates because sets only store unique values
    unique_emails = sorted(set(all_emails))

    return unique_emails

# ─── Core: Save Emails to Output File ────────────────────────────────────────

def save_emails(emails, output_filename):
    """
    Saves the extracted email list to a .txt file.
    Each email is written on its own line.
    """

    with open(output_filename, "w") as f:
        f.write("Extracted Email Addresses\n")
        f.write("=" * 30 + "\n")
        for email in emails:
            f.write(email + "\n")
        f.write("=" * 30 + "\n")
        f.write(f"Total: {len(emails)} unique email(s) found\n")

    print(f"\n  💾 Emails saved to '{output_filename}'")
    print(f"  📂 Location: {os.path.abspath(output_filename)}")

# ─── Display Results in Console ──────────────────────────────────────────────

def display_results(emails):
    """Neatly prints all found emails in the console."""
    print("\n" + "=" * 40)
    print("      📧 EXTRACTED EMAIL ADDRESSES")
    print("=" * 40)

    if not emails:
        print("  ❌ No valid email addresses found.")
    else:
        for i, email in enumerate(emails, start=1):
            # enumerate() gives both index and value: (1, email), (2, email)...
            print(f"  {i:>2}. {email}")

    print("=" * 40)
    print(f"  ✅ Total unique emails found: {len(emails)}")

# ─── Main Program ─────────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 40)
    print("  📂 EMAIL EXTRACTOR — CodeAlpha Task 3")
    print("=" * 40)

    # Step 1: Ask user for input file
    print("\n  Do you have your own .txt file, or use a sample?")
    choice = input("  Enter '1' for sample, '2' to use your own file: ").strip()

    if choice == "1":
        create_sample_input()
        input_file = "input.txt"
    elif choice == "2":
        input_file = input("  Enter the path to your .txt file: ").strip()
    else:
        print("  Invalid choice. Using sample file.")
        create_sample_input()
        input_file = "input.txt"

    # Step 2: Extract emails
    print(f"\n  🔍 Scanning '{input_file}' for email addresses...")
    emails = extract_emails(input_file)

    # Step 3: Display results
    display_results(emails)

    # Step 4: Save to output file
    if emails:
        save = input("\n  Save extracted emails to a file? (y/n): ").strip().lower()
        if save == "y":
            save_emails(emails, "extracted_emails.txt")

    print("\n  Thank you for using Email Extractor! 👋\n")

# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
