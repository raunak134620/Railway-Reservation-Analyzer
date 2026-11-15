import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

REQUIRED_COLUMNS = [
    "PNR", "Train", "Class", "Fare", "Status"
]

VALID_STATUSES = ["Confirmed", "Waiting", "Cancelled"]


def load_bookings(filename):

    if not Path(filename).is_file():
        print(f"Error: File '{filename}' not found.")
        return None

    try:
        df = pd.read_csv(filename, dtype=str)
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return None
    except Exception as error:
        print(f"Error reading CSV: {error}")
        return None

    df.columns = df.columns.str.strip()

    missing = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing:
        print("Missing columns:", ", ".join(missing))
        return None

    df = df[REQUIRED_COLUMNS].copy()

    for col in REQUIRED_COLUMNS:
        df[col] = (
            df[col].fillna("").astype(str).str.strip()
        )

    valid_rows = []

    for _, row in df.iterrows():

        fare = pd.to_numeric(
            row["Fare"], errors="coerce"
        )

        if pd.isna(fare) or fare < 0:
            print(
                f"Warning: Row with PNR {row['PNR']} "
                "skipped - invalid fare."
            )
            continue

        if not row["PNR"] or not row["Train"] or not row["Status"]:
            print(
                f"Warning: Row with PNR {row['PNR']} "
                "skipped - missing required value."
            )
            continue

        row["Fare"] = str(fare)
        row["Status"] = row["Status"].title()

        if row["Status"] not in VALID_STATUSES:
            print(
                f"Warning: Row with PNR {row['PNR']} "
                "skipped - invalid status."
            )
            continue

        valid_rows.append(row)

    clean_df = pd.DataFrame(
        valid_rows, columns=REQUIRED_COLUMNS
    )

    clean_df["Fare"] = pd.to_numeric(
        clean_df["Fare"]
    )

    return clean_df


def draw_chart(data, title, ylabel, filename):

    if data.empty:
        print("No data available for chart.")
        return

    plt.figure(figsize=(8, 5))

    data.plot(kind="bar")

    plt.title(title)
    plt.xlabel("Train")
    plt.ylabel(ylabel)
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig(filename)

    print("Chart saved as", filename)

    plt.show()


def bookings_per_train(df):

    counts = df.groupby("Train").size().sort_index()

    print("\nBookings per train:")

    for train, count in counts.items():
        print(f"{train} : {count}")

    print("Total bookings:", len(df))

    draw_chart(
        counts,
        "Bookings per Train",
        "Number of Bookings",
        "bookings_per_train.png"
    )


def revenue_per_train(df):

    confirmed = df[
        df["Status"] == "Confirmed"
    ]

    revenue = (
        confirmed.groupby("Train")["Fare"]
        .sum()
        .sort_index()
    )

    print("\nConfirmed revenue per train:")

    for train, amount in revenue.items():
        print(f"{train} : Rs. {amount:.0f}")

    total = revenue.sum()

    print(f"Total confirmed revenue: Rs. {total:.0f}")

    draw_chart(
        revenue,
        "Confirmed Revenue per Train",
        "Revenue (Rs.)",
        "revenue_per_train.png"
    )


def status_summary(df):

    counts = df["Status"].value_counts()

    print("\nBookings by status:")

    for status in VALID_STATUSES:
        print(f"{status}: {counts.get(status, 0)}")


def main():

    print("=" * 45)
    print("    RAILWAY RESERVATION ANALYZER")
    print("=" * 45)

    filename = input(
        "Enter CSV filename [bookings.csv]: "
    ).strip()

    if not filename:
        filename = "bookings.csv"

    df = load_bookings(filename)

    if df is None:
        return

    print(f"\nValid records analysed: {len(df)}")

    if df.empty:
        return

    while True:

        print("\n------------- MENU -------------")
        print("1. Bookings per train")
        print("2. Revenue per train")
        print("3. Count bookings by status")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            bookings_per_train(df)

        elif choice == "2":
            revenue_per_train(df)

        elif choice == "3":
            status_summary(df)

        elif choice == "4":
            print("Thank you for using Railway Reservation Analyzer.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
