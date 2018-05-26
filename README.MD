FrostCraft Resource Pack
=======
![alt tag](https://raw.githubusercontent.com/FrostMiser/FrostCraft-Resource-Pack/master/pack.png)

This is a custom resource pack for mc.frostcraft.com. Find more information about FrostCraft on http://frostcraft.com

## Notes on Item Models
This applies to files in \models\item\

\_gold\_hoe is to be used if we ever switch to using custom models for wands.
Many of the wands need to have the uv's switch up slightly to avoid small texture issues.
4.0 > 3.99 and such.

## Notes on Wand Models
This applies to files in models\wand\

* Only Wand files should be in this folder.

* A Wand files name format is
 * dmgvaluenumber\_wand\_name-type
 * E.G. 5\_wand\_mushroom-model.json or \_wand\_mushroom-setup.json

### Calculating Damage Value
To get the override damage value for the model:

1. Divide by 1/32 (or the number of damage values the item has)
2. Take that number and then multiply it by what slot you want.
3. Eg. 1/32 = 0.03125, 0.03125 * 5 = 0.15625

The \_wand\_display file is a template, for what should be used for the display tags at the bottom of the model files.



## Todo / Ideas
---------------------------------
###Additional Wands
* Magic Wand | Black with white Top 
* Mushroom Wand | Rough handle with red white  mushroom top
* Candy Cane Wand | Candy cane
* Cane Wand | Old wooden cane 
* Magic Stick | Rough Stick with 1-2 Leafs at the end

