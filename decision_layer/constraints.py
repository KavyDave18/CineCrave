import re


def normalize_title(title):
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s]", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def get_franchise_key(title):
    title = normalize_title(title)

    franchise_patterns = [
        r"^batman",
        r"^superman",
        r"^star wars",
        r"^star trek",
        r"^spider man",
        r"^pirates of the caribbean",
        r"^harry potter",
        r"^x men",
        r"^the fast and the furious",
        r"^twilight",
    ]

    for pattern in franchise_patterns:
        if re.match(pattern, title):
            return pattern

    return title


def apply_constraints(ranked_items, cfg):
    max_per_franchise = cfg.get(
        "decision_layer", {}
    ).get("max_per_franchise", 2)

    counts = {}
    filtered = []

    for title, score in ranked_items:
        key = get_franchise_key(title)

        count = counts.get(key, 0)

        if count >= max_per_franchise:
            continue

        counts[key] = count + 1
        filtered.append((title, score))

    return filtered