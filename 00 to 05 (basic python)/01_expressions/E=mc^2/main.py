# Constant speed of light in m/s
C: int = 299792458  # 299,792,458 m/s

def main():
    # Ask user to enter mass in kilograms
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * C^2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display step-by-step result
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

# Run the program
if __name__ == '__main__':
    main()
