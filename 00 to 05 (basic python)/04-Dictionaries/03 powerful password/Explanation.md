🧠 Logic Recap: Password Verification using Dictionary + Hashing

Variable / Function        : What It Represents                              : User Input? : Explanation
--------------------------------------------------------------------------------------------------------------
stored_logins              : Dictionary storing email → hashed password      : ❌ No        : Predefined securely
login(...)                 : Checks if hashed input password matches stored  : ✅ Yes       : Returns True/False
hash_password(...)         : Converts input password into a SHA256 hash      : ✅ Yes       : Uses hashlib module
sha256(password.encode())  : Built-in hashing technique                      : ❌ No        : Converts plain to secure
==                         : Compares two hash strings                       : ❌ No        : Determines success
