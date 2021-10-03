# Made by ostSTRUPpen
# -----------Čísla chyb-----------
#	0-99 = Obecné errory
#		0 = Příkaz neexistuje
#		1 = Argument nezadán
# 		2 = Zadaný argument neexistuje
#   
#	100-199 = Errory pro příkaz help
#		100 =
#
#	200-299 = Errory pro příkaz exit
#		200 = 
#
#	300-399 = Errory pro příkaz list
#		300 = Číslo menší/rovno nule
#		301 = Číslo vyšší než počet studentů
#
#	400-499 = Errory pro příkaz	del
#		400 = Číslo menší/rovno nule
#		401 = Číslo vyšší než počet studentů
#		402 = Ne a/n
#
#	500-599 = Errory pro příkaz add
#		500 =
def handle(error_code, command, args):
	if error_code == 0:
		output = 'Zadaný příkaz ({}) neexistuje! Použijte help'
		return output.format(command)
	elif error_code == 1:
		output = 'Nezadal jste žádný argument! Použijte {} -?'
		return output.format(command)
	elif error_code == 2:
		output = 'Zadaný argument: {}, neexistuje! Použijte {} -?'
		return output.format(args, command)
	elif error_code == 300 or error_code == 400:
		output = 'Číslo musí být větší než 0!'
		return output
	elif error_code == 301 or error_code == 401:
		output = 'Číslo musí být menší než počet studentů! Počet studentů: '
		return output
	elif error_code == 402:
		output = 'Odpověď \'{}\' nezačíná na písmeno \'a\' nebo \'n\' a neodpovídá proto očekávanámu vzorci! \nPříkaz byl v ukončen!'
		return output.format(command)

commands = [['help', 'Vypíše toto menu'], ['list', 'Výpis studentů, Argumenty: -a = Vypíše všechny studenty (např: list -a)|-l = Vypíše počet studentů (např: list -l)|-ČÍSLO = Vypíše daného studenta (např: list -1)'], [
	'exit', 'Ukončí program'], ['del ', 'Odstraní studenta Argumenty: -ČÍSLO = odstraní studenta se zadaným pořadovým číslem (např: del -5)'], ['add ', 'Umožňuje přidat studenta']]

def help(command):
	output = '{}    =   {}\n'
	if command == 'all':
		all_commands = ''
		for comm in (commands):
			all_commands += output.format(comm[0],comm[1])
		return all_commands
	elif command == commands[0][0].strip():
		return output.format(commands[0][0], commands[0][1])
	elif command == commands[1][0].strip():
		return output.format(commands[1][0], commands[1][1])
	elif command == commands[2][0].strip():
		return output.format(commands[2][0], commands[2][1])
	elif command == commands[3][0].strip():
		return output.format(commands[3][0], commands[3][1])
	elif command == commands[4][0].strip():
		return output.format(commands[4][0], commands[4][1])