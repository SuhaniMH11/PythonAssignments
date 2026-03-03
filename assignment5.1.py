nums = input("Enter integers separated by space: ")
t = tuple(map(int, nums.split()))

print("Total items:", len(t))
print("Last item:", t[-1])
print("Reverse order:", t[::-1])

if 5 in t:
    print("Yes")
else:
    print("No")

new_tuple = t[1:-1]
sorted_tuple = tuple(sorted(new_tuple))
print("After removing first & last and sorting:", sorted_tuple)