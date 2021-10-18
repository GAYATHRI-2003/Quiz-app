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
          


