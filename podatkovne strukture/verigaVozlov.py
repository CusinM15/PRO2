class Vozel:
    '''
    Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
    '''
    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

class VerizniSeznam:
    '''
    Razred, ki predstavlja verižni seznam z začetkom in koncem.
    '''
    def __init__(self):
        self._dolzina = 0
        self._zacetek = None
        self._konec = None

    def __str__(self):
        niz = ''
        vozel = self._zacetek
        while vozel is not None:
            niz += '{} -> '.format(repr(vozel.podatek))
            vozel = vozel.naslednji
        return niz + '•'

    def vstavi_na_zacetek(self, x):
        '''
            doda nov vozel na začetku
        '''
        self._dolzina += 1
        if self._zacetek is None:
            veriga = Vozel(x)
            self._zacetek = veriga
            self._konec = veriga
        else:
            veriga = Vozel(x, self._zacetek)
            self._zacetek = veriga

    def zacetek(self):
        '''
            vrne vrednost prvega vozla
        '''
        if self._zacetek is None:
            raise IndexError('Verižni seznam je prazen')
        else:
            return self._zacetek.podatek

    def izbrisi_zacetek(self):
        '''
            odstrani začetni vozel
        '''
        self._dolzina -= 1
        if self._zacetek is None:
                raise IndexError('Verižni seznam je prazen')
        elif self._zacetek == self._konec:
            self._zacetek = None 
            self._konec = None
        else:
            self._zacetek = self._zacetek.naslednji

    def vstavi_na_konec(self, x):
        '''
            doda vozel x na koncu verige
        '''
        self._dolzina += 1
        if self._zacetek is None:
            nov = Vozel(x) 
            self._zacetek = nov
            self._konec = nov
        else:
            konec = self._konec
            nov = Vozel(x)
            konec.naslednji = nov
            self._konec = nov

    def konec(self):
        '''
            vrne vrednost zadnjega vozla
        ''' 
        if self._zacetek is None:
            raise IndexError('Verižni seznam je prazen')
        else:
            return self._konec.podatek

    def izbrisi_konec(self):
        '''
            izbriše zadnji vozel veriznega vozla
        '''
        self._dolzina -= 1
        if self._zacetek is None:
                raise IndexError('Verižni seznam je prazen')
        elif self._zacetek == self._konec:
            self._zacetek = None 
            self._konec = None
        else:
            pom = self._zacetek
            while pom.naslednji != self._konec:
                pom = pom.naslednji
            pom.naslednji = None
            self._konec = pom

    def je_prazen(self):
        '''
            vrne True/False
        '''
        return self._zacetek is None

    def dolzina(self):
        '''
            vrne dolžino verige
        '''
        return self._dolzina

    def filtriraj(self, f):
        '''
            izbriše iz verižnega seznama, pri katerih je f(vrednost) == False
        '''
        dolzina = self._dolzina
        self._dolzina = 0
        while dolzina != 0:
            x = self._zacetek.podatek
            if  f(x):
                self.vstavi_na_konec(x)
                # dodamo na konec verige
                # dolžino ustrezno poveča vstavi_na_konec
            dolzina = dolzina - 1
            # zmanšamo dolžino
            self.izbrisi_zacetek
            # tega rabimo odstraviti smo ga pa šeenkrat vstavili
            self._zacetek = self._zacetek.naslednji
        
    def __lt__(self, other):
        '''
            primerja najprej po velikosti, v primeru enakosti pa leksikografsko  
        '''
        leva = self.dolzina()
        desna = other.dolzina()
        if leva < desna:
            return True
        elif leva > desna:
            return False
        else:
            # pomeni enako dolgi verigi
            rezultat = None
            for _ in range(leva):
                x = self.zacetek()
                y = other.zacetek()
                if rezultat is None:
                    # pomeni da moramo še primerjati, ni pa treba vseh pregledati
                    if x < y:
                        rezultat = True
                    elif x > y:
                        rezultat = False
                self.izbrisi_zacetek()
                self.vstavi_na_konec(x)
                # dolžino povečam in zmanšam hkrati, pa največ bodo enkrat zakrožili
                other.izbrisi_zacetek()
                other.vstavi_na_konec(y)
            return rezultat 