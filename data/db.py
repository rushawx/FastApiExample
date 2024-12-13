from models.dog import Dog, DogType
from models.timestamp import Timestamp

dogs_db = {
    0: Dog(name="Bob", pk=0, kind=DogType("terrier")),
    1: Dog(name="Marli", pk=1, kind=DogType("bulldog")),
    2: Dog(name="Snoopy", pk=2, kind=DogType("dalmatian")),
    3: Dog(name="Rex", pk=3, kind=DogType("dalmatian")),
    4: Dog(name="Pongo", pk=4, kind=DogType("dalmatian")),
    5: Dog(name="Tillman", pk=5, kind=DogType("bulldog")),
    6: Dog(name="Uga", pk=6, kind=DogType("bulldog")),
}

post_db = [Timestamp(id=0, timestamp=12), Timestamp(id=1, timestamp=10)]
