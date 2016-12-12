SELECT ships.name, ships.launched, classes.country, classes.bore
FROM ships
JOIN classes
ON classes.class = ships.class;

SELECT ships.name, ships.launched, classes.country, classes.bore
FROM classes
LEFT JOIN ships
ON classes.class = ships.class
WHERE ships.name = classes.class;

SELECT ships.name
FROM ships
JOIN outcomes
ON ships.name = outcomes.ship
JOIN battles
ON outcomes.battle = battles.name
WHERE battles.name = 'North Cape';

SELECT classes.country, ships.name
FROM classes
LEFT JOIN ships ON classes.class = ships.class
LEFT JOIN outcomes ON outcomes.ship = ships.name
WHERE outcomes.battle IS NULL;
