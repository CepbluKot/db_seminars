-- DDL:

CREATE TABLE main (
    UID integer(10),
    NAME varchar(255),
    SURNAME varchar(255),
    PATRONYMIC varchar(255),
    PHONE_REF integer(10),
    ADDRESS_REF integer(10),
    CONSTRAINT MAIN_PK primary key(UID)
)

CREATE TABLE phone (
    UID integer(10),
    MAIN_REF integer(10),
    PHONE_NUMBER varchar(255),
    CONSTRAINT PHONE_PK primary key(UID)
)

CREATE TABLE address (
    UID integer(10),
    MAIN_REF integer(10),
    ADDRESS varchar(255),
    CONSTRAINT ADDRESS_PK primary key(UID)
)

alter table main 
	add constraint main_phone_FK foreign key(PHONE_REF) references phone(MAIN_REF);

alter table main
    add constraint main_address_FK foreign key(ADDRESS_REF) references address(MAIN_REF);


-- DML:

SELECT * FROM main;
SELECT * FROM phone;
SELECT * FROM address;
select last_value from main_id_seq;

insert into main (NAME, SURNAME, PATRONYMIC, PHONE_REF, ADDRESS_REF)  values ( %s, %s, %s, %s, %s);
insert into phone (MAIN_REF, number) values (%s, %s);
insert into address (MAIN_REF, address) values (%s, %s);
