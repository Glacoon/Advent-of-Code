# ADVENT OF CODE 2025 - DAY 2

# --- Part 1 Functions ---

def parse_input(instructions):
    """
    Create a tab with every ranges

    Args:
        instructions: list of the inputs from input.txt

    Returns:
        _type_: tab of int and an int
    """
    tab = instructions.split(',')
    tab_num = []
    max_id_value = 0
    
    for element in tab:
        element = element.strip()
        if not element: 
            continue
        
        try:
            start_str, end_str = element.split('-')
        except ValueError:
            continue
        
        start_int = int(start_str.strip())
        end_int = int(end_str.strip())
        
        tab_num.append((start_int, end_int))

        if end_int > max_id_value:
            max_id_value = end_int
            
    return tab_num, max_id_value

def generate_invalid_ids(max_id_value):
    """
        Generate a set of every invalid ids possible from 1 to the biggest Id from the list of ranges

    Args:
        max_id_value (_type_): biggest id reachable

    Returns:
        _type_: Set of invalid ids
    """
    invalid_ids_set = set()
    max_len_pattern = len(str(max_id_value)) // 2
    
    for pattern_length in range(1, max_len_pattern + 1):
        
        start_pattern_value = 10 ** (pattern_length - 1)
        end_pattern_value = 10 ** pattern_length 

        for base_Pattern_Value in range(start_pattern_value, end_pattern_value):
            
            id_String = str(base_Pattern_Value) * 2
            invalid_ID_Value = int(id_String)
            
            if invalid_ID_Value > max_id_value:
                break
                
            invalid_ids_set.add(invalid_ID_Value)
            
    return invalid_ids_set

def solve_puzzle(invalid_ids, ranges):
    """
    Compare the set of values one by one to the list of ranges

    Args:
        invalid_ids (_type_): set of invalid ids
        ranges (_type_): list of every ranges possible

    Returns:
        _type_: sum of every invalid ids fitting in ranges
    """
    total_sum = 0
    
    for Invalid_ID_Value in invalid_ids:
        for start_id, end_id in ranges:
            if start_id <= Invalid_ID_Value <= end_id:
                
                total_sum += Invalid_ID_Value
                
                break
                
    return total_sum

# --- Part 2 ---

def generate_invalid_ids_part_2(max_id_value):
    invalid_ids_set = set()
    max_total_length = len(str(max_id_value))
    
    for repetition_count in range(2, max_total_length + 1):
        
        max_length_pattern = max_total_length // repetition_count
        
        for pattern_length in range(1, max_length_pattern + 1):
            
            start_pattern_value = 10 ** (pattern_length - 1)
            end_pattern_value = 10 ** pattern_length
            
            for base_Pattern_Value in range(start_pattern_value, end_pattern_value):
                
                id_String = str(base_Pattern_Value) * repetition_count
                invalid_ID_Value = int(id_String)
                
                if invalid_ID_Value > max_id_value:
                    break
                    
                invalid_ids_set.add(invalid_ID_Value)
                
    return invalid_ids_set


# --- Main ---

if __name__ == "__main__":
    try:
        with open('2025/input/input-2.txt', 'r') as file:
            input_data = file.read().strip()
            
        print("ADVENT OF CODE 2025 - DAY 2")
        
        ranges, max_id_limit = parse_input(input_data)
        
        invalid_patterns = generate_invalid_ids(max_id_limit)
        
        final_sum = solve_puzzle(invalid_patterns, ranges)
        
        print(f"Result: {final_sum}")
        
    except FileNotFoundError:
        print("Error: Input file not found")