# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Affichage des informations initiales
print("Investissement initial :", montant_initial, "€")
print("Taux de rendement annuel :", taux_rendement_annuel, "%")

# Simulation financière sur plusieurs années (par exemple, 5 ans)
nombre_annees = 5

# Boucle de simulation pour chaque année
for annee in range(1, nombre_annees + 1):
    rendement = montant_initial * (taux_rendement_annuel / 100)
    montant_initial += rendement
    print(f"Année {annee}: Montant après rendement : {montant_initial:.2f} €")

# Affichage du montant final
print("Montant final après", nombre_annees, "années :", montant_initial, "€")
# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage
augmentation_capital = 5000  # Augmentation du capital en euros
augmentation_taux = 2  # Augmentation du taux de rendement en pourcentage

# Affichage des informations initiales
print("Investissement initial :", montant_initial, "€")
print("Taux de rendement annuel :", taux_rendement_annuel, "%")
print("Augmentation du capital par an :", augmentation_capital, "€")
print("Augmentation du taux de rendement par an :", augmentation_taux, "%")

# Simulation financière sur plusieurs années (par exemple, 5 ans)
nombre_annees = 5

# Boucle de simulation pour chaque année
for annee in range(1, nombre_annees + 1):
    rendement = montant_initial * (taux_rendement_annuel / 100)
    montant_initial += rendement + augmentation_capital
    taux_rendement_annuel += augmentation_taux
    
    gain_annuel = rendement + augmentation_capital
    print(f"Année {annee}: Gain annuel : {gain_annuel:.2f} €, Montant total : {montant_initial:.2f} €, Taux de rendement : {taux_rendement_annuel:.2f}%")

# Affichage du montant final
print("Montant final après", nombre_annees, "années :", montant_initial, "€")
# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage
augmentation_capital = 5000  # Augmentation du capital en euros
augmentation_taux = 2  # Augmentation du taux de rendement en pourcentage
retrait_percentage = 10  # Pourcentage à retirer du montant total
diminution_rendement = 1  # Diminution du taux de rendement en pourcentage

# Affichage des informations initiales
print("Investissement initial :", montant_initial, "€")
print("Taux de rendement annuel :", taux_rendement_annuel, "%")
print("Augmentation du capital par an :", augmentation_capital, "€")
print("Augmentation du taux de rendement par an :", augmentation_taux, "%")
print("Pourcentage à retirer du montant total :", retrait_percentage, "%")
print("Diminution du rendement après retrait :", diminution_rendement, "%")

# Simulation financière sur plusieurs années (par exemple, 5 ans)
nombre_annees = 5

# Boucle de simulation pour chaque année
for annee in range(1, nombre_annees + 1):
    rendement = montant_initial * (taux_rendement_annuel / 100)
    montant_initial += rendement + augmentation_capital
    taux_rendement_annuel += augmentation_taux
    
    gain_annuel = rendement + augmentation_capital
    print(f"Année {annee}: Gain annuel : {gain_annuel:.2f} €, Montant total avant retrait : {montant_initial:.2f} €, Taux de rendement : {taux_rendement_annuel:.2f}%")
    
    # Retrait de 10% du montant total
    montant_initial *= (100 - retrait_percentage) / 100
    
    # Diminution du rendement de 1% après le retrait
    taux_rendement_annuel -= diminution_rendement

# Affichage du montant final
print("Montant final après", nombre_annees, "années :", montant_initial, "€")
