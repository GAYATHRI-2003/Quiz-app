p=0
q=0
r=0
flag =0
def score(a,b):
	global p
	global q
	global r
	if (a==1):
		if (b==1):
			p=p+2
		else:
			p=p-1
	elif (a==2):
		if (b==1):
		  	q=q+6
		else:
			q=q-3
	elif (a==3):
		if (b==1):
		  	r=r+10
		else:
			r=r-5
def display():
	global p
	global q
	global r
	global flag 
	flag=1
	print('---------------------------------------------')
	print('---------------------------------------------')
	print('        SCORE  BOARD')
	print('---------------------------------------------')
	print('YOUR SCORE IN LEVEL 1:',p)
	print('YOUR SCORE IN LEVEL 2:',q)
	print('YOUR SCORE IN LEVEL 3:',r)
	print('---------------------------------------------')
	print('TOTAL SCORE               :',p+q+r)
	print('---------------------------------------------')
	print('---------------------------------------------')
	
def sports():
 print('\nLEVEL 1!!')
 print('\nQUIZ :1')
 print("How many number of  rings are present in the olympic flag?")
 print("A. 4 \nB. 6 \nC. 5 \nD. 7")
 ans=input("Enter your answer:").lower()
 if ans == 'c. 5' or ans == 'c' or ans == '5' or ans == 'c.5':	     
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("The correct answer is: C. 5")
   score(1,0)
 print('\nQUIZ :2')
 print("Who holds the record of being the first Indian in history to win an Asian gold medal in javelin throw(men's event)?")
 print("A. Neeraj Chopra \nB. Shivpal Singh \nC. Davinder singh Kang \nD. Gurtej Singh")
 ans=input("Enter your answer with space:").lower()
 if ans == 'a. neeraj chopra' or ans == 'a' or ans == 'neeraj chopra' or ans == 'a.neeraj chopra' :	     
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("The correct answer is: A. Neeraj chopra")
   score(1,0)
 print('\nQUIZ :3')
 print(" What is the nickname of Sachin Tendulkar?")
 print("A. The Little Genius \nB. The Little Master\nC. The God of Cricket\nD. Super Star of Cricket")
 ans=input("Enter your answer with space:").lower()
 if ans == 'b.the little master' or ans == 'b' or ans == 'the little master' or ans == 'b. the little master' :	     
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("The correct answer is: B. The Little Master")
   score(1,0)
 print('\nQUIZ :4')
 print("How many players are on a baseball team?")
 print("A. 10 \nB. 8 \nC. 9 \nD. 11")
 ans=input("Enter your answer:").lower()
 if ans == 'c.9' or ans == 'c' or ans == '9' or ans == 'c. 9' :	     
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("The correct answer is: C. 9")
   score(1,0)
 print('\nQUIZ :5')
 print("What does NBA stands for?")
 print("A. National Basketball Assembly \nB. Nation's Basketball Association \nC. Nation's Basketball Assembly \nD. National  Basketball Association")
 ans=input("Enter your answer:").lower()
 if ans == 'd. national basketball association' or ans == 'd' or ans == 'national basketball association ' or ans == 'd.national basketball association':	     
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("The correct answer is: D. National Basketball Association")
   score(1,0)
   
 
 print("\nDo you want to go next level!!")
 print("\nEnter 'YES' to go next level or 'NO' to exit:")
 opt=input("Enter your choice:").lower()
 if opt == 'yes':
  print('\nLEVEl 2!!')
  print('\nQUIZ :1')
  print("Who is the first batsman to cross 10,000 runs in tests ?")
  print("A. Sunil Gavaskar \nB. Sachin Tendulkar\nC. Allan Border\nD. Brian Lara")
  ans=input("Enter your answer with space:").  lower()
  if ans == 'a.sunil gavaskar' or ans == 'a' or ans == 'sunil gavaskar' or ans == 'a. sunil gavaskar' :	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("The correct answer is: A. Sunil Gavaskar")
   score(2,0)
  print('\nQUIZ :2')
  print("What sport is dubbed the ‘king of sports’ ?")
  print("A. Kabadi \nB. Soccer\nC. Hockey \nD. Badmitton")
  ans=input("Enter your answer:").  lower()
  if ans == 'b.soccer' or ans == 'b' or ans == 'soccer' or ans == 'b. soccer':	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("The correct answer is: B. Soccer")
   score(2,0)
  print('\nQUIZ :3')
  print("Who won the first ever Cricket World Cup in 1975 ?")
  print("A. Australia\nB. England \nC. India\nD.West Indies")
  ans=input("Enter your answer with space:").  lower()
  if ans == 'd. west indies' or ans == 'd' or ans == 'west indies' or ans == 'd.west indies':	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("The correct answer is: D. West Indies")
   score(2,0)
  print('\nQUIZ :4')
  print(" Who set a new record for most number of sixes by an individual in an ODI innings?")
  print("A. Virat Kholi\nB. Sachin Tendulkar\nC. Eoin Morgan\nD. Chris Gayle")
  ans=input("Enter your answer with space:").  lower()
  if ans == 'c. eoin morgan' or ans == 'c' or ans == 'eoin morgan' or ans == 'c.eoin morgan':	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("The correct answer is: C. Eoin Morgan")
   score(2,0)
  print('\nQUIZ :5')
  print(" In Kho-Kho , the players occupying the squares are known as?")
  print("A. Lobby\nB. Raiders\nC. Chasers\nD. Chukke")
  ans=input("Enter your answer with space:").  lower()
  if ans == 'c. chasers' or ans == 'c' or ans == 'chasers' or ans == 'c.chasers':	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("The correct answer is: C. Chasers")
   score(2,0)
 else:
  display()
  

 global flag
 if flag ==0:
  print("\nDo you want to go next level!")
  print("\nEnter 'YES' to go next level or 'NO' to exit:")
  opt=input("Enter your choice:").lower()
  if opt == 'yes':
   print('\nLEVEl 3!!')
   print('\nQUIZ :1')
   print("Who bowled the fastest delivery ever of 100.2mph?")
   print("A. Brett Lee\nB. Shoaib Akhtar\nC. Shaun Tait\nD. Jeffrey Thompson")
   ans=input("Enter your answer with space:").  lower()
   if ans == 'b. shoaib akhtar' or ans == 'b' or ans == 'shoaib akhtar' or ans == 'b.shoaib akhtar ' :     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")
    print("The correct answer is: B. Shoaib Akhtar")
    score(3,0)
   print('\nQUIZ :2')
   print("What country has competed the most times in the summer Olympics without winning any medal at all?")
   print("A. Liechtenstein\nB. South Africa\nC. Philipiness\n D. Srilanka")
   ans=input("Enter your answer:").  lower()
   if ans == 'a. liechtenstein' or ans == 'a' or ans == 'liechtenstein' or ans == 'a.liechtenstein':	     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")
    print("The correct answer is: A. Liechtenstein")
    score(3,0)
   print('\nQUIZ :3')
   print("Which of the following Indian Sports Team is also known as “The Bhangra Boys?")
   print("A. Volley Ball\nB. Basket ball \nC. Cricket\nD.  Foot Ball")
   ans=input("Enter your answer with space:").  lower()
   if ans == 'd. foot ball' or ans == 'd' or ans == 'foot ball' or ans == 'd.foot ball':	     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")
    print("The correct answer is: D. Foot Ball")
    score(3,0)
   print('\nQUIZ :4')
   print("The World Military Cup organized by the International Military Sports Council (CISM) involves which among the following sports?")
   print("A. Volley Ball \nB. Cricket\nC. Foot Ball\nD. Basket Ball")
   ans=input("Enter your answer with space:").  lower()
   if ans == 'c. foot ball' or ans == 'c' or ans == 'foot ball' or ans == 'c.foot ball':	     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")    
    print("The correct answer is: C. Foot Ball")
    score(3,0)
   print('\nQUIZ :5')
   print("The ”Marquess of Queensberry rules” is a code of generally accepted rules in which of the following sports?")
   print(" A. Chess\nB. Boxing\n C. Hockey\n D. Tennis")
   ans=input("Enter your answer with space:").  lower()
   if ans == 'b.boxing' or ans == 'b' or ans == 'boxing' or ans == 'b. boxing':	     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")    
    print("The correct answer is: B. Boxing")
    score(3,0)
  else:
   display()
  print("Congratulations !! You completed all the questions!!")
  display()	
def general():
        print("\nLEVEL 1!!")
        print("\nQuiz:1")
        print("Who was the first Indian Women in space?")
        print("A. Kalpana Chawla\nB. Sunitha Williams\nC. Koneru Humpy\nD. None of the above")
        print("Enter your Answer")
        answer=input().lower()
        if(answer=="a" or answer=="a. kalpana chawla" or answer=="a.kalpana chawla" or answer=="kalpana chawla"):
          print("correct answer")
          score(1,1)
        else:
          print("wrong answer")
          print("Correct answer: A. Kalpana Chawla")
          score(1,0)
        print("\nQuiz:2")
        print("Who was the first Man to Climb Mount Everest Without Oxygen?")
        print("A. Junko Tabei\nB. Reinhold Messner\nC. Peter Habeler\nD. Phu Dorji")
        print("Enter your Answer")
        answer=input().lower()
        if(answer=="d" or answer=="d. phu dorji" or answer=="d.phu dorji" or answer=="phu dorji"):
          print("correct answer")
          score(1,1)
        else:
          print("wrong answer")
          print("Correct answer: D. Phu Dorji")
          score(1,0)
        print("\nQuiz:3")
        print("Who wrote the Indian National Anthem?")
        print("A. Bakim Chandra Chatterji\nB. Rabindranath Tagore\nC. Swami Vivekanand\nD. None of the above")
        print("Enter your Answer")
        answer=input().lower()
        if(answer=="b" or answer=="b. rabindranath tagore" or answer=="b.rabindranath tagore" or answer=="rabindranath tagore"):
          print("correct answer")
          score(1,1)
        else:
          print("wrong answer")
          print("Correct answer: B. Rabindranath Tagore")
          score(1,0)
        print("\nQuiz:4")
        print("Who was the first Indian Scientist to win a Nobel Prize?")
        print("A. CV Raman\nB. Amartya Sen\nC. Hargobind Khorana\nD. Subramanian Chrandrashekar")
        print("Enter your Answer")
        answer=input().lower()
        if(answer=="a" or answer=="a. cv raman" or answer=="a.cv raman" or answer=="cv raman"):
          print("correct answer")
          score(1,1)
        else:
          print("wrong answer")
          print("Correct answer: A. CV Raman")
          score(1,0)
        print("\nQuiz:5")
        print("Who was the first Indian to win the Booker Prize?")
        print("A. Dhan Gopal Mukerji\nB. Nirad C. Chaudhuri\nC. Arundhati Roy\nD. Aravind Adiga")
        print("Enter your Answer")
        answer=input().lower()
        if(answer=="c" or answer=="c. arundhati roy" or answer=="c.arundhati roy" or answer=="arundhati roy"):
          print("correct answer")
          score(1,1)
        else:
          print("wrong answer")
          print("Correct answer: C. Arundhati Roy")
          score(1,0)
        print("\nDo you want to go next level!!")
        print("\nEnter 'YES' to go next level or 'NO' to exit:")
        opt=input("Enter your choice:").lower()
        if opt == 'yes':
         print('\nLEVEl 2!!')    
         print("\nQuiz:1")
         print("How many string does a bass guitar usually have?")
         print("A. four\nB. five\nC. three\nD. six")
         print("Enter your Answer")
         answer=input().lower()
         if(answer=="a" or answer=="a. four" or answer=="a.four" or answer=="four"):
           print("correct answer")
           score(2,1)
         else:
           print("wrong answer")
           print("Correct answer: A. four")
           score(2,0)
         print("\nQuiz:2")
         print("Which continent has the biggest population?")
         print("A. Africa\nB. Europe\nC. Asia\nD. Antarctica")
         print("Enter your Answer")
         answer=input().lower()
         if(answer=="c" or answer=="c. asia" or answer=="c.asia" or answer=="asia"):
          print("correct answer")
          score(2,1)
         else:
          print("wrong answer")
          print("Correct answer: C. Asia")
          score(2,0)
         print("\nQuiz:3")
         print("Who developed the theory of relativity?")
         print("A. Issac Newton\nB. Albert Einstein\nC. Charles Darwin\nD. Marie Curie")
         print("Enter your Answer")
         answer=input().lower()
         if(answer=="b" or answer=="b. albert einstein" or answer=="b.albert einstein" or answer=="albert einstein"):
          print("correct answer")
          score(2,1)
         else:
          print("wrong answer")
          print("Correct answer: B. Albert Einstein")
          score(2,0)
         print("\nQuiz:4")
         print("Blood is filtered by which pair of organs?")
         print("A. Liver\nB. Kidneys\nC. Heart\nD. Lungs")
         print("Enter your Answer")
         answer=input().lower()
         if(answer=="b" or answer=="b. kidneys" or answer=="b.kidneys" or answer=="kidneys"):
          print("correct answer")
          score(2,1)
         else:
          print("wrong answer")
          print("Correct answer: B. Kidneys")
          score(2,0)
         print("\nQuiz:5")
         print("In which year World Trade Organisation came into existence?")
         print("A. 1992\nB. 1993\nC. 1994\nD. 1995")
         print("Enter your Answer")
         answer=input().lower()
         if(answer=="d" or answer=="d. 1995" or answer=="d.1995" or answer=="1995"):
          print("correct answer")
          score(2,1)
         else:
          print("wrong answer")
          print("Correct answer: D. 1995")
          score(2,0)
        else:
            display()
        global flag
        if flag ==0:
         print("\nDo you want to go next level!")
         print("\nEnter 'YES' to go next level or 'NO' to exit:")
         opt=input("Enter your choice:").lower()
         if opt == 'yes':
          print('\nLEVEl 3!!')
          print("\nQuiz:1")
          print("Which of the following personalities gave ‘The Laws of Heredity’?")
          print("(A) Robert Hook\n(B) G.J. Mendel\n(C) Charles Darwin\n(D) William Harvey")
          print("Enter your Answer")
          answer=input().lower()
          if(answer=="b" or answer=="b. g.j.mendel" or answer=="b.g.j.mendel" or answer=="g.j.mendel"):
           print("correct answer")
           score(3,1)
          else:
           print("wrong answer")
           print("Correct answer: (B) G.J. Mendel")
           score(3,0)
          print("\nQuiz:2")
          print("Who created a famous Geet Govind?")
          print("(A) Bana Bhatt\n(B) Kalidas\n(C) Jayadev\n(D) Bharat Muni")
          print("Enter your Answer")
          answer=input().lower()
          if(answer=="c" or answer=="c. jayadev" or answer=="c.jayadev" or answer=="jayadev"):
           print("correct answer")
           score(3,1)
          else:
           print("wrong answer")
           print("Correct answer: (C) Jayadev")
           score(3,0)
          print("\nQuiz:3")
          print("Which of the following represents the Finance Commissions that have been set-up so far?")
          print("(A) 10\n(B) 11\n(C) 12\n(D) 13")
          print("Enter your Answer")
          answer=input().lower()
          if(answer=="d" or answer=="d. 13" or answer=="d.13" or answer=="13"):
           print("correct answer")
           score(3,1)
          else:
           print("wrong answer")
           print("Correct answer: (D) 13")
           score(3,0)
          print("\nQuiz:4")
          print("Which of the following is the largest and the deepest ocean of the world?")
          print("(A) Arctic\n(B) Atlantic\n(C) Pacific\n(D) Indian")
          print("Enter your Answer")
          answer=input().lower()
          if(answer=="c" or answer=="c. pacific" or answer=="c.pacific" or answer=="pacific"):
           print("correct answer")
           score(3,1)
          else:
           print("wrong answer")
           print("Correct answer: (C) Pacific")
           score(3,0)
          print("\nQuiz:5")
          print("Which Mughal ruler was called 'Alamgir'?")
          print("(A) Aurangzeb\n(B) Jahangir\n(C) Akbar\n(D) Shah Jahan")
          print("Enter your Answer")
          answer=input().lower()
          if(answer=="a" or answer=="a. aurangzeb" or answer=="a.aurangzeb" or answer=="aurangzeb"):
           print("correct answer")
           score(3,1)
          else:
           print("wrong answer")
           print("Correct answer: (A) Aurangzeb")
           score(3,0)
        else:
           print("\nCongratulations !! You completed all the questions!!")
           display()
def technology():
 print('\nLEVEL 1!!')
 print('\nQUIZ :1')
 print("OS computer abbreviation usually means ?")
 print(" A.Order of Significance \n   B.	Open Software \n C.	Operating System \n D.	Optical Sensor")
        
 ans=input("Enter your answer:").lower()
 if ans == 'c.Operating System' or ans == 'c' or ans == 'Operating System' or ans == 'c.Operating System':	     
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("correct answer: c.Operating System")
   score(1,0)
 print('\nQUIZ :2')
 print("MOV extension refers usually to what kind of file?")
 print(" A.	Image file \n B.	Animation/movie file \n C.	Audio file \n D.	MS Office document ")
 ans=input("Enter your answer with space:").lower()
 if ans == 'b. Animation/movie file' or ans == 'b' or ans == 'Animation/movie file' or ans == 'b.Animation/movie file' :
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("correct answer: b.Animation/movie file")
   score(1,0)
 print('\nQUIZ :3')
 print("What is part of a database that holds only one type of information?")
 print("A.	Report \n B.	Field \n C.	Record \n D.	File")
 ans=input("Enter your answer with space:").lower()
 if ans == 'b.Field' or ans == 'b' or ans == 'Field' or ans == 'b. Field' :
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("correct answer: b. Field")
   score(1,0)
 print('\nQUIZ :4')
 print("Most modern TV's draw power even if turned off. The circuit the power is used in does what function?")
 print("A.	Sound \n B.	Remote control \n C.	Color balance \n D.	High voltage")
 ans=input("Enter your answer:").lower()
 if ans == 'b.Remote control' or ans == 'b' or ans == 'Remote control' or ans == 'b. Remote control' :	     
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("correct answer: b. Remote control")
   score(1,0)
 print('\nQUIZ :5')
 print("Which is a type of Electrically-Erasable Programmable Read-Only Memory?")
 print("A.	Flash \n B.	Flange \n C.	Fury \n D.	FRAM")
 ans=input("Enter your answer:").lower()
 if ans == 'a. Flash' or ans == 'a' or ans == 'Flash ' or ans == 'a.Flash':	     
   print("Correct answer!!")
   score(1,1)
 else:
   print("Wrong answer!!")
   print("correct answer: a.Flash")
   score(1,0)
 print("\nDo you want to go next level!!")
 print("\nEnter 'YES' to go next level or 'NO' to exit:")
 opt=input("Enter your choice:").lower()
 if opt == 'yes':
  print('\nLEVEl 2!!')
  print('\nQUIZ :1')
  print("In which decade was the SPICE simulator introduced?")
  print("A.	1950s \n B.	1960s \n C.	1970s D.	1980s")
  ans=input("Enter your answer with space:").  lower()
  if ans == 'c. 1970s' or ans == 'c' or ans == '1970s' or ans == 'c. 1970s' :	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("correct answer: c.1970s")
   score(2,0)
  print('\nQUIZ :2')
  print("	The purpose of choke in tube light is ?")
  print("A.	To decrease the current \n B.	To increase the current \n C.	To decrease the voltage momentarily \n D.	To increase the voltage momentarily")
  ans=input("Enter your answer:").  lower()
  if ans == 'd. To increase the voltage momentarily' or ans == 'd' or ans == 'To increase the voltage momentarily' or ans == 'd. To increase the voltage momentarily':	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("correct answer: d. To increase the voltage momentarily")
   score(2,0)
  print('\nQUIZ :3')
  print("	In the United States the television broadcast standard is...?")
  print("A.	PAL \n B.	NTSC \n C.	SECAM \n D.	RGB")

  ans=input("Enter your answer with space:").  lower()
  if ans == 'b. NTSC' or ans == 'b' or ans == 'NTSC' or ans == 'b.NTSC':	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("correct answer: b.NTSC")
   score(2,0)
  print('\nQUIZ :4')
  print(" What do we call a collection of two or more computers that are located within a limited distance of each other and that are connected to each other directly or indirectly?")
  print("A.	Inernet \n B.	Interanet \n C.	Local Area Network \n D.	Wide Area Network")
  ans=input("Enter your answer with space:").  lower()
  if ans == 'c. Local Area Network' or ans == 'c' or ans == 'Local Area Network' or ans == 'c.Local Area Network':  
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("correct answer: c.Local Area Network")
   score(2,0)
  print('\nQUIZ :5')
  print("Sometimes computers and cache registers in a foodmart are connected to a UPS system. What does UPS mean?")
  print("A.	United Parcel Service \n B.	Uniform Product Support \n C.	Under Paneling Storage \n D.	Uninterruptable Power Supply")

  ans=input("Enter your answer with space:").  lower()
  if ans == 'd. Uninterruptable Power Supply' or ans == 'd' or ans == 'Uninterruptable Power Supply' or ans == 'd.Uninterruptable Power Supply':	     
   print("Correct answer!!")
   score(2,1)
  else:
   print("Wrong answer!!")
   print("correct answer: d.Uninterruptable Power Supply")
   score(2,0)
 else:
  display()
  

 global flag
 if flag ==0:
  print("\nDo you want to go next level!")
  print("\nEnter 'YES' to go next level or 'NO' to exit:")
  opt=input("Enter your choice:").lower()
  if opt == 'yes':
   print('\nLEVEl 3!!')
   print('\nQUIZ :1')
   print("	Who co-founded Hotmail in 1996 and then sold the company to Microsoft?")
   print("A.	Shawn Fanning \n B.	Ada Byron Lovelace \n C.	Sabeer Bhatia \n D.	Ray Tomlinson")     
   ans=input("Enter your answer with space:").  lower()
   if ans == 'c. Sabeer Bhatia' or ans == 'c' or ans == 'Sabeer Bhatia' or ans == 'c.Sabeer Bhatia ' :     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")
    print("correct answer: c.Sabeer Bhatia ")
    score(3,0)
   print('\nQUIZ :2')
   print("	'.TMP' extension refers usually to what kind of file?")
   print("A.	Compressed Archive file\n B.	Image file \n C.	Temporary file \n D.	Audio file  ")
   ans=input("Enter your answer:").  lower()
   if ans == 'c. Temporary file' or ans == 'c' or ans == 'Temporary file' or ans == 'c.Temporary file':
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")
    print("correct answer: c.Temporary file ")
    score(3,0)
   print('\nQUIZ :3')
   print("	In the UK, what type of installation requires a fireman's switch?")
   print("A.	Neon Lighting \n B.	High Pressure Sodium Lighting \n C.	Water Features \n D.	Hotel Rooms")
   ans=input("Enter your answer with space:").  lower()
   if ans == 'a. Neon Lighting' or ans == 'a' or ans == 'Neon Lighting' or ans == 'a.Neon Lighting':	     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")
    print("correct answer: a.Neon Lighting ")
    score(3,0)
   print('\nQUIZ :4')
   print("	Who created Pretty Good Privacy (PGP)?")
   print("A.	Phil Zimmermann\n B.	Tim Berners-Lee \n C.	Marc Andreessen \n D.	Ken Thompson   ")

   ans=input("Enter your answer with space:").  lower()
   if ans == 'a. Phil Zimmermann' or ans == 'a' or ans == 'Phil Zimmermann' or ans == 'a.Phil Zimmermann':	     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")
    print("correct answer: a.Phil Zimmermann ")
    score(3,0)
   print('\nQUIZ :5')
   print("What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.")
   print("A.	URL (Universal Resource Locator) \n B.	LAN (Local Area Network) \n C.	WAN (Wide Area Network) \n D.	World Wide Web")

   ans=input("Enter your answer with space:").  lower()
   if ans == 'a.URL (Universal Resource Locator)' or ans == 'a' or ans == 'URL (Universal Resource Locator)' or ans == 'a. URL (Universal Resource Locator)':	     
    print("Correct answer!!")
    score(3,1)
   else:
    print("Wrong answer!!")
    print("correct answer: a.Universal Resource Locator ")
    score(3,0)
  else:
    print("\nCongratulations !! You completed all the questions!!")
    display()
print("Welcome to QUIZ MASTER ! ")
print("press 1 for GENERAL questions\npress 2 for SPORTS questions\npress 3 for TECHNOLOGY questions")
print("Let's start the Quiz!!")
choice=int(input("Enter your choice:")) 
if(choice==1):
    general()
elif choice==2:
    sports()
elif choice==3:
    technology()
else:
    print("INVALID INPUT ! PLEASE ENTER THE CORRECT INPUT...")

          


