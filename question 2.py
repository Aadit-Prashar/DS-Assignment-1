# Function to implement Tower of Hanoi
def hanoi(n, source, spare, target):
    if n == 1:
        print(f"Move disk 1 from ",source,"to", target)
        return 1
    
    count1 = hanoi(n - 1, source, target, spare)
    # Move n-1 disks from the source to spare
    
    print(f"Move disk ",n," from ",source," to ",target)
    # Move the nth disk from source to target

    count2 = hanoi(n - 1, spare, source, target)
    # Move n-1 disks from spare to target
    
    return count1 + 1 + count2
# The Time Complexity is O(2^n) because the number of moves required follows the formula 2^n - 1 simplifies into O(2^n)
# The Space Complexity is O(n) because the maximum depth of the recursion stack is equal to the number of disks

# Main method
def main():
    n = 3
    print(f"Move sequence for n = {n}:")
    total_moves = hanoi(n, 'A', 'B', 'C')
    print(f"Total moves: {total_moves}")

if __name__ == "__main__":
    main()