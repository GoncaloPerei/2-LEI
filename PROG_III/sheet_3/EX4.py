reservations = [
    ("A", 9, 11, "Ana"),
    ("A", 10, 12, "Bruno"),
    ("A", 12, 14, "Carla"),
    ("B", 9, 10, "Daniel"),
    ("B", 10, 12, "Eva"),
    ("B", 11, 13, "Filipe")
]

# =====================================================================
# EXERCISE 1: Group Reservations by Classroom
# =====================================================================
# Maps each classroom ID to a list of its reservation tuples: (start, end, person)
classrooms = {}

for classroom, inicio, fim, aluno in reservations:
    classrooms.setdefault(classroom, []).append((inicio, fim, aluno))

print(f"Classroom Reservations: {classrooms}")

# =====================================================================
# EXERCISE 2: Sort Reservations by Start Time (Chronological Order)
# =====================================================================
# Creates a dictionary where each classroom's bookings are sorted by ascending start time
sorted_reservations = {}
for classroom, reservations in classrooms.items():
    sorted_reservations = sorted(reservations, key=lambda x: x[0])
    sorted_reservations[classroom] = sorted_reservations

print(f"Sorted Reservations (Descending by Start Time): {sorted_reservations}")

# =====================================================================
# EXERCISE 3 & 4: Detect Overlapping Reservation Pairs
# =====================================================================
def find_overlapping_reservations(r1, r2):
    """Determines whether two reservations overlap on a half-open interval [start, end).

    Strict inequalities (<) ensure that adjacent bookings (e.g., ending at 10
    and starting at 10) are not treated as conflicts.

    Args:
        r1 (tuple): First booking tuple (start, end, person).
        r2 (tuple): Second booking tuple (start, end, person).

    Returns:
        bool: True if there is a conflict, False otherwise.
    """
    start1, end1, _ = r1
    start2, end2, _ = r2
    return start1 < end2 and start2 < end1

conflicts = {}
for classroom, reservations in classrooms.items():
    classroom_conflicts = []
    for i in range(len(reservations)):
        for j in range(i + 1, len(reservations)):
            if find_overlapping_reservations(reservations[i], reservations[j]):
                classroom_conflicts.append((reservations[i], reservations[j]))
    conflicts[classroom] = classroom_conflicts

print(f"Overlapping Reservations: {conflicts}")

# =====================================================================
# EXERCISE 5: Compute Total Occupancy Time Without Double-Counting
# =====================================================================
def merge_reservations(reservations):
    """Merges overlapping or contiguous time intervals into unified blocks.

    Args:
        reservations (list[tuple]): List of reservation tuples for a single
        room.

    Returns:
        list[list[int]]: Disjoint, non-overlapping [start, end] time intervals.
    """
    if not reservations:
        return []
    
    sorted_res = sorted(reservations, key=lambda x: x[0])
    
    merged = [[sorted_res[0][0], sorted_res[0][1]]]
    
    for start, end, _ in sorted_res[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
            
    return merged

occupied_times = {}
for classroom, reservations in classrooms.items():
    merged_intervals = merge_reservations(reservations)
    total_time = sum(end - start for start, end in merged_intervals)
    occupied_times[classroom] = total_time

print(f"Total Occupied Time per Classroom: {occupied_times}")
