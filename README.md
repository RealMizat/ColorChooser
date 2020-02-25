'''----------------------------------___________ ColorChooser __________----------------------------------


This Project isn't really a project, or at least any main files or builds. This is just going to be random scipt from Tkinter apps, probably 
most posted before it is anywhere near complete. I simply see a need to post it for some reason, weather it is a good example of how to use 
a certain dialog (colorchooser ect.), or maybe just a really random way of doing something and may need that code in the future. At least as
of typing this (Febuary, 2020) the two files uploaded are for those reasons. I will post more serious projects once I have something that can
at least be used by someone (an actual program not just code snipits). As of now things I post here will be realated to UI/GUI builds, I will
post a little description below on each and why I posted them.

The first upload is just a truly bare bones tkinter script, that has the ColorChooser Dialog. It is very hard to find examples of the 
Color Chooser and how it works, or working examples. That is the main reason it is posted, it is probably the most simple way to add
some functionality to Tkinter ColorChooser, besides just printing the hex color code. The code will show how to change the color of a button
but can be used as a guide or outline/reference to a simple GUI or a window/frame of a more complex GUI. It does use grid, and also the text
function, label function and button function, as well as title. I think it is a good example for begginers to look at and use as a base for
their first project, or use of ColorChooser and the askcolor function.



The second upload... oh man... Well you see when you have something that you can barley understand yourself, and litterally did everything
in a much harder way than needed, well thats basically the majority of that code. That's not all, I made it more crazy by pretty much copy
and pasteing the colorchooser code I uploaded first, witch is coded in a way different manner. So, what I did was spend a little time trying
to get the two to work with minimal changes, and that's what I got. I use the word "work" lightly. I however would love to actually implemnt 
the two together, in a sleek, functional way. If you want to run that code, save it in the same file/directory as images that are .GIF, and 
label them as the buttons/.GIF code says. button1.gif button2.gif ... quit-button.gif and a backround ect. What that code does is creates a 
frame with labels that are the images mentioned. Then the images/labels can be pressed, currently they just show that they have been clicked
in the IDE. I had to change the ColorChooser code to Pack and at the bottom where the main loop is i simply added 'and root' for running
the mainloop, yes very intuitive lol. Change that or delete it, and delete everythig that also is in the ColorChooser application, also
go down towards the bottom, and you will see one line with a (False) argument, and it is about the sizing and windows, change that to True
to get full screen, no top exit/minimize bar, basically makes it like a DVD Player menu just needs functions added to the Button Presses,
however could look amazing with the correct images and colors as you only see images, so it is a way of having Tkinter look as customized as
possible. Goodluck understanding the code, if you can feel free to use it, also just go ahead and comment or delete out the else: statement
that has the colorchooser option, only leaving the if: statement, that will basically fix all the changes I made before haxing it up for
the other script to work. You should also be able to change locations, or even change the geometry manager, I will probably create a simple
version that uses grid, also uses Functions/Objects and CLass' completely different. If you think the use/format for the entire class is good
then good for you, I hate it personally and don't know why it exists, especially when I mashed in some random other code, I was lol'ing
when the color chooser actually showed up, I wont lie. 




______________________________________________________________________________________
:::,''.:::::,:""""``::::::::-----\\ ::!===============\\:::|/----------------77:::::::|
::/||\`\::://///\\ \:::::::/ |||||\\::L____ -    -____7::::|L____    _______// :::::::|
:////:\ \::////^|\\ \:::::/ ||/^\||\\:`...|\|   |/|-----`::::::::|\  /| ------`:::::::|
////:::\ \:///:::\\\ \:::/ ||/___\|||\::::|\|   |/|::::::::::::::|\  /| |:::::::::::::|
////::::\ | |:::::\\\ \_/ |||||||||\| ||::|/|   |\|::::::::::::::|/  \| |:::::::::::::|
////:::::::::::::::\\\  V|||:::::|||| ||::|/|   |\|::::::::::::::|/  \| |:::::::::::::|
////::::::::::::::::\\\ /||::::::|||| | |:|/[   |\|::::::::::::::|/  \| |:::::::::::::|
=======================================================================================

Bare bones use of the ColorChooser dialog in Tkinter. It was difficult to find any examples of the Color Chooser actually changing the color of anything, here is a simple GUI where it will change the color of a Button.
