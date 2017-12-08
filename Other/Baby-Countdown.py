from datetime import *
from pushbullet import Pushbullet
import random

###################################
#Pushbullet Variables 
###################################
api_key = open('/home/pi/APIConfigs/Pushbulletkey.config', 'r').read() #read$
api_key = api_key.replace("\n", "") #Remove Whitespace
#print api_key
pb = Pushbullet(api_key) 

#Dates
today = date.today()
DDay = date(2018,06,17)

#Interjections

interjections = ['AH','AINT THAT SOMETHING','ALL RIGHT','awesome','bada bing','BEAUTIFUL','BINGO','BLESS THE LORD','booya','Boo-yah ','BOY','BOY AM I LUCKY','BOY OH BEANS','boy oh boy','BOY OH BOY','BOYEE','BY GOLLY','BY THE GOLLIES','CHEERS','CHRISTMAS COMIN AGAIN','CONGRATULATIONS','cowabunga','CRAZY','Dang! ','DEAR ME','DELIGHTFUL','DO LORDY-MAMMA','DONT TELL ME','Eep','ELDORADO','Er..','EUREKA','EXCELLENT','fantastic','FANTASTIC','FAR OUT','FINE','GEE','Gee ','GEE GOSH DARN','GEE THATS SURE NICE','gee whiz','GEE WHIZ','GEE, THATS WONDERFUL','GEEEE-HAWW','GLORY','GLORY BE','GLORY FOR ME','GLORY HALLELUJAH','GOD BLESS EM','GODLEE','GOL','GOL DANG, THATS NICE','GOLLY','Golly','golly ','GOLLY BUSTER','GOLLY DARN','GOLLY MOSES','golly willikers','GOOD','GOOD FOR ME','GOOD GOLLY','good golly ','GOOD HEAVENS','GOOD SHOT','GOODNESS GODNESS AGNES','GOODY','GOODY FOR ME','GOODY GUMDROP','GOODY-GOODY','GOODY-GOODY GUMDROPS','gosh','GOSH','Gosh ','GOT SOME HAPPY NEWS','GRAND','GREAT','GREAT DAY IN THE MORNING','Gulp ','HALLELUJAH','Hamana-hamana ','HAPPY DAY','HAPPY DAYS','HAPPY HOORAY','HE MIGHT SQUEAL','HEAVENS TO BETSY','HELL YEAH MAN, LETS GO AGAIN','HELLS FIRE','HEY','HEY, GREAT','HIP-HIP-HOORAY','HIP-HURRAH, BOYS','HOKEY MAN','HOLY COW','HOLY GEE','HOLY MACKEREL','holy mackerel ','Holy Mackrel','holy moley ','holy Moses ','HOLY SCUD CATFISH','holy smokes','HOO-HEE','HOORAH','HOORAW','HOORAY','hooray ','HOORAY FOR OUR SIDE','HOO-WEE','HORRAY','HOT DAMN','HOT DIGGETY','HOT DIGGETY DAMN','HOT DIGGETY DOG','HOT DIKKETY','HOT DIKKETY HOT','HOT DOG','HOT ZIGGETY','HOW ABOUT THAT','HOW BOUT THAT','HOW NICE','HOW WONDERFUL','HURRAH','Hurrah ','I AM SO GLAD','I CANT BELIEVE IT','I DID','I DONT BELIEVE IT','I LIKE THIS','I RUN INTO A GOLD MINE','I THANKS THE LORD','ILL BE','ILL BE DAMNED','ILL BE DOGGONED','IM GLAD OF IT','IM HAPPY AS A DEAD PIG IN THE SUNSHINE','IM THRILLED TO DEATH','ISNT THAT NICE','ISNT THAT SOMETHING','ITS GREAT','JEEMINY CHRISTMAS','jeez','JESUS CHRIST','JIMINY CRICKETS','JOY','JOY AND ECSTASY','JOY, JOY','jumpin jiminy','JUMPING JEHOSAPHAT','JUMPING JELLY-BEANS','KONTAKA','LOOK WHAT WE GOT','lordy lordy','LOVELY','mama mia','MAN ALIVE','MAN, IM HAVING A GOOD TIME','MAN, MAN','my goodness','MY GOODNESS','MY OH MY','NEAT','NO FOOLIN','no way Jose','NOW YOURE TALKING','NR','OH','oh boy','OH BOY','OH BOYS','OH BROTHER','OH GEE','OH GLORY','OH GOOD','OH GOODY','OH GOSH','OH GREAT','OH HAPPINESS','OH HELL','OH HOW WONDERFUL','OH IM SO GLAD','OH ISNT IT NICE','OH JOY','OH JOY, OH BOY, WHERE DO WE GO FROM HERE','OH LOOK','OH LOOK WHAT I HAVE','OH MERCY','oh my','OH MY','oh my goodness','OH MY GOODNESS','oh my gosh','OH MY GOSH','OH MY GRACIOUS','OH THATS GREAT','OH WOW','OH YEAH','OLE','Ole','OOH','OOH GOODY','OOH-WEE','OO-PEE','OUT OF SIGHT','PEACHY PURPLE','PRAISE BE','Psst ','RAW','REALLY','Rock and Roll!','Sheesh','SHIP AHOY','super','swell','SWELL','Ta-da ','TERRIFIC','THANK GOD','THANK GOD I GET A GOOD ENJOY','THANK GOODNESS','THANK THE LORD','THANK YOU','THANK YOU SO MUCH','THANK YOU, JESUS','THAT SURE WAS A HUMDINGER','THAT-A-BABY','THATS ALL RIGHT','THATS GREAT','THATS JUST WHAT I NEEDED','THATS NEAT','THATS SWELL','THATS THE MOST','THATS WONDERFUL','THIS IS GREAT','THIS IS THE BERRIES','THIS MUST BE MY DAY','THREE CHEERS','TREMENDOUS','Uh','Ummm','Va-va-voom ','WAHOO','WELL ILL BE CUSSED','WELL ILL BE DAMNED','WELL ILL BE SWITCHED','WHAT A SURPRISE','WHAT DO YOU KNOW','WHEE','Whee!','WHEW','Whoa ','WHOD HAVE THOUGHT IT','WHOO BOY','WHOOP','whoop de doo','WHOOPEE','Whoopee!','WHOOPS','WHOO WEE','WONDERFUL','WOO','Woo Hoo','WOO-EE','woo-hoo','WOW','Wow','WOW-EE','WOWIE','WTF!','yabba dabba do','yadda yadda','YA-HO','YAHOO','Yay','YE GODS','YEA','YEA MAN','YEAH','YEAH MAN','YEEE-AH','Yee-haw','YES','Yikes ','yippee','YIPPEE','Yippee','Yo-ho-ho ','YOORO','Yoowza','YOU DONT MEAN IT','YOURE KIDDING','YOURE NOT KIDDING, ARE YOU','YOW','ZIGGETY-DAMN','Zoinks ','Zowie']

ranint = random.choice(interjections) #Choose random interjections

diff = DDay - today
diffdays = diff.days

if diffdays > 0:
	print "%s!! There are only %s days until Baby Sage!" % (ranint, diff.days)
  #s = "%s!! There are only %s days until Baby Sage!" % (ranint, diff.days)
	#push = pb.push_note(s, ranint)
else:
	print "%s! Baby Sage over due!" % (ranint)
  
