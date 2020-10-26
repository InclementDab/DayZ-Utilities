# The-Fallen-Converter V.1.0
A tool for DayZ Standalone Server Admins to convert types.xml files to TraderConfig.txt

Created by Fallen and Gnik

Code done by Fallen, Concept done by Gnik

For Questions/Suggestions Message @Gnik#0001 or Fallen#0448 on Discord

If you'd like to support this project you can [Donate Here](https://paypal.me/OblivionGS)

HOW TO USE: Place types.xml file into your The Fallen Converter File with the converter.exe and run the exe. See TraderConfig.txt for output

NOTICE:
This converter sorts into Traders/Categories based off the types.xml categories! 

Notice the different categories and how it pulled the categories & names of the items.

This converter will pull the <type name="Example"> and insert it as the ClassName inside your TraderConfig.txt
  then it will pull the <category name="food"/> and insert it as the Category insider your TraderConfig.txt
 Notice that in our example below it pulls the item "Example" and places it under the Consume Trader in the Category Food  with a Quantity of "*" and a Buy price of "1" and a sell price of "-1".
  
 Yes in this current version you have to edit your Quantity, Buy Price, and Sell Price. 
 
 Notice the other listed Categories under Misc Trader, any items from MassManyItemsOverhaul will be thrown into the <Category> Mass, any items from BaseBuildingPlus into Bbp, any items from MuchStuffPack into Msp  any items from viking pack into Viking, any items from MunghardsItemPack into Mung.  
 Any items that do NOT have a <category name=""/> will be placed into the Vehicles Category. 
  
 For the Base Categories; Food, Containers, Tools,  Weapons, Explosives, Clothes, Vehiclesparts, and Vehicles the types.xml will be sorted into those categories as long as the <category name="Is_One_Of_The_Above_Base_Categories"/>.
 
 See Example Below to get a Fill for how it filters

Tips:

types.xml file must be named "types.xml"
types.xml file must start with <types> and end with </types>
Once you get your TraderConfig.txt I do highly recommend uploading it too: https://dayz.skyn1.se/ to further edit your TraderConfig.txt with ease


ex:

Input:
```
-- Start of types.xml --



<types>
	<type name="Example"> --See Below
        <nominal>0</nominal>
        <lifetime>3600</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0"/>
        <category name="food"/> --See Below
        <tag name="shelves"/>
        <usage name="Farm"/>
        <usage name="Town"/>
        <usage name="Village"/>
    </type>

    <type name="Example1"> --See Below
        <nominal>0</nominal>
        <lifetime>3600</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0"/>
        <category name="containers"/> --See Below
        <tag name="shelves"/>
        <usage name="Farm"/>
        <usage name="Town"/>
        <usage name="Village"/>
    </type>

    <type name="Example2"> --See Below
        <nominal>0</nominal>
        <lifetime>3600</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0"/>
        <category name="tools"/> --See Below
        <tag name="shelves"/>
        <usage name="Farm"/>
        <usage name="Town"/>
        <usage name="Village"/>
    </type>

    <type name="Example3"> --See Below
        <nominal>0</nominal>
        <lifetime>3600</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0"/>
        <category name="weapons"/> --See Below
        <tag name="shelves"/>
        <usage name="Farm"/>
        <usage name="Town"/>
        <usage name="Village"/>
    </type>

    <type name="Example4"> --See Below
        <nominal>0</nominal>
        <lifetime>3600</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0"/>
        <category name="explosives"/> --See Below
        <tag name="shelves"/>
        <usage name="Farm"/>
        <usage name="Town"/>
        <usage name="Village"/>
    </type>

    <type name="Example5"> --See Below
        <nominal>0</nominal>
        <lifetime>3600</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0"/>
        <category name="clothes"/> --See Below
        <tag name="shelves"/>
        <usage name="Farm"/>
        <usage name="Town"/>
        <usage name="Village"/>
    </type>

    <type name="Example5"> --See Below
        <nominal>0</nominal>
        <lifetime>3600</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0"/>
        <category name="vehicles"/> --See Below
        <tag name="shelves"/>
        <usage name="Farm"/>
        <usage name="Town"/>
        <usage name="Village"/>
    </type>

    <type name="Example6"> --See Below Example of a type without a category getting filtered into the vehicles category in your trader config
        <nominal>0</nominal>
        <lifetime>3600</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0"/>
    </type>
</types>


--End of Types.xml --
 ```
 
 
 
 Output:
 
 
 
 ```
 --Start of Example TraderConfig.txt --
<CurrencyName> #tm_ruble
	<Currency> MoneyRuble1, 	1
	<Currency> MoneyRuble5, 	5
	<Currency> MoneyRuble10, 	10
	<Currency> MoneyRuble25, 	25
	<Currency> MoneyRuble50, 	50
	<Currency> MoneyRuble100, 	100


<Trader> Consume Trader
	<Category> Food
		Example,                                                            *,			1,			-1


<Trader> Misc Trader
	<Category> Containers
		Example1,                                                           *,			1,			-1

	<Category> Tools
		Example2,                                                           *,			1,			-1

	<Category> Viking

	<Category> Bbp

	<Category> Msp

	<Category> Mass

	<Category> Cp

	<Category> Mung


<Trader> Weapon Trader
	<Category> Weapons
		Example3,                                                           *,			1,			-1

	<Category> Explosives
		Example4,                                                           *,			1,			-1


<Trader> Clothing Trader
	<Category> Clothes
		Example5,                                                           *,			1,			-1


<Trader> Weapon Supplies Trader

<Trader> Vehicles Trader
	<Category> Vehiclesparts

	<Category> Vehicles
		Example5,                                                           *,			1,			-1
		Example6,                                                           V,			1,			-1
    
    
--End of TraderConfig.txt--
```
