# Github-profile-name-writer
###Write you name using the github commits and make your profile awesome. :D###
###LIKE THIS###
![Image of Ironman on github Profile](https://github.com/ironmaniiith/Github-profile-name-writer/blob/master/extras/ironmanGithub.jpg)

####If you don't enjoy reading, then just follow this and enjoy. :D

1.	Make a new repo (say testRepo)
2.	Run the file run.sh, it will ask you the information like username and id, enter it.
3.	You will obtain	a file runThis.sh, just copy that file in your cloned version of testRepo and run it, that's all...


For other related queries refer this

#### I want my name in darker color, what to do.? ####
* Just increase the number of commits when asked for while running the script run.sh


#### How to select date from which I want to start writing my name####
* That's simple, go to you profile page and select a base block from which you want to start writing your name, just inspect element it, you will see a value for data-date, this is it.

The first quantity is year, second is month and third is date, just add these info when you run the script run.sh

For help, here are two screenshots

1. Base date (Your name will appear above this date's level)
![Image of Base Date](https://github.com/ironmaniiith/Github-profile-name-writer/blob/master/extras/baseDate.jpg)
2. Inspect Element to find date.
![Image of Inspect Date](https://github.com/ironmaniiith/Github-profile-name-writer/blob/master/extras/inspectDate.jpg)


#### What if I want to change the pattern of some alphabets.####
* Now that's simple, go to the components folder, you will find a file named alphabets, just draw your pattern in that file, run bash parse.sh and that's it, your final output is in finalIndexing.txt, just replace all this obtained value of variables and arrays in the file main.py (replacing the old one). Now what are you waiting for, go and run your newly customized main.py. ;-)


#### What about numbers.?####
* I'll add them soon, but you know what, you can also fork the repository, go give it a shot. :D


#### Is this a useful thing..?####
* No not at all.. hahhahahahahaha. :D, it's just for fun and for making your github profile awesome, go see this link -> https://github.com/ironmaniiith

#### If you are in college and your college don't allow ssh to github, follow this####
* Suppose you username is 'ironman' and password is 'blablapassword'
	
	Just run this in you local copy of the repository

	git remote rm origin

	git remote add origin "https://ironman:blablapassword@github.com/ironman/testRepo.git" (where testRepo is the name of you repository in which your commits will be going)
	
	Now just run the final script runThis.sh, it won't ask for the password

#### What more.?####
* Well dude, I'm not a poet or essay writer, so unfortunately you won't find anything more. ;-)

Any suggestions are always welcomed.

Don't forget to star the repo if you like it...

Ironmaniiith

https://github.com/ironmaniiith