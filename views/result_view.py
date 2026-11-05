class ResultView:
    def afficher_resultat(self, actions, total_cost, total_profit, exec_time):
        print("\nMeilleure combinaison d'actions :")
        if actions:
            for action in actions:
                print(f"- {action[0]} (Coût: {action[1]}€, Profit: {action[2]}%)")
        else:
            print("Aucune action sélectionnée.")

        print(f"\nCoût total : {total_cost}€")
        print(f"Profit total : {total_profit}€")
        print(f"\nTemps d'exécution : {exec_time:.2f} secondes")
