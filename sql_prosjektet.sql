CREATE TABLE Stasjon
(
	Navn TEXT PRIMARY KEY,
	meterOverHavet INTEGER
);

CREATE TABLE Strekning
(
	StrekningsNavn TEXT PRIMARY KEY,
	fremdriftsEnergi TEXT
);

CREATE TABLE Delstrekning
(
	DelstrekningsID TEXT PRIMARY KEY,
	StrekningsNavn TEXT,
	startStasjon TEXT,
	endeStasjon TEXT,
	lengde REAL,
	antallSpor INTEGER,
	FOREIGN KEY (StrekningsNavn) REFERENCES Strekning(StrekningsNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (startStasjon) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (endeStasjon) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE Operator
(
	OperatorNavn TEXT PRIMARY KEY
);

CREATE TABLE Tog
(
	TogID INTEGER PRIMARY KEY
);


CREATE TABLE Rute
(
	RuteID INTEGER PRIMARY KEY,
	TogID INTEGER,
	Retning TEXT,
	startStasjon TEXT,
	endeStasjon TEXT,
	OperatorNavn TEXT,
	FOREIGN KEY (TogID) REFERENCES Tog(TogID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (startStasjon) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (endeStasjon) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (OperatorNavn) REFERENCES Operator(OperatorNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE InngaarIRute
(
	RuteID INTEGER,
	DelstrekningsID TEXT,
	PRIMARY KEY (RuteID, DelstrekningsID),
	FOREIGN KEY (RuteID) REFERENCES Rute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (DelstrekningsID) REFERENCES Delstrekning(DelstrekningsID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE RuteDag
(
	RuteID INTEGER,
	ukedag TEXT,
	PRIMARY KEY (RuteID, ukedag),
	FOREIGN KEY (RuteID) REFERENCES Rute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE RuteTabell
(
	RuteID INTEGER,
	tabellID INTEGER,
	StasjonsNavn TEXT,
	tid TEXT,
	PRIMARY KEY (RuteID, tabellID),
	FOREIGN KEY (RuteID) REFERENCES Rute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (StasjonsNavn) REFERENCES Stasjon(Navn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE RuteForekomst
(
	ForekomstID INTEGER PRIMARY KEY,
	RuteID INTEGER,
	dato TEXT,
	FOREIGN KEY (RuteID) REFERENCES Rute(RuteID)
		ON UPDATE CASCADE
);

CREATE TABLE Vogn
(
	OperatorNavn TEXT,
	VognID INTEGER,
	Navn TEXT,
	PRIMARY KEY (OperatorNavn, VognID),
	FOREIGN KEY (OperatorNavn) REFERENCES Operator(OperatorNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE DelAvTog
(
	TogID INTEGER,
	OperatorNavn TEXT,
	VognID INTEGER,
	NummerIRekke INTEGER,
	PRIMARY KEY (TogID, OperatorNavn, VognID),
	FOREIGN KEY (TogID) REFERENCES Tog(TogID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES Vogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE SitteVogn
(
	OperatorNavn TEXT,
	VognID INTEGER,
	antallRader INTEGER,
	seterPerRad INTEGER,
	PRIMARY KEY (OperatorNavn, VognID),
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES Vogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE SoveVogn
(
	OperatorNavn TEXT,
	VognID INTEGER,
	antallKupeer INTEGER,
	PRIMARY KEY (OperatorNavn, VognID),
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES Vogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE Billett
(
	ForekomstID INTEGER,
	billettID INTEGER,
	FOREIGN KEY (ForekomstID) REFERENCES RuteForekomst(ForekomstID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	PRIMARY KEY (ForekomstID, billettID)
);

CREATE TABLE BillettOmfatter
(
	ForekomstID INTEGER,
	billettID INTEGER,
	DelstrekningsID INTEGER,
	PRIMARY KEY (ForekomstID, billettID, DelstrekningsID),
	FOREIGN KEY (ForekomstID, billettID) REFERENCES Billett(ForekomstID, billettID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (DelstrekningsID) REFERENCES Delstrekning(DelstrekningsID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE SitteBillett
(
	ForekomstID INTEGER,
	billettID INTEGER,
	OperatorNavn TEXT,
	VognID INTEGER,
	SeteID INTEGER,
	PRIMARY KEY (OperatorNavn, VognID, SeteID),
	FOREIGN KEY (ForekomstID, billettID) REFERENCES Billett(ForekomstID, billettID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (OperatorNavn, VognID, SeteID) REFERENCES Sete(OperatorNavn, VognID, SeteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE SoveBillett
(
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

CREATE TABLE Sete
(
	OperatorNavn TEXT,
	VognID INTEGER,
	SeteID INTEGER,
	PRIMARY KEY (OperatorNavn, VognID, SeteID),
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES SitteVogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE Seng
(
	OperatorNavn TEXT,
	VognID INTEGER,
	SengeID INTEGER,
	KupeNr INTEGER,
	PRIMARY KEY (OperatorNavn, VognID, SengeID),
	FOREIGN KEY (OperatorNavn, VognID) REFERENCES SoveVogn(OperatorNavn, VognID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE Kunde
(
	KundeNr INTEGER PRIMARY KEY,
	epostAddr TEXT,
	Navn TEXT,
	telefonNR TEXT
);

CREATE TABLE KundeHos
(
	KundeNr INTEGER,
	OperatorNavn TEXT,
	PRIMARY KEY (KundeNr, OperatorNavn),
	FOREIGN KEY (KundeNr) REFERENCES Kunde(KundeNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (OperatorNavn) REFERENCES Operator(OperatorNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE KundeOrdre
(
	OrdreNr INTEGER PRIMARY KEY,
	KundeNr INTEGER,
	datoForBestilling TEXT,
	tidspunktForBestilling TEXT,
	antallBilletter INTEGER,
	FOREIGN KEY (KundeNr) REFERENCES Kunde(KundeNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


CREATE TABLE Bestilling
(
	OrdreNr INTEGER,
	ForekomstID INTEGER,
	billettID INTEGER,
	PRIMARY KEY (OrdreNr, ForekomstID, billettID),
	FOREIGN KEY (OrdreNr) REFERENCES KundeOrdre(OrdreNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (ForekomstID, billettID) REFERENCES Billett(ForekomstID, billettID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);
