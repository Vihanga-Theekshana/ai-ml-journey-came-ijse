import sys


def to_bool(value):
    return value.strip().lower() == "true"


def is_missing_score(score):
    return score is None or score == "" or score.strip().lower() == "none"


def parse_line(line):
    parts = [p.strip() for p in line.split("|")]

    # safety check (IMPORTANT FIX)
    if len(parts) < 6:
        return None

    try:
        age = int(parts[0])
        label = parts[1].strip().lower()

        score_raw = parts[2].strip()
        score = None if is_missing_score(score_raw) else float(score_raw)

        country = parts[3].strip()
        is_premium = to_bool(parts[4])
        has_missing = to_bool(parts[5])

        return age, label, score, country, is_premium, has_missing

    except (ValueError, IndexError):
        return None


def is_eligible(sample, allow_spam, max_age):
    age, label, score, country, is_premium, has_missing = sample

    if not (18 <= age <= max_age):
        return False

    if not allow_spam and label == "spam":
        return False

    if score is None or score < 0.60:
        return False

    if not (country == "LK" or is_premium):
        return False

    if has_missing:
        return False

    return True


def process(lines):
    allow_spam = False
    max_age = 65
    count = 0

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("ALLOW spam"):
            allow_spam = True
            continue

        if line.startswith("AGE max="):
            max_age = int(line.split("=")[1].strip())
            continue

        sample = parse_line(line)

        if sample and is_eligible(sample, allow_spam, max_age):
            count += 1

    return count


def main():
    lines = sys.stdin.read().splitlines()
    print(process(lines))


if __name__ == "__main__":
    main()