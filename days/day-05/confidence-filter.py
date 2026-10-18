def main():
    """Process confidence values with filtering rules."""
    import sys

    raw_lines = []
    drop_threshold = None

    # Read all input lines
    for line in sys.stdin:
        line = line.rstrip("\n")
        raw_lines.append(line)

    parsed_values = []

    # First pass: handle parsing and config
    for line in raw_lines:
        stripped = line.strip()

        # Ignore blank lines
        if not stripped:
            continue

        # Ignore comments
        if stripped.startswith("#"):
            continue

        # Handle configuration line
        if stripped.startswith("DROP below="):
            try:
                drop_threshold = float(stripped.split("=")[1])
            except ValueError:
                continue
            continue

        # Try converting to float
        try:
            value = float(stripped)
            parsed_values.append((stripped, value))
        except ValueError:
            print(f"Skipping invalid value: {line}")

    # Apply filtering using list comprehension
    if drop_threshold is not None:
        filtered_values = [
            value for _, value in parsed_values
            if value >= drop_threshold
        ]
    else:
        filtered_values = [value for _, value in parsed_values]

    # Final output
    if not filtered_values:
        print("No valid values")
        return

    print(filtered_values)
    average = sum(filtered_values) / len(filtered_values)
    print(f"{average:.3f}")


if __name__ == "__main__":
    main()