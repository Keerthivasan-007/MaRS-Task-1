def muchiko_filter(data, window_size):
    """
    Muchiko Filter: Uses AVERAGE of sliding window
    
    Example: data=[4,5,6,7,8], window_size=3
    - Window [4,5,6] → average = 5
    - Window [5,6,7] → average = 6
    - Window [6,7,8] → average = 7
    Output: [5, 6, 7]
    """
    result = []
    
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        average = sum(window) / len(window)
        result.append(int(average))
    
    return result
 
 
def sanchiko_filter(data, window_size):
    """
    Sanchiko Filter: Uses MEDIAN of sliding window
    
    Example: data=[4,7,6,1,8], window_size=3
    - Window [4,7,6] → sorted [4,6,7] → median = 6
    - Window [7,6,1] → sorted [1,6,7] → median = 6
    - Window [6,1,8] → sorted [1,6,8] → median = 6
    Output: [6, 6, 6]
    """
    result = []
    
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        window_sorted = sorted(window)
        median = window_sorted[len(window_sorted) // 2]
        result.append(median)
    
    return result
 
 
def main():
    
    # Get input
    data_input = input("Enter sensor data (comma separated): ")
    data = [int(x.strip()) for x in data_input.split(",")]
    
    window_size = int(input("Enter window size: "))
    
    # Apply filters
    muchiko_result = muchiko_filter(data, window_size)
    sanchiko_result = sanchiko_filter(data, window_size)
    
    print(f"Original Data:  {data}")
    print(f"Muchiko Filter: {muchiko_result}")
    print(f"Sanchiko Filter: {sanchiko_result}")
    
    if muchiko_result == sanchiko_result:
        print("BOTH FILTERS GAVE SAME OUTPUT!")
        print("Data is CLEAN (no spikes or outliers)")
        print("No noise detected!")
        print("Either filter is safe to use")
        print(f"\nCLEAN DATA: {muchiko_result}")
    else:
        
        # Calculate differences
        muchiko_avg = sum(muchiko_result) / len(muchiko_result)
        sanchiko_avg = sum(sanchiko_result) / len(sanchiko_result)
        difference = abs(muchiko_avg - sanchiko_avg)
        
        if difference > 0.5:
            print("Data has OUTLIERS/SPIKES detected")
            print("Sanchiko (median) is MORE RELIABLE")
            print(f"Difference: {difference:.2f}")
            print(f"\nRECOMMENDED: {sanchiko_result} (Sanchiko)")
        else:
            print("Data has SLIGHT variations")
            print("Both filters are acceptable")
            print(f"Difference: {difference:.2f}")
            print(f"\nRECOMMENDED: {sanchiko_result} (Sanchiko - safer choice)")

 
if __name__ == "__main__":
    main()