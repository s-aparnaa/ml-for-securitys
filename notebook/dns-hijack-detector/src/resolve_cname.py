# resolve_cname.py

import dns.resolver

def resolve_cname(domain):
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        return str(answers[0].target).strip('.')
    except Exception:
        return None  # Catch resolution failures, NXDOMAIN, etc.
