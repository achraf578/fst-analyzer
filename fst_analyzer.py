"""
FST Branch Analyzer Business Logic Module

This module provides routines for calculating competitiveness ratios
(applicants per seat), building branch dictionaries, sorting branch rankings,
and persisting results to disk.
"""

from typing import List, Dict, Any


def calculate_fst_ratio(applicants: int, seats: int) -> float:
    """
    Calculate the competitiveness ratio of applicants to available seats.

    Parameters:
        applicants (int): Total number of applicant submissions.
        seats (int): Total number of available open seats.

    Returns:
        float: Computed ratio (applicants / seats).

    Raises:
        ValueError: If seat count is zero or negative.
    """
    # Validate that seat count is strictly positive
    if seats <= 0:
        raise ValueError("Seats must be greater than zero.")
    
    # Return ratio of applicants per seat
    return applicants / seats


def create_fst_record(city: str, branch: str, applicants: int, seats: int) -> Dict[str, Any]:
    """
    Construct an FST branch evaluation record dictionary.

    Parameters:
        city (str): City location of the FST faculty.
        branch (str): Branch or degree specialization name.
        applicants (int): Total applicant count.
        seats (int): Total available seat count.

    Returns:
        Dict[str, Any]: Formatted FST branch dictionary including computed ratio.
    """
    # Calculate ratio for the branch entry
    ratio = calculate_fst_ratio(applicants, seats)

    # Return structured record dictionary
    return {
        "City": city.strip().title(),    # Format city name in title case
        "Branch": branch.strip().upper(),# Format branch abbreviation in uppercase
        "Applicants": applicants,        # Store total applicants count
        "Seats": seats,                  # Store available seats count
        "Ratio": round(ratio, 2)         # Store ratio rounded to 2 decimal places
    }


def rank_fsts(fst_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Sort FST branch records in ascending order of competitiveness ratio.

    Parameters:
        fst_records (List[Dict[str, Any]]): List of un-ranked FST branch records.

    Returns:
        List[Dict[str, Any]]: Sorted list of FST branch records.
    """
    # Sort branch records based on Ratio key value ascending
    return sorted(fst_records, key=lambda item: item["Ratio"])


def save_fst_records(fst_records: List[Dict[str, Any]], filename: str = "FST.txt") -> None:
    """
    Append processed FST analysis records to text file on disk.

    Parameters:
        fst_records (List[Dict[str, Any]]): List of FST branch records to write.
        filename (str): Target text output file. Defaults to 'FST.txt'.
    """
    # Open target file in append mode and write serialized string
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{fst_records}\n")
