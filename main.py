"""
FST Branch Analyzer Console Application Main Entry Point

This module handles user input prompts for gathering applicant/seat metrics,
invokes ratio computation and sorting functions, and displays final rankings.
"""

from fst_analyzer import (
    create_fst_record,
    rank_fsts,
    save_fst_records,
)


def main():
    """
    Main interactive entry point for the FST Branch Analyzer.
    """
    print("========================================")
    print("         FST BRANCH ANALYZER            ")
    print("========================================")

    # Initialize empty list to hold FST branch evaluation records
    fsts = []

    # Prompt user for number of FST entries to analyze
    try:
        count = int(input("How many FST branches do you want to analyze? "))
    except ValueError:
        print("Invalid number. Exiting program.")
        return

    # Loop through requested count to collect data for each branch
    for i in range(1, count + 1):
        print(f"\n--- Entry {i} of {count} ---")
        city = input("Enter City name: ").strip()
        branch = input("Enter Branch/Specialization: ").strip()

        # Prompt loop for numeric inputs with error validation
        while True:
            try:
                applicants = int(input("Enter number of applicants: "))
                seats = int(input("Enter number of available seats: "))
                
                # Construct FST branch record dictionary
                record = create_fst_record(city, branch, applicants, seats)
                fsts.append(record)
                
                # Display individual branch ratio summary
                print(f"Recorded FST {record['City']} ({record['Branch']}): Ratio = {record['Ratio']:.2f}")
                break
            except (ValueError, ZeroDivisionError) as e:
                print(f"Error: {e}. Please re-enter valid positive integers.")

    # Process and display final ranked results if entries were added
    if fsts:
        # Sort branch records ascending by ratio
        sorted_fsts = rank_fsts(fsts)
        
        print("\n========================================")
        print("           FINAL RANKINGS               ")
        print("========================================")
        
        # Display ranked leaderboard
        for rank, fst in enumerate(sorted_fsts, start=1):
            print(f"Rank {rank} | {fst['City']} ({fst['Branch']}): Ratio {fst['Ratio']:.2f}")

        # Append evaluation records to persistent text log file
        save_fst_records(sorted_fsts)
        print("\nAnalysis appended to FST.txt successfully.")


if __name__ == "__main__":
    main()
