        if i=='ElSadat' :
            temp=ElSadat
            mycanv.itemconfig(temp,fill='green')
        if i=='Shebin' :
            temp=Shebin
            mycanv.itemconfig(temp,fill='green')
        if i=='Meleeg' :
            temp=Meleeg
            mycanv.itemconfig(temp,fill='green')
        if i=='ElHamoul' :
            temp=ElHamoul
            mycanv.itemconfig(temp,fill='green')
        if i=='Menouf' :
            temp=Menouf
            mycanv.itemconfig(temp,fill='green')
        if i=='Tala' :
            temp=Tala
            mycanv.itemconfig(temp,fill='green')
        if i=='Shanawan' :
            temp=Shanawan
            mycanv.itemconfig(temp,fill='green')
        if i=='ElBagour' :
            temp=ElBagour
            mycanv.itemconfig(temp,fill='green')
        if i=='ElShohadaa' :
            temp=ElShohadaa
            mycanv.itemconfig(temp,fill='green')
        
        
        if path[cnt-1]+path[cnt]=='TalaShebin' or path[cnt-1]+path[cnt]=='ShebinTala' :
            temp=ShebinTala
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='TalaElShohadaa' or (path[cnt-1]+path[cnt])=='ElShohadaaTala' :
            temp=ElShohadaaTala
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ElShohadaaShebin' or (path[cnt-1]+path[cnt])=='ShebinElShohadaa' :
            temp=ShebinElShohadaa
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ElShohadaaMenouf' or (path[cnt-1]+path[cnt])=='MenoufElShohadaa' :
            temp=MenoufElShohadaa
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='MenoufShanawan' or (path[cnt-1]+path[cnt])=='ShanawanMenouf' :
            temp=ShanawanMenouf
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShebinMenouf' or (path[cnt-1]+path[cnt])=='MenoufShebin' :
            temp=MenoufShebin
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='MenoufElHamoul' or (path[cnt-1]+path[cnt])=='ElHamoulMenouf' :
            temp=ElHamoulMenouf
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShanawanElBagour' or (path[cnt-1]+path[cnt])=='ElBagourShanawan' :
            temp=ElBagourShanawan
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='MenoufElBagour' or (path[cnt-1]+path[cnt])=='ElBagourMenouf' :
            temp=ElBagourMenouf
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShebinShanawan' or (path[cnt-1]+path[cnt])=='ShanawanShebin' :
            temp=ShanawanShebin
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ElSadatShebin' or (path[cnt-1]+path[cnt])=='ShebinElSadat' :
            temp=ShebinElSadat
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShebinMeleeg' or (path[cnt-1]+path[cnt])=='MeleegShebin' :
            temp=MeleegShebin
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='AshmounElSadat' or (path[cnt-1]+path[cnt])=='ElSadatAshmoun' :
            temp=ElSadatAshmoun
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShanawanElHamoul' or (path[cnt-1]+path[cnt])=='ElHamoulShanawan' :
            temp=ElHamoulShanawan
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='MeleegElHamoul' or (path[cnt-1]+path[cnt])=='ElHamoulMeleeg' :
            temp=ElHamoulMeleeg
            mycanv.itemconfig(temp,fill='green')
        cnt=cnt+1






b1 = Button(text='BFS' ,command=test ).pack(pady=5)
b3= Button(text='DFS' , command=test2).pack(pady=5)

b2 = Button(text='Try Again' ,command=reset ).pack()

#l = Label(text='hema' , fg='green' ).grid(row=2 , column=1)
window.mainloop()

"""
Spyder Editor

This is a temporary script file.
"""


runfile('C:/Users/noor/.spyder-py3/tttt.py', wdir='C:/Users/noor/.spyder-py3')
runfile('C:/Users/noor/Desktop/search.py', wdir='C:/Users/noor/Desktop')

## ---(Thu Dec  9 06:07:51 2021)---
runfile('C:/Users/noor/Desktop/AI Project.py', wdir='C:/Users/noor/Desktop')

## ---(Fri Dec 10 03:28:14 2021)---
runfile('C:/Users/noor/.spyder-py3/AI Project.py', wdir='C:/Users/noor/.spyder-py3')