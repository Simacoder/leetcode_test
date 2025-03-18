# counting routes in twon 
def countTown(n, routes):
    my_var = 1
    for i in routes:
        my_var = (i * my_var) % 1234567
    return my_var % 1234567

# test code

n = 4
routes = [3, 4, 5]
results = countTown(n, routes)
print(results)