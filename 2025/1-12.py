# ADVENT OF CODE 2025 - DAY 1 - FINAL CORRECTED VERSION

# --- Part 1 Functions ---

def calculate_position(current_position, direction, steps):
    """
    Calculates the new position on the 0-99 dial, handling wrap-around.
    """
    if direction == 'R':
        new_pos = (current_position + steps) % 100
    elif direction == 'L':
        new_pos = (current_position - steps) % 100
    else:
        raise ValueError("Invalid rotation direction")
    return new_pos  
    
    
def solve_part1(instructions):
    """
    Solves Part 1: Counts how many times the dial lands on 0 at the END of a rotation.
    """
    position = 50
    point_zero = 0
    
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        
        position = calculate_position(position, direction, steps)
        
        if position == 0:
            point_zero += 1
            
    return point_zero


# --- Part 2 Functions ---

def calculate_position_part2(current_position, direction, steps):
    """
    Calculates the new position and the number of times 0 is landed on during the rotation.
    """
    if direction == 'R':
        new_pos = (current_position + steps) % 100
        crosses = (current_position + steps) // 100
        return new_pos, crosses
        
    elif direction == 'L':
        new_pos = (current_position - steps) % 100
        
        if current_position == 0:
            if steps % 100 == 0 and steps > 0:
                crosses = steps // 100
            else:
                crosses = steps // 100
        else:
            if steps >= current_position:
                crosses = 1 + (steps - current_position) // 100
            else:
                crosses = 0
        
        return new_pos, crosses
    else:
        raise ValueError("Invalid rotation direction")


def solve_part2(instructions):
    """
    Solves Part 2: Counts how many times the dial lands on 0 during ANY click.
    """
    position = 50
    point_zero = 0
    
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:].strip())
        
        position, crosses = calculate_position_part2(position, direction, steps)
        point_zero += crosses
    
    return point_zero



# --- Main ---

if __name__ == "__main__":
    try:
        with open('2025/input/input.txt', 'r') as file:
            rotation_lines = [line.strip() for line in file if line.strip()]
        
        print("ADVENT OF CODE 2025 - DAY 1")
        print("=" * 60)
        
        part1_answer = solve_part1(rotation_lines)
        print(f"Part 1: {part1_answer}")
        
        part2_answer = solve_part2(rotation_lines)
        
        print(f"Part 2:  {part2_answer}")
        
        print("=" * 60)
        
    except FileNotFoundError:
        print("Error: Input file not found.")