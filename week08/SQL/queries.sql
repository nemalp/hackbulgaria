SELECT address
FROM studio
WHERE name='MGM';

SELECT birthdate
FROM moviestar
WHERE name='Sandra Bullock';

SELECT name
FROM movieexec
WHERE networth>10000000;

SELECT name
FROM moviestar
WHERE gender='M' OR address='Perfect Rd';

INSERT INTO moviestar(name, address, gender,  birthdate) VALUES ('Zahari Baharov', 'Unknown', 'M', '1980-07-09');

DELETE FROM studio
WHERE address LIKE '%5%';

UPDATE movie
SET studioname = 'FOX'
WHERE title LIKE '%star%';

SELECT moviestar.name
FROM moviestar, starsin, movie
WHERE moviestar.name=starsin.starname AND moviestar.gender='M' AND movie.title='Terms of Endearment' AND movie.title=starsin.movietitle;

SELECT starsin.starname
FROM starsin, movie
WHERE starsin.movietitle=movie.title AND movie.studioname='MGM' AND movie.year = 1995;

SELECT movie.title
FROM movie
WHERE movie.length > (SELECT movie.length FROM movie WHERE movie.title='Gone With the Wind');

SELECT movieexec.name
FROM movieexec
WHERE movieexec.networth > (SELECT movieexec.networth FROM movieexec WHERE movieexec.name = 'Merv Griffin');

ALTER TABLE studio
ADD 'PRESIDENTNAME' VARCHAR(20);

INSERT INTO studio (PRESIDENTNAME)
VALUES ('President1')
WHERE name='MGM';



