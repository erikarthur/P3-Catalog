-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database if exists tournament;

create database tournament;

drop table if exists players;

CREATE TABLE players
(
  "id" serial NOT NULL,
  name text,
  CONSTRAINT key PRIMARY KEY ("id")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE players
  OWNER TO vagrant;
GRANT ALL ON TABLE players TO vagrant;
GRANT SELECT, UPDATE, INSERT, TRUNCATE, DELETE ON TABLE players TO public;


drop table if exists standings;
CREATE TABLE standings
(
  "id" serial NOT NULL,
  PLAYER_ID  INT NOT NULL,
  MATCHES INT NOT NULL,
  WINS  INT NOT NULL,
  LOSSES INT NOT NULL
)
WITH (
  OIDS=FALSE
);
ALTER TABLE standings
  OWNER TO vagrant;
GRANT ALL ON TABLE standings TO vagrant;
GRANT SELECT, UPDATE, INSERT, TRUNCATE, DELETE ON TABLE standings TO public;


drop table if exists matches;
CREATE TABLE matches
(
  "id" serial NOT NULL,
  WinnerID INT NOT NULL,
  LoserID INT NOT NULL
)
WITH (
  OIDS=FALSE
);
ALTER TABLE matches
  OWNER TO vagrant;
GRANT ALL ON TABLE matches TO vagrant;
GRANT SELECT, UPDATE, INSERT, TRUNCATE, DELETE ON TABLE matches TO public;
