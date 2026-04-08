#!/bin/bash

# Generate a random battery percentage between 0 and 100
BATTERY=$(( RANDOM % 101 ))
echo "Checking battery status... Current level is ${BATTERY}%."

# Check if battery is below 20%
if [ "$BATTERY" -lt 20 ]; then
    echo "Battery low! Return to base!"
    exit 1
fi

echo "Checking communication array..."
# Ping google.com with 1 packet (-c 1) and a 2-second timeout (-W 2)
# Output is redirected to /dev/null to keep the console output clean
# We use 2>&1 to push the stderr to the same channel 1 that points to /dev/null
if ! ping -c 1 -W 2 google.com > /dev/null 2>&1; then
    echo "Communication failure!"
    exit 1
fi

# If script reaches this point, all checks have passed
echo "All systems operational!"
exit 0
