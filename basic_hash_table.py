'''
This is a basic hash table for integer values.
'''
import random


def basic_hash_table(value_l, n_buckets=5):
    '''
    Input:
        - value_l: a list of integer numbers
        - n_buckets: desired amount of buckets. 

    Output:
        - hash_table: a hash table stored as a dictionary, where keys contain the hash keys, and the values will provide the hashed elements of the input list. 
    '''
    def hash_function(value):
        '''
        The hash function is just the remainder of the integer division between each element and the desired number of buckets.
        '''
        return int(value) % n_buckets
    hash_table = {i: [] for i in range(n_buckets)}
    for value in value_l:
        hash_value = hash_function(value)
        hash_table[hash_value].append(value)
    return hash_table


random.seed(1)
test_l = [random.randint(0, 100) for _ in range(10)]
print(basic_hash_table(test_l))
