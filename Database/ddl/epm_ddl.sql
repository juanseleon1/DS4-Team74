DROP TABLE asset CASCADE CONSTRAINTS;

DROP TABLE cause CASCADE CONSTRAINTS;

DROP TABLE clasificacion CASCADE CONSTRAINTS;

DROP TABLE problem CASCADE CONSTRAINTS;

DROP TABLE remedy CASCADE CONSTRAINTS;

DROP TABLE status CASCADE CONSTRAINTS;

DROP TABLE work_order CASCADE CONSTRAINTS;

DROP TABLE worktype CASCADE CONSTRAINTS;

CREATE TABLE asset (
    assetnum                        INTEGER NOT NULL,
    description                     VARCHAR(100),
    assettag                        VARCHAR(50),
    slxjdetecnico                   VARCHAR(20),
    installdate                     TIMESTAMP(0),
    siteid                          VARCHAR(20),
    priority                        INTEGER,
    status_status_id                INTEGER,
    clasificacion_classstructureid  INTEGER
);

ALTER TABLE asset ADD CONSTRAINT asset_pk PRIMARY KEY ( assetnum );

CREATE TABLE cause (
    cause_id     INTEGER NOT NULL,
    failurecode  VARCHAR(30),
    description  VARCHAR(100)
);

ALTER TABLE cause ADD CONSTRAINT cause_pk PRIMARY KEY ( cause_id );


CREATE TABLE clasificacion (
    classstructureid  INTEGER NOT NULL,
    classstructure    VARCHAR(100) NOT NULL
);

ALTER TABLE clasificacion ADD CONSTRAINT clasificacion_pk PRIMARY KEY ( classstructureid );


CREATE TABLE problem (
    problem_id   INTEGER NOT NULL,
    failurecode  VARCHAR(30),
    description  VARCHAR(100)
);

ALTER TABLE problem ADD CONSTRAINT problem_pk PRIMARY KEY ( problem_id );


CREATE TABLE remedy (
    remedy_id    INTEGER NOT NULL,
    failurecode  VARCHAR(30),
    description  VARCHAR(100)
);

ALTER TABLE remedy ADD CONSTRAINT remedy_pk PRIMARY KEY ( remedy_id );


CREATE TABLE status (
    status_id  INTEGER NOT NULL,
    status     VARCHAR(20) NOT NULL
);

ALTER TABLE status ADD CONSTRAINT status_pk PRIMARY KEY ( status_id );


CREATE TABLE work_order (
    wonum                 INTEGER NOT NULL,
    description           VARCHAR(100),
    reportdate            TIMESTAMP(0),
    actstart              TIMESTAMP(0),
    actfinish             TIMESTAMP(0),
    worklog               VARCHAR(600),
    asset_assetnum        INTEGER,
    worktype_worktype_id  INTEGER,
    cause_cause_id        INTEGER,
    problem_problem_id    INTEGER,
    remedy_remedy_id      INTEGER
);

ALTER TABLE work_order ADD CONSTRAINT work_order_pk PRIMARY KEY ( wonum );


CREATE TABLE worktype (
    worktype_id  INTEGER NOT NULL,
    worktype     VARCHAR(30) NOT NULL
);

ALTER TABLE worktype ADD CONSTRAINT worktype_pk PRIMARY KEY ( worktype_id );

ALTER TABLE asset
    ADD CONSTRAINT asset_clasificacion_fk FOREIGN KEY ( clasificacion_classstructureid )
        REFERENCES clasificacion ( classstructureid );

ALTER TABLE asset
    ADD CONSTRAINT asset_status_fk FOREIGN KEY ( status_status_id )
        REFERENCES status ( status_id );

ALTER TABLE work_order
    ADD CONSTRAINT work_order_asset_fk FOREIGN KEY ( asset_assetnum )
        REFERENCES asset ( assetnum );

ALTER TABLE work_order
    ADD CONSTRAINT work_order_cause_fk FOREIGN KEY ( cause_cause_id )
        REFERENCES cause ( cause_id );

ALTER TABLE work_order
    ADD CONSTRAINT work_order_problem_fk FOREIGN KEY ( problem_problem_id )
        REFERENCES problem ( problem_id );

ALTER TABLE work_order
    ADD CONSTRAINT work_order_remedy_fk FOREIGN KEY ( remedy_remedy_id )
        REFERENCES remedy ( remedy_id );

ALTER TABLE work_order
    ADD CONSTRAINT work_order_worktype_fk FOREIGN KEY ( worktype_worktype_id )
        REFERENCES worktype ( worktype_id );

