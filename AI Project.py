
import tkinter as tk
from tkinter import *
from tkinter import ttk
from queue import Queue

#GUI
window = Tk()
window.geometry('600x600')
window.title('search algorithm')


mycanv= Canvas(window,width=400,height=400, bg="white")
mycanv.pack()

TalaShebin=mycanv.create_line(45,45,175,175,width=4)
TalaElShohadaa = mycanv.create_line(45,45,145,45,width=4)
Tala=mycanv.create_oval(25,25,65,65,fill="black")
mycanv.create_text(30,75,text="Tala",fill="blue")


ElShohadaaShebin =mycanv.create_line(145,45,175,175,width=4)
ElShohadaa= mycanv.create_oval(125,25,165,65,fill="black")
mycanv.create_text(145,15,text="El Shohadaa",fill="blue")

ElShohadaaMenouf= mycanv.create_line(145,45,275,60,width=4)
MenoufShanawan= mycanv.create_line(275,60,260,270,width=4)
ShebinMenouf= mycanv.create_line(275,60,175,175,width=4)
MenoufElHamoul = mycanv.create_line(275,60,350,360,width=4)
MenoufElBagour= mycanv.create_line(275,60,365,190,width=4)
Menouf = mycanv.create_oval(255,40,295,80,fill="black")
mycanv.create_text(275,30,text="Menouf",fill="blue")

ShanawanElBagour= mycanv.create_line(260,270,365,190,width=4)
ElBagour = mycanv.create_oval(345,170,385,210,fill="black")
mycanv.create_text(375,160,text="El Bagour",fill="blue")

ShebinShanawan= mycanv.create_line(175,175,260,270,width=4)
ElSadatShebin= mycanv.create_line(175,175,55,210,width=4)
ShebinMeleeg= mycanv.create_line(175,175,140,280,width=4)
Shebin= mycanv.create_oval(155,155,195,195,fill="black")
mycanv.create_text(130,165,text="Shebin",fill="blue")

AshmounElSadat= mycanv.create_line(55,210,35,360,width=4)
ElSadat= mycanv.create_oval(35,190,75,230,fill="black")
mycanv.create_text(45,180,text="El Sadat",fill="blue")


Ashmoun= mycanv.create_oval(15,340,55,380,fill="black")
mycanv.create_text(85,365,text="Ashmoun",fill="blue")

ShanawanElHamoul= mycanv.create_line(260,270,350,360,width=4)
Shanawan= mycanv.create_oval(240,250,280,290,fill="black")
mycanv.create_text(210,270,text="Shanawan",fill="blue")

MeleegElHamoul= mycanv.create_line(140,280,350,360,width=4)
Meleeg= mycanv.create_oval(120,260,160,300,fill="black")
mycanv.create_text(97,270,text="Meleeg",fill="blue")


ElHamoul= mycanv.create_oval(330,340,370,380,fill="black")
mycanv.create_text(300,370,text="El Hamoul",fill="blue")

    
#ALGORITHMS
def bfs(start_node, target_node):
    adj_list={
            'Tala':['ElShohadaa','Shebin'],
            'ElShohadaa':['Menouf','Tala','Shebin'],
            'Shebin':['ElShohadaa','Menouf','Tala','Shanawan','Meleeg','ElSadat'],
            'Menouf':['ElShohadaa','Shebin','Shanawan','ElBagour','ElHamoul'],
            'ElSadat':['Shebin','Ashmoun'],
            'ElBagour':['Menouf','Shanawan'],
            'Shanawan':['Shebin','ElBagour','ElHamoul','Menouf'],
            'ElHamoul':['Menouf','Shanawan','Meleeg'],
            'Meleeg':['Shebin','ElHamoul'],
            'Ashmoun':['ElSadat']
            }
    # Set of visited nodes to prevent loops
    visited = set()
    queue = Queue()

    # Add the start_node to the queue and visited list
    queue.put(start_node)
    visited.add(start_node)
    
    # start_node has not parents
    parent = dict()
    parent[start_node] = None

    # Perform step 3
    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == target_node:
            path_found = True
            break

        for next_node in adj_list[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)
                
    # Path reconstruction
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node]) 
            target_node = parent[target_node]
        path.reverse()
    return path

def dfs2(start, target,paths,visited=set()):
    route=[]
    
    def dfs( start, target, paths, visited = set()):
        adj_list = {
               'Tala':['ElShohadaa','Shebin'],
                'ElShohadaa':['Menouf','Tala','Shebin'],
                'Shebin':['ElShohadaa','Menouf','Tala','Shanawan','Meleeg','ElSadat'],
                'Menouf':['ElShohadaa','Shebin','Shanawan','ElBagour','ElHamoul'],
                'ElSadat':['Shebin','Ashmoun'],
                'ElBagour':['Menouf','Shanawan'],
                'Shanawan':['Shebin','ElBagour','ElHamoul','Menouf'],
                'ElHamoul':['Menouf','Shanawan','Meleeg'],
                'Meleeg':['Shebin','ElHamoul'],
                'Ashmoun':['ElSadat']
                }
        paths.append(start)
        route.append(start)
        visited.add(start)
        if start == target:
            return paths
        for neighbour in adj_list[start]:
            if neighbour not in visited:
                result = dfs( neighbour, target, paths, visited)
                if result is not None:
                    return result
        paths.pop()
        return None
    route=dfs(start,target,paths,visited=set())
    return route


class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        H = {
            'Tala': 1,
            'ElShohadaa': 1,
            'Shebin': 1,
            'Menouf': 1,
            'ElSadat': 1,
            'ElBagour': 1,
            'Shanawan': 1,
            'ElHamoul': 1,
            'Meleeg': 1,
            'Ashmoun': 1
        }
 
        return H[n]
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                
                return reconst_path
 
            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None
   
def astar():
    adj_list={
            'Tala':[('ElShohadaa',100.00 ),('Shebin', 183.85)],
            'ElShohadaa':[('Menouf', 130.86),('Tala', 100.00),('Shebin', 133.42)],
            'Shebin':[('ElShohadaa', 133.42),('Menouf', 152.40),('Tala', 183.85),('Shanawan', 127.48),('Meleeg', 110.68),('ElSadat', 125.00)],
            'Menouf':[('ElShohadaa', 130.86),('Shebin', 152.40),('Shanawan', 210.54),('ElBagour', 158.11),('ElHamoul', 309.23)],
            'ElSadat':[('Shebin', 125.00),('Ashmoun', 151.33)],
            'ElBagour':[('Menouf', 158.11),('Shanawan', 132.00)],
            'Shanawan':[('Shebin', 127.48),('ElBagour', 132.00),('ElHamoul', 127.28),('Menouf', 210.54)],
            'ElHamoul':[('Menouf', 309.23),('Shanawan', 127.28),('Meleeg', 224.72)],
            'Meleeg':[('Shebin', 110.68),('ElHamoul', 224.72)],
            'Ashmoun':[('ElSadat', 151.33)]
            }
    graph1=Graph(adj_list)
    path=[]
    path= graph1.a_star_algorithm(start.get(),end.get())
    iterate(path)
    
    
label =Label(text='From : ').pack()
start=tk.StringVar()
combo=ttk.Combobox(window,textvariable = start)
combo.pack()
combo.config(values=('ElShohadaa','Ashmoun','Menouf','Tala','Shanawan','Meleeg','ElSadat','Shebin','ElBagour','ElHamoul'))


label2 =Label(text='To : ').pack()
end=tk.StringVar()
combo2=ttk.Combobox(window, textvariable = end)
combo2.pack()
combo2.config(values=('ElShohadaa','Ashmoun','Menouf','Tala','Shanawan','Meleeg','ElSadat','Shebin','ElBagour','ElHamoul'))


def reset():
    
    mycanv.itemconfig(Tala,fill='black')
    mycanv.itemconfig(ElShohadaa,fill='black')
    mycanv.itemconfig(Menouf,fill='black')
    mycanv.itemconfig(ElBagour,fill='black')
    mycanv.itemconfig(Shebin,fill='black')
    mycanv.itemconfig(ElSadat,fill='black')
    mycanv.itemconfig(Ashmoun,fill='black')
    mycanv.itemconfig(Shanawan,fill='black')
    mycanv.itemconfig(Meleeg,fill='black')
    mycanv.itemconfig(ElHamoul,fill='black')
    
    mycanv.itemconfig(TalaShebin,fill='black')
    mycanv.itemconfig(TalaElShohadaa,fill='black')
    mycanv.itemconfig(ElShohadaaShebin,fill='black')
    mycanv.itemconfig(ElShohadaaMenouf,fill='black')
    mycanv.itemconfig(MenoufShanawan,fill='black')
    mycanv.itemconfig(ShebinMenouf,fill='black')
    mycanv.itemconfig(MenoufElHamoul,fill='black')
    mycanv.itemconfig(ShanawanElBagour,fill='black')
    mycanv.itemconfig(MenoufElBagour,fill='black')
    mycanv.itemconfig(ShebinShanawan,fill='black')
    mycanv.itemconfig(ElSadatShebin,fill='black')
    mycanv.itemconfig(ShebinMeleeg,fill='black')
    mycanv.itemconfig(AshmounElSadat,fill='black')
    mycanv.itemconfig(ShanawanElHamoul,fill='black')
    mycanv.itemconfig(MeleegElHamoul,fill='black')


def iterate(way):
    path=way
    temp=""
    cnt=1
    for i in path:
        if i=='Ashmoun' :
            temp=Ashmoun
            mycanv.itemconfig(temp,fill='green')
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
            temp=TalaShebin
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='TalaElShohadaa' or (path[cnt-1]+path[cnt])=='ElShohadaaTala' :
            temp=TalaElShohadaa
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ElShohadaaShebin' or (path[cnt-1]+path[cnt])=='ShebinElShohadaa' :
            temp=ElShohadaaShebin
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ElShohadaaMenouf' or (path[cnt-1]+path[cnt])=='MenoufElShohadaa' :
            temp=ElShohadaaMenouf
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='MenoufShanawan' or (path[cnt-1]+path[cnt])=='ShanawanMenouf' :
            temp=MenoufShanawan
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShebinMenouf' or (path[cnt-1]+path[cnt])=='MenoufShebin' :
            temp=ShebinMenouf
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='MenoufElHamoul' or (path[cnt-1]+path[cnt])=='ElHamoulMenouf' :
            temp=MenoufElHamoul
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShanawanElBagour' or (path[cnt-1]+path[cnt])=='ElBagourShanawan' :
            temp=ShanawanElBagour
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='MenoufElBagour' or (path[cnt-1]+path[cnt])=='ElBagourMenouf' :
            temp=MenoufElBagour
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShebinShanawan' or (path[cnt-1]+path[cnt])=='ShanawanShebin' :
            temp=ShebinShanawan
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ElSadatShebin' or (path[cnt-1]+path[cnt])=='ShebinElSadat' :
            temp=ElSadatShebin
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShebinMeleeg' or (path[cnt-1]+path[cnt])=='MeleegShebin' :
            temp=ShebinMeleeg
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='AshmounElSadat' or (path[cnt-1]+path[cnt])=='ElSadatAshmoun' :
            temp=AshmounElSadat
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='ShanawanElHamoul' or (path[cnt-1]+path[cnt])=='ElHamoulShanawan' :
            temp=ShanawanElHamoul
            mycanv.itemconfig(temp,fill='green')
        if (path[cnt-1]+path[cnt])=='MeleegElHamoul' or (path[cnt-1]+path[cnt])=='ElHamoulMeleeg' :
            temp=MeleegElHamoul
            mycanv.itemconfig(temp,fill='green')
        cnt=cnt+1
    

def test2():
    helps=list()
    path=[]
    path=dfs2(start.get(),end.get(),helps)
    iterate(path)

def test():
    path=[]
    path=bfs(start.get(),end.get())
    iterate(path)
 
def astar():
    adj_list={
            'Tala':[('ElShohadaa',100.00 ),('Shebin', 183.85)],
            'ElShohadaa':[('Menouf', 130.86),('Tala', 100.00),('Shebin', 133.42)],
            'Shebin':[('ElShohadaa', 133.42),('Menouf', 152.40),('Tala', 183.85),('Shanawan', 127.48),('Meleeg', 110.68),('ElSadat', 125.00)],
            'Menouf':[('ElShohadaa', 130.86),('Shebin', 152.40),('Shanawan', 210.54),('ElBagour', 158.11),('ElHamoul', 309.23)],
            'ElSadat':[('Shebin', 125.00),('Ashmoun', 151.33)],
            'ElBagour':[('Menouf', 158.11),('Shanawan', 132.00)],
            'Shanawan':[('Shebin', 127.48),('ElBagour', 132.00),('ElHamoul', 127.28),('Menouf', 210.54)],
            'ElHamoul':[('Menouf', 309.23),('Shanawan', 127.28),('Meleeg', 224.72)],
            'Meleeg':[('Shebin', 110.68),('ElHamoul', 224.72)],
            'Ashmoun':[('ElSadat', 151.33)]
            }
    graph1=Graph(adj_list)
    path=[]
    path= graph1.a_star_algorithm(start.get(),end.get())
    iterate(path)
          
    
b1 = Button(text='BFS' ,command=test ,activebackground='green').pack(pady=5)
b3= Button(text='DFS' , command=test2 , activebackground='green').pack(pady=5)
b4= Button(text='A*' , command=astar ,activebackground='green').pack(pady=5)


b2 = Button(text='Try Again' ,command=reset , bg='gray', activebackground='red').place(x=350,y=530)


window.mainloop()


