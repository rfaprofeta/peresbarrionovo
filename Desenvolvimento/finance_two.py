#!/home/rfa/anaconda3/bin/python3
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
plt.style.use('seaborn-poster')
plt1.style.use('bmh')

def plot_two(query):
	r = requests.get("https://finance.google.com/finance/getprices", params=query)
	lines = r.text.splitlines()
	new_index = []
	new_value = []
	basetime = 0
	for price in lines:
		cols = price.split(",")
		if cols[0][0] == 'a':
			basetime = int(cols[0][1:])
			new_index.append(datetime.fromtimestamp(basetime))
			new_value.append([float(cols[1])])			
		elif cols[0][0].isdigit():
			date = basetime + (int(cols[0])*int(query['i']))
			new_index.append(datetime.fromtimestamp(date))
			new_value.append([float(cols[1])])
	return new_index,new_value
			
def plot_one(queries, period, interval):
	for query in queries:
		query['i'] = interval
		query['p'] = period
		r = requests.get("https://finance.google.com/finance/getprices", params=query)
		lines = r.text.splitlines()
		index = []
		value = []
		basetime = 0
		for price in lines:
			cols = price.split(",")
			if cols[0][0] == 'a':
				basetime = int(cols[0][1:])
				date = basetime
				value.append([float(cols[1])])
				index.append(datetime.fromtimestamp(date))
			elif cols[0][0].isdigit():
				date = basetime + (int(cols[0])*int(query['i']))
				value.append([float(cols[1])])
				index.append(datetime.fromtimestamp(date))
	return index,value
	
	
lista={"Abbott":"ABTT34","Abbvie DRN":"ABBV34","ABC Brasil":"ABCB4","Accenture":"ACNB34","Aco Altona":"EALT3","Aco Altona":"EALT4","Advanced-DH":"ADHM3","AES Elpa":"AELP3","AES Tietê":"TIET3","AES Tietê":"TIET4","AES Tietê":"TIET11","Aetna Inc DRN":"AETB34","Afluente T ":"AFLT3","Andrade Gutierrez":"ANDG3B","AG Concessões":"ANDG4B","AG Part":"CANT3B","AG Part":"CANT4B","Aig Group DRN":"AIGB34","Alef":"ALEF3B","Alfa Consorc ON":"BRGE3","Alfa Consorc":"BRGE5","Alfa Consorc":"BRGE6","Alfa Consorc":"BRGE7","Alfa Consorc":"BRGE8","Alfa Consorc":"BRGE11","Alfa Consorc":"BRGE12","Financeira Alfa":"CRIV3","Financeira Alfa":"CRIV4","Alfa Holding":"RPAD3","Alfa Holding":"RPAD5","Alfa Holding":"RPAD6","Alfa Invest":"BRIV3","Alfa Invest":"BRIV4","Aliansce":"ALSC3","Aliperti":"APTI3","Aliperti":"APTI4","ALL Norte":"FRRN3B","ALL Norte":"FRRN5B","ALL Norte":"FRRN6B","Alliar ON":"AALR3","Alpargatas":"ALPA3","Alpargatas":"ALPA4","Alphabet DRN":"GOGL34","Alphabet DRN":"GOGL35","Alupar":"ALUP3","Alupar":"ALUP4","Alupar":"ALUP11","Amazon":"AMZO34","Amazonia":"BAZA3","Ambev":"ABEV3","American Air DRN":"AALL34","American Express":"AXPB34","Amgen":"AMGN34","Ampla Energ":"CBEE3","Anima":"ANIM3","Apple":"AAPL34","ArcelorMittal":"ARMT34","Arconic DRN":"ARNC34","Arezzo":"ARZZ3","Atompar":"ATOM3","Att Inc DRN":"ATTB34","Avon":"AVON34","Azevedo":"AZEV3","Azevedo":"AZEV4","Azul":"AZUL4","B2W":"BTOW3","Bahema":"BAHI3","Banco Pan":"BPAN4","Banese":"BGIP3","Banese":"BGIP4","Banestes":"BEES3","Banestes":"BEES4","Bank America":"BOAC34","Banpara":"BPAR3","Banrisul":"BRSR3","Banrisul":"BRSR5","Banrisul":"BRSR6","Santander DR3":"BSAN33","Bardella":"BDLL3","Bardella":"BDLL4","Battistella":"BTTL3","Battistella":"BTTL4","Baumer":"BALM3","Baumer":"BALM4","BB Seguridade":"BBSE3","Bdru BDR":"BDRU11","Bdrx BDR":"BDRX11","Berkshire DRN":"BERK34","Best Buy DRN":"BBYY34","Betapart":"BETP3B","Bic Monark":"BMKS3","Biogen DRN":"BIIB34","Biomm":"BIOM3","Biomm ON":"BIOM9","Biosev DIR":"BSEV1","Biosev":"BSEV3","Blackrock DRN":"BLAK34","BNY Mellon":"BONY34","Boeing":"BOEI34","Bombril":"BOBR3","Bombril":"BOBR4","Bonaire Part":"BNPA3B","Boston Prop DRN":"BOXP34","Br Brokers":"BBRK3","BR Home":"HCBR3","BR Insurance":"BRIN3","BR Malls Par":"BRML3","BR Pharma":"BPHA3","BR Properties":"BRPR3","Bradesco":"BBDC3","Bradesco":"BBDC4","Bradespar":"BRAP3","Bradespar":"BRAP4","Banco do Brasil":"BBAS3","Brasilagro":"AGRO3","Braskem":"BRKM3","Braskem":"BRKM5","Braskem":"BRKM6","Brazilian FR":"BFRE11","Brazilian FR":"BFRE12","Banco BRB":"BSLI3","Banco BRB":"BSLI4","BRF":"BRFS3","Bristol Myers":"BMYB34","BRQ":"BRQB3","BTG Pactual":"BPAC3","BTG Pactual":"BPAC5","Btgp Banco UNT":"BPAC11","Cabinda Part":"CABI3B","Caconde Part":"CACO3B","Caianda Part":"CAIA3B","Cambuci":"CAMB3","Cambuci":"CAMB4","Camil":"CAML3","Capitalpart":"CPTP3B","Carrefour BR":"CRFB3","Casan":"CASN3","Casan":"CASN4","Caterpillar":"CATP34","CCR":"CCRO3","CCX Carvão":"CCXC3","CEB":"CEBR3","CEB":"CEBR5","CEB":"CEBR6","Cedro":"CEDO3","Cedro":"CEDO4","CEEE-D":"CEED3","CEEE-D":"CEED4","CEEE-GT":"EEEL3","CEEE-GT":"EEEL4","CEG":"CEGR3","Celesc":"CLSC3","Celesc":"CLSC4","Celgene Corp":"CLGN34","Celgpar":"GPAR3","Celpa":"CELP3","Celpa":"CELP5","Celpa":"CELP6","Celpa":"CELP7","Celpe":"CEPE3","Celpe":"CEPE5","Celpe":"CEPE6","Celulose Irani":"RANI3","Celulose Irani":"RANI4","Cemar":"ENMA3B","Cemar":"ENMA5B","Cemar":"ENMA6B","Cemepe":"MAPT3","Cemepe":"MAPT4","Cemig":"CMIG3","Cemig":"CMIG4","CESP":"CESP3","CESP":"CESP5","CESP":"CESP6","Chesapeake DRN":"CHKE34","Chevron":"CHVX34","Cia Hering":"HGTX3","Cielo":"CIEL3","Cims":"CMSA3","Cims":"CMSA4","Cinesystem":"CNSY3","Cisco":"CSCO34","Citigroup":"CTGP34","Coca Cola":"COCA34","Coelba":"CEEB3","Coelba":"CEEB5","Coelba":"CEEB6","COELCE":"COCE3","COELCE":"COCE5","COELCE":"COCE6","Cognizant DRN":"CTSH34","Colgate":"COLG34","Comcast":"CMCS34","Comgas":"CGAS3","Comgas":"CGAS5","Conc Rio Ter":"CRTE3B","Conc Rio Ter":"CRTE5B","Const A Lind":"CALI3","Const A Lind":"CALI4","Copasa":"CSMG3","Copel":"CPLE3","Copel":"CPLE5","Copel":"CPLE6","Cophillips":"COPH34","Cor Ribeiro":"CORR3","Cor Ribeiro":"CORR4","Cosan Log":"RLOG3","Cosan Ltd":"CZLT33","Cosan":"CSAN3","Cosern":"CSRN3","Cosern":"CSRN5","Cosern":"CSRN6","Costco DRN":"COWC34","Coteminas":"CTNM3","Coteminas":"CTNM4","Coty Inc":"COTY34","CPFL Energia":"CPFE3","CPFL Renovav":"CPRE3","CR2":"CRDE3","Cremer":"CREM3","Cristal":"CRPG5","Cristal":"CRPG6","CSU Cardsyst":"CARD3","Ctc S.A. ON":"CTCA9","CTC S/A":"CTCA3","CVC Brasil":"CVCB3","Cvs Health DRN":"CVSH34","Cyre Com":"CCPR3","Cyrela":"CYRE3","Danaher Corp":"DHER34","Dasa":"DASA3","Delta DRN":"DEAI34","Dimed":"PNVL3","Dimed":"PNVL4","Direcional":"DIRR3","Dohler":"DOHL3","Dohler":"DOHL4","Dommo Energia":"DMMO3","DTCOM Direct":"DTCY3","DTCOM Direct":"DTCY4","Dufry":"DAGB33","Duke Energy DRN":"DUKB34","Duratex":"DTEX3","Ebay":"EBAY34","Ecorodovias":"ECOR3","Elekeiroz":"ELEK3","Elekeiroz":"ELEK4","Elektro":"EKTR3","Elektro":"EKTR4","Eletrobras":"ELET3","Eletrobras":"ELET5","Eletrobras":"ELET6","Eletron":"ETRO3B","Eletropar":"LIPR3","Eletropaulo":"ELPL3","EMAE":"EMAE3","EMAE":"EMAE4","Embraer":"EMBR3","Encorpar":"ECPR3","Encorpar":"ECPR4","Energias BR":"ENBR3","Energisa MT":"ENMT3","Energisa MT":"ENMT4","Energisa":"ENGI3","Energisa":"ENGI4","Energisa":"ENGI11","Eneva":"ENEV3","Engie Brasil":"EGIE3","Equatorial":"EQTL3","Estácio Participações":"ESTC3","Estrela":"ESTR3","Estrela":"ESTR4","Eternit":"ETER3","Eucatex":"EUCA3","Eucatex":"EUCA4","Even":"EVEN3","Excelsior":"BAUH3","Excelsior":"BAUH4","Exprescripts DRN":"ESRX34","Exxon Mobil":"EXXO34","Eztec":"EZTC3","Facebook":"FBOK34","Fedex Corp":"FDXB34","Femsa":"FMXB34","Fer C Atlant":"VSPT3","Fer C Atlant":"VSPT4","Fer Heringer":"FHER3","Ferbasa":"FESA3","Ferbasa":"FESA4","Fibam":"FBMC3","Fibam":"FBMC4","Fibria":"FIBR3","Financ/termo 120":"TAXA4","Financ/termo 150":"TAXA5","Financ/termo 180":"TAXA6","Financ/termo 30":"TAXA1","Financ/termo 60":"TAXA2","Financ/termo 90":"TAXA3","Financ/termo DIA":"TAXA0","Finansinos":"FNCN3","First Solar DRN":"FSLR34","Fleury":"FLRY3","Ford Motors":"FDMO34","Forjas Taurus":"FJTA3","Forjas Taurus":"FJTA4","Fras-le":"FRAS3","Freeport":"FCXO34","Futuretel":"FTRT3B","Gafisa":"GFSA3","Gama Part":"OPGM3B","Gap DRN":"GPSI34","GE":"GEOO34","Gen Dynamics":"GDBR34","General Mot DRN":"GMCO34","Generalshopp":"GSHP3","Ger Paranap":"GEPA3","Ger Paranap":"GEPA4","Gerdau Met":"GOAU3","Gerdau Met":"GOAU4","Gerdau":"GGBR3","Gerdau":"GGBR4","Gilead DRN":"GILD34","Gol":"GOLL4","Goldman Sachs":"GSGI34","Gopro DRN":"GPRO34","GP Invest":"GPIV33","GPC Part":"GPCP3","Grazziotin":"CGRA3","Grazziotin":"CGRA4","Grendene":"GRND3","Grucai":"GRUC3","Grucai":"GRUC6","Guararapes":"GUAR3","Guararapes":"GUAR4","Habitasul":"HBTS3","Habitasul":"HBTS5","Habitasul":"HBTS6","Haga":"HAGA3","Haga":"HAGA4","Halliburton":"HALI34","Helbor":"HBOR3","Hercules":"HETA3","Hercules":"HETA4","Hershey Co":"HSHY34","Home Depot":"HOME34","Honeywell":"HONB34","Hoteis Othon":"HOOT3","Hoteis Othon":"HOOT4","HP Company":"HPQB34","Hypera":"HYPE3","I Dividendos IDI":"IDIV11","IBM":"IBMB34","Ibovespa IBO":"IBOV11","Ibrasil IBR":"IBRA11","Ibrx 50 IBX":"IBXL11","Ibrx Brasil IBX":"IBXX11","Ico2 ICO":"ICO211","Iconsumo ICO":"ICON11","Ideiasnet":"IDNT3","Ieeletrica IEE":"IEEX11","Ifinanceiro IFN":"IFNC11","IGB S/A ":"IGBR3","Igc - Nm IGN":"IGNM11","ETF IGC Trade":"IGCT11","Igovernanca IGC":"IGCX11","Iguatemi":"IGTA3","Ihpardini":"PARD3","Imat Basicos IMA":"IMAT11","IMC S/A":"MEAL3","Imobiliario IMO":"IMOB11","Ind Cataguas":"CATA3","Ind Cataguas":"CATA4","Ind Fdo Imob IFI":"IFIX11","Inds Romi":"ROMI3","Industrial IND":"INDX11","Indusval":"IDVL3","Indusval":"IDVL4","Inepar":"INEP3","Inepar":"INEP4","Intel":"ITLC34","Invepar":"IVPR3B","Invepar":"IVPR4B","Invest Bemge":"FIGE3","Invest Bemge":"FIGE4","Iochpe Maxion":"MYPK3","IRB Brasil RE":"IRBR3","Isustentabil ISE":"ISEE11","Itag Along ITA":"ITAG11","Itaitinga":"SQRM3","Itaitinga":"SQRM11","Itausa ON":"ITSA9","Itaúsa":"ITSA3","Itausa PN":"ITSA10","Itaúsa":"ITSA4","Itautec":"ITEC3","Itaú Unibanco":"ITUB3","Itaú Unibanco":"ITUB4","Ivbx2 IVB":"IVBX11","J B Duarte":"JBDU3","J B Duarte":"JBDU4","JBS":"JBSS3","Jc Penney DRN":"JCPC34","JHSF Part":"JHSF3","João Fortes":"JFEN3","Johnson":"JNJB34","Josapar":"JOPA3","Josapar":"JOPA4","JP Morgan":"JPMC34","JSL":"JSLG3","Karsten":"CTKA3","Karsten":"CTKA4","Kepler Weber":"KEPL3","Kimberly Cl":"KMBB34","Klabin":"KLBN3","Klabin":"KLBN4","Klabin":"KLBN11","Kraft Heinz":"KHCB34","Kroton":"KROT3","L Brands":"LBRN34","Le Lis Blanc":"LLIS3","Light":"LIGT3","Lilly":"LILY34","Linx":"LINX3","Litel":"LTEL3B","Litel ":"LTEL5B","Litel ":"LTEL11B","Localiza":"RENT3","Locamerica":"LCAM3","Lockheed":"LMTB34","Log-In":"LOGN3","Lojas Americanas":"LAME3","Lojas Americanas":"LAME4","Lojas Hering":"LHER3","Lojas Hering":"LHER4","Lojas Marisa":"AMAR3","Lojas Renner":"LREN3","Longdis":"SPRT3B","Lopes Brasil":"LPSB3","Lupatech":"LUPA3","M. Dias Branco":"MDIA3","Macy S DRN":"MACY34","Maestroloc":"MSRO3","Magazine Luiza":"MGLU3","Magnesita":"MAGG3","Mangels":"MGEL3","Mangels":"MGEL4","Marcopolo":"POMO3","Marcopolo":"POMO4","Marfrig":"MRFG3","Mastercard":"MSCD34","Mcdonalds":"MCDC34","Medtronic DRN":"MDTC34","Melhor SP":"MSPA3","Melhor SP":"MSPA4","Mendes Jr":"MEND3","Mendes Jr":"MEND5","Mendes Jr":"MEND6","Menezes Cort":"MNZC3B","Banco Mercantil":"BMEB3","Merc Brasil ON":"BMEB9","Banco Mercantil":"BMEB4","Merc Financ":"MERC3","Merc Financ":"MERC4","Merc Invest":"BMIN3","Merc Invest":"BMIN9","Merc Invest":"BMIN4","Merck":"MRCK34","Metal Iguacu":"MTIG3","Metal Iguacu":"MTIG4","Metal Leve":"LEVE3","Metalfrio":"FRIO3","Metisa":"MTSA3","Metisa":"MTSA4","Metlife Inc":"METB34","Microsoft":"MSFT34","Midlarge Cap MLC":"MLCX11","Mills":"MILS3","Minasmaquina":"MMAQ3","Minasmaquina":"MMAQ4","Minerva":"BEEF3","Minupar":"MNPR3","MMX Mineracao":"MMXM3","Mondelez Int":"MDLZ34","Mont Aranha":"MOAR3","Morgan Stanley":"MSBR34","Mosaic":"MOSC34","Movida":"MOVI3","MRS Logist":"MRSA3B","MRS Logist":"MRSA5B","MRS Logist":"MRSA6B","MRV":"MRVE3","Multiplan":"MULT3","Multiplus":"MPLU3","Mundial":"MNDL3","Nadir Figueiredo":"NAFG3","Nadir Figueiredo":"NAFG4","Natura":"NATU3","Netflix":"NFLX34","Newtel Part":"NEWT3B","Nike":"NIKE34","Banco do Nordeste":"BNBR3","Nordon Met":"NORD3","Nortec Quimica":"NRTQ3","Nutriplant":"NUTR3","Oderich":"ODER3","Oderich":"ODER4","Odontoprev":"ODPV3","OGX Petróleo":"OGXP3","Oi":"OIBR3","Oi":"OIBR4","Omega Ger":"OMGE3","Opport Energ":"OPHE3B","Oracle":"ORCL34","OSX Brasil":"OSXB3","Ourofino":"OFSA3","Pão de Açúcar (CBD) ":"PCAR3","Pão de Açúcar - CBD ":"PCAR4","Panatlantica":"PATI3","Panatlantica":"PATI4","Par Al Bahia":"PEAB3","Par Al Bahia":"PEAB4","Paranapanema":"PMAM3","Banco Patagônia":"BPAT33","PDG Realty":"PDGR3","Pepsico Inc":"PEPB34","Petróleo Manguinhos":"RPMG3","Petrobras BR":"BRDT3","Petrobras":"PETR3","Petrobras":"PETR4","Petro Rio":"PRIO3","Pettenati":"PTNT3","Pettenati":"PTNT4","Pfizer":"PFIZ34","Procter Gamble":"PGCO34","Banco Pine":"PINE3","Banco Pine":"PINE4","Plascar Part":"PLAS3","Polpar":"PPAR3","Pomifrutas":"FRTA3","Porto Seguro":"PSSA3","Portobello":"PTBL3","Positivo":"POSI3","Profarma":"PFRM3","Proman":"PRMN3B","Prompt Part":"PRPT3B","Prumo":"PRML3","QGEP Part":"QGEP3","Qualcomm":"QCOM34","Qualicorp":"QUAL3","Quality Soft":"QUSW3","Raia Drogasil":"RADL3","Randon Part":"RAPT3","Randon Part":"RAPT4","Recrusul":"RCSL3","Recrusul":"RCSL4","Rede Energia":"REDE3","Renova":"RNEW3","Renova":"RNEW4","Renova":"RNEW11","Riosulense":"RSUL3","Riosulense":"RSUL4","RNI":"RDNI3","Ross Stores DRN":"ROST34","Rossi":"RSID3","Rumo":"RAIL3","Sabesp":"SBSP3","Salesforce DRN":"SSFO34","Sanchez Ener DRN":"SANC34","Sanepar":"SAPR3","Sanepar":"SAPR4","Sansuy":"SNSY3","Sansuy":"SNSY5","Sansuy":"SNSY6","Santander BR":"SANB3","Santander BR":"SANB4","Santander BR":"SANB11","Santanense":"CTSA3","Santanense":"CTSA4","Santanense":"CTSA8","Santos BRP":"STBP3","São Carlos":"SCAR3","Sao Martinho":"SMTO3","Saraiva Livr":"SLED3","Saraiva Livr":"SLED4","Sauipe":"PSEG3","Sauipe":"PSEG4","Schlumberger":"SLBG34","Schulz ":"SHUL3","Schulz":"SHUL4","Schwab DRN":"SCHW34","Seg Al Bahia":"CSAB3","Seg Al Bahia":"CSAB4","Selectpart":"SLCT3B","Senior Sol":"SNSL3","Ser Educa":"SEER3","CSN":"CSNA3","Sierra Brasil":"SSBR3","SLC Agrícola":"SLCE3","Small Cap SML":"SMLL11","Smiles ON":"SMLS3","Somos Educa":"SEDU3","Sondotecnica":"SOND3","Sondotecnica":"SOND5","Sondotecnica":"SOND6","Springer":"SPRI3","Springer":"SPRI5","Springer":"SPRI6","Springs":"SGPS3","Sprint DRN":"SPRN34","Spturis":"AHEB3","Spturis":"AHEB5","Spturis":"AHEB6","Starbucks":"SBUB34","Statkraft":"STKF3","Sudeste":"OPSE3B","Sul 116 Part":"OPTS3B","Sul America":"SULA3","Sul America":"SULA4","Sul America":"SULA11","Suzano Holding":"NEMO3","Suzano Holding":"NEMO5","Suzano Holding":"NEMO6","Suzano Papel":"SUZB3","Taesa":"TAEE3","Taesa":"TAEE4","Taesa":"TAEE11","Target Corp":"TGTB34","Tarpon Inv":"TRPN3","Technos":"TECN3","Tecnisa ON":"TCSA3","Tecnosolo":"TCNO3","Tecnosolo":"TCNO4","Tectoy":"TOYB3","Tectoy":"TOYB4","Tegma":"TGMA3","Teka":"TEKA3","Teka":"TEKA4","Tekno":"TKNO3","Tekno":"TKNO4","Telebras":"TELB3","Telebras":"TELB4","Telefônica":"VIVT3","Telefônica":"VIVT4","Tenda":"TEND3","Terra Santa":"TESA3","Tesla Inc DRN":"TSLA34","Tex Renaux":"TXRX3","Tex Renaux":"TXRX4","Texas Inc":"TEXA34","Thermfischer DRN":"TMOS34","Tiffany":"TIFF34","Tim":"TIMP3","Time For Fun":"SHOW3","Time Warner":"TWXB34","TOTVS":"TOTS3","Tran Paulist":"TRPL3","Tran Paulist":"TRPL4","Transocean DRN":"RIGG34","Travelers DRN":"TRVC34","Trevisa":"LUXM3","Trevisa":"LUXM4","Trisul":"TRIS3","Triunfo Part":"TPIS3","Tupy":"TUPY3","Twitter":"TWTR34","Ubs Group DRN":"UBSG34","Ultrapar":"UGPA3","Unicasa":"UCAS3","Union Pacific":"UPAC34","Unipar":"UNIP3","Unipar":"UNIP5","Unipar":"UNIP6","United Tech":"UTEC34","UPS":"UPSS34","Uptick":"UPKP3B","US Bancorp":"USBC34","Us Steel DRN":"USSX34","Usiminas":"USIM3","Usiminas":"USIM5","Usiminas":"USIM6","Utilities UTI":"UTIL11","Vale":"VALE3","Valero Ener DRN":"VLOE34","Valid":"VLID3","Verizon":"VERZ34","Via Varejo":"VVAR3","Via Varejo":"VVAR4","Via Varejo ":"VVAR11","Visa Inc":"VISA34","Viver":"VIVR3","Vulcabras":"VULC3","Wal Mart":"WALM34","Walt Disney":"DISB34","WEG":"WEGE3","Wells Fargo":"WFCO34","Western Union":"WUNI34","Wetzel ":"MWET3","Wetzel":"MWET4","Whirlpool":"WHRL3","Whirlpool":"WHRL4","Wilson Sons":"WSON33","Wiz S.A.":"WIZS3","Xerox Corp":"XRXB34"}

chave=lista.keys()
valores=lista.values()

'''
escolha = int(input("Escolha a opção desejada"+"\n"+"- 1-> Nome da Empresa"+"\n"+"- 2-> Código da Ação"+"\n" ))

if (escolha == 1):

    saida = 1

    while(saida):

        busca=input('Qual a empresa buscada ?'+'\n')
        try:
            saida = 0
            code=lista[busca]
        except Exception as exc:
            saida = 1
            print ("Não Identificamos esta ação, TENTE novamente:")
else:
    saida2 = 1
    while(saida2):
        code=input("Escreva o Código desejado:"+"\n")
        for y in valores:
            if y == code:
                saida2 = 0
        if saida2 == 1:
               print("\n"+"Não identificamos este código, TENTE novamente:")
'''

for namestock in valores:
	code = namestock
	posicao=0    

	for x in valores:
	    if x == code:
	        local = posicao
	    else:
	        posicao+=1

	retorno = ""
	posicao2 = 0
	        
	for x2 in chave:
	    if posicao2 <= local:
	        retorno = x2
	        posicao2+=1

	params = [{'q': code,'x': "",}]
	period = "1D"
	interval = 60*15

	x0,y0 = plot_one(params, period, interval)
	plt.plot(x0,y0, 'b--')
	plt.title(code+" - "+retorno)
	plt.xlabel('Horas')
	plt.ylabel('Valor (R$)')
	plt.xticks(rotation=30)
	plt.savefig('Fig1.jpg')

	param = {'q': code,'i': "86400",'x': "",'p': "1M"}

	x1,y1 = plot_two(param)
	plt1.plot(x1,y1)
	plt1.title(code+" - "+retorno)
	plt1.xlabel('Dias')
	plt1.ylabel('Valor (R$)')
	plt1.xticks(rotation=30)
	plt1.savefig('Fig2.jpg')
