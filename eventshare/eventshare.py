import csv
create_event=open('create event.csv','a')

view_event=open('create event.csv','r')

print(':::::::: HELLO WELCOME TO EVENTSHARE ::::::::')
def homepage():
    
    sel=input('If you want to create an event type ''c'' \n If you want to view existing events type ''v''>>>>>>>>>>::')
    if sel=='c':
        name=input('Enter event name :')
        Etype=input('\nWhat type of event is this (art/science/sports) :')
        des=input('Please give a short description of your event :')
        Ewrite=csv.writer(create_event)
        Ewrite.writerow([name,Etype,des])
        create_event.close()
        print('  EVENT UPDATED! ')
        Q=input('Do you wish to go back to the home page(Y/N) ? :')
        if Q=='Y':
           homepage()
        elif Q=='N':
            quit()
    elif sel=='v':
        Eread=csv.reader(view_event)
        for i in Eread:
            for j in i:
                namevent=i[0]
                typevent=i[1]
                desevent=i[2]
            if len(i) !=0: 
                  print('\nEvent name :',namevent)
                  print('Event type :',typevent)
                  print('Event description :',desevent)
            
           
        Q=input('Do you wish to go back to the home page(Y/N) ? :')
        if Q=='Y':
           homepage()
        elif Q=='N':
            quit()
homepage()
create_event.close()

