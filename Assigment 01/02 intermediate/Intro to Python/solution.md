```python
# Planetary Weights – Full Solution

# Constants for gravity relative to Earth
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14


def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt the user for the name of a planet
    planet = input("Enter a planet: ")

    # Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        # Assume the only remaining valid input is Neptune
        gravity_constant = NEPTUNE_GRAVITY

    # Calculate the equivalent weight on the selected planet
    planetary_weight = earth_weight * gravity_constant
    rounded_weight = round(planetary_weight, 2)

    # Display the result
    print("The equivalent weight on " + planet + ":", rounded_weight)


if __name__ == "__main__":
    main()
```

