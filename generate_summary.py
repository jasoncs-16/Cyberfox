def generate_summary(max_min: list) -> str:
    """Formats the result of get_max_min() as a simple string."""
    (max_name, max_val), (min_name, min_val) = max_min
    return f"Highest: {max_name} ({max_val}) | Lowest: {min_name} ({min_val})"