
ALTER USER "postgres" WITH PASSWORD 'postgres';


CREATE DATABASE media;


CREATE TABLE md_artifact(
	id serial PRIMARY KEY,
	title varchar(200),
	description varchar(500),
	participants varchar(500),
	artifact_category varchar(20),
	artifact_type varchar(20),
	status varchar(20),
	video_url varchar(200),
	image_url varchar(200),
	tags varchar(100),
	published_date date,
	created_at timestamp,
	created_by varchar(50),
	modified_at timestamp,
	modified_by varchar(50)
);
		