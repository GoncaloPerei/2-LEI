def solution(n):

    bR = bin(n)[2:]

    max_gap = 0
    current_gap = 0
    em_gap = False

    for bit in bR:
        if bit == '1':
            if em_gap:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            em_gap = True
        elif em_gap:
            current_gap += 1

    return max_gap

print("N = 1041 (10000010001_2):", solution(1041)) 
print("N = 529 (1000010001_2):", solution(529))
print("N = 20 (10100_2):", solution(20)) 
print("N = 15 (1111_2):", solution(15))
print("N = 32 (100000_2):", solution(32))