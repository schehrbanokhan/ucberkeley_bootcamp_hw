-- HOMEWORK SQL

USE sakila;

-- Q1a

SELECT 
    first_name, last_name
FROM
    actor;
    
-- Q1b

SELECT 
    CONCAT_WS(' ', `first_name`, `last_name`) AS `Actor Name`
FROM
    actor;

-- Q2a

SELECT 
    first_name, last_name, actor_id
FROM
    actor
WHERE
    first_name = 'Joe';

-- Q2b
SELECT 
    first_name, last_name, actor_id
FROM
    actor
WHERE
    last_name LIKE '%GEN%';

-- Q2c
SELECT 
    last_name, first_name
FROM
    actor
WHERE
    last_name LIKE '%LI%'
ORDER BY last_name ASC , first_name ASC;

-- Q2d
SELECT 
    country_id, country
FROM
    country
WHERE
    country IN ('Afghanistan' , 'Bangladesh', 'China');

-- Q3a

ALTER  TABLE  actor
ADD description BLOB;

-- Q3b

ALTER TABLE actor 
DROP COLUMN  description;

-- Q4a

SELECT 
    last_name, COUNT(last_name)
FROM
    actor
GROUP BY last_name;

-- Q4b

SELECT 
    last_name, COUNT(last_name)
FROM
    actor
GROUP BY last_name
HAVING COUNT(last_name) >= 2;

-- Q4c

UPDATE actor 
SET 
    first_name = 'HARPO'
WHERE
    first_name = 'GROUCHO';

-- Q4d

UPDATE actor 
SET 
    first_name = 'GROUCHO'
WHERE
    first_name = 'HARPO'
        AND last_name = 'Williams';


-- Q5a

SHOW CREATE TABLE sakila.address;
-- OR
DESCRIBE sakila.address;


-- Q6a

SELECT 
    first_name, last_name, address
FROM
    staff
        JOIN
    address ON address.address_id = staff.address_id;

-- Q6b

SELECT 
    payment.staff_id, SUM(amount)
FROM
    payment
        INNER JOIN
    staff ON staff.staff_id = payment.staff_id
WHERE
    MONTH(payment_date) = '8'
        AND YEAR(payment_date) = '2005'
GROUP BY staff_id;

-- Q6c 

SELECT 
    film_actor.film_id, film.title, COUNT(*)
FROM
    film_actor
        INNER JOIN
    film ON film_actor.film_id = film.film_id
GROUP BY film_id;

-- Q6d

SELECT 
    COUNT(inventory_id) AS 'number of copies'
FROM
    inventory
WHERE
    film_id = (SELECT 
            film_id
        FROM
            film
        WHERE
            title = 'Hunchback Impossible');

-- Q6e

SELECT 
    first_name, last_name, SUM(amount) AS 'Total Amount Paid'
FROM
    payment
        JOIN
    customer ON customer.customer_id = payment.customer_id
GROUP BY first_name , last_name
ORDER BY last_name ASC;


-- Q7a

SELECT 
    film_id, title
FROM
    film
WHERE
    title LIKE '%K'
        OR title LIKE '%Q'
        AND language_id = (SELECT 
            language_id
        FROM
            language
        WHERE
            name = 'English');

-- Q7b

SELECT 
    first_name, last_name
FROM
    actor
WHERE
    actor_id IN (SELECT 
            actor_id
        FROM
            film_actor
        WHERE
            film_id IN (SELECT 
                    film_id
                FROM
                    film
                WHERE
                    title = 'Alone Trip'));

-- Q7c

SELECT 
    customer.first_name, customer.last_name, customer.email
FROM
    customer
        JOIN
    address ON address.address_id = customer.address_id
        JOIN
    city ON address.city_id = city.city_id
        JOIN
    country ON city.country_id = country.country_id
WHERE
    country = 'Canada';

-- Q7d

SELECT 
    film.film_id,
    title,
    description,
    rating,
    category.name AS 'Category'
FROM
    film
        INNER JOIN
    film_category ON film.film_id = film_category.film_id
        INNER JOIN
    category ON category.category_id = film_category.category_id
        AND category.name = 'Family';

-- Q7e

SELECT 
    title, COUNT(*) AS 'frequency'
FROM
    rental
        JOIN
    inventory ON rental.inventory_id = inventory.inventory_id
        JOIN
    film ON film.film_id = inventory.film_id
GROUP BY title
ORDER BY frequency DESC;

-- Q7f

SELECT 
    store.store_id AS 'Store', SUM(amount) AS 'Money brought in'
FROM
    payment
        JOIN
    rental ON payment.rental_id = rental.rental_id
        JOIN
    inventory ON inventory.inventory_id = rental.inventory_id
        JOIN
    store ON store.store_id = inventory.store_id
GROUP BY store.store_id;

-- Q7g

SELECT 
    store_id, city, country
FROM
    store
        JOIN
    address ON store.address_id = address.address_id
        JOIN
    city ON city.city_id = address.city_id
        JOIN
    country ON country.country_id = city.country_id;

-- Q7h

SELECT 
    name AS 'Genre', SUM(amount) AS 'Revenue'
FROM
    rental
        JOIN
    payment ON payment.rental_id = rental.rental_id
        JOIN
    inventory ON rental.inventory_id = inventory.inventory_id
        JOIN
    film_category ON film_category.film_id = inventory.film_id
        JOIN
    category ON category.category_id = film_category.category_id
GROUP BY category.name
ORDER BY Revenue DESC
LIMIT 5;


-- Q8a

CREATE VIEW `top_5_genres` AS
    SELECT 
        name AS 'Genre', SUM(amount) AS 'Revenue'
    FROM
        rental
            JOIN
        payment ON payment.rental_id = rental.rental_id
            JOIN
        inventory ON rental.inventory_id = inventory.inventory_id
            JOIN
        film_category ON film_category.film_id = inventory.film_id
            JOIN
        category ON category.category_id = film_category.category_id
    GROUP BY category.name
    ORDER BY Revenue DESC
    LIMIT 5;

-- Q8b

SELECT 
    *
FROM
    top_5_genres;

-- Q8c

DROP VIEW IF EXISTS sakila.top_5_genres;



