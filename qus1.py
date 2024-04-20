class Star_Cinema:
     hall_list=[]
     def entry_hall(self,Hall):
          self.hall_list.append(Hall)
class Hall:
     def __init__(self,rows,cols,hall_no):
          self.seats={}
          self.show_list=[]
          self.rows=rows
          self.cols=cols
          self.hall_no=hall_no

     def entry_show(self,id, movie_name, time):
        tp={"id":id,"movie":movie_name,"time":time}
        self.show_list.append(tp)
        self.seats[id]=[[0 for x in range(self.cols)] for y in range(self.rows)]
     def book_seats(self,id,rows,cols):
          if id in [show['id'] for show in self.show_list]:
                    if self.seats[id][rows][cols]==0:
                         self.seats[id][rows][cols]=1
                         print(f"\n\tSeat {rows},{cols} booked Succesfully !")
                    else:
                         print(f"this seat is already book")
          else:
               print(f"this seat is invalid")
     def view_show_list(self):
          for show in self.show_list:
               print(f"Id:{show['id']},movie_name:{show['movie']},time:{show['time']}")

     def view_available_seats(self,id):
           if id in [show['id'] for show in self.show_list]:
               for i in range (self.rows):
                    for j in range (self.cols):
                         if self.seats[id][i][j]==0:
                              print(f"({i} {j})")
           else:
                print(f"this seat is invalid")
     def view_all_show_today(self,movie_name,show_id,time):
          print(f"MOVIE NAME: {movie_name}({show_id}) SHOW ID: {show_id} TIME: {time} ")

cinema=Star_Cinema()
hall=Hall(7,7,111)
cinema.entry_hall(hall)
hall.entry_show(111,"jawan","5:00")

hall1=Hall(7,7,111)
cinema.entry_hall(hall1)
hall1.entry_show(333,"jawan","5:00")

run=True
while run:
     print("Options: \n")
     print("1 : View all show today")
     print("2 : view available seats")
     print("3 : book ticket")
     print("4 : exit")
     ch=int(input("\nEnter Option: "))      
     if ch==1:
        hall.view_all_show_today("Jawan Maji",111,"25/10/2023  11:00AM")
        hall.view_all_show_today("Sujon Maji",333,"25/10/2023  02:00PM")
     elif ch==2:
          h=int(input("\nEnter Show ID: "))
          if h==111:
               hall.view_available_seats(h)
          elif h==333:
               hall1.view_available_seats(h)
     elif ch==3:
          id=int(input("\nEnter Show ID: "))
          t=int(input("\nNumber of ticket: "))
          row=int(input("\nEnter seat row: "))
          col=int(input("\nEnter seat col: "))
          if id==111:
               hall.book_seats(id,row,col)
          elif id==333:
               hall1.book_seats(id,row,col)

     elif ch==4:
          run=False



          
