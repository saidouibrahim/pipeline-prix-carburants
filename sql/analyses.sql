-- 1. Prix moyen de chaque carburant en France
-- AVG( veut dire average (c est une fonction sql qui permet de calculer la moyenne d'une colone)
SELECT carburant, AVG(prix) AS prix_moyen
FROM prix
GROUP BY carburant
ORDER BY prix_moyen;

-- 2. Prix minimum et maximum de chaque carburant en France

SELECT carburant, min(prix) As prixx_minum, max(prix) AS prix_maximum
FROM prix 
GROUP BY carburant