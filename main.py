from fst_analyzer import (
    create_fst_record,
    rank_fsts,
    save_fst_records,
)


def main():
    print("========================================")
    print("         FST BRANCH ANALYZER            ")
    print("========================================")

    fsts = []

    try:
        count = int(input("How many FST branches do you want to analyze? "))
    except ValueError:
        print("Invalid number.")
        return

    for i in range(1, count + 1):
        print(f"\n--- Entry {i} of {count} ---")
        city = input("Enter City: ").strip()
        branch = input("Enter Branch: ").strip()

        while True:
            try:
                applicants = int(input("Enter number of applicants: "))
                seats = int(input("Enter number of seats available: "))
                record = create_fst_record(city, branch, applicants, seats)
                fsts.append(record)
                print(f"-> FST {record['City']} ({record['Branch']}): Ratio = {record['Ratio']:.2f}")
                break
            except (ValueError, ZeroDivisionError) as e:
                print(f"Error: {e}. Please re-enter valid numeric values.")

    if fsts:
        sorted_fsts = rank_fsts(fsts)
        print("\n========================================")
        print("           FINAL RANKINGS               ")
        print("========================================")
        for rank, fst in enumerate(sorted_fsts, start=1):
            print(f"Rank {rank} | {fst['City']} ({fst['Branch']}): Ratio {fst['Ratio']:.2f}")

        save_fst_records(sorted_fsts)
        print("\nAnalysis saved to FST.txt")


if __name__ == "__main__":
    main()
