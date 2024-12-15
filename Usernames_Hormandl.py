def create_usernames(data):
    # Vytvoříme nový slovník pro transformovaná data, kde budeme ukládat pouze aktivní studenty a jejich uživatelská jména
    transformed_data = {
        "students": [],
        "active": [],
        "usernames": []
    }

    # Slovník pro sledování počtu uživatelských jmen (pro generování unikátních loginů)
    username_counts = {}

    # Projdeme všechny studenty a jejich status
    for student, is_active in zip(data["students"], data["active"]):
        if is_active:  # Zkontrolujeme, zda je student aktivní
            # Přidáme aktivního studenta a jeho status do transformovaných dat
            transformed_data["students"].append(student)
            transformed_data["active"].append(is_active)

            # Rozdělíme jméno studenta na příjmení (surname) a křestní jméno (firstname)
            firstname, surname = student.split(" ")

            # Vytvoříme základ uživatelského jména s 5 písmený příjmení a 3 písmeny křestního jména
            base_username = (surname[:5].lower() + firstname[:3].lower())

            # Generování unikátních uživatelských jmen
            if base_username in username_counts:
                # Pokud už uživatelské jméno existuje, zvýšíme číslo
                username_counts[base_username] += 1
                unique_username = base_username[:-1] + str(username_counts[base_username])
            else:
                # Pokud uživatelské jméno ještě neexistuje, přidáme ho a začneme počítat od 1
                username_counts[base_username] = 1
                unique_username = base_username

            # Uložení uživatelského jména do transformovaných dat
            transformed_data["usernames"].append(unique_username)

    return transformed_data


# Testovací data
data = {
    "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere", "Jiri Hormandl"],
    "active": [True, False, True, True, True]
}

## Test funkce
result = create_usernames(data)

# Zobrazíme výsledek pro lepší přehlednost
print("Result:", result)

# Očekávaný výstup
expected = {
    "students": ["Adam Levine", "John Deere", "John Deere", "Jiri Hormandl"],
    "active": [True, True, True, True],
    "usernames": ["levinada", "deerejoh", "deerejo2", "hormajir"]
}

# Porovnání
assert result == expected, f"Test selhal! Očekávaný výstup: {expected}, ale výstup byl: {result}"