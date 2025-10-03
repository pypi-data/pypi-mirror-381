"""
Core utility functions for DSA Toolkit
"""

from typing import List, Any


def validate_sorting(data: List[Any], ascending: bool = True) -> bool:
    """Validate if data is properly sorted."""
    if len(data) <= 1:
        return True

    for i in range(1, len(data)):
        if ascending and data[i] < data[i-1]:
            return False
        elif not ascending and data[i] > data[i-1]:
            return False
    return True


def print_array(arr: List[Any], title: str = "Array") -> None:
    """Print array with a title."""
    print(f"{title}: {arr}")


def generate_test_data(size: int = 10, max_val: int = 100) -> List[int]:
    """Generate random test data for algorithms."""
    import random
    return [random.randint(1, max_val) for _ in range(size)]


if __name__ == "__main__":
    # Simple demo
    test_arr = generate_test_data(5)
    print_array(test_arr, "Test Data")
    print(f"Is sorted: {validate_sorting(test_arr)}")