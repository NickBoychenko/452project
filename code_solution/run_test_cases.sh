for test_file in test_cases/*; do
    if [ -f "$test_file" ]; then
        echo "Running test on $test_file"
        python approximate.py < "$test_file"
        echo
    fi
done
