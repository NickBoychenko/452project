#!/bin/bash

solutions=("approximate.py" "exact.py")

# test_cases/center_cases/*
# test_cases/string_cases/*
# test_cases/connected_cases/*
# test_cases/*
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
