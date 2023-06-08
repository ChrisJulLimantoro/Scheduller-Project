TRUNCATE public.db_matkul;
ALTER SEQUENCE public.db_matkul_id_seq RESTART WITH 1;
INSERT INTO public.db_matkul (name,singkatan,paralel,dosen,ruangan,jadwal_kuliah,lama_kuliah,jadwal_ujian,sks) VALUES
	('Cyber Ops','CO','B','Andreas','P 502',0,6,0,3),
	('Cyber Ops','CO','A','Leo','P 502',27,6,0,3),
	('Cyber Ops','CO','C','Agus','P 502',27,6,0,3),
	('Sistem Operasi','SO','A','Rudi','P 502',2,4,7,3),
	('Sistem Operasi','SO','C','Agus','P 502',76,4,7,3),
	('Sistem Operasi','SO','B','Rudi','P 502',141,4,7,3),
	('Grafika Komputer','Grafkom','A','Liliana','P 502',2,6,14,3),
	('Grafika Komputer','Grafkom','B','Liliana','P 502',12,6,14,3),
	('Komunikasi Interpersonal','Komal','B','Stephanus','P 502',12,6,27,3),
	('Komunikasi Interpersonal','Komal','A','Stephanus','P 502',41,6,27,3);
INSERT INTO public.db_matkul (name,singkatan,paralel,dosen,ruangan,jadwal_kuliah,lama_kuliah,jadwal_ujian,sks) VALUES
	('Komunikasi Interpersonal','Komal','C','Stephanus','P 502',40,6,27,3),
	('Komunikasi Interpersonal','Komal','D','Stephanus','P 502',92,6,27,3),
	('Analisis Desain Sistem Informasi','ADSI','C','Lily','P 502',12,6,34,3),
	('Analisis Desain Sistem Informasi','ADSI','D','Alex','P 502',60,6,34,3),
	('Analisis Desain Sistem Informasi','ADSI','B','Silvia','P 502',66,6,34,3),
	('Analisis Desain Sistem Informasi','ADSI','A','Yulia','P 502',93,6,34,3),
	('Kecerdasan Buatan','KB','C','Alvin','P 502',35,6,41,3),
	('Kecerdasan Buatan','KB','B','Greg','P 502',66,6,41,3),
	('Kecerdasan Buatan','KB','A','Hans','P 502',35,6,41,3);
INSERT INTO public.db_matkul (name,singkatan,paralel,dosen,ruangan,jadwal_kuliah,lama_kuliah,jadwal_ujian,sks) VALUES
	('Interaksi Manusia Komputer','IMK','C','Adi','P 502',54,6,54,3),
	('Interaksi Manusia Komputer','IMK','A','Andreas','P 502',54,6,54,3),
	('Interaksi Manusia Komputer','IMK','B','Krisna','P 502',108,6,54,3),
	('Metode Numerik','Metnum','A','Leo','P 502',60,6,61,3),
	('Metode Numerik','Metnum','B','Stephanus','P 502',87,6,61,3),
	('Metode Numerik','Metnum','C','Stephanus','P 502',93,6,61,3),
	('Statistika Terapan','ST','A','Stephanus','P 502',81,6,68,3),
	('Data Mining','Datmin','A','Stephanus','P 502',87,6,81,3),
	('Analisa Proses Bisnis','APB','A','Krisna','P 502',93,6,88,3);
