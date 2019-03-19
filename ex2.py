class otziv:
    def __init__(self,comment):
        self.comment=comment

class book:
    def __init__(self,name,avtor,god,zhanr):
        self.name=name
        self.avtor=avtor
        self.god=god
        self.zhanr=zhanr
        self.otzivi=[]
    def __eq__(self, other):
        return self is other
    def __ne__(self, other):
        return self is not other
    def __repr__(self):
        return 'name = %s  avtor = %s'%(self.name,self.avtor)
    def __str__(self):
        pisma=''
        for h in self.otzivi:
            pisma+=h.comment+'; '
        return 'name = %s  Zhanr = %s  OTZIV => %s'%(self.name,self.zhanr,pisma)
    def mnenie(self,pishi):
        self.otzivi.append(otziv(pishi))


book1=book('vojna','TOLSTOJ',1844,'roman')
book2=book('prestuplenie','Dostoevskij',1944,'drama')
book3=book('gore','gogol',2000,'komedia')
print(book1)
print(book2)
print(book3)
print('book1=book2 {}'.format(book1 == book2))
print('book2!=book3 {}'.format(book2!=book3))
book1.mnenie('lazha')
print(book1)
book1.mnenie('syper')
print(book1)