"""Add missing 'metadata' to display_data outputs so nbconvert validation passes."""
import json
import sys

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "us-medical-insurance-costs.ipynb"
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    fixed = 0
    for cell in nb.get("cells", []):
        for out in cell.get("outputs", []):
            if isinstance(out, dict) and out.get("output_type") in ("display_data", "execute_result") and "metadata" not in out:
                out["metadata"] = {}
                fixed += 1

    if fixed > 0:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        print(f"Fixed {fixed} output(s) in {path}")
    else:
        print(f"No fixes needed in {path}")


if __name__ == "__main__":
    main()
