# study the stacks 
import queue

my_book_stack = queue.LifoQueue(maxsize = 0)

my_book_stack.put("Malcom X")
my_book_stack.put("Einstein")
my_book_stack.put("Godel")

print(f"The size is : {my_book_stack.qsize()}")
print(my_book_stack.get())
print(my_book_stack.get())
print(my_book_stack.get())

print(f"Empty stack: {my_book_stack.empty()}")
