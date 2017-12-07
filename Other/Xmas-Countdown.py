import sys
import datetime
import time
from pushbullet import Pushbullet
import random

api_key = open('/home/pi/APIConfigs/Pushbulletkey.config', 'r').read() #read Pushbullet Key from /home/pi/Pushbulletkey.config file
api_key = api_key.replace("\n", "") #Remove Whitespace
#print api_key
pb = Pushbullet(api_key) 

jokes = ['What does Santa suffer from if he gets stuck in a chimney? Claustrophobia!', 'Why does Santa have three gardens? So he can ho ho ho!', 'Why did Santas helper see the doctor? Because he had a low elf esteem!','What kind of motorbike does Santa ride? A Holly Davidson!','What do you call a cat in the desert? Sandy Claws!','Who delivers presents to cats? Santa Paws!','What do you call a dog who works for Santa? Santa Paws!','What do you call Father Christmas in the beach? Sandy Clause!','What do you get if you cross Santa with a detective? Santa Clues!','What did the sea Say to Santa? Nothing! It just waved!','What does Santa do with fat elves? He sends them to an Elf Farm!','What do you get if you cross Santa with a duck? A Christmas Quacker!','Who delivers presents to baby sharks at Christmas? Santa Jaws','What says Oh Oh Oh? Santa walking backwards!','What goes Ho Ho Whoosh, Ho Ho Whoosh? Santa going through a revolving door!','What is Santas favorite place to deliver presents? Idaho-ho-ho!','Why does Santa go down the chimney on Christmas Eve? Because it soots him!','Who is Santas favorite singer? Elf-is Presley!','What do you call Santas little helpers? Subordinate clauses!','What do Santas little helpers learn at school? The elf-abet!','What did Santa say to the smoker? Please dont smoke, its bad for my elf!','Where does Santa go when hes sick? To the elf center!','What do you call a bankrupt Santa? Saint Nickel-less!','Where do elves go to dance? Christmas Balls!','What do elves eat for breakfast? Frosted Flakes!','What do you call a frozen elf hanging from the ceiling? An elfcicle!','Who is the king of Santas rock and roll helpers? Elfis! (Thank you, thank you very much!)','What type of Shoes does Santa wear when he travels on a train? Platforms!','What do you get if Santa goes down the chimney when a fire is lit? Krisp Kringle!','Who is Santa Claus married to? Mary Christmas!','How long do a reindeers legs have to be? Long enough so they can touch the ground!','What do reindeer hang on their Christmas trees? Horn-aments!','Why are Christmas trees so bad at sewing? They always drop their needles!','Who is the Music Elfs favorite reindeer? Dancer!','Whats worse than Rudolph with a runny nose? Frosty the snowman with a hot flush!','Did Rudolph go to school? No. He was Elf-taught!','Why did the Rudolph cross the road? Because he was tied to the chicken!','What do you call Rudolph with lots of snow in his ears? Anything you want, he cant hear you!', 'What did Santa ask Rudolph about the weather? Is it going to rain dear?!', 'Why did the turkey cross the road? Because he wasnt chicken!', 'Why did the turkey cross the road? Because it was the chickens day off!', 'What happened to the turkey at Christmas? It got gobbled!', 'Why did the turkey join the band? Because it had the drumsticks!', 'What do you get when you cross a snowman with a vampire? Frostbite!', 'What do snowmen wear on their heads? Ice caps!', 'How do snowmen get around? They ride an icicle','What do snowmen eat for lunch? Iceburgers!','When is a boat just like snow? When its adrift!','What song do you sing at a snowmans birthday party? Freeze a jolly good fellow!','How does Good King Wenceslas like his pizzas? One thats deep pan, crisp and even!','Who hides in the bakery at Christmas? A mince spy!','What did Adam say on the day before Christmas? Its Christmas, Eve!', 'How does Christmas Day end? With the letter Y!','How many letters are in the angelic alphabet? The Christmas alphabet has no EL!','What carol is heard in the desert? O camel ye faithful!','What do angry mice send to each other at Christmas? Cross Mouse Cards!','What is the best xmas present in the world? A broken drum, you just cant beat it!','How do sheep in Mexico say Merry Christmas? Fleece Navidad!','What are the best Christmas sweaters made from? Fleece Navidad!','How did Scrooge with the football game? The ghost of Christmas passed!','What athlete is warmest in winter? A long jumper!','What do you get if you eat Christmas decorations? Tinsilitis!','What is the worst disease that you get at Christmas? Excemas!','Whats green, covered in tinsel and goes ribbet ribbet? A Mistle-toad!','Whats the most popular Christmas wine? I dont like Brussels sprouts!','Why do ghosts live in the fridge? Because its cool!','What happened to the man who stole an Advent Calendar? He got 25 days!','What did the beaver say to the Christmas Tree? Nice gnawing you!','Why are Christmas Trees like bad knitters? They keep loosing their needles!','What do you get if you cross a Christmas tree with an apple? A pineapple!','What do crackers, fruitcake and nuts remind me of? You!','Whats the best thing to put into a Christmas Cake? Your teeth!','What do you get if you cross a bell with a skunk? Jingle Smells!','Where would you find chili beans? At the north pole!','Why is everyone so thirsty at the north pole? No well, no well!','Why dont penguins fly? Because theyre not tall enough to be pilots!','What do sheep say at Christmas? Wool-tide Bleatings! or A Merry Christmas to Ewe!','What do you call a bunch of chess players bragging about their games in a hotel lobby? Chess nuts boasting in an open foyer!','Whats green, covered in tinsel and goes ribbet ribbet? Mistle-toad!','Which football team did the baby Jesus support? Manger-ster United!','How did Mary & Joseph know how much Jesus weighted when he was born? There was a weight in a manger!','What do you call a three legged donkey? A wonky donkey!','Whats the name of the one horse in "Jingle Bells"? Bob. (Bells on Bobs tail ring!)','What is the most competitive season? Win-ter!','Children: This turkey tastes like an old sofa! Mom: Well, you asked for something with plenty of stuffing!','Knock Knock! Whos there? Pudding Pudding who? Pudding in your face!','Knock Knock Whos there? Snow Snow who? Snow business like show business!','Knock knock! Whos there? Hanna Hanna who? Hanna partridge in a pear tree!','Knock knock! Whos there? Holly Holly who? Holly-days are here again!','Knock knock! Whos there? Harold Harold who? Hark the Harold Angels Sing!','Santa went to the Doctors with a problem. Doctor: What seems to be the problem? Santa: I seem to have a mince pie stuck up my bottom! Doctor: Well your in luck because Ive got just the cream for that!','Two snowmen in a field, one turned to the other and said I dont know about you but I can smell carrots.!','Did you know that Santas not allowed to go down chimneys this year? It was declared unsafe by the Elf and Safety Commission.','There were two biscuits, on a plate, all ready for Santa to eat. One biscuit decided to go and hide in the biscuit tin as it didnt want to get eaten. As it was going to the kitchen, Santa came in and stood on it and all the other biscuit could say was Crumbs!.']
randjoke = random.choice(jokes) #Choose random Joke

dt = datetime.datetime.now()
month = datetime.date.today().strftime("%B") #Month e.g. Dec
#print month
daynumber = datetime.datetime.now().day 

mon = 12 - dt.month
Xday = 24 - dt.day
NYday = 31 -dt.day
hr = 23 - dt.hour
mn = 60 - dt.minute
sec = 60 - dt.second

if month == "December" and daynumber < 25:
	time2wait = random.randint(1,37600) #random time in next 10 hours
	print time2wait
	time.sleep(time2wait)
	s = repr(Xday) + ' days ' + repr(hr) + ' hours ' + repr(mn) + ' mins ' + repr(sec) + ' secs' + ' until Christmas'
	#print s
	push = pb.push_note(s, randjoke)
elif month == "December" and daynumber == 25:
	s = "ITS CHRISTMAS!!!!!!!!!!"
	b = "Go and un-wrap some presents!!!"
	push = pb.push_note(s, b)
elif month == "December" and daynumber > 25:
	s = repr(NYday) + ' days ' + repr(hr) + ' hours ' + repr(mn) + ' mins ' + repr(sec) + ' secs' + ' until New Year!'
	b = ""
	push = pb.push_note(s, s)
else:
	print ""
