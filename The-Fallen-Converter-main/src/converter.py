import xml.etree.ElementTree as ET
import os

tree = ET.parse("types.xml")
root = tree.getroot()

precursor = """<CurrencyName> #tm_ruble
	<Currency> MoneyRuble1, 	1
	<Currency> MoneyRuble5, 	5
	<Currency> MoneyRuble10, 	10
	<Currency> MoneyRuble25, 	25
	<Currency> MoneyRuble50, 	50
	<Currency> MoneyRuble100, 	100\n"""

categories = {
	"Food": [],
	"Containers": [],
	"Tools": [],
	"Weapons": [],
	"Explosives": [],
	"Clothes": [],
	"Vehiclesparts": [],
	"Vehicles": [],
	"Viking": [],
	"Bbp": [],
	"Msp": [],
	"Mass": [],
	"Cp": [],
	"Mung": [],
}

traders = {
	"Consume Trader": ["Food"], # 0
	"Misc Trader": ["Containers", "Tools", "Viking", "Bbp", "Msp", "Mass", "Cp", "Mung"], # 1
	"Weapon Trader": ["Weapons", "Explosives"], # 2
	"Clothing Trader": ["Clothes"], # 3
	"Weapon Supplies Trader": [""], # 4
	"Vehicles Trader": ["Vehiclesparts", "Vehicles"] # 5
}

banned_prefixes = [
	"animal",
	"christmastree",
	"fence",
	"land_wreck",
	"watchtower",
	"waterbottle",
	"wreck",
	"zmb",
	"slottedwood",
	"BusPsychoWheel_offroad_Ruined",
	"CigarettePack",
	"Armor_Rack"
]

for child in root:
	name = child.attrib["name"]
	category = ""
	quantity = "*"

	for childs_child in child:
		if childs_child.tag == "category":
			category = childs_child.attrib["name"]

	shouldContinue = True
	for prefix in banned_prefixes:
		if len(prefix) <= len(name):
			if name[:len(prefix)].lower() == prefix.lower():
				shouldContinue = False

	if shouldContinue == False:
		continue

	if name[:7].lower() == "skyline":
		continue

	elif name[:3].lower() == "bbp":
		category = "Bbp"
	
	elif name[:3].lower() == "msp":
		category = "Msp"
	
	elif name[:4].lower() == "mass":
		category = "Mass"

	elif name[:2].lower() == "cp":
		category = "Cp"

	elif name[-4:].lower() == "mung":
		category = "Mung"

	elif name[:11].lower() == "rag_hummer_":
		category = "Vehiclesparts"

	elif name[:10].lower() == "rag_viking":
		category = "Viking"

	elif name[-9:].lower() == "destroyed":
		continue

	elif name[-9:].lower() == "_deployed":
		continue

	elif category == "":
		category = "Vehicles"
		quantity = "V"

	categories[category.capitalize()].append({"name": name, "quantity": quantity})

if os.path.exists("TraderConfig.txt"): 
	os.remove("TraderConfig.txt")

f = open("TraderConfig.txt", "a+")
f.write(precursor)

for trader in traders:
	f.write("\n\n<Trader> " + trader)
	
	for category in categories:
		if category in traders[trader]:
			f.write("\n" + 	"	<Category> " + category.capitalize() + "\n")
			for item in categories[category]:
				writeString = "{:<70}".format("		" + item["name"] + ",")
				f.write(writeString + item["quantity"] + ",			1,			-1\n")

f.close()