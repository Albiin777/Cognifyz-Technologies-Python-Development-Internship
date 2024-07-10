'''LEVEL 1 TASK 3
EMAIL VALIDATOR'''

import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return 'Valid Email'
    else:
        return 'Invalid Email'
emails = ["user@example.com",
    "user.name+tag+sorting@example.com",
    "user.name@example.co.uk",
    "user@subdomain.example.com",
    "user@123.123.123.123",
    "user@[123.123.123.123]",
    "user@example",
    "user@.example.com",
    "user@.com",
    "user@com",
    "user@exam_ple.com",
    "user@exam+ple.com",]
for email in emails:
    print(f"{email}: {is_valid_email(email)}")
