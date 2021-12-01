import math
import pygame
import time


class Panel(object):

    def __init__(self,canvas,elevator_list):
        self.cp_1_x=-20
        self.cp_1_y=-200
        self.cp_2_x=170
        self.cp_3_y=100
        self.canvas=canvas
        self.button_list = []
        for i in range (0, 2):
            self.button_list.append([])
        self.elevator_list=elevator_list
        self.flag_list = []
        for i in range (0, 2):
            new = []
            for j in range (0, 12):
                new.append(False)
            self.flag_list.append(new)


        ####   NORMAL LIFT

        #MAIN LIFT BODY
        self.body_1 = canvas.create_rectangle(50+self.cp_1_x,300+self.cp_1_y,200+self.cp_1_x,550+self.cp_1_y,fill="#A9A9A9",activefill="#C1E950")
        self.display_half_1   = canvas.create_rectangle(50+self.cp_1_x,300+self.cp_1_y,200+self.cp_1_x,350+self.cp_1_y,fill="#B18D92")
        self.button_1_13_id = canvas.create_text(80 + self.cp_1_x, 320 + self.cp_1_y, anchor="nw", activefill="blue")
        canvas.itemconfig(self.button_1_13_id, text="NORMAL LIFT")
        self.name_1 = canvas.create_text(120+self.cp_1_x,285+self.cp_1_y, text="LIFT CONTROLLERS", activefill="red")
        

        #BUTTON 1
        self.button_1_1   = canvas.create_rectangle(60+self.cp_1_x,360+self.cp_1_y,90+self.cp_1_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_1_1_id = canvas.create_text(70+self.cp_1_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_1_id, text="❶")
        canvas.tag_bind(self.button_1_1, '<Button-1>', lambda x: self.PanelButtonClicked(1,1,self.flag_list[0][0]))
        canvas.tag_bind(self.button_1_1_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,1,self.flag_list[0][0]))
        self.button_list[0].append(self.button_1_1)
        
        #BUTTON 2
        self.button_1_2 = canvas.create_rectangle(110+self.cp_1_x,360+self.cp_1_y,140+self.cp_1_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_1_2_id = canvas.create_text(120+self.cp_1_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_2_id, text="❷")
        canvas.tag_bind(self.button_1_2, '<Button-1>', lambda x: self.PanelButtonClicked(1,2,self.flag_list[0][1]))
        canvas.tag_bind(self.button_1_2_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,2,self.flag_list[0][1]))
        self.button_list[0].append(self.button_1_2)

        #BUTTON 3
        self.button_1_3 = canvas.create_rectangle(160+self.cp_1_x,360+self.cp_1_y,190+self.cp_1_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_1_3_id = canvas.create_text(170+self.cp_1_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_3_id, text="❸")
        canvas.tag_bind(self.button_1_3, '<Button-1>', lambda x: self.PanelButtonClicked(1,3,self.flag_list[0][2]))
        canvas.tag_bind(self.button_1_3_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,3,self.flag_list[0][2]))
        self.button_list[0].append(self.button_1_3)

        #BUTTON 4
        self.button_1_4 = canvas.create_rectangle(60+self.cp_1_x,410+self.cp_1_y,90+self.cp_1_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_1_4_id = canvas.create_text(70+self.cp_1_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_4_id, text="❹")
        canvas.tag_bind(self.button_1_4, '<Button-1>', lambda x: self.PanelButtonClicked(1,4,self.flag_list[0][3]))
        canvas.tag_bind(self.button_1_4_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,4,self.flag_list[0][3]))
        self.button_list[0].append(self.button_1_4)

        #BUTTON 5
        self.button_1_5 = canvas.create_rectangle(110+self.cp_1_x,410+self.cp_1_y,140+self.cp_1_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_1_5_id = canvas.create_text(120+self.cp_1_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_5_id, text="❺")
        canvas.tag_bind(self.button_1_5, '<Button-1>', lambda x: self.PanelButtonClicked(1,5,self.flag_list[0][4]))
        canvas.tag_bind(self.button_1_5_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,5,self.flag_list[0][4]))
        self.button_list[0].append(self.button_1_5)

        #BUTTON 6
        self.button_1_6 = canvas.create_rectangle(160+self.cp_1_x,410+self.cp_1_y,190+self.cp_1_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_1_6_id = canvas.create_text(170+self.cp_1_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_6_id, text="❻")
        canvas.tag_bind(self.button_1_6, '<Button-1>', lambda x: self.PanelButtonClicked(1,6,self.flag_list[0][5]))
        canvas.tag_bind(self.button_1_6_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,6,self.flag_list[0][5]))
        self.button_list[0].append(self.button_1_6)
        
        #BUTTON 7
        self.button_1_7 = canvas.create_rectangle(60+self.cp_1_x,460+self.cp_1_y,90+self.cp_1_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_1_7_id = canvas.create_text(70+self.cp_1_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_7_id, text="❼")
        canvas.tag_bind(self.button_1_7, '<Button-1>', lambda x: self.PanelButtonClicked(1,7,self.flag_list[0][6]))
        canvas.tag_bind(self.button_1_7_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,7,self.flag_list[0][6]))
        self.button_list[0].append(self.button_1_7)
        
        #BUTTON 8
        self.button_1_8 = canvas.create_rectangle(110+self.cp_1_x,460+self.cp_1_y,140+self.cp_1_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_1_8_id = canvas.create_text(120+self.cp_1_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_8_id, text="❽")
        canvas.tag_bind(self.button_1_8, '<Button-1>', lambda x: self.PanelButtonClicked(1,8,self.flag_list[0][7]))
        canvas.tag_bind(self.button_1_8_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,8,self.flag_list[0][7]))
        self.button_list[0].append(self.button_1_8)
        
        #BUTTON 9
        self.button_1_9 = canvas.create_rectangle(160+self.cp_1_x,460+self.cp_1_y,190+self.cp_1_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_1_9_id = canvas.create_text(170+self.cp_1_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_9_id, text="❾")
        canvas.tag_bind(self.button_1_9, '<Button-1>', lambda x: self.PanelButtonClicked(1,9,self.flag_list[0][8]))
        canvas.tag_bind(self.button_1_9_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,9,self.flag_list[0][8]))
        self.button_list[0].append(self.button_1_9)
        
        #BUTTON GROUND FLOOR
        self.button_1_10 = canvas.create_rectangle(110+self.cp_1_x,510+self.cp_1_y,140+self.cp_1_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_1_10_id = canvas.create_text(120+self.cp_1_x, 520+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_10_id, text="⓿")
        canvas.tag_bind(self.button_1_10, '<Button-1>', lambda x: self.PanelButtonClicked(1,'G',self.flag_list[0][9]))
        canvas.tag_bind(self.button_1_10_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,'G',self.flag_list[0][9]))
        self.button_list[0].append(self.button_1_10)
        
         #BUTTON Open Door
        self.button_1_11 = canvas.create_rectangle(60+self.cp_1_x,510+self.cp_1_y,90+self.cp_1_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_1_11_id = canvas.create_text(65+self.cp_1_x, 517+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_11_id, text="≤|≥")
        canvas.tag_bind(self.button_1_11, '<Button-1>', lambda x: self.PanelButtonClicked(1,'O',self.flag_list[0][10]))
        canvas.tag_bind(self.button_1_11_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,'O',self.flag_list[0][10]))
        self.button_list[0].append(self.button_1_11)
        
        #BUTTON Close Door
        self.button_1_12 = canvas.create_rectangle(160+self.cp_1_x,510+self.cp_1_y,190+self.cp_1_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_1_12_id = canvas.create_text(165+self.cp_1_x, 517+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_12_id, text="≥|≤")
        canvas.tag_bind(self.button_1_12, '<Button-1>', lambda x: self.PanelButtonClicked(1,'C',self.flag_list[0][11]))
        canvas.tag_bind(self.button_1_12_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,'C',self.flag_list[0][11]))
        self.button_list[0].append(self.button_1_12)
        

        #DIRECT LIFT

        #MAIN LIFT BODY

        self.body_2 = canvas.create_rectangle(50+self.cp_1_x,300+self.cp_3_y,200+self.cp_1_x,550+self.cp_3_y,fill="#A9A9A9",activefill="#C1E950")
        self.display_half_2   = canvas.create_rectangle(50+self.cp_1_x,300+self.cp_3_y,200+self.cp_1_x,350+self.cp_3_y,fill="#B18D92")
        self.button_2_13_id = canvas.create_text(80 + self.cp_1_x, 320 + self.cp_3_y, anchor="nw", activefill="blue")
        canvas.itemconfig(self.button_2_13_id, text="DIRECT LIFT")



        #BUTTON 1
        self.button_2_1   = canvas.create_rectangle(60+self.cp_1_x,360+self.cp_3_y,90+self.cp_1_x,390+self.cp_3_y,fill="#A9A9A9")
        self.button_2_1_id = canvas.create_text(70+self.cp_1_x, 370+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_1_id, text="❶")
        canvas.tag_bind(self.button_2_1, '<Button-1>', lambda x: self.PanelButtonClicked(2,1,self.flag_list[1][0]))
        canvas.tag_bind(self.button_2_1_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,1,self.flag_list[1][0]))
        self.button_list[1].append(self.button_2_1)
        
        #BUTTON 2
        self.button_2_2 = canvas.create_rectangle(110+self.cp_1_x,360+self.cp_3_y,140+self.cp_1_x,390+self.cp_3_y,fill="#A9A9A9")
        self.button_2_2_id = canvas.create_text(120+self.cp_1_x, 370+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_2_id, text="❷")
        canvas.tag_bind(self.button_2_2, '<Button-1>', lambda x: self.PanelButtonClicked(2,2,self.flag_list[1][1]))
        canvas.tag_bind(self.button_2_2_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,2,self.flag_list[1][1]))
        self.button_list[1].append(self.button_2_2)
        
        #BUTTON 3
        self.button_2_3 = canvas.create_rectangle(160+self.cp_1_x,360+self.cp_3_y,190+self.cp_1_x,390+self.cp_3_y,fill="#A9A9A9")
        self.button_2_3_id = canvas.create_text(170+self.cp_1_x, 370+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_3_id, text="❸")
        canvas.tag_bind(self.button_2_3, '<Button-1>', lambda x: self.PanelButtonClicked(2,3,self.flag_list[1][2]))
        canvas.tag_bind(self.button_2_3_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,3,self.flag_list[1][2]))
        self.button_list[1].append(self.button_2_3)
        
        #BUTTON 4
        self.button_2_4 = canvas.create_rectangle(60+self.cp_1_x,410+self.cp_3_y,90+self.cp_1_x,440+self.cp_3_y,fill="#A9A9A9")
        self.button_2_4_id = canvas.create_text(70+self.cp_1_x, 420+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_4_id, text="❹")
        canvas.tag_bind(self.button_2_4, '<Button-1>', lambda x: self.PanelButtonClicked(2,4,self.flag_list[1][3]))
        canvas.tag_bind(self.button_2_4_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,4,self.flag_list[1][3]))
        self.button_list[1].append(self.button_2_4)
        
        #BUTTON 5
        self.button_2_5 = canvas.create_rectangle(110+self.cp_1_x,410+self.cp_3_y,140+self.cp_1_x,440+self.cp_3_y,fill="#A9A9A9")
        self.button_2_5_id = canvas.create_text(120+self.cp_1_x, 420+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_5_id, text="❺")
        canvas.tag_bind(self.button_2_5, '<Button-1>', lambda x: self.PanelButtonClicked(2,5,self.flag_list[1][4]))
        canvas.tag_bind(self.button_2_5_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,5,self.flag_list[1][4]))
        self.button_list[1].append(self.button_2_5)
        
        #BUTTON 6
        self.button_2_6 = canvas.create_rectangle(160+self.cp_1_x,410+self.cp_3_y,190+self.cp_1_x,440+self.cp_3_y,fill="#A9A9A9")
        self.button_2_6_id = canvas.create_text(170+self.cp_1_x, 420+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_6_id, text="❻")
        canvas.tag_bind(self.button_2_6, '<Button-1>', lambda x: self.PanelButtonClicked(2,6,self.flag_list[1][5]))
        canvas.tag_bind(self.button_2_6_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,6,self.flag_list[1][5]))
        self.button_list[1].append(self.button_2_6)
        
        #BUTTON 7
        self.button_2_7 = canvas.create_rectangle(60+self.cp_1_x,460+self.cp_3_y,90+self.cp_1_x,490+self.cp_3_y,fill="#A9A9A9")
        self.button_2_7_id = canvas.create_text(70+self.cp_1_x, 470+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_7_id, text="❼")
        canvas.tag_bind(self.button_2_7, '<Button-1>', lambda x: self.PanelButtonClicked(2,7,self.flag_list[1][6]))
        canvas.tag_bind(self.button_2_7_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,7,self.flag_list[1][6]))
        self.button_list[1].append(self.button_2_7)
        
        #BUTTON 8
        self.button_2_8 = canvas.create_rectangle(110+self.cp_1_x,460+self.cp_3_y,140+self.cp_1_x,490+self.cp_3_y,fill="#A9A9A9")
        self.button_2_8_id = canvas.create_text(120+self.cp_1_x, 470+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_8_id, text="❽")
        canvas.tag_bind(self.button_2_8, '<Button-1>', lambda x: self.PanelButtonClicked(2,8,self.flag_list[1][7]))
        canvas.tag_bind(self.button_2_8_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,8,self.flag_list[1][7]))
        self.button_list[1].append(self.button_2_8)

        #BUTTON 9
        self.button_2_9 = canvas.create_rectangle(160+self.cp_1_x,460+self.cp_3_y,190+self.cp_1_x,490+self.cp_3_y,fill="#A9A9A9")
        self.button_2_9_id = canvas.create_text(170+self.cp_1_x, 470+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_9_id, text="❾")
        canvas.tag_bind(self.button_2_9, '<Button-1>', lambda x: self.PanelButtonClicked(2,9,self.flag_list[1][0]))
        canvas.tag_bind(self.button_2_9_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,9,self.flag_list[1][0]))
        self.button_list[1].append(self.button_2_9)
        
        #BUTTON G
        self.button_2_10 = canvas.create_rectangle(110+self.cp_1_x,510+self.cp_3_y,140+self.cp_1_x,540+self.cp_3_y,fill="#A9A9A9")
        self.button_2_10_id = canvas.create_text(120+self.cp_1_x, 520+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_10_id, text="⓿")
        canvas.tag_bind(self.button_2_10, '<Button-1>', lambda x: self.PanelButtonClicked(2,'G',self.flag_list[1][9]))
        canvas.tag_bind(self.button_2_10_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,'G',self.flag_list[1][9]))
        self.button_list[1].append(self.button_2_10)
        
         #BUTTON Open
        self.button_2_11 = canvas.create_rectangle(60+self.cp_1_x,510+self.cp_3_y,90+self.cp_1_x,540+self.cp_3_y,fill="#A9A9A9")
        self.button_2_11_id = canvas.create_text(65+self.cp_1_x, 517+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_11_id, text="≤|≥")
        canvas.tag_bind(self.button_2_11, '<Button-1>', lambda x: self.PanelButtonClicked(2,'O',self.flag_list[1][10]))
        canvas.tag_bind(self.button_2_11_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,'O',self.flag_list[1][10]))
        self.button_list[1].append(self.button_2_11)
        
        #BUTTON Close
        self.button_2_12 = canvas.create_rectangle(160+self.cp_1_x,510+self.cp_3_y,190+self.cp_1_x,540+self.cp_3_y,fill="#A9A9A9")
        self.button_2_12_id = canvas.create_text(165+self.cp_1_x, 517+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_12_id, text="≥|≤")
        canvas.tag_bind(self.button_2_12, '<Button-1>', lambda x: self.PanelButtonClicked(2,'C',self.flag_list[1][11]))
        canvas.tag_bind(self.button_2_12_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,'C',self.flag_list[1][11]))
        self.button_list[1].append(self.button_2_12)

    def PanelButtonClicked(self,liftno,event,flag):
        print ("Lift "+str(liftno)+" : Button "+str(event))
        
        if flag == False:
            
            if event == 'G':
                self.canvas.itemconfig(self.button_list[liftno-1][9], fill="#ff0")
                self.flag_list[liftno-1][9] = True
                self.elevator_list[liftno-1].addFloor(0,"none")
            elif not(event == 'C') and not(event == 'O'):    
                self.canvas.itemconfig(self.button_list[liftno-1][event-1], fill="#ff0")
                self.flag_list[liftno-1][event-1] = True

            if  event == 'C' or event == 'O' or event =='G':
                if event == 'O':
                    if self.elevator_list[liftno-1].status == "closing" or self.elevator_list[liftno-1].status == "idle":
                        self.elevator_list[liftno-1].status = "opening"         
                elif event == 'C':
                    if self.elevator_list[liftno-1].status == "opening" or self.elevator_list[liftno-1].status == "open":
                        self.elevator_list[liftno-1].status = "closing"
            else:
                self.elevator_list[liftno-1].addFloor(event,"none")


