from typing import List, Dict, Any


def calculate_fst_ratio(applicants: int, seats: int) -> float:
    """Calculate the applicants-to-seats ratio."""
    if seats <= 0:
        raise ValueError("Seats must be greater than zero.")
    return applicants / seats


def create_fst_record(city: str, branch: str, applicants: int, seats: int) -> Dict[str, Any]:
    """Create and compute an FST record dictionary."""
    ratio = calculate_fst_ratio(applicants, seats)
    return {
        "City": city.strip().title(),
        "Branch": branch.strip().upper(),
        "Applicants": applicants,
        "Seats": seats,
        "Ratio": round(ratio, 2)
    }


def rank_fsts(fst_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Sort FST records by ratio ascending."""
    return sorted(fst_records, key=lambda item: item["Ratio"])


def save_fst_records(fst_records: List[Dict[str, Any]], filename: str = "FST.txt") -> None:
    """Append FST analysis records to file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{fst_records}\n")
