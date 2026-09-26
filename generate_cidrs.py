import dns.resolver
import os

# Target Kumon North America infrastructure domains
DOMAINS = [
    "kumon.com",
    "www.kumon.com",
    "mykumon.com",
    "://mykumon.com",
    "kumonfranchise.com",
    "kumongroup.com",
    "kumonapp.digital.kumon.com",
    "student2-lon.digital.kumon.com",
    "dwc.digital.kumon.com"
]

def resolve_to_cidr(domain):
    cidrs_v4 = set()
    cidrs_v6 = set()
    
    # Resolve IPv4 (A Records)
    try:
        answers_v4 = dns.resolver.resolve(domain, 'A')
        for rdata in answers_v4:
            cidrs_v4.add(f"{rdata.address}/32")
    except Exception:
        pass  # Skip if no record or resolution failure
        
    # Resolve IPv6 (AAAA Records)
    try:
        answers_v6 = dns.resolver.resolve(domain, 'AAAA')
        for rdata in answers_v6:
            cidrs_v6.add(f"{rdata.address}/128")
    except Exception:
        pass
        
    return cidrs_v4, cidrs_v6

def main():
    all_v4 = set()
    all_v6 = set()
    
    for domain in DOMAINS:
        v4, v6 = resolve_to_cidr(domain)
        all_v4.update(v4)
        all_v6.update(v6)
        
    # Ensure delivery directory exists
    os.makedirs("ip-lists", exist_ok=True)
    
    # Save combined target files
    with open("ip-lists/kumon_ipv4_cidrs.txt", "w") as f:
        f.write("\n".join(sorted(list(all_v4))) + "\n")
        
    with open("ip-lists/kumon_ipv6_cidrs.txt", "w") as f:
        f.write("\n".join(sorted(list(all_v6))) + "\n")
        
    # Save combined file for uniform firewalls
    with open("ip-lists/kumon_all_cidrs.txt", "w") as f:
        combined = sorted(list(all_v4)) + sorted(list(all_v6))
        f.write("\n".join(combined) + "\n")

if __name__ == "__main__":
    main()
