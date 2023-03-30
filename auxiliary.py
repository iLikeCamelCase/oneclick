# need this:
# python -m pip install git+https://gitea.ksol.io/karolyi/py3-validate-email@v1.0.10

#email format

def generateEmails(first, last, domain, initials = ''):
    """Given a name and an email domain (eg. gmail.com), will
    create possible email addresses for that person based on a 
    predefined list of email format types.

    Args:
        first (str): first name
        last (str): last name
        domain (str): company domain
        initial (str, optional): initials Defaults to ''.
    """

    # FIX - this assumes first name of at least length 3
    # and last name of at least length 4
    
    template_values = {
        'first' : first,
        'last' : last,   
        'initials' : initials,
        'domain' : domain
    }
    
    # CHAT-GPT made these, I don't know if there are duplicates
    email_formats = [
        '{first}@{domain}',
        '{last}@{domain}',
        '{first[0]}{last}@{domain}',
        '{first}.{last}@{domain}',
        '{first}_{last}@{domain}',
        '{first}-{last}@{domain}',
        '{first}{last}@{domain}',
        '{last}{first}@{domain}',
        '{last}.{first}@{domain}',
        '{last}_{first}@{domain}',
        '{last}-{first}@{domain}',
        '{first[0]}_{last}@{domain}',
        '{first[0]}-{last}@{domain}',
        '{first[0]}{last}@{domain}',
        '{last[0]}_{first}@{domain}',
        '{last[0]}-{first}@{domain}',
        '{last[0]}{first}@{domain}',
        '{first}.{last[0]}@{domain}',
        '{first}_{last[0]}@{domain}',
        '{first}-{last[0]}@{domain}',
        '{first}{last[0]}@{domain}',
        '{first[0]}{last[0]}@{domain}',
        '{first[0]}.{last}@{domain}',
        '{first[0]}_{last}@{domain}',
        '{first[0]}-{last}@{domain}',
        '{first[0]}{last}@{domain}',
        '{last[0]}{first[0]}@{domain}',
        '{last[0]}.{first}@{domain}',
        '{last[0]}_{first}@{domain}',
        '{last[0]}-{first}@{domain}',
        '{first[0]}{last[0]}@{domain}',
        '{last}.{first[0]}@{domain}',
        '{last}_{first[0]}@{domain}',
        '{last}-{first[0]}@{domain}',
        '{last[0]}{first[0]}@{domain}',
        '{first}.{last[0]}@{domain}',
        '{first}_{last[0]}@{domain}',
        '{first}-{last[0]}@{domain}',
        '{first[0]}_{last[0]}@{domain}',
        '{first[0]}-{last[0]}@{domain}',
        '{first[0]}.{last[0]}@{domain}',
        '{last[0]}.{first[0]}@{domain}',
        '{last[0]}_{first[0]}@{domain}',
        '{last[0]}-{first[0]}@{domain}',
        '{first}_{last}@{domain}',
        '{first}-{last}@{domain}',
        '{first}{last}@{domain}',
        '{last}_{first}@{domain}',
        '{last}-{first}@{domain}',
        '{last}{first}@{domain}',
        '{first[0]}{last[0]}{initials}@{domain}',
        '{last}{initials}.{first}@{domain}',
        '{initials}.{last}@{domain}',
        '{first}.{initials}@{domain}',
        '{first[0]}{initials}{last[0]}@{domain}',
        '{first}{last}{initials}@{domain}',
        '{initials}{last[0]}@{domain}',
        '{first[0]}{last[0]}{initials}@{domain}',
        '{initials}.{first}@{domain}',
        '{first}_{initials}@{domain}',
        '{initials}_{last}@{domain}',
        '{first[0]}{initials}.{last}@{domain}',
        '{first}{last[0]}{initials}@{domain}',
        '{last[0]}{initials}{last}@{domain}',
        '{initials}{first[0]}{last[0]}@{domain}',
        '{first[0]}{last[0]}_{initials}@{domain}',
        '{initials}{first}{last}@{domain}'
        ]

    emailList = []
    
    for form in email_formats:
        emailList.append(form.format(**template_values))
        
    return emailList
