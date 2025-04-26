#%%
class Voiture:
    def __init__(self, marque, model):
        self.marque = marque
        self.model = model
        
    def afficher_info(self):
        print(f"Marque: {self.marque}, Modèle: {self.model}")
    
# %%
honda = Voiture("Honda", "Civic")
honda.afficher_info()
#