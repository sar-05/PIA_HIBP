#!/usr/bin/env python

def validate_email(email, email_pattern):
    mo = email_pattern.serch(email)
    if mo == None:
        raise ValueError(f"Invalid email format{email}")
    return email    
