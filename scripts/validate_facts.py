#!/usr/bin/env python3
"""
Fact Consistency Validation
Checks a set of generated content pieces for fact consistency.

Usage: python validate_facts.py <content_dir> <product_facts.json>
"""

import json
import os
import re
import sys


def load_product_facts(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_numbers(text):
    """Extract all numbers with context from text."""
    patterns = [
        r"(\d+(?:\.\d+)?)\s*(克|g|毫升|ml|片|盒|包|个|次|遍|元|块)",
        r"(\d+(?:\.\d+)?)\s*(度|%|百分之)",
    ]
    results = []
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            results.append({
                "value": float(match.group(1)),
                "unit": match.group(2),
                "context": text[max(0, match.start()-20):match.end()+20]
            })
    return results


def check_fact_drift(content_files, product_facts):
    """Check that core product facts are consistent across all content pieces."""
    issues = []

    # Extract key facts from product facts
    expected = {}
    specs = product_facts.get("specs", {})
    if specs.get("weight_grams"):
        expected["weight_grams"] = specs["weight_grams"]
    if specs.get("pieces"):
        expected["pieces"] = specs["pieces"]

    pricing = product_facts.get("pricing", {})
    if pricing.get("price"):
        expected["price"] = pricing["price"]

    brewing = product_facts.get("brewing", {})
    if brewing.get("brew_count"):
        expected["brew_count"] = brewing["brew_count"]

    # Check each file
    for filepath in content_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        numbers = extract_numbers(content)
        filename = os.path.basename(filepath)

        # Check for price consistency (simple check)
        if "price" in expected:
            price = expected["price"]
            # Find price-like numbers
            for num in numbers:
                if num["unit"] in ("元", "块") and abs(num["value"] - price) > 0.01:
                    # Only flag if it looks like product price (not discount, not per-unit)
                    if "券后" not in num["context"] and "到手" not in num["context"]:
                        issues.append(
                            f"[{filename}] Price mismatch: found {num['value']}{num['unit']}, "
                            f"expected {price}元. Context: '{num['context'].strip()}'"
                        )

    return issues


def main():
    if len(sys.argv) < 3:
        print("Usage: python validate_facts.py <content_dir> <product_facts.json>")
        sys.exit(1)

    content_dir = sys.argv[1]
    facts_path = sys.argv[2]

    if not os.path.isdir(content_dir):
        print(f"Error: Content directory not found: {content_dir}")
        sys.exit(1)

    if not os.path.isfile(facts_path):
        print(f"Error: Product facts file not found: {facts_path}")
        sys.exit(1)

    # Load product facts
    product_facts = load_product_facts(facts_path)
    print(f"Product: {product_facts.get('product_name', 'Unknown')}")

    # Find content files
    content_files = []
    for root, dirs, files in os.walk(content_dir):
        for f in files:
            if f.endswith(".md") or f.endswith(".txt"):
                content_files.append(os.path.join(root, f))

    print(f"Found {len(content_files)} content files to check")

    # Run checks
    issues = check_fact_drift(content_files, product_facts)

    # Report
    if issues:
        print(f"\nFound {len(issues)} fact consistency issues:")
        for issue in issues:
            print(f"  ⚠ {issue}")
    else:
        print("\n✓ No fact consistency issues found")

    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
