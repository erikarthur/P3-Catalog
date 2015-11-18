-- Table: owners

DROP TABLE if exists items cascade;
DROP TABLE if exists categories cascade;
DROP TABLE if exists owners cascade;

CREATE TABLE owners
(
  id serial NOT NULL,
  name character varying(250) NOT NULL,
  email character varying(250) NOT NULL,
  CONSTRAINT owners_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE owners
  OWNER TO postgres;


-- Table: categories



CREATE TABLE categories
(
  id serial NOT NULL,
  name character varying(250) NOT NULL,
  owner_id integer,
  CONSTRAINT categories_pkey PRIMARY KEY (id),
  CONSTRAINT categories_owner_id_fkey FOREIGN KEY (owner_id)
      REFERENCES owners (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE categories
  OWNER TO postgres;

-- Table: items



CREATE TABLE items
(
  id serial NOT NULL,
  name character varying(80) NOT NULL,
  description character varying(250),
  picture character varying(250),
  owner_id integer,
  category_id integer,
  CONSTRAINT items_pkey PRIMARY KEY (id),
  CONSTRAINT items_category_id_fkey FOREIGN KEY (category_id)
      REFERENCES categories (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT items_owner_id_fkey FOREIGN KEY (owner_id)
      REFERENCES owners (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE items
  OWNER TO postgres;

