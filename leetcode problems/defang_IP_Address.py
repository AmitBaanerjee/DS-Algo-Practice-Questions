# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".
#
#
#
# Example 1:
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:
#
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
#
#
# Constraints:
#
# The given address is a valid IPv4 address.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_symbol="[.]"
        address_list=address.strip().split(".")
        address_length=len(address_list)-1
        counter,i=0,0
        result=""
        while counter!=address_length:
            result=result+address_list[i]+new_symbol
            i+=1
            counter+=1
        return result+address_list[-1]
