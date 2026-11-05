from itertools import combinations
from typing import List, Dict, Tuple

class ActionModel:
    def __init__(self, fichier_csv: str):
        self.fichier_csv = fichier_csv
        self.budget_max = 500.0

    def calculer_profit(self, action: Dict) -> float:
        """
        Calcule le profit réel en euros pour une action donnée
        en tenant compte du format du dataset
        """
        if 'data_test.csv' in self.fichier_csv:
            # Pour data_test.csv, le profit est en pourcentage du coût
            return action['prix'] * action['profit']
        else:
            # Pour dataset1 et dataset2, le profit est directement en euros
            return float(action['profit']) * (float(action['prix']) / 100)

    def force_brute(self, actions: List[Dict]) -> Tuple[List[Dict], float, float]:
        """
        Trouve la meilleure combinaison d'actions en utilisant la force brute.
        """
        meilleure_combinaison = []
        meilleur_profit = 0
        meilleur_cout = 0

        for r in range(1, len(actions) + 1):
            for combo in combinations(actions, r):
                cout_total = sum(action['prix'] for action in combo)
                if cout_total <= self.budget_max:
                    profit_total = sum(self.calculer_profit(action) for action in combo)
                    if profit_total > meilleur_profit:
                        meilleur_profit = profit_total
                        meilleure_combinaison = list(combo)
                        meilleur_cout = cout_total

        return meilleure_combinaison, meilleur_cout, meilleur_profit

    def optimisation(self, actions: List[Dict]) -> Tuple[List[Dict], float, float]:
        """
        Trouve une combinaison optimisée d'actions en utilisant le ratio profit/prix.
        """
        actions_avec_ratio = []
        for action in actions:
            profit_reel = self.calculer_profit(action)
            ratio = profit_reel / action['prix']
            actions_avec_ratio.append({**action, 'ratio': ratio})

        actions_triees = sorted(
            actions_avec_ratio,
            key=lambda x: x['ratio'],
            reverse=True
        )
        
        meilleure_combinaison = []
        cout_total = 0
        profit_total = 0

        for action in actions_triees:
            if cout_total + action['prix'] <= self.budget_max:
                meilleure_combinaison.append(action)
                cout_total += action['prix']
                profit_total += self.calculer_profit(action)

        return meilleure_combinaison, cout_total, profit_total
