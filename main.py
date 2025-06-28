# main.py

from cocomo.effort import calculate_effort
from cocomo.schedule import calculate_schedule

def main():
    size = float(input("Enter software size in KSLOC (e.g., 100): "))
    pm, E = calculate_effort(size)
    tdev = calculate_schedule(pm, E)

    print(f"\nEstimated Effort (Person-Months): {pm}")
    print(f"Estimated Development Time (Months): {tdev}")
    print(f"Average Team Size: {round(pm / tdev, 2)}")

if __name__ == "__main__":
    main()
