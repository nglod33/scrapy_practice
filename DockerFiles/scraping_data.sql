CREATE TABLE IF NOT EXISTS quotes (
    Text VARCHAR(10000),
    Author VARCHAR(50),
    Tags VarCHAR(10000),
    Ts TIMESTAMP,
    Uri varchar(500)
);