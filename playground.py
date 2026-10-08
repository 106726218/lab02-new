# Track class
class Track:
    def __init__(self, name, location):
        """
        TODO:
        - Store the name and location in the object
        """
        self.name = name
        self.location = location
        pass


# reads in a single track from the given file
def read_track(a_file):
    """
    TODO:
    - Read the track name from the file
    - Read the track location from the file
    - Create and return a Track object
    """
    name = a_file.readline().strip()
    location = a_file.readline().strip()
    return Track(name, location)
    pass


# Takes a single track and prints it to the terminal
def print_track(track):
    """
    TODO:
    - Print the track name
    - Print the track location in the correct format
    """

    pass


def main():
    """
    TODO:
    - Open the file for reading
    - Call read_track(a_file)
    - Call print_track(track)
    - Close the file
    """

    pass


if __name__ == "__main__":
    main()
