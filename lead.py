import re

def extract_emails(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.findall(pattern, text)

def main():
    print("=== Lead Generation Tool ===\n")
    
    text = input("Paste text with emails:\n")
    
    emails = extract_emails(text)
    
    print("\n--- Extracted Emails ---\n")
    
    if emails:
        for email in emails:
            print(email)
    else:
        print("No emails found.")

if __name__ == "__main__":
    main()
