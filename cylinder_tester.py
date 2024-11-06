#TO-DO: write purpose of this file
#!/usr/bin/env python3
# Author: Daniel Tian
# Date: November 6th, 2024
# Purpose: Calls the Cylinder Class

from cylinder import Cylinder

def main():
    Object1 = Cylinder(4,5)
    Object2 = Cylinder()
    print(Object1.surface_area())
    print(Object1.volume())
    print(Object2.surface_area())
    print(Object2.volume())


if __name__ == "__main__":
    main()