def is_valid_config(config, limits, D):
    """
    Check if a configuration is valid:
    1. All segments within limits
    2. Sum equals target (implicit in caller)
    3. |Inner - Outer| <= D
    """
    inner, middle, outer = config
    l1, l2, l3 = limits
    
    # Check limits
    if inner < 0 or inner > l1:
        return False
    if middle < 0 or middle > l2:
        return False
    if outer < 0 or outer > l3:
        return False
    
    # Check stability constraint
    if abs(inner - outer) > D:
        return False
    
    return True

def calculate_cost(prev_config, curr_config, wear_factors):
    """Calculate movement cost between two configurations"""
    w1, w2, w3 = wear_factors
    prev_inner, prev_middle, prev_outer = prev_config
    curr_inner, curr_middle, curr_outer = curr_config
    
    cost = (abs(curr_inner - prev_inner) * w1 +
            abs(curr_middle - prev_middle) * w2 +
            abs(curr_outer - prev_outer) * w3)
    
    return cost

def find_valid_configs(target, limits, D):
    """Find all valid configurations for a given target"""
    l1, l2, l3 = limits
    valid_configs = []
    
    # Iterate through all possible combinations
    for inner in range(min(l1 + 1, target + 1)):
        for middle in range(min(l2 + 1, target + 1 - inner)):
            outer = target - inner - middle
            
            # Check if outer is within limits
            if outer < 0 or outer > l3:
                continue
            
            config = (inner, middle, outer)
            
            # Check if configuration is valid
            if is_valid_config(config, limits, D):
                valid_configs.append(config)
    
    return valid_configs

def min_cost_manipulator(limits, wear_factors, targets, D):
    """
    Find minimum total wear cost to complete all targets.
    
    Uses dynamic programming approach:
    - For each target, find all valid configurations
    - Calculate cost from previous target's configuration
    - Keep track of minimum cost path
    """
    
    if not targets:
        return 0
    
    # Start from initial state
    current_configs = {(0, 0, 0): 0}  # config -> min_cost_to_reach
    
    # Process each target
    for target in targets:
        next_configs = {}  # config -> min_cost_to_reach
        
        # Find all valid configurations for this target
        valid_configs = find_valid_configs(target, limits, D)
        
        if not valid_configs:
            return -1  # Target unreachable
        
        # For each valid configuration of current target
        for next_config in valid_configs:
            min_cost = float('inf')
            
            # Try reaching it from each previous configuration
            for prev_config, prev_cost in current_configs.items():
                move_cost = calculate_cost(prev_config, next_config, wear_factors)
                total_cost = prev_cost + move_cost
                min_cost = min(min_cost, total_cost)
            
            next_configs[next_config] = min_cost
        
        current_configs = next_configs
    
    # Return minimum cost among all final configurations
    return min(current_configs.values())
 
 
def main():
    
    # Get input
    print("Enter arm segment limits (L1, L2, L3):")
    limits = list(map(int, input("  ").split(',')))
    
    print("Enter wear factors (W1, W2, W3):")
    wear_factors = list(map(int, input("  ").split(',')))
    
    print("Enter target distances (comma separated):")
    targets = list(map(int, input("  ").split(',')))
    
    print("Enter stability constraint D (max |Inner - Outer|):")
    D = int(input("  "))

    result = min_cost_manipulator(limits, wear_factors, targets, D)
    
    if result == -1:
        print("TARGET UNREACHABLE!")
        print("No valid configuration exists for one or more targets.")
    else:
        print(f" MINIMUM TOTAL WEAR COST: {result}")
    
if __name__ == "__main__":
    main()