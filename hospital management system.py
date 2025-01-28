

import pickle
import random
def create_patient():
    
    f=open('abc.dat','ab')
    name=input('enter name')
    print('patient number=',random.randint(0,100))
    patient_number=int(input('enter above number'))

    
    age=int(input('enter age'))
    ph=int(input('enter phone number'))
    l=[name,patient_number,age,ph]
    pickle.dump(l,f)
    f.close()
def display_patient():
    f=open('abc.dat','rb')
    try:
        while True:
            s=pickle.load(f)
            print(s)
    except EOFError:
        f.close()
def beds():
    f=open('bed.dat','ab')
    name=input('enter name')
    print('patient number=',random.randint(0,100))
    patient_number=int(input('enter above number'))

    
    age=int(input('enter age'))
    ph=int(input('enter phone number'))
    
    l=[name,patient_number,age,ph,beds]
    pickle.dump(l,f)
    f.close()

def add_doc():
    with open('Doctor.dat','ab') as f:
        name=input("enter the name of the Doctor: ")
        age=int(input('enter age'))
        ph=int(input('enter phone number'))
        field=input("enter dermotologist , physician or gynacologist ")
        l=[name,age,ph,field]
        pickle.dump(l,f)
        print(name ,"added")

def display_doc():
    f=open('Doctor.dat','rb')
    try:
        while True:
            s=pickle.load(f)
            print(s)
    except EOFError:
        f.close()

def update():
    name=input("enter name to update: ")
    f = open("Doctor.dat",'rb+')
    st= []
    while True:
        try:
            s=pickle.load(f)
            st.append(s)
            
        except EOFError:
            f.close()
            break
    ph=int(input('new phone number'))
    f = open("Doctor.dat",'wb')
    for x in st:
        if x[0]==name:
            x[2]=ph
            
            pickle.dump(x,f)
        else:
            pickle.dump(x,f)
            
    
    f.close()

def create_admin():
    f=open('admin.dat','ab')
    name=input('name')
    role=input('enter role')
    ph=int(input('phone number'))
    print('pswd=  123')
    l=[name,role,ph]
    pickle.dump(l,f)
    f.close()
def admin_display():
    f=open('admin.dat','rb')
    try:
        while True:
            s=pickle.load(f)
            print(s)
    except EOFError:
        f.close()
    

def remove_doc():
    n=input("Enter name of the doctor to be removed: ")
    f=open('Doctor.dat','rb+')
    l=[]
    try:
        while True:
            e = pickle.load(f)
            l.append(e)
    except EOFError:
        f.close()
    for i in l:
        if i[0]==n:
            l.remove(i)
            break
    f=open("Doctor.dat",'wb')
    for x in l:
        pickle.dump(x,f)
    print(n,"removed")
def create_covid():
    c=0
    f=open('abc.dat','ab')
    name=input('enter name')
        
    pswd=input('make a pswd')
    age=int(input('enter age'))
    ph=int(input('enter phone number'))
    l=[name,pswd,age,ph,c]
    pickle.dump(l,f)
    f.close()
def display_covid():
    f=open('abc.dat','rb')
    try:
        while True:
            s=pickle.load(f)
            print(s)
            
    except EOFError:
        f.close()

def vaccine():
    l=[]
    name=input('enter name')
    pswd=input('enter pswd')
    f=open('abc.dat','rb+')
    try:
        while True:
                s=pickle.load(f)
                l.append(s)
                
                if s[0]==name and s[1]==pswd:
                    print('welcome',s[0])
                    k=s
                    
                    print('your current doses given are',k[4])
                    if k[4] ==0 :
                            
                        print('slots availaible: [1-1pm-2pm,2-4pm-4.30pm,3-6-7.00pm]')
                        time=int(input('1/2/3'))
                        print('covishield vaccine booked for',time)
                                
                        
                        break
                                
                                
                           
                    if k[4]==1:
                        print('you have to get 2nd dose ')
                        print('slots availaible: [1-1pm-2pm,2-4pm-4.30pm,3-6-7.00pm]')
                        time=int(input('1/2/3'))
                        print('vaccine booked for',time)
                        break
                            
                    if k[4]==2:
                        print('fully vaccinated')
                        break
                            
                        
                                
                                
                                         
            
            
                 
                    
    except EOFError:
        f.close()
    f=open('abc.dat','wb')
    for x in l:
        
        if x[0]==name and x[1]==pswd:
            x[4]+=1
            pickle.dump(x,f)
        else:
            pickle.dump(x,f)
                     
    f.close()
            
def beds():
    l=[]
    b=open('beds.dat','ab')
    name=input('enter name')
    age=int(input('enter age'))
    ph=int(input('enter phone number'))
    
    m=[name,age,ph]
    pickle.dump(m,b)
    b.close()
    f=open('beds.dat','rb')
    
    try:
        while True:
            s=pickle.load(f)
            l.append(s)
            
    except EOFError:
        f.close()
    if len(l)>10:
                print('not availaible')
                l.pop()
    else:
        print('booked')
        m=open('booked.dat','ab')
        for x in l:
            pickle.dump(x,m)
        m.close()
        
    

        
    
    
    
user=input('admin\patient\covid special')
if user == 'patient' :
    while True:
        print('welcome to orchid hospital , pls select the option to move forward')
        print('book appointmnet ........... 1')
        print('giving reviews or suggestion.........2')
        print('book beds...................3')
        print('exit...........4')
        ch=int(input('enter choice'))
        p={}
        if ch==1:
            create_patient()
            print('what field of doctors you want to contact?')
            field=input('d-dermotologist/p-physician/g-gynacologist')
            if field == 'd' :
                print('doctors availaible:[dr.myesha,dr.swati,dr.millind]')
                j=input('enter doctor name')
                if j == 'dr.myesha':
                    print('slots availaible: [1pm-2pm,4pm-4.30pm,6-7.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                    
                if j == 'dr.swati':
                    print('slots availaible: [1pm-2pm,4.30pm-5pm,5.30-6.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                    p[name]=i
                if j == 'dr.millind':
                    print('slots availaible: [2pm-3pm,4pm-4.30pm,7-8.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                    
            if field == 'p' :
                print('doctors availaible:[dr.ram,dr.lakshman,dr.bharat]')
                j=input('enter doctor name')
                if j == 'dr.ram':
                    print('slots availaible: [1pm-2pm,4pm-4.30pm,-6-7.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                    
                if j == 'dr.lakshman':
                    print('slots availaible: [1pm-2pm,4.30pm-5pm,5.30-6.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                    
                if j == 'dr.bharat':
                    print('slots availaible: [2pm-3pm,4pm-4.30pm,7-8.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                    
            if field == 'g' :
                print('doctors availaible:[dr.karan,dr.meher,dr.rene]')
                j=input('enter doctor name')
            
                if j == 'dr.karan':
                    print('slots availaible: [1pm-2pm,4pm-4.30pm,-6-7.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                    
                if j == 'dr.meher':
                    print('slots availaible: [1pm-2pm,4.30pm-5pm,5.30-6.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                   
                if j == 'dr.rene':
                    print('slots availaible: [2pm-3pm,4pm-4.30pm,7-8.00pm]')
                    i=input('enter slot')
                    print('appointment booked for',i,'with',j)
                    
            

        
            
        if ch == 2:
            l=[]
            create_patient()
            sug=input('enter suggestion')
            l.append(sug)
            print('thankyou')            
            
        if ch == 3:
            beds()  
        
        if ch==4:
            print('thankyou')
            break
if  user=='admin':
    n=input("enter name")
    p=input("enter password")
    if p=='123':
        print("Welcome Admin")
        while True:
            print("Choose an option (1,2,3,4,5)")
            print('1.Add a Doctor ')
            print('2.Remove a Doctor')
            print('3.Change information about Doctors')
            
            print('4.Exit')
            ch=int(input("Enter your option"))
            if ch==1:
                add_doc()
                display_doc()
            elif ch==2:
                remove_doc()
                display_doc()
            elif ch==3:
                update()
                display_doc()
            

            elif ch==4:
                print("Exiting")
                break
            else:
                print("wrong option")

if user == 'covid special' :
    while True:
        print('welcome to orchid hospital , pls select the option to move forward')
        print('book vaccine ........... 1')
        print('should you get covid tested.........2')
        print('covid test..........3')
        print('exit.....4')
        ch=int(input('enter choice'))
        if ch==1:
            j=input('have an account?(y\n)')
        
            if j in 'yY':
                vaccine()
            
                        
                                
            else:
                create_covid()
                vaccine()
        if ch==2:
            s=0
            print('do you have cough?')
            ch=input('y/n')
            if ch in'yY':
                s+=1
            print('do you have cold?')
            ch=input('y/n')
            if ch in'yY':
                s+=1
            print('do you have fever?')
            ch=input('y/n')
            if ch in'yY':
                s+=1
            print('do you have headache?')
            ch=input('y/n')
            if ch in'yY':
                s+=1
            print('have yo met a covid possitive person in last week?')
            ch=input('y/n')
            if ch in'yY':
                s+=1
            if s>=3:
                print('get tested')
            else:
                print('not required and take precautions')
        if ch ==3:
            print('slots availaible: [1-1pm-2pm,2-4pm-4.30pm,3-6-7.00pm]')
            k=input('enter slot')
            print('test booked for',k,'enter through gate 2')
        
        if ch==4:
            print('thankyou')
            break
        

































