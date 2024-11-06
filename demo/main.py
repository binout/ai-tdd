from enum import Enum
from typing import List


class ErrorCode(Enum):
    A001 = "Missing required field"
    A002 = "Invalid delivery or attestation date"
    A003 = "Invalid beneficiary, member not found"
    A004 = "Invalid beneficiary, failed to fetch dependents data" 
    A005 = "Invalid beneficiary name, no match with the insured data and beneficiaries"
    A006 = "Invalid document type"
    A007 = "Invalid response, no data in segments"
    A008 = "Invalid response, multiple segment groups"
    A009 = "Invalid product, cnk code not found in BESCO database"
    A010 = "Invalid quantity"
    A011 = "Invalid care act date"
    A012 = "Invalid cost id"
    A013 = "Invalid cost wording"
    A014 = "Mutuality intervention conflict"
    A015 = "No public product price for act"
    A016 = "No mutuality intervention found"
    A017 = "Missing total paid"
    A018 = "Missing total due"
    A019 = "Negative amount"
    A020 = "Hospital RIZIV number not found"

"""
A autoparsed ticket can have multiple errors.
We add the tag 'external' to autoparsed tickets 
except if one of the following errors appear: 
- A009
- A012
- A013
"""
