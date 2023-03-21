create table Stasjon (
	Navn TEXT PRIMARY key,
	meterOverHavet INTEGER
);

create table Strekning (
	Navn TEXT PRIMARY KEY,
	fremdriftsEnergi TEXT
);

create table Delstrekning (
	StrekningsID TEXT PRIMARY KEY,
	InngaarIstrekning TEXT,
	startStasjon TEXT,
	endeStasjon TEXT,
	lengde REAL,
	antallSpor INTEGER,
	FOREIGN KEY (InngaarIstrekning) REFERENCES Strekning(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (startStasjon) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (endeStasjon) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

create table Operator (
	OperatorNavn TEXT PRIMARY KEY
);

create table Tog (
	TogID INTEGER PRIMARY KEY
);


create table Rute (
	RuteID INTEGER PRIMARY KEY,
	TogID INTEGER,
	Retning TEXT,
	startStasjon TEXT,
	endeStasjon TEXT,
	driftesAv TEXT,
	FOREIGN KEY (TogID) REFERENCES Tog(TogID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (startStasjon) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN key (endeStasjon) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN Key (driftesAv) REFERENCES Operator(OperatorNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


create table InngaarIRute (
	RuteID INTEGER,
	StrekningsID TEXT,
	PRIMARY KEY (RuteID, StrekningsID),
	FOREIGN key (RuteID) REFERENCES Rute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN key (StrekningsID) REFERENCES Delstrekning(StrekningsID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

create table RuteDag (
	RuteID INTEGER,
	ukedag TEXT,
	PRIMARY KEY (RuteID, ukedag),
	FOREIGN KEY (RuteID) REFERENCES Rute(Rute)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

create table RuteTabell (
	RuteID INTEGER,
	tabellID INTEGER,
	StasjonsNavn TEXT,
	tid text,
	PRIMARY KEY (RuteID, tabellID),
	FOREIGN KEY (RuteID) REFERENCES Rute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	FOREIGN KEY (StasjonsNavn) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);
	
create table RuteForekomst (
	ForekomstID INTEGER PRIMARY KEY,
	RuteID INTEGER,
	dato TEXT,
	FOREIGN KEY (RuteID) REFERENCES Rute(RuteID)
		ON UPDATE CASCADE
);

create table Vogn (
	OperatorNavn TEXT,
	VognID INTEGER,
	Navn TEXT,
	PRIMARY KEY (OperatorNavn, VognID),
	FOREIGN KEY (OperatorNavn) REFERENCES Operator(OperatorNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

create table DelAvTog (
	TogID INTEGER,
	OperatorNavn TEXT,
	VognID INTEGER,
	NummerIRekke INTEGER,
	PRIMARY KEY (TogID, OperatorNavn, VognID),
	FOREIGN KEY (TogID) REFERENCES Tog(TogID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES Vogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

create table SitteVogn (
	OperatorNavn TEXT,
	VognID INTEGER,
	antallRader INTEGER,
	seterPerRad INTEGER,
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES Vogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	
	PRIMARY KEY (OperatorNavn, VognID)
);

create table SoveVogn (
	OperatorNavn TEXT,
	VognID INTEGER,
	antallKupeer INTEGER,
	PRIMARY KEY (OperatorNavn, VognID),
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES Vogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


create table Billett (
	ForekomstID INTEGER,
	billettID INTEGER,
	FOREIGN KEY (ForekomstID) REFERENCES RuteForekomst(ForekomstID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	PRIMARY KEY (ForekomstID, billettID)
);



create table BillettOmfatter(
	ForekomstID INTEGER,
	billettID INTEGER,
	StrekningsID INTEGER,
	PRIMARY KEY (ForekomstID, billettID, StrekningsID),
	FOREIGN KEY (ForekomstID, billettID) REFERENCES Billett(ForekomstID, billettID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	
	FOREIGN KEY (StrekningsID) REFERENCES Delstrekning(StrekningsID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


create table SitteBillett (
	ForekomstID INTEGER,
	billettID INTEGER,
	OperatorNavn TEXT,
	VognID INTEGER,
	SeteID INTEGER,
	PRIMARY KEY (OperatorNavn, VognID, SeteID),
	FOREIGN KEY (ForekomstID, billettID) REFERENCES Billett(ForekomstID, billettID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	FOREIGN KEY (OperatorNavn, VognID, SeteID) REFERENCES Sete(OperatorNavn, VognID, SeteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);



create table SoveBillett (
	ForekomstID INTEGER,
	billettID INTEGER,
	OperatorNavn TEXT,
	VognID INTEGER,
	SengeID INTEGER,
	PRIMARY KEY (OperatorNavn, VognID, SengeID),
	FOREIGN KEY (ForekomstID, billettID) REFERENCES Billett(ForekomstID, billettID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (OperatorNavn, VognID, SengeID) REFERENCES Seng(OperatorNavn, VognID, SengeID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);




create table Sete (
	OperatorNavn TEXT,
	VognID INTEGER,
	SeteID INTEGER,
	PRIMARY KEY (OperatorNavn, VognID, SeteID),
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES SitteVogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

create table Seng (
	OperatorNavn TEXT,
	VognID INTEGER,
	SengID INTEGER,
	KupeNr INTEGER,
	PRIMARY KEY (OperatorNavn, VognID, SengID),
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES SoveVogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);





create table Kunde(
	KundeNr INTEGER PRIMARY KEY, 
	epostAddr TEXT,
	Navn TEXT,
	telefonNR TEXT
);

create table KundeHos(
	KundeNr INTEGER,
	OperatorNavn TEXT,
	PRIMARY KEY (KundeNr, OperatorNavn),
	FOREIGN KEY (KundeNr) REFERENCES Kunde(KundeNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	FOREIGN KEY (OperatorNavn) REFERENCES Operator(OperatorNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);



create table KundeOrdre (
	OrdreNr INTEGER PRIMARY KEY,
	KundeNr INTEGER,
	datoForBestilling TEXT,
	tidspunktForBestilling TEXT, 
	antallBilletter INTEGER,
	FOREIGN KEY (KundeNr) REFERENCES Kunde(KundeNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


create TABLE Bestilling (
	OrdreNr INTEGER,
	ForekomstID INTEGER,
	billettID INTEGER,
	PRIMARY KEY (OrdreNr, ForekomstID, billettID),
	FOREIGN KEY (OrdreNr) REFERENCES KundeOrdre(OrdreNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	FOREIGN KEY (ForekomstID, billettID) REFERENCES Billett(ForekomstID, billettID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);
