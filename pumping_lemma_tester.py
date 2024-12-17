import re

def is_pumpable(s, p):
    """
    Check if a string satisfies the pumping lemma for regular languages.
    
    Args:
        s (str): The input string.
        p (int): Pumping length.
    
    Returns:
        (bool, tuple): Whether the string can be pumped and the (x, y, z) parts.
    """
    n = len(s)
    if n < p:
        print("The string is shorter than the pumping length. It cannot be tested.")
        return False, ()
    
    # Try all possible splits of the string into x, y, z
    for i in range(p):  # Start y at different positions
        for j in range(1, n - i + 1):  # Ensure |y| > 0
            x = s[:i]
            y = s[i:i+j]
            z = s[i+j:]
            
            # Check the pumping property: xy^i z must still belong to the language
            for k in range(5):  # Test for k = 0, 1, 2, 3, 4 (pumping up and down)
                pumped = x + (y * k) + z
                if not re.fullmatch(regex, pumped):
                    print(f"Failed for k={k}: {pumped} does not match the language.")
                    return False, (x, y, z)
            print(f"String satisfies pumping for split: x='{x}', y='{y}', z='{z}'")
            return True, (x, y, z)
    
    print("No valid split found that satisfies the pumping lemma.")
    return False, ()

if __name__ == "__main__":
    # Input
    print("Pumping Lemma Checker for Regular Languages")
    regex = input("Enter a regular expression to describe the language: ")
    string = input("Enter a string to test: ")
    p = int(input("Enter the pumping length (p): "))

    # Validate the string against the regular language
    if not re.fullmatch(regex, string):
        print("The input string does not belong to the given regular language.")
    else:
        # Check the pumping lemma
        result, parts = is_pumpable(string, p)
        if result:
            print(f"The string '{string}' can be pumped. Split into: x='{parts[0]}', y='{parts[1]}', z='{parts[2]}'")
        else:
            print(f"The string '{string}' cannot be pumped. It violates the pumping lemma.")
