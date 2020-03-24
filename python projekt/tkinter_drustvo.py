# za hitrejšni callback so vsa društva v slovarju "ročno"
slovar = {'Maribor': 200, 'Cerkno': 1, 'Dolenje Jezero': 1, 'Jazbina': 1,
          'Ljubljana': 464, 'Šempeter v Savinj. dolini': 3, 'Morje': 1,
          'Gornje Retje': 1, 'Cerknica': 11, 'Trbovlje': 28, 'Novo mesto': 48,
          'Koper': 48, 'Murska Sobota': 31, 'Ravne na Koroškem': 18, 'Kamnik': 13,
          'Prevalje': 3, 'Trebnje': 3, 'Vareja': 1, 'Nova vas': 2, 'Slovenske Konjice': 11,
          'Škofja Loka': 14, 'Slovenska vas': 1, 'Veliko Mlačevo': 1, 'Stahovica': 1,
          'Radovljica': 8, 'Dol pri Hrastniku': 3, 'Trzin': 7, 'Domžale': 17, 'Miren': 2,
          'Kočevje': 14, 'Poljana': 1, 'Kranj': 41, 'Fram': 3, 'Škale': 1, 'Rovte': 1, 'Velenje': 32,
          'Renče': 2, 'Nova Gorica': 15, 'Moščanci': 1, 'Bovec': 2, 'Loče': 1, 'Žalec': 11,
          'Lovrenc na Pohorju': 2, 'Javorje': 2, 'Stržišče': 1, 'Nazarje': 5, 'Vinska Gora': 2,
          'Gradišče': 1, 'Zgornja Polskava': 1, 'Tržič': 6, 'Mojstrana': 1, 'Jesenice': 9, 'Križe': 1,
          'Kebelj': 1, 'Ajdovščina': 10, 'Podboršt pri Komendi': 1, 'Ilirska Bistrica': 7, 'Postojna': 25,
          'Polhov Gradec': 1, 'Zgornje Jezersko': 3, 'Litija': 9, 'Mala Loka': 1, 'Krško': 20,
          'Brdo pri Lukovici': 1, 'Šmarje pri Jelšah': 5, 'Loke': 1, 'Rogaška Slatina': 3,
          'Celje': 87, 'Brežice': 10, 'Zagorje ob Savi': 16, 'Neverke': 1, 'Vrhnika': 7,
          'Ptuj': 23, 'Drenov Grič': 1, 'Logatec': 8, 'Solkan': 4, 'Okroglo': 1, 'Naklo': 3,
          'Medvode': 4, 'Polzela': 3, 'Šmartno ob Paki': 2, 'Uršna sela': 1, 'Bloška Polica': 2,
          'Bakovci': 2, 'Učakovci': 1, 'Vransko': 3, 'Vipava': 3, 'Ljutomer': 11, 'Mežica': 3,
          'Slovenska Bistrica': 9, 'Senovo': 3, 'Moravče': 1, 'Črna na Koroškem': 2, 'Šentjur': 12,
          'Dragomer': 3, 'Hrastnik': 10, 'Borovnica': 1, 'Pivka': 1, 'Kostanjevica na Krki': 2,
          'Gorica pri Slivnici': 2, 'Vojnik': 4, 'Vuzenica': 1, 'Sevnica': 8, 'Dobrovo': 1, 'Bistričica': 1,
          'Žirovnica': 1, 'Horjul': 1, 'Videm pri Ptuju': 1, 'Sveti Vid': 1, 'Markovci': 1, 'Podbrezje': 1,
          'Martjanci': 3, 'Višnja Gora': 2, 'Sv. Trojica v Slov. goricah': 1, 'Slovenj Gradec': 10,
          'Stari trg pri Ložu': 3, 'Mozirje': 3, 'Rimske Toplice': 1, 'Podčetrtek': 1, 'Razbor': 2, 'Muta': 4,
          'Podbrdo': 1, 'Sežana': 5, 'Črni Vrh': 1, 'Radeče': 3, 'Dobrna': 2, 'Starošince': 2, 'Lipa pri Frankolovem': 1,
          'Pševo': 2, 'Dobruša': 1, 'Črnomelj': 9, 'Tolmin': 7, 'Ranca': 1, 'Kamniška Bistrica': 1, 'Mala Mislinja': 1,
          'Grosuplje': 5, 'Galicija': 2, 'Podbočje': 1, 'Babinci': 1, 'Čemšenik': 1, 'Preddvor': 1, 'Dravograd': 5,
          'Brezje': 1, 'Šalovci': 1, 'Brezje pri Grosupljem': 2, 'Bistrica ob Sotli': 1, 'Breg pri Polzeli': 1,
          'Jakob pri Šentjurju': 1, 'Limbuš': 5, 'Pekre': 3, 'Velike Lašče': 1, 'Velika Štanga': 2, 'Mengeš': 4, 'Verd': 2,
          'Lesce': 1, 'Zaboršt': 2, 'Štorje': 1, 'Lendava': 13, 'Cirkulane': 3, 'Kobarid': 1, 'Sladka Gora': 1,
          'Mlinše': 3, 'Možjanca': 1, 'Lipje': 1, 'Veliki Kamen': 1, 'Semič': 2, 'Studeno': 2, 'Zrkovci': 1,
          'Železniki': 1, 'Gornja vas': 1, 'Strunjan': 1, 'Andrejci': 1, 'Dolane': 1, 'Šedem': 1, 'Beltinci': 7,
          'Kostanjek': 1, 'Žužemberk': 1, 'Prosečka vas': 1, 'Laze pri Dramljah': 1, 'Trnje': 1, 'Zbilje': 2,
          'Britof': 2, 'Hočko Pohorje': 4, 'Vnanje Gorice': 4, 'Ponoviče': 1, 'Izola': 8, 'Čadram': 1, 'Brestanica': 1,
          'Tržišče': 1, 'Škofljica': 2, 'Dobova': 2, 'Zagradec pri Grosupljem': 1, 'Ivanjkovci': 1, 'Gabrovka': 1,
          'Bertoki': 1, 'Begunje pri Cerknici': 2, 'Središče ob Dravi': 1, 'Dvor': 1, 'Njiverce': 1, 'Sromlje': 2,
          'Trška Gora': 1, 'Pilštanj': 1, 'Gornja Radgona': 8, 'Žetale': 2, 'Ljubno ob Savinji': 2, 'Laško': 5, 'Rova': 1,
          'Lavrica': 2, 'Stanjevci': 1, 'Brezovci': 1, 'Koblarji': 1, 'Iška': 1, 'Loka pri Žusmu': 1, 'Rožna Dolina': 2,
          'Arnače': 2, 'Žabnica': 2, 'Plintovec': 1, 'Selnica ob Dravi': 2, 'Mlaka': 1, 'Košiše': 1, 'Celestrina': 2, 'Krka': 1,
          'Poljčane': 1, 'Štatenberg': 1, 'Prečna': 1, 'Lukovica pri Domžalah': 1, 'Gotovlje': 1, 'Ruše': 9, 'Raka': 1,
          'Vidonci': 1, 'Lokovec': 2, 'Ormož': 7, 'Mala Nedelja': 1, 'Mali Kamen': 1, 'Kamnica': 3, 'Zapotok': 1, 'Dolenja vas': 1,
          'Velika Polana': 1, 'Babna Gora': 1, 'Barka': 1, 'Selnica ob Muri': 2, 'Ivančna Gorica': 1, 'Ribnica na Pohorju': 1,
          'Vitovlje': 1, 'Pesnica pri Mariboru': 1, 'Grajena': 1, 'Zalog pri Cerkljah': 1, 'Štore': 2, 'Črešnjice': 1,
          'Zgornja Selnica': 1, 'Radlje ob Dravi': 5, 'Bresternica': 2, 'Verače': 1, 'Središče': 1, 'Piran': 5, 'Ambrus': 1,
          'Dole pri Litiji': 1, 'Černelavci': 1, 'Kojsko': 1, 'Ankaran': 3, 'Dolga vas': 1, 'Miklavž na Dravskem polju': 4,
          'Podgorica': 1, 'Lopata': 1, 'Metlika': 6, 'Zgornja Bistrica': 1, 'Svečina': 1, 'Telče': 1, 'Veržej': 1,
          'Lokve': 3, 'Goričane': 1, 'Rakek': 3, 'Kriška vas': 1, 'Zlatoličje': 1, 'Črenšovci': 2, 'Suhi Vrh': 1,
          'Spodnji Kamenščak': 2, 'Grgarske Ravne': 1, 'Orehek': 1, 'Bukovje': 1, 'Most na Soči': 1, 'Dragočajna': 1,
          'Vanča vas': 1, 'Spodnja Idrija': 1, 'Otočec': 2, 'Rodik': 1, 'Bukovec': 1, 'Petrovče': 1, 'Šmarje': 1,
          'Cankova': 3, 'Idrija': 3, 'Svinjsko': 1, 'Podnanos': 1, 'Čentiba': 2, 'Žabče': 1, 'Smrečje': 1, 'Krnica': 2,
          'Šentjanž pri Dravogradu': 1, 'Šmarje-Sap': 1, 'Črneče': 1, 'Trnov Hrib': 1, 'Sv. Ema': 1, 'Braslovče': 2,
          'Velike Bloke': 1, 'Idrijske Krnice': 1, 'Goričice': 1, 'Bled': 3, 'Prosenjakovci': 2, 'Šmihel': 1, 'Videm': 1,
          'Štajngrova': 2, 'Komenda': 1, 'Žirovski Vrh Sv. Urbana': 1, 'Pivola': 1, 'Kromberk': 3, 'Robanov Kot': 1, 'Rakičan': 5,
          'Gorišnica': 1, 'Dornava': 3, 'Šentjanž': 1, 'Vače': 3, 'Topol pri Medvodah': 1, 'Pristava': 1, 'Gornji Grad': 2,
          'Sladki Vrh': 1, 'Lucija': 3, 'Ribnica': 2, 'Odranci': 1, 'Zgornje Poljčane': 1, 'Bohinjska Bistrica': 2, 'Stara Cerkev': 1,
          'Stara Loka': 3, 'Šmartno pri Slovenj Gradcu': 1, 'Spodnje Preloge': 1, 'Podturn pri Dol. Toplicah': 1, 'Bogojina': 2,
          'Velike Brusnice': 1, 'Laze': 1, 'Senožeti': 1, 'Ključarovci pri Ljutomeru': 1, 'Spodnje Dobrenje': 1, 'Spodnje Poljčane': 1,
          'Dragomelj': 1, 'Draga': 1, 'Gomilica': 1, 'Spodnja Rečica': 1, 'Radna': 1, 'Topolovec': 1, 'Zgornja Besnica': 1, 'Šoštanj': 5,
          'Šmartno': 1, 'Vitanje': 3, 'Vršnik': 1, 'Ravenska vas': 1, 'Renkovci': 1, 'Cerklje na Gorenjskem': 3, 'Zali Log': 1,
          'Lož': 1, 'Smlednik': 3, 'Ivanovci': 1, 'Lenart v Slov. goricah': 2, 'Krn': 1, 'Spodnji Duplek': 2, 'Kamnik pod Krimom': 1,
          'Osek': 1, 'Pohorje': 1, 'Dolina pri Lendavi': 2, 'Plitvica': 1, 'Spodnji Hotič': 1, 'Orle': 1, 'Rečica ob Savinji': 3,
          'Gornja Bistrica': 1, 'Gornji Lakoš': 1, 'Šempeter pri Gorici': 1, 'Pernica': 1, 'Pacinje': 1, 'Dobrava pri Konjicah': 1,
          'Smolnik': 1, 'Polica': 1, 'Jagodje': 2, 'Slovenski Javornik': 1, 'Dutovlje': 1, 'Češnjica pri Kropi': 1, 'Dobovec': 1,
          'Srednje Bitnje': 1, 'Mekinje': 1, 'Podgrad': 2, 'Hraše': 1, 'Arto': 1, 'Spodnja Polskava': 1, 'Hrvatini': 1, 'Rogatec': 1,
          'Brode': 1, 'Cven': 1, 'Šmarjeta': 1, 'Boben': 1, 'Hrastje': 1, 'Trčova': 1, 'Lipovci': 1, 'Hotiza': 2, 'Radenci': 3,
          'Spodnje Škofije': 2, 'Svibno': 1, 'Podkraj pri Zagorju': 1, 'Križni Vrh': 1, 'Sv. Lovrenc': 1, 'Planina': 1, 'Prebold': 3,
          'Bizeljsko': 1, 'Čušperk': 1, 'Šafarsko': 1, 'Podgorje': 1, 'Preserje pri Radomljah': 2, 'Varpolje': 1, 'Branik': 1,
          'Hrastovec v Slov. goricah': 1, 'Rakov Škocjan': 1, 'Radomlje': 1, 'Dobrovnik': 2, 'Polenci': 1, 'Hrovača': 1, 'Brje': 1,
          'Pomjan': 2, 'Lindek': 1, 'Kozarišče': 2, 'Črni Potok': 1, 'Spodnje Hoče': 2, 'Gozd Martuljek': 1, 'Solčava': 1, 'Straža': 1,
          'Mlajtinci': 1, 'Zgornje Pirniče': 1, 'Suhor': 1, 'Zgornje Bitnje': 1, 'Legen': 2, 'Podlog v Savinjski dolini': 1,
          'Oplotnica': 1, 'Kampel': 1, 'Škofja vas': 1, 'Logarovci': 1, 'Skoke': 1, 'Slivnica pri Mariboru': 1,
          'Brezje pri Šentjerneju': 1, 'Spodnji Brnik': 1, 'Nova vas pri Mokricah': 1, 'Teharje': 1, 'Lukovica pri Brezovici': 2,
          'Podcerkev': 1, 'Zgornje Škofije': 1, 'Golnik': 1, 'Veliki Otok': 1, 'Podgozd': 1, 'Čatež ob Savi': 1, 'Metulje': 1,
          'Ribniško selo': 1, 'Brezovska Gora': 1, 'Podvinje': 1, 'Kidričevo': 1, 'Portorož': 1, 'Rače': 1, 'Zgornja Hajdina': 1,
          'Zgornje Laže': 1, 'Kranjska Gora': 1, 'Fala': 1, 'Lucova': 1, 'Potok': 1, 'Loka pri Mengšu': 1, 'Levec': 1, 'Zbigovci': 1,
          'Srednje Jarše': 1, 'Kanji Dol': 1, 'Vinje': 1, 'Vodice': 1, 'Velesovo': 1, 'Zgornja Jablanica': 1, 'Tolsti Vrh pri Mislinji': 1,
          'Šentjungert': 1, 'Selo pri Vodicah': 1, 'Lendavske Gorice': 1, 'Kastelec': 1, 'Laze pri Gobniku': 1, 'Spodnji Slemen': 1,
          'Kropa': 1, 'Nova vas nad Dragonjo': 1, 'Kubed': 1, 'Strmec': 1, 'Dvorjane': 1}
from tkinter import *

class Stevilo():
    def __init__(self, master):
        # Dodamo widget z "navodilom
        vprasanje = Label(master, text = 'Vtipkajte ime Slovensjega mesta')
        vprasanje.grid(row = 0, column = 0) # določim še položaj
        # Dodamo polje za vnos in predpostavimo da za vsa mesta, ki niso v slovarju odgovor 0
        # Za ta polje potrebujem dva widgeta
        self.ime = StringVar(master, value = None)
        polje_ime = Entry(master, textvariable = self.ime)
        polje_ime.grid(row = 1, column = 0)
        # Ustvarimo gumb da se program zažene
        gumb = Button(master, text = 'Koliko društev ima to mesto?', command = self.isci)
        gumb.grid(row = 2, column = 0)
        # Sedaj pa še polje za odgovor tamora biti IntVar saj bo odgovor celo število
        self.rezultat = IntVar(master, value = 0)
        polje_rezultat = Label(master, textvariable = self.rezultat)
        polje_rezultat.grid(row = 3, column = 0)
    def isci(self):
        '''
            vrne število društeev v tem mestu če jih ta nima vrne 0
        '''
        if self.ime.get() in slovar:
            self.rezultat.set(slovar[self.ime.get()])
        else:
            self.rezultat.set(0)




root = Tk()
aplikacija = Stevilo(root)
root.geometry("250x250")
root.title('Društva:')
root.mainloop()