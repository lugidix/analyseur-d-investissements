from colorama import Fore, Style

class ActionView:
    def calculer_rendement(self, action, fichier_csv):
        """
        Calcule le rendement en pourcentage selon le type de dataset
        """
        if 'data_test.csv' in fichier_csv:
            return action['profit'] * 100  # Already in percentage
        else:
            return action['profit']  # Already in percentage for dataset1 and dataset2

    def afficher_resultats(self, meilleure_combinaison, cout_total, profit_total, temps_execution):
        print("\n" + "=" * 50)
        print("          RÉSULTATS DE L'ANALYSE")
        print("=" * 50 + "\n")
        
        if not meilleure_combinaison:
            print(f"{Fore.YELLOW}Aucune combinaison valide trouvée.{Style.RESET_ALL}")
            return

        print(f"{'Action':<30} {'Coût':>10} {'Rendement':>12} {'Profit':>10}")
        print("-" * 65)

        for action in meilleure_combinaison:
            if 'data_test.csv' in action.get('fichier_csv', ''):
                rendement = action['profit'] * 100
                profit_euros = action['prix'] * action['profit']
            else:
                rendement = action['profit']
                profit_euros = (action['prix'] * action['profit']) / 100

            print(
                f"{action['nom']:<30} "
                f"{action['prix']:>9.2f}€ "
                f"{rendement:>11.1f}% "
                f"{profit_euros:>9.2f}€"
            )

        print("-" * 65)
        
        rendement_total = (profit_total / cout_total) * 100 if cout_total > 0 else 0
        
        print(f"\nRÉSUMÉ:")
        print(f"Coût total:      {Fore.CYAN}{cout_total:>9.2f}€{Style.RESET_ALL}")
        print(f"Profit total:    {Fore.GREEN}{profit_total:>9.2f}€{Style.RESET_ALL}")
        print(f"Rendement total: {rendement_total:>9.1f}%")
        print(f"\nTemps d'exécution: {temps_execution:.3f} secondes")
        print("\n" + "=" * 50)
