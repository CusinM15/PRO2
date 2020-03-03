class drustvo:
    def __init__(self, sez):
        self.maticna = sez[0]
        self.ime = sez[1]
        self.mesto = sez[2]
        self.naziv = sez[4]
        self.dejavnost = sez[6]
        self.datum = sez[7]
        self.zap_ste = sez[8]
        self.aktivnost = sez[10]
        self.naslov = sez[11]
        self.prosto = sez[13]
    def __str__(self):
        return self.mesto
    def __repr__(self):
        return self.mesto + ', ' + self.prosto
        
    
    '''def nahajajo(self):
        if 'Maribor' == self.naslov:
            pass'''

vsa_dru = list()
k = [['5921449000', 'VZGOJNO-IZOBRAŽEVALNI ZAVOD ANTONA MARTINA SLOMŠKA MARIBOR', 'Maribor', '354', 'Zavod', '85.310', 'Srednješolsko splošno izobraževanje', '2012-03-22T00:00:00', '1481', '070', 'DA', 'Vrbanska cesta 30, 2000 Maribor', '2000', 'NE'], ['5258669000', 'KULTURNO UMETNIŠKO DRUŠTVO CERKNO', 'Cerkno', '453', 'Društvo, zveza društev', '90.030', 'Umetniško ustvarjanje', '2011-11-18T00:00:00', '1242', '014', 'DA', 'Bevkova ulica 9, 5282 Cerkno', '5282', 'NE'], ['1331647000', 'JEZERSKI HRAM Zavod za ohranjanje naravne in kulturne dediščine, Cerknica', 'Dolenje Jezero', '354', 'Zavod', '91.030', 'Varstvo kulturne dediščine', '2012-01-06T00:00:00', '1338', '013', 'DA', 'Dolenje Jezero 1 E, 1380 Cerknica', '1380', 'NE'], ['5152801000', 'LOVSKA DRUŽINA POGOREVC ČRNA NA KOROŠKEM', 'Jazbina', '453', 'Društvo, zveza društev', '01.700', 'Lovstvo', '2011-10-03T00:00:00', '1158', '016', 'DA', 'Jazbina 9, 2393 Črna na Koroškem', '2393', 'NE'], ['3655822000', 'Študentska svetovalnica Študentske organizacije Univerze v Ljubljani, Zavod za svetovalne dejavnosti', 'Ljubljana', '354', 'Zavod', '58.110', 'Izdajanje knjig', '2011-10-24T00:00:00', '1179', '061', 'DA', 'Kersnikova ulica 4, 1000 Ljubljana', '1000', 'NE'], ['5118921000', 'TURISTIČNO DRUŠTVO ŠEMPETER V SAVINJSKI DOLINI', 'Šempeter v Savinj. dolini', '453', 'Društvo, zveza društev', '91.030', 'Varstvo kulturne dediščine', '2012-09-05T00:00:00', '1753', '190', 'DA', 'Ob rimski nekropoli 2, 3311 Šempeter v S000', 'USTANOVA IMAGO SLOVENIAE - PODOBA SLOVENIJE', 'Ljubljana', '401', 'Ustanova', '90.010', 'Umetniško uprizarjanje', '2012-09-27T00:00:00', '1767', '061', 'DA', 'Gornji trg 16, 1000 Ljubljana', '1000', 'NE'], ['1454099000', 'PARNAS Zavod za kulturo in turizem, Velike Lašče', 'Gornje Retje', '354', 'Zavod', '91.030', 'Varstvo kulturne dediščine', '2011-10-28T00:00:00', '1201', '134', 'DA', 'Gornje Retje 3, 1315 Velike Lašče', '1315', 'NE'], ['5858020000', 'PAJN Zavod za sonaravno bivanje', 'Cerknica', '354', 'Zavod', '90.030', 'Umetniško ustvarjanje', '2014-03-20T00:00:00', '2667', '013', 'DA', 'Videm 2 A, 1380 Cerknica', '1380', 'NE'], ['6428703000', 'Zavod za kulturo, šport, turizem in mladinsko dejavnost Trbovlje, socialno podjetje', 'Trbovlje', '354', 'Zavod', '55.201', 'Počitniški domovi in letovišča', '2014-02-25T00:00:00', '2630', '129', 'DA', 'Šuštarjeva kolonija 27, 1420 Trbovlje', '1420', 'NE']]
for i in range(len(k)):
    k[i][1] = drustvo(k[i])
    vsa_dru.append(k[i][1])

for i in vsa_dru:
    print(repr(i))



