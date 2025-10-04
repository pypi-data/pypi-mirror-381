# ResidentPortal Python Client

Python client for interacting with ResidentPortal accounts.

This package is still in development and any part can be changed at anytime with no warning.
PR's and feedback are welcome.

**WARNING**

The Resident Portal API is not public. Use at your own risk.

I can only test based on what I can see from using my account with the Resident Portal API,
so any help would be great with testing and finding bugs. If one is encountered, please create
a GitHub issue. The controllers and actions I could find are located in the repository under
controllers.json, however, the HTTP method is not documented for each.

## Install

```bash
pip install resident_portal
```

## Usage

```python
from resident_portal import User

rp = User("email@domain.com", "Password123!!", "subdomain")
await rp.login() # Log the client in
print(rp.leases) # List of leases user is associated with

lease = rp.leases[0] # First lease in the list
print(await lease.get_lease_balance()) # Get the leases balance

```