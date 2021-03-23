"""
Modify the function below to use a different procedure for generating a hash. Research some other basic methods ("mid-squares", "division hashing", "multiplicative hashing", etc.) for ideas.
"""
def my_hashing_func(str, table_size):
    bytes_representation = str.encode()

    product = 0
    for byte in bytes_representation:
        product *= byte

    return product % table_size