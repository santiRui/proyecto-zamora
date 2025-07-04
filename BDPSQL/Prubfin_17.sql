PGDMP  	    7                }            defin_17/05    17.4    17.4     +           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            ,           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            -           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            .           1262    24897    defin_17/05    DATABASE     s   CREATE DATABASE "defin_17/05" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-MX';
    DROP DATABASE "defin_17/05";
                     postgres    false            �            1259    24910    familia    TABLE       CREATE TABLE public.familia (
    dni_familia integer NOT NULL,
    nombre character varying(100),
    apellido character varying(100),
    gmail character varying(150),
    telefono character varying(10),
    password character varying(200),
    dni_institu_familia integer NOT NULL
);
    DROP TABLE public.familia;
       public         heap r       postgres    false            �            1259    24898    institucion    TABLE     B  CREATE TABLE public.institucion (
    dni_institu integer NOT NULL,
    nombre character varying(100),
    apellido character varying(100),
    gmail character varying(150),
    telefono character varying(10),
    password character varying(200),
    roles character varying(100),
    id_roles_institu integer NOT NULL
);
    DROP TABLE public.institucion;
       public         heap r       postgres    false            �            1259    24905    roles    TABLE     f   CREATE TABLE public.roles (
    id_roles integer NOT NULL,
    nombre_roles character varying(100)
);
    DROP TABLE public.roles;
       public         heap r       postgres    false            (          0    24910    familia 
   TABLE DATA           p   COPY public.familia (dni_familia, nombre, apellido, gmail, telefono, password, dni_institu_familia) FROM stdin;
    public               postgres    false    219   �       &          0    24898    institucion 
   TABLE DATA           x   COPY public.institucion (dni_institu, nombre, apellido, gmail, telefono, password, roles, id_roles_institu) FROM stdin;
    public               postgres    false    217          '          0    24905    roles 
   TABLE DATA           7   COPY public.roles (id_roles, nombre_roles) FROM stdin;
    public               postgres    false    218   "       �           2606    24916    familia familia_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.familia
    ADD CONSTRAINT familia_pkey PRIMARY KEY (dni_familia);
 >   ALTER TABLE ONLY public.familia DROP CONSTRAINT familia_pkey;
       public                 postgres    false    219            �           2606    24904    institucion institucion_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT institucion_pkey PRIMARY KEY (dni_institu);
 F   ALTER TABLE ONLY public.institucion DROP CONSTRAINT institucion_pkey;
       public                 postgres    false    217            �           2606    24909    roles roles_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id_roles);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public                 postgres    false    218            �           2606    24922    familia fk_dni_institu_familia    FK CONSTRAINT     �   ALTER TABLE ONLY public.familia
    ADD CONSTRAINT fk_dni_institu_familia FOREIGN KEY (dni_institu_familia) REFERENCES public.institucion(dni_institu) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.familia DROP CONSTRAINT fk_dni_institu_familia;
       public               postgres    false    217    219    4750            �           2606    24917    institucion fk_id_roles_institu    FK CONSTRAINT     �   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT fk_id_roles_institu FOREIGN KEY (id_roles_institu) REFERENCES public.roles(id_roles) ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.institucion DROP CONSTRAINT fk_id_roles_institu;
       public               postgres    false    217    4752    218            (      x������ � �      &      x������ � �      '      x������ � �     