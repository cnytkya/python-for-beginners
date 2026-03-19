# mantıksal op'ler birden fazla karşılaştırmayı birleştirmek için kullanılır.

"""
    Operator	   Description	                                        Example
    and 	  Returns True if both statements are true	                x < 5 and  x < 10	
    or	      Returns True if one of the statements is true	            x < 5 or x < 4	
    not	      Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

"""

# and: her iki koşul doğru ise sonuç True olur.
# or: en az bir koşul sağlanırsa o zaman durum True olur.
# not: sonucu tersine çevirir. true ise false,false ise true olur.

a = 5
b = 3
c = 6
print(a > b and a > c) # sonuç: False
print(a > b or a > c) # sonuç: True
print(not(a > c)) # sonuç: True 