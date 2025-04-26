def add(numbers: str) -> int:
    """
    Funkcja add przyjmuje string z liczbami oddzielonymi przecinkami lub znakami nowej linii
    i zwraca ich sumę. Obsługuje przypadki:
    - pusty string -> zwraca 0
    - liczby oddzielone przecinkiem lub \n
    - przypadek nieprawidłowego wejścia (np. "1,\n") rzuca ValueError
    """
    if not numbers:
        return 0

    # Zamiana znaków nowej linii na przecinki
    numbers = numbers.replace('\n', ',')
    parts = numbers.split(',')

    # Sprawdzanie poprawności wejścia (brak pustych elementów)
    for part in parts:
        if part == '':
            raise ValueError("Invalid input: empty number between delimiters")

    # Konwersja na int i sumowanie
    numbers_list = list(map(int, parts))
    return sum(numbers_list)
