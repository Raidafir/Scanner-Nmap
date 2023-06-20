import subprocess
import shutil
from colorama import init, Fore, Style

# Fonction pour exécuter une commande et obtenir la sortie
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8')

# Fonction pour afficher les résultats du scan avec la ligne de séparation adaptée
def print_results(scan_results, separator_line):
    print("Résultats du scan :")
    print(Fore.MAGENTA + scan_results + Style.RESET_ALL)  # Mettre les résultats en magenta
    print(Fore.GREEN + separator_line + Style.RESET_ALL)  # Afficher la ligne de séparation

# Demander à l'utilisateur de saisir l'adresse IP
ip_address = input("Veuillez entrer une adresse IP à scanner : ")

# Commande 1: nmap -sS -Pn -p- (ip)
command1 = f"nmap -sS -Pn -p- {ip_address}"
print("Commande 1 :", command1)

# Exécuter la commande 1 et obtenir les résultats
results1 = run_command(command1)

# Obtenir la largeur de la console
console_width = shutil.get_terminal_size().columns

# Afficher une ligne colorée de la même largeur que la console
separator_line = '-' * console_width
print(Fore.GREEN + separator_line + Style.RESET_ALL)

# Afficher les résultats du scan 1
print_results(results1, separator_line)

# Commande 2: nmap -sC -sV -O -p (ports) (ip)
ports = input("Veuillez entrer les ports à scanner (ex: 80,443,8080) : ")
command2 = f"nmap -sC -sV -O -p {ports} {ip_address}"
print("Commande 2 :", command2)

# Exécuter la commande 2 et obtenir les résultats
results2 = run_command(command2)

# Afficher les résultats du scan 2
print_results(results2, separator_line)

# Commande 3: nmap --script vuln (ip)
command3 = f"nmap --script vuln {ip_address}"
print("Commande 3 :", command3)

# Exécuter la commande 3 et obtenir les résultats
results3 = run_command(command3)

# Afficher les résultats du scan 3
print_results(results3, separator_line)
