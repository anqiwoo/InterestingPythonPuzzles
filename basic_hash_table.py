'''
This is a basic hash table for numerical values.
'''
import random


def basic_hash_table(value_l, n_buckets=5):
    def hash_function(value):
        return int(value) % n_buckets
    hash_table = {i: [] for i in range(n_buckets)}
    for value in value_l:
        hash_value = hash_function(value)
        hash_table[hash_value].append(value)
    return hash_table


random.seed(1)
test_l = [random.randint(0, 100) for _ in range(10)]
print(basic_hash_table(test_l))
