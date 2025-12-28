import sys

class PackageSorter:
    HEAVY_MASS_MINIMUM = 20
    BULKY_DIMENSION_MINIMUM = 150
    BULKY_VOLUME_MINIMUM = 1000000
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


    def sort_package(self, width: float, height: float, length: float, mass: float) -> str:
        if width <= 0 or height <= 0 or length <= 0:
            raise ValueError("Dimensions must be greater than 0")
        if mass <= 0:
            raise ValueError("Mass must be greater than 0")
        
        isBulky = self._is_bulky(width, height, length)
        isHeavy = self._is_heavy(mass)

        if isBulky and isHeavy:
            return PackageSorter.REJECTED
        elif isBulky or isHeavy:
            return PackageSorter.SPECIAL
        return PackageSorter.STANDARD

    def _is_bulky(self, width: float, height: float, length: float) -> bool:
        if width * height * length >= self.BULKY_VOLUME_MINIMUM:
            return True
        if width >= PackageSorter.BULKY_DIMENSION_MINIMUM or height >= PackageSorter.BULKY_DIMENSION_MINIMUM or length >= PackageSorter.BULKY_DIMENSION_MINIMUM:
            return True
        return False

    def _is_heavy(self, mass: float) -> bool:
        return mass >= PackageSorter.HEAVY_MASS_MINIMUM

if __name__ == "__main__":
    # This block ensures the code runs only when executed as a script
    sorter = PackageSorter()

    if len(sys.argv) == 1:
        print(sorter.sort_package(10, 20, 140, 15))
    elif len(sys.argv) != 5:
        raise ValueError("Must provide 4 arguments")
    else:
        print(sorter.sort_package(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))