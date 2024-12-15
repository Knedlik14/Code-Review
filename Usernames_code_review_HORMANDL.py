from typing import Dict, List

def create_usernames(data: Dict[str, List]) -> Dict[str, List]:
    """
    Generuje slovník obsahující aktivní studenty a jejich unikátní uživatelská jména.

    Args:
        data (dict): Slovník obsahující:
            - "students" (list of str): Celá jména studentů.
            - "active" (list of bool): Aktivní status odpovídající každému studentovi.

    Returns:
        dict: Slovník s klíči:
            - "students" (list of str): Jména aktivních studentů.
            - "active" (list of bool): Status aktivních studentů (vždy True).
            - "usernames" (list of str): Unikátní uživatelská jména pro aktivní studenty.
    """
    transformed_data = {
        "students": [],
        "active": [],
        "usernames": []
    }

    username_counts = {}

    for student, is_active in zip(data["students"], data["active"]):
        if is_active:
            # Přidání jména a statusu aktivního studenta
            transformed_data["students"].append(student)
            transformed_data["active"].append(is_active)

            # Rozdělení celého jména na křestní a příjmení
            firstname, surname = student.split(" ")

            # Vytvoření základního uživatelského jména (5 písmen příjmení, 3 písmena křestního jména)
            base_username = f"{surname[:5].lower()}{firstname[:3].lower()}"

            # Zajištění unikátnosti uživatelského jména
            if base_username in username_counts:
                username_counts[base_username] += 1
                unique_username = f"{base_username[:-1]}{username_counts[base_username]}"
            else:
                username_counts[base_username] = 1
                unique_username = base_username

            # Přidání unikátního uživatelského jména do transformovaných dat
            transformed_data["usernames"].append(unique_username)

    return transformed_data

# Testovací data
data = {
    "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere", "Jiri Hormandl"],
    "active": [True, False, True, True, True]
}

# Test funkce
result = create_usernames(data)

# Očekávaný výstup
expected = {
    "students": ["Adam Levine", "John Deere", "John Deere", "Jiri Hormandl"],
    "active": [True, True, True, True],
    "usernames": ["levinada", "deerejoh", "deerejo2", "hormajir"]
}

# Porovnání a výstup
assert result == expected, f"Test selhal! Očekávaný výstup: {expected}, ale výstup byl: {result}"
print("Result:", result)