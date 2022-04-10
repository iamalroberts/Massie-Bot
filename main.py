import os
import discord
import re
from replit import db
from keep_alive import keep_alive

def initializeDB():
  if len(db.keys())==0:
    db["Mad Hatter#0827"] = [0, 0, 0, 0, 0, 0, 0, 0]
    db["iamalroberts#9609"] = [0, 0, 0, 0, 0, 0, 0, 0]
    db["Disco Lemonade#8713"] = [0, 0, 0, 0, 0, 0, 0, 0]
    db["SpencerDGuth#2200"] = [0, 0, 0, 0, 0, 0, 0, 0]
    db["ZeOneEyedBandit#5145"] = [0, 0, 0, 0, 0, 0, 0, 0]
    db["Torahassup#1120"] = [0, 0, 0, 0, 0, 0, 0, 0]
    db["Meviah#0230"] = [0, 0, 0, 0, 0, 0, 0, 0]
    db["jakehayes#8723"] = [0, 0, 0, 0, 0, 0, 0, 0]
    print('DB initialized')
  else:
    print('DB already exists')
    return
 #These numbers are only needed for first year. They won't match going forward because of adding and subtracting points through testing. 
def initializeDBOnTime():
  db["Mad Hatter#0827"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["iamalroberts#9609"] = [0, 3, 15, 15, 8, 0, 25, 0]
  db["Disco Lemonade#8713"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["SpencerDGuth#2200"] = [5, 0, 0, 0, 0, 0, 0, 5]
  db["ZeOneEyedBandit#5145"] = [0, 0, 2, 0, 5, 3, 1, 0]
  db["Torahassup#1120"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["Meviah#0230"] = [3, 0, 0, 0, 10, 0, 0, 0]
  db["jakehayes#8723"] = [0, 0, 0, 0, 10, 5, 0, 8]
  print('DB initialized one time')
  return 'DB initialized one time'
  
def resetDbValuesToZeroes():
  db["Mad Hatter#0827"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["iamalroberts#9609"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["Disco Lemonade#8713"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["SpencerDGuth#2200"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["ZeOneEyedBandit#5145"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["Torahassup#1120"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["Meviah#0230"] = [0, 0, 0, 0, 0, 0, 0, 0]
  db["jakehayes#8723"] = [0, 0, 0, 0, 0, 0, 0, 0]
  print('DB fully reset')
  return "DB fully reset"

#TODO figure out how to format this properly


def printUserTotals():
  strToPrint=""
  hdr = "{:<25s}{:<12s}{:>6s}{:>6s}"
  #print(hdr.format("User","House", "Given","Taken" ))
  header = hdr.format("User","House", "Given","Taken" )
  #print("-----------------------------------------------------")
  dashes = "-----------------------------------------------------"
  txt = "{:<25s}{:<12s}{:>6d}{:>6d}"
  strToPrint+=header + "\n"+ dashes+"\n"
  for x in range(len(db.keys())):
    currentKey = list(sorted(db.keys(), key=lambda x:x.lower()))[x]
    #print(txt.format(currentKey,"Gryffindor",db[currentKey][0], db[currentKey][1]))
    Gs = txt.format(currentKey,"Gryffindor",db[currentKey][0], db[currentKey][1])
    #print(txt.format("","HufflePuff",db[currentKey][2], db[currentKey][3]))
    Hs = txt.format(currentKey,"HufflePuff",db[currentKey][2], db[currentKey][3])
    #print(txt.format("","Ravenclaw",db[currentKey][4],  db[currentKey][5]))
    Rs = txt.format(currentKey,"Ravenclaw",db[currentKey][4],  db[currentKey][5])
    #print(txt.format("","Slytherin", db[currentKey][6],  db[currentKey][7]))
    Ss = txt.format(currentKey,"Slytherin", db[currentKey][6],  db[currentKey][7])
    #print()
    strToPrint+=Gs+"\n"+Hs+"\n"+Rs+"\n"+Ss+"\n\n"
  return strToPrint





def getValues(txt):
  house = txt.split(' @')[2].split()[0]
  x = txt.split('[',1)[0]
  y= x.split()
  #print(y)
  if(y[0] == '@Mad' or y[0] == '@Disco'):
      sender = y[0]+" " + y[1]
      action = y[2]
      points = y[3]
      if(y[6]== '@Mad' or y[6] == '@Disco'):
          receiver = y[6] + " " + y[7]
      else:
          receiver = y[6]
  else:
      sender = y[0]
      action = y[1]
      points = y[2]
      if(y[5]== '@Mad' or y[5] == '@Disco'):
          receiver = y[5] + " " + y[6]
      else:
          receiver = y[5]
  return sender.strip('@'),action,points,receiver.strip('@'),house
  

def getNewPointTotals(houseName, action, oldList, points):
	if(houseName == 'Gryffndor'): #intentional misspelling
		if(action == 'awarded'):
			oldList[0]+=points
		else:
			oldList[1]-=points
	if(houseName == 'Hufflepuff'):
		if(action == 'awarded'):
			oldList[2]+=points
		else:
			oldList[3]-=points
	if(houseName == 'Ravenclaw'):
		if(action == 'awarded'):
			oldList[4]+=points
		else:
			oldList[5]-=points
	if(houseName == 'Slytherin'):
		if(action == 'awarded'):
			oldList[6]+=points
		else:
			oldList[7]-=points
	return oldList 



client = discord.Client()
initializeDB()

pattern = re.compile(".*(deducted|awarded).*points (from|to) @.*")
patternSingular = re.compile(".*(deducted|awarded).*point (from|to) @.*")
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  clientID = client.user.id
  botMention = f'<@!{clientID}>' #Because we type in discord the bots nickname -__-
  botMentionRealName = f'<@{clientID}>' #discord Username
  
  if message.author == client.user:
    return
#TODO add another if that looks for a comma to filter out points given to a house
# or handle it. 
  if pattern.match(message.content) or patternSingular.match(message.content) :
    sender1,action1,points1,receiver1,house1 = getValues(message.content)
    print(sender1)
    print(action1)
    print(points1)
    print(receiver1)
    print(house1)
    print(getNewPointTotals(house1, action1, db[sender1], int(points1)))
  
  if message.content.startswith(botMention) or message.content.startswith(botMentionRealName):
    #print(message.content)
    if(len(message.content.split("> "))>1):
      inputCommand = message.content.split("> ")[1].lower()
      if inputCommand == 'audit':
        await message.channel.send(printUserTotals())
      elif inputCommand == 'reset':
        await message.channel.send(resetDbValuesToZeroes())
      elif inputCommand == 'restore original dataset':
        await message.channel.send(initializeDBOnTime())
      elif inputCommand == 'help':
        await message.channel.send("Pathetic.")
      else:
        await message.channel.send("Um..what?")
    else:
        await message.channel.send("That's my name. Don't wear it out.")
keep_alive()
client.run(os.environ['TOKEN'])