###############################################
# Final project for ISTA 301
# Description:
#       A Breakout clone game which construct
#  with funny design and features. 
###############################################

import pygame,sys,random

# Basic Setup
pygame.init()
screen=pygame.display.set_mode([720,540])
screen.fill([255,255,255])
my_ball=pygame.image.load("trumball.png")       #ball picture
my_plank=pygame.image.load("plank.png")  	#plank picture
my_gameover=pygame.image.load("gameover.png")	#gameover picture
my_redblock=pygame.image.load("red2.png")	#blocks
my_blueblock=pygame.image.load("blue2.png")
my_whiteblock=pygame.image.load("white2.png")

# While loop checking if the game is over or not
continueplay=True
while continueplay==True:
	pygame.draw.rect(screen,[255,255,255],[0,0,screen.get_width(),screen.get_height()],0)	
	pygame.display.flip()
	
	# Starting to draw each blocks which construct to be like a flag
	n=6
	for i in range(0,3):
		screen.blit(my_blueblock,[0+i*120,0])
	for i in range(3,n):
		screen.blit(my_redblock,[0+i*120,0])
	pygame.display.flip()
	
	# the list of 1st floor rectangles above the screen
	list1=[]
	for i in range(0,n):
		list1.append(1)
		
	for i in range(0,3):
		screen.blit(my_blueblock,[0+i*120,23])
	for i in range(3,n):
		screen.blit(my_whiteblock,[0+i*120,23])
	pygame.display.flip()
	# the list of 2th floor rectangles above the screen
	list2=[]
	for i in range(0,n):
		list2.append(1)
		
	for i in range(0,3):
		screen.blit(my_blueblock,[0+i*120,46])
	for i in range(3,n):
		screen.blit(my_redblock,[0+i*120,46])
	pygame.display.flip()
	# the list of 3th floor rectangles above the screen
	list3=[]
	for i in range(0,n):
		list3.append(1)
		
	for i in range(0,n):
		screen.blit(my_whiteblock,[0+i*120,69])
	pygame.display.flip()
	# the list of 4th floor rectangles above the screen
	list4=[]
	for i in range(0,n):
		list4.append(1)
		
	for i in range(0,n):
		screen.blit(my_redblock,[0+i*120,92])
	pygame.display.flip()
	# the list of 5 floor rectangles above the screen
	list5=[]
	for i in range(0,n):
		list5.append(1)

	x=300
	y=180
	x_speed=random.randint(3,4)
	y_speed=11
	# Construct the play ball
	screen.blit(my_ball,[x,y])					
	plankx=screen.get_width()/2-100
	planky=screen.get_height()-40
	plankstep=10 # move the plank each time user press left or right
	# init the left and right
	pressleft=False  	
	pressright=False
	# Construct the plank
	screen.blit(my_plank,[plankx,planky])
	def loadtext(scores):
                textstr='Flags: '+str(30-scores)
                text_screen=my_font.render(textstr, True, (255, 0, 0))
                screen.blit(text_screen, (0,438))
	pygame.display.flip()
	my_font=pygame.font.SysFont(None,44)
	scores=0
	pressc=False
	pressx=False
	running=True
	while running:
		pygame.mouse.set_visible(False)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			# Checking if user press left or right to move plank
			if event.type==pygame.KEYDOWN:			
				if event.key == pygame.K_LEFT:
					pressleft=True
					pressright=False
				if event.key == pygame.K_RIGHT:
					pressleft=False
					pressright=True		
				if event.key==pygame.K_c:
					pressc=True
					pressx=False
				if event.key==pygame.K_x:
					pressx=True
					pressc=False
				if event.key==pygame.K_c:
					pressc=True
					pressx=False
				if event.key==pygame.K_x:
					pressx=True
					pressc=False
		# Time delay for each time the ball hit a blank
		# It is manageable and depends on how user would like to play
		pygame.time.delay(20)			
		# redraw/reconstruct the old ball
		pygame.draw.rect(screen,[255,255,255],[x,y,50,50],0)
		x=x+x_speed
		y=y+y_speed
		# hit the left and right side of the screen
		# change direction of x
		if x>=screen.get_width()-50 or x<=0:			
			x_speed=-x_speed
		# hit the top  side of the screen
		if y<=0:				
			y_speed=-y_speed
		screen.blit(my_ball,[x,y])
		pygame.display.flip()
		# find ball's x in which rectangle
		for m in range(0,n):
			if x>=120*m and x<=120*(m+1) :
				xx=m
		# ball hit the rectangles above the screen
		# clear the hitted rectangle
		if list5[xx]==1:
			if y<=23*4+10 and y_speed<0:
				pygame.draw.rect(screen,[255,255,255],[0+120*xx,23*4,120,23],0)
				y_speed=-y_speed
				pygame.draw.rect(screen,[255,255,255],[0,438,160,44],0)
				# clear the scores
				scores+=1
				loadtext(scores)   
				pygame.display.flip()  
				list5[xx]=0
				splat=pygame.mixer.Sound("dingdong.wav")
				splat.play()
		if list4[xx]==1:
			if y<=23*3+10 and y_speed<0:
				pygame.draw.rect(screen,[255,255,255],[0+120*xx,23*3,120,23],0)
				y_speed=-y_speed
				pygame.draw.rect(screen,[255,255,255],[0,438,160,44],0)
				scores+=1
				loadtext(scores)   
				pygame.display.flip()  
				list4[xx]=0
				splat=pygame.mixer.Sound("dingdong.wav")
				splat.play()
		if list3[xx]==1:
			if y<=23*2+10 and y_speed<0:
				pygame.draw.rect(screen,[255,255,255],[0+120*xx,23*2,120,23],0)
				y_speed=-y_speed
				pygame.draw.rect(screen,[255,255,255],[0,438,160,44],0)
				scores+=1
				loadtext(scores)   
				pygame.display.flip()  
				list3[xx]=0
				splat=pygame.mixer.Sound("dingdong.wav")
				splat.play()
		if list2[xx]==1 :
			if y<=23*1+10 and y_speed<0:
				pygame.draw.rect(screen,[255,255,255],[0+120*xx,23*1,120,23],0)
				y_speed=-y_speed
				pygame.draw.rect(screen,[255,255,255],[0,438,160,44],0)
				scores+=1
				loadtext(scores)   
				pygame.display.flip()  
				list2[xx]=0
				splat=pygame.mixer.Sound("dingdong.wav")
				splat.play()
		if list1[xx]==1:
			if y<=23*0+10 and y_speed<0:
				pygame.draw.rect(screen,[255,255,255],[0+120*xx,23*0,120,23],0)
				y_speed=-y_speed
				pygame.draw.rect(screen,[255,255,255],[0,438,160,44],0)
				scores+=1
				loadtext(scores)   
				pygame.display.flip()  
				list1[xx]=0
				splat=pygame.mixer.Sound("dingdong.wav")
				splat.play()
		#redraw the blocks
		for i in range (0,6):
			if list1[i]==1:
				if i<=2:
					screen.blit(my_blueblock,[0+i*120,0])
				if i>=3:
					screen.blit(my_redblock,[0+i*120,0])
		for i in range (0,6):
			if list2[i]==1:
				if i<=2:
					screen.blit(my_blueblock,[0+i*120,23])
				if i>=3:
					screen.blit(my_whiteblock,[0+i*120,23])
		for i in range(0,6):
			if list3[i]==1:
				if i<=2:
					screen.blit(my_blueblock,[0+i*120,46])
				if i>=3:
					screen.blit(my_redblock,[0+i*120,46])
		for i in range(0,6):
			if list4[i]==1:
				screen.blit(my_whiteblock,[0+i*120,69])
		for i in range(0,6):
			if list5[i]==1:
				screen.blit(my_redblock,[0+i*120,92])
		pygame.display.flip()
		# moving the plank while press left or right
		if pressleft==True:
			for i in range(0,10):
				if plankx<=0:
					break
				#clear the old plank
				pygame.draw.rect(screen,[255,255,255],[plankx,planky,200,40],0)
				plankx=plankx-plankstep
				#draw a new plank
				screen.blit(my_plank,[plankx,planky])		
				pygame.display.flip()  
			pressleft=False
		if pressright==True:
			for i in range(0,10):
				if plankx>=screen.get_width()-200:
					break
				pygame.draw.rect(screen,[255,255,255],[plankx,planky,200,40],0)
				plankx=plankx+plankstep
				screen.blit(my_plank,[plankx,planky])
				pygame.display.flip()  
			pressright=False
		pygame.draw.rect(screen,[255,255,255],[0,438,160,44],0)	
		loadtext(scores)   
		pygame.display.flip()  
		# while ball hit on plank
		if x+7>=plankx-5 and x+7<=plankx+200-10:
			if y>=screen.get_height()-100:
				y_speed=-y_speed
		# ball not hit on plank
		# consider exit the game
		if y>=screen.get_height()-100 and (x+7<plankx-5 or x+7>plankx+200-10):
			screen.blit(my_gameover,[screen.get_width()/2-150,screen.get_height()/2-21])
			textstr2='press X to exit. '
			text_screen2=my_font.render(textstr2, True, (255, 0, 0))
			screen.blit(text_screen2, (screen.get_width()/2-100,screen.get_height()/2-21+50))
			textstr3='or wait 3 seconds to play again. '
			text_screen3=my_font.render(textstr3, True, (255, 0, 0))
			screen.blit(text_screen3, (screen.get_width()/2-200,screen.get_height()/2-21+100))
			pygame.display.flip()
			x=300
			y=180
			pygame.time.delay(5000)
			pygame.draw.rect(screen,[255,255,255],[0,0,screen.get_width(),screen.get_height()],0)	
			plankx=screen.get_width()/2-100
			planky=screen.get_height()-40
			screen.blit(my_plank,[plankx,planky])
			pygame.display.flip()
			break
		if pressx==True:
			running=False
			continueplay=False
			pygame.quit()
			break
pygame.quit()				

