def list_2d_to_table(list_2d, header, char_set=None):
	""" 
	┌──┬────────────┐
	│O.│Název cesty │
	├──┼────────────┤
	│8c│Pučmeloun   │
	│7a│Modrá jablka│
	│6b│Zelená Madla│
	└──┴────────────┘"""
	if char_set == None: 
		s = {
			"│": "│",
			"┬": "┬",
			"─": "─",
		}
	else:
		s = char_set

	listdelek = []
	for column in range(len(header)):
		maxdelka = len(header[column])
		for line in list_2d:
			delka = len(line[column])
			maxdelka = max(delka, maxdelka)
		listdelek.append(maxdelka)

	table = "┌%s┐\n" % s["┬"].join(s["─"] * d for d in listdelek)

	table += s["│"]
	separator = ""
	for delka, cell in zip(listdelek, header):
		table += separator
		table += ("%%-%ds" % delka) % cell 
		separator = "│"
	table += "│\n"

	table += "├%s┤\n" % "┼".join(s["─"] * d for d in listdelek)

	table += s["│"]
	separator = ""
	for row in list_2d:
		for cell, delka in zip(row, listdelek):
			table += separator	
			table += ("%%-%ds" % delka) % cell
			separator = "│"
		table += s["│"]
		table += "\n"

	table += "└%s┘\n" % "┴".join(s["─"] * d for d in listdelek)	
	return table

if __name__ == '__main__':

	s = {
			"│": " ",
			"┬": " ",
			"─": " ",
		}

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
	print(list_2d_to_table(list_2d1, header1, s))
	print("test2")
	print(list_2d_to_table(list_2d2, header2))
