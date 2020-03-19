def list_2d_to_table(list_2d, header):
	""" 
	┌──┬────────────┐
	│O.│Název cesty │
	├──┼────────────┤
	│8c│Pučmeloun   │
	│7a│Modrá jablka│
	│6b│Zelená Madla│
	└──┴────────────┘"""
	
	listdelek = []
	for column in range(len(header)):
		maxdelka = len(header[column])
		for line in list_2d:
			delka = len(line[column])
			maxdelka = max(delka, maxdelka)
		listdelek.append(maxdelka)
	print(listdelek)


	top = ("┌" + "─" * listdelek[0] + "┬" + "─" * listdelek[1] + "┐" + "\n" 
	+ "│" + (("%%-%ds" % listdelek[0]) % header[0]) + "│" + header[1] + "│" + "\n")

	#for d in listdelek: 
	#	top += "─" * d
	top = "┌%s┐\n" % "┬".join("─" * d for d in listdelek)
	
	top += "│"
	separator = ""
	for column in range(len(header)):
		top += separator
		top += ("%%-%ds" % listdelek[column]) % header[column] 
		separator = "│"
	top += "│\n"

	#print("top = [%s]" % top)
	
	for line in list_2d:
		top += "│%-25s│\n" % "│".join(line)




	return top








header1 = ["O.", "Název cesty"]

list_2d1 = [
	["8c+", "Pučmeloun"],
	["7a", "Modrá jablka"],
	["6b", "Zelená Madla"],
]

header2 = ["Den", "Stupně"]

list_2d2 = [
	["8c", "Pučmeloun"],
	["7a", "Modrá jablka"],
	["6b", "Zelená Madla"],
]




print("test1")
print(list_2d_to_table(list_2d1, header1))
print("test2")
print(list_2d_to_table(list_2d2, header2))
