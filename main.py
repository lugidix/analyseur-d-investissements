import os
from colorama import init, Fore, Style
from controllers.action_controller import ActionController
import platform

def clear_screen():
    """Nettoie l'écran de manière compatible avec différents OS"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def main():
    init(autoreset=True)
    
    while True:
        clear_screen()
        print("\n=== ANALYSEUR D'INVESTISSEMENTS ===\n")
        
        print("Choisissez une méthode d'investissement:")
        print(f"{Fore.CYAN}1.{Style.RESET_ALL} Force brute (Analyse exhaustive)")
        print(f"{Fore.CYAN}2.{Style.RESET_ALL} Optimisée (Analyse rapide)")
        print(f"{Fore.CYAN}0.{Style.RESET_ALL} Quitter")
        
        method = input("\nVotre choix (0-2) : ")

        if method == '0':
            print("\nAu revoir!")
            break

        if method not in ['1', '2']:
            print(f"\n{Fore.RED}Choix invalide{Style.RESET_ALL}")
            input("Appuyez sur Entrée pour continuer...")
            continue

        print("\nChoisissez un dataset à utiliser:")
        print(f"{Fore.CYAN}1.{Style.RESET_ALL} data_test.csv (Petit dataset)")
        print(f"{Fore.CYAN}2.{Style.RESET_ALL} dataset1_Python+P7.csv")
        print(f"{Fore.CYAN}3.{Style.RESET_ALL} dataset2_Python+P7.csv")
        
        dataset_choice = input("\nVotre choix (1-3) : ")
        
        if dataset_choice not in ['1', '2', '3']:
            print(f"\n{Fore.RED}Choix invalide{Style.RESET_ALL}")
            input("Appuyez sur Entrée pour continuer...")
            continue

        datasets = [
            r"data\data_test.csv",
            r"data\dataset1_Python+P7.csv",
            r"data\dataset2_Python+P7.csv"
        ]

        try:
            dataset_path = datasets[int(dataset_choice) - 1]
            controller = ActionController(dataset_path)

            if method == '1':
                print("\nAnalyse en cours (force brute)...")
                controller.executer_force_brute()
            else:
                print("\nAnalyse en cours (optimisée)...")
                controller.executer_optimise()

        except Exception as e:
            print(f"\n{Fore.RED}Erreur: {e}{Style.RESET_ALL}")

        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()