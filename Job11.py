def time_to_text(minutes):
    try:
        minutes = int(minutes)  
        if minutes < 0:
            print("Le nombre de minutes doit être positif.")
        else:
            heures = minutes // 60
            minutes_restantes = minutes % 60
            if heures == 0 and minutes_restantes == 0:
                print("Aucune minute n'a été spécifiée.")
            elif heures == 0:
                print(f"{minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}")
            elif minutes_restantes == 0:
                print(f"{heures} heure{'s' if heures > 1 else ''}")
            else:
                print(f"{heures} heure{'s' if heures > 1 else ''} et {minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

time_to_text(120)
time_to_text(75)
time_to_text("abc")  
