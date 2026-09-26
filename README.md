Kumon IPs
====

This project automatically keeps track of the underlying infrastructure network paths used by Kumon systems. Because dynamic CDNs route their infrastructure, this repository updates daily using GitHub Actions to maintain exact firewall target ranges.

All IP-Lists are in the [CIDR-Notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) and can be used as whitelists in your webserver's firewall or as an exception for rate-limits.

The lists are updated daily via a scheduled GitHub Action.

----

# Plain Text Targets for Firewalls

Point your automated Firewall threat feeds or address-object lists directly to the raw file URLs below:

Combined CIDRs: `https://raw.githubusercontent.com/britemindz/KumonIPs/refs/heads/main/iplists/kumon_all_cidrs.txt`
IPv4 Blocks: `https://raw.githubusercontent.com/britemindz/KumonIPs/refs/heads/main/iplists/kumon_ipv4_cidrs.txt`
IPv6 Blocks: `https://raw.githubusercontent.com/britemindz/KumonIPs/refs/heads/main/iplists/kumon_ipv6_cidrs.txt`
