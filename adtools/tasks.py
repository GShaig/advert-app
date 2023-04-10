import whois

from celery import shared_task

@shared_task
def dom_aval(domain):
    try:
        w = whois.whois(domain)
        a = w.text
        if "Domain not found" in a or "DOMAIN NOT FOUND" in a or "Not Found" in a or "No match" in a or "No Data Found" in a or "Status: AVAILABLE" in a:
            dot = "1"
            return dot
        else:
            dot = "0"
            return dot
    except:
        dot = "1"
        return dot