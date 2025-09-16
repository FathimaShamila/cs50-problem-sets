-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT day FROM crime_scene_reports WHERE street = 'Humphrey Street' ;
SELECT id FROM crime_scene_reports WHERE street = 'Humphrey Street' AND day = 28 AND year = 2024 AND month = 07;
CREATE TEMP TABLE suspects_exit_bakery AS SELECT name,phone_number,license_plate FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE activity = 'exit' AND hour = 10 AND minute <= 25 AND day = 28 AND month = 07 AND year = 2024);
SELECT id,name,transcript FROM interviews WHERE year = 2024 AND month = 07 AND day = 28 AND transcript LIKE '%bakery%';
SELECT caller,receiver,duration FROM phone_calls WHERE day = 28 AND month = 07 AND year = 2024 AND duration < 60;
CREATE TEMP TABLE suspects AS SELECT name,phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE activity = 'exit' AND hour = 10 AND minute <= 25 AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND month = 07 AND year = 2024 AND activity = 'entrance' AND hour <=10 AND minute <= 15));
CREATE TEMP TABLE suspects_atm AS SELECT name,phone_number,passport_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2024 AND month = 07 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'));
SELECT name FROM suspects_atm WHERE phone_number IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 07 AND year = 2024 AND duration < 60);
SELECT name,license_plate FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE activity = 'entrance' AND day = 28 AND month = 07 AND year = 2024);
SELECT * FROM bakery_security_logs WHERE license_plate = (SELECT license_plate FROM people WHERE name = 'Eugene');
SELECT phone_number,name FROM people,suspects_phonecall WHERE phone_number IN (SELECT receiver FROM suspects_phonecall);
SELECT * FROM suspects_exit_bakery WHERE phone_number IN (SELECT caller FROM suspects_phonecall);
SELECT id FROM airports WHERE city = 'Fiftyville';
SELECT * FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city = ' Fiftyville');
 CREATE TEMP TABLE suspects_flights AS SELECT * FROM flights WHERE origin_airport_id = 8 AND month = 7 AND day = 29 AND hour < 12;
SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM suspects_flights);
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM suspects_flights));
