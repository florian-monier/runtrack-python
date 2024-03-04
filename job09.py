class Produit:
    def __init__(self, nom, prix_unitaire, quantite_en_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_en_stock = quantite_en_stock

    def afficher_informations(self):
        print(f"Produit: {self.nom}")
        print(f"Prix unitaire: {self.prix_unitaire} €")
        print(f"Quantité en stock: {self.quantite_en_stock} unités")
        print()

    def mettre_a_jour_prix(self):
        self.prix_unitaire *= 1.10  # Augmentation de 10%

    def ajouter_stock(self, quantite):
        self.quantite_en_stock += quantite

    def acheter_produit(self, quantite):
        if quantite > 0 and quantite <= self.quantite_en_stock:
            self.quantite_en_stock -= quantite
            print(f"Vous avez acheté {quantite} unités de {self.nom}.")
        else:
            print("Quantité invalide ou insuffisante en stock.")

# Création d'un produit
produit1 = Produit("Ordinateur portable", 800, 50)

# Affichage des informations du produit
produit1.afficher_informations()

# Ajout de produits en stock
produit1.ajouter_stock(20)

# Affichage des informations mises à jour
produit1.afficher_informations()

# Mise à jour du prix suite à l'inflation
produit1.mettre_a_jour_prix()

# Affichage des informations après la mise à jour du prix
produit1.afficher_informations()

# Interaction utilisateur pour acheter des produits
quantite_acheter = int(input("Combien d'unités souhaitez-vous acheter ? "))
produit1.acheter_produit(quantite_acheter)

# Affichage des informations après l'achat
produit1.afficher_informations()
