CREATE TABLE stations(
    id TEXT  PRIMARY KEY,
    adresse TEXT,
    ville TEXT,
    cp TEXT,
    departement TEXT,
    code_departement TEXT,
    region TEXT,
    latitude REAL,
    longitude REAL,
    type_route  TEXT
);


CREATE TABLE prix(
    station_id  TEXT,
    carburant TEXT,
    prix REAL,
    date_maj TEXT,
    PRIMARY KEY (station_id, carburant, date_maj),
    FOREIGN KEY (station_id) REFERENCES stations(id)
);