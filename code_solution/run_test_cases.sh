#!/bin/bash

solutions=("approximate.py" "exact.py")

for i in "${solutions[@]}"; do
    echo "Testing on $i"
    for test_file in test_cases/*; do
        if [ -f "$test_file" ]; then
            echo "Running test on $test_file"
            python "$i" < "$test_file"
            echo
        fi
    done
done
