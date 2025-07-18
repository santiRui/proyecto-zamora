PGDMP      (    
            }            Samora    17.4    17.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    17134    Samora    DATABASE     n   CREATE DATABASE "Samora" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-AR';
    DROP DATABASE "Samora";
                     postgres    false            �            1259    17135    familia    TABLE     C  CREATE TABLE public.familia (
    dni_familia integer NOT NULL,
    nombre character varying(100),
    apellido character varying(100),
    gmail character varying(150),
    telefono text,
    password text,
    dni_institu_familia integer,
    CONSTRAINT chk_telefono_familia CHECK ((telefono ~ '^[0-9]{7,15}$'::text))
);
    DROP TABLE public.familia;
       public         heap r       postgres    false            �            1259    17140    institucion    TABLE       CREATE TABLE public.institucion (
    dni_institu integer NOT NULL,
    nombre character varying(100),
    apellido character varying(100),
    gmail character varying(150),
    telefono character varying(10),
    password text,
    id_roles_institu integer NOT NULL,
    roles character varying,
    CONSTRAINT chk_gmail_institucion CHECK (((gmail)::text ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'::text)),
    CONSTRAINT chk_telefono_institucion CHECK (((telefono)::text ~ '^[0-9]{7,15}$'::text))
);
    DROP TABLE public.institucion;
       public         heap r       postgres    false            �            1259    17145    roles    TABLE     f   CREATE TABLE public.roles (
    id_roles integer NOT NULL,
    nombre_roles character varying(100)
);
    DROP TABLE public.roles;
       public         heap r       postgres    false            �          0    17135    familia 
   TABLE DATA           p   COPY public.familia (dni_familia, nombre, apellido, gmail, telefono, password, dni_institu_familia) FROM stdin;
    public               postgres    false    217   �       �          0    17140    institucion 
   TABLE DATA           x   COPY public.institucion (dni_institu, nombre, apellido, gmail, telefono, password, id_roles_institu, roles) FROM stdin;
    public               postgres    false    218   D       �          0    17145    roles 
   TABLE DATA           7   COPY public.roles (id_roles, nombre_roles) FROM stdin;
    public               postgres    false    219   a       ,           2606    17149    familia familia_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.familia
    ADD CONSTRAINT familia_pkey PRIMARY KEY (dni_familia);
 >   ALTER TABLE ONLY public.familia DROP CONSTRAINT familia_pkey;
       public                 postgres    false    217            .           2606    17151    institucion institucion_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT institucion_pkey PRIMARY KEY (dni_institu);
 F   ALTER TABLE ONLY public.institucion DROP CONSTRAINT institucion_pkey;
       public                 postgres    false    218            0           2606    17153    roles roles_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id_roles);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public                 postgres    false    219            1           2606    17167    familia fk_dni_institu_familia    FK CONSTRAINT     �   ALTER TABLE ONLY public.familia
    ADD CONSTRAINT fk_dni_institu_familia FOREIGN KEY (dni_institu_familia) REFERENCES public.institucion(dni_institu) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.familia DROP CONSTRAINT fk_dni_institu_familia;
       public               postgres    false    217    218    4654            2           2606    17172    institucion fk_id_roles_institu    FK CONSTRAINT     �   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT fk_id_roles_institu FOREIGN KEY (id_roles_institu) REFERENCES public.roles(id_roles) ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.institucion DROP CONSTRAINT fk_id_roles_institu;
       public               postgres    false    4656    219    218            �   }   x���=�0��9L��ddF�t1E8�ޟؐ,�'˟)�#,��
z���Zz�m_�i}N�n�9ŀx`a@b���$�$��������g�1p�K����
��9 �
k��w9Oι��4R      �      x������ � �      �      x������ � �     