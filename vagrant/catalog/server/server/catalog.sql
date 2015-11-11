-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--drop database if exists tournament;

--create database tournament;--

DROP TABLE if EXISTS categories CASCADE;

CREATE TABLE categories
(
  id serial NOT NULL,
  category CITEXT,
  owner_id integer,
  CONSTRAINT categories_pk PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE categories
  OWNER TO vagrant;
GRANT ALL ON TABLE categories TO vagrant;

DROP TABLE if EXISTS items CASCADE;

CREATE TABLE items
(
  id serial NOT NULL,
  category integer,
  item_owner integer,
  item_name CITEXT,
  item_description text,
  item_picture text,
  CONSTRAINT items_pk PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE items
  OWNER TO vagrant;
GRANT ALL ON TABLE items TO vagrant;

DROP TABLE if EXISTS owners CASCADE;

CREATE TABLE owners
(
  id serial NOT NULL,
  owner_id integer,
  owner_name CITEXT,
  CONSTRAINT owners_pk PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE owners
  OWNER TO vagrant;
GRANT ALL ON TABLE owners TO vagrant;

INSERT INTO owners(id, owner_id, owner_name) VALUES (default, 1, 'Erik Arthur');
INSERT INTO owners(id, owner_id, owner_name) VALUES (default, 2, 'Terry Arthur');
INSERT INTO owners(id, owner_id, owner_name) VALUES (default, 3, 'Zach Arthur');
INSERT INTO owners(id, owner_id, owner_name) VALUES (default, 4, 'Maddie Arthur');
INSERT INTO owners(id, owner_id, owner_name) VALUES (default, 5, 'Jack Arthur');
INSERT INTO owners(id, owner_id, owner_name) VALUES (default, 6, 'Carol Arthur');

INSERT INTO categories(id, owner_id, category) VALUES (default, 1, 'Skateboards');
INSERT INTO categories(id, owner_id, category) VALUES (default, 1, 'Snowboards');
INSERT INTO categories(id, owner_id, category) VALUES (default, 2, 'Candles');
INSERT INTO categories(id, owner_id, category) VALUES (default, 3, 'Instruments');
INSERT INTO categories(id, owner_id, category) VALUES (default, 3, 'Video Games');
INSERT INTO categories(id, owner_id, category) VALUES (default, 4, 'Soccer');
INSERT INTO categories(id, owner_id, category) VALUES (default, 4, 'Recipes');
INSERT INTO categories(id, owner_id, category) VALUES (default, 5, 'TV Programs');
INSERT INTO categories(id, owner_id, category) VALUES (default, 5, 'Remote Controls');
INSERT INTO categories(id, owner_id, category) VALUES (default, 6, 'Quilting');
INSERT INTO categories(id, owner_id, category) VALUES (default, 6, 'Sewing');


INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 1, 1, 'Vanguard Loaded');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 1, 1, 'Sector9 Pin');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 2, 1, 'Never Summer');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 2, 1, 'Snow Mullet');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 2, 1, 'Prior Split');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 2, 1, 'Burton Fish');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 3, 2, 'Small Candle');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 3, 2, 'Medium Candle');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 3, 2, 'Large Candle');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 4, 3, 'Alto Sax');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 4, 3, 'Tenor Sax');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 4, 3, 'Bassoon');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 5, 3, 'Halo V');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 5, 3, 'PGR III');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 5, 3, 'CoD IV');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 6, 4, 'Cleats');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 6, 4, 'Jersey');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 6, 4, 'Shorts');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 6, 4, 'Ball');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 7, 4, 'Soup');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 7, 4, 'Bread');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 7, 4, 'Chicken');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 7, 4, 'Cookies');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 8, 5, '60 Minutes');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 8, 5, 'Dateline');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 8, 5, 'Fox and Friends');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 9, 5, 'TV');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 9, 5, 'VCR');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 9, 5, 'DVD');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 10, 6, 'Cloth');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 10, 6, 'Fleece');

INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 11, 6, 'Needles');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 11, 6, 'Thread');
INSERT INTO items(id, category, item_owner, item_name) VALUES (default, 11, 6, 'Sewing Machine');


-- CREATE OR REPLACE VIEW player_standings_view AS
--  SELECT players.id,
--     players.name,
--     standings.wins,
--     standings.matches
--    FROM standings,
--     players
--   WHERE players.id = standings.id
--   ORDER BY standings.wins DESC, players.name;

-- ALTER TABLE "player_standings_view"
--   OWNER TO vagrant;

-- CREATE OR REPLACE VIEW swiss_pairings_view AS
--  SELECT players.id,
--     players.name,
--     standings.wins,
--     random() AS seed,
--     standings.ties,
--     standings.used_bye
--    FROM standings,
--     players
--   WHERE players.id = standings.id
--   ORDER BY standings.wins DESC, seed DESC;

-- ALTER TABLE swiss_pairings_view
--   OWNER TO vagrant;
