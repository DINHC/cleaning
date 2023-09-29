CREATE TABLE whitewine (
	fixedacidity VARCHAR(30), 
	volatileacidity VARCHAR(30),
	citricacidity VARCHAR(30), 
	residualsugar VARCHAR(30),
	chlorides VARCHAR(30),
	freesulfurdioxide VARCHAR(30),
	totalsulfurdioxide VARCHAR(30),
	density VARCHAR(30), 
	pH VARCHAR(30), 
	sulphates VARCHAR(30), 
	alchohol VARCHAR(30),
	quality VARCHAR(30)
);

DROP TABLE whitewine

SELECT * FROM whitewine;

SELECT quality, alchohol, residualsugar
FROM whitewine 
WHERE >6 ;


CREATE TABLE whitewine2 (
	fixedacidity VARCHAR(30), 
	volatileacidity INT,
	citricacidity INT, 
	residualsugar INT,
	chlorides INT,
	freesulfurdioxide INT,
	totalsulfurdioxide INT,
	density INT, 
	pH INT, 
	sulphates INT, 
	alchohol INT,
	quality INT
);

DROP TABLE whitewine2;