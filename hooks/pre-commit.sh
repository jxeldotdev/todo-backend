#!/bin/bash

echo "Running pre-commit hooks!"

if exec $GIT_DIR/hooks/lint.sh; then
    linters_passed=true
else
    linters_passed=false
fi

if exec $GIT_DIR/hooks/unit.sh; then
    tests_passed=true
else
    test_passed=false
fi

if $linters_passed;
    echo "Linters ran successfully ✅"
else
    echo "Linters failed ❌"
fi

if $tests_passed; then
    echo "Unit tests ran successfully ✅"
else
    echo "Unit tests failed ❌"
if 