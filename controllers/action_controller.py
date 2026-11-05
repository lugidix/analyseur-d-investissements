import csv
import time
from models.action_model import ActionModel
from views.action_view import ActionView
from colorama import init, Fore, Style

class ActionController:
    def __init__(self, fichier_csv):
        self.action_model = ActionModel(fichier_csv)
        self.view = ActionView()
        init()  # Initialize colorama

    def lire_donnees(self):
        actions = []
        try:
            with open(self.action_model.fichier_csv, newline='', encoding='utf-8-sig') as csvfile:
                # Detect file type based on path
                if 'data_test.csv' in self.action_model.fichier_csv:
                    return self.lire_donnees_test(csvfile)
                else:
                    return self.lire_donnees_standard(csvfile)
        except FileNotFoundError:
            print(f"{Fore.RED}Erreur: Fichier CSV introuvable.{Style.RESET_ALL}")
            return []

    def lire_donnees_standard(self, csvfile):
        actions = []
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        
        for row in reader:
            try:
                nom = row[0].strip()
                prix = float(row[1].strip())
                profit = float(row[2].strip())  # Le profit est en pourcentage
                
                if prix <= 0 or profit < 0:
                    print(f"{Fore.YELLOW}Attention: Ignoré {nom} - Prix ou profit invalide{Style.RESET_ALL}")
                    continue
                    
                action = {
                    'nom': nom,
                    'prix': round(prix, 2),
                    'profit': profit,
                    'fichier_csv': self.action_model.fichier_csv
                }
                actions.append(action)
            except (IndexError, ValueError) as e:
                print(f"{Fore.YELLOW}Attention: Ligne ignorée {row}: {e}{Style.RESET_ALL}")
        
        return actions

    def lire_donnees_test(self, csvfile):
        actions = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                prix = float(row[' Coût par action (en euros)'].strip())
                profit = float(row[' Bénéfice (après 2 ans)'].replace('%', '').strip()) / 100
                
                if prix <= 0 or profit < 0:
                    continue
                    
                action = {
                    'nom': row['Actions'].strip(),
                    'prix': round(prix, 2),
                    'profit': profit,
                    'fichier_csv': self.action_model.fichier_csv
                }
                actions.append(action)
            except (KeyError, ValueError) as e:
                print(f"{Fore.YELLOW}Attention: Ligne ignorée {row}: {e}{Style.RESET_ALL}")
                
        return actions

    def executer_force_brute(self):
        actions = self.lire_donnees()
        if actions:
            print(f"\n{Fore.CYAN}Analyse de {len(actions)} actions...{Style.RESET_ALL}")
            start_time = time.time()
            meilleure_combinaison, cout_total, profit_total = self.action_model.force_brute(actions)
            temps_execution = time.time() - start_time
            self.view.afficher_resultats(meilleure_combinaison, cout_total, profit_total, temps_execution)

    def executer_optimise(self):
        actions = self.lire_donnees()
        if actions:
            print(f"\n{Fore.CYAN}Analyse de {len(actions)} actions...{Style.RESET_ALL}")
            start_time = time.time()
            meilleure_combinaison, cout_total, profit_total = self.action_model.optimisation(actions)
            temps_execution = time.time() - start_time
            self.view.afficher_resultats(meilleure_combinaison, cout_total, profit_total, temps_execution)