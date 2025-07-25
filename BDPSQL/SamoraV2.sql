PGDMP               	        }            Samora    17.4    17.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
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
       public         heap r       postgres    false            �            1259    17140    institucion    TABLE       CREATE TABLE public.institucion (
    dni_institu integer NOT NULL,
    nombre character varying(100),
    apellido character varying(100),
    gmail character varying(150),
    telefono character varying(100),
    password text,
    id_roles_institu integer NOT NULL,
    roles character varying,
    CONSTRAINT chk_gmail_institucion CHECK (((gmail)::text ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'::text)),
    CONSTRAINT chk_telefono_institucion CHECK (((telefono)::text ~ '^[0-9]{7,15}$'::text))
);
    DROP TABLE public.institucion;
       public         heap r       postgres    false            �            1259    17225    recuperacion_password    TABLE     �   CREATE TABLE public.recuperacion_password (
    token character varying(100) NOT NULL,
    dni_usuario integer NOT NULL,
    tipo_usuario character varying(20) NOT NULL,
    fecha_expiracion timestamp without time zone NOT NULL
);
 )   DROP TABLE public.recuperacion_password;
       public         heap r       postgres    false            �            1259    17223    roles_id_roles_seq    SEQUENCE     {   CREATE SEQUENCE public.roles_id_roles_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.roles_id_roles_seq;
       public               postgres    false            �            1259    17145    roles    TABLE     �   CREATE TABLE public.roles (
    id_roles integer DEFAULT nextval('public.roles_id_roles_seq'::regclass) NOT NULL,
    nombre_roles character varying(100)
);
    DROP TABLE public.roles;
       public         heap r       postgres    false    220            �          0    17135    familia 
   TABLE DATA           p   COPY public.familia (dni_familia, nombre, apellido, gmail, telefono, password, dni_institu_familia) FROM stdin;
    public               postgres    false    217   8       �          0    17140    institucion 
   TABLE DATA           x   COPY public.institucion (dni_institu, nombre, apellido, gmail, telefono, password, id_roles_institu, roles) FROM stdin;
    public               postgres    false    218   i       �          0    17225    recuperacion_password 
   TABLE DATA           c   COPY public.recuperacion_password (token, dni_usuario, tipo_usuario, fecha_expiracion) FROM stdin;
    public               postgres    false    221   �       �          0    17145    roles 
   TABLE DATA           7   COPY public.roles (id_roles, nombre_roles) FROM stdin;
    public               postgres    false    219   �       �           0    0    roles_id_roles_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.roles_id_roles_seq', 8, true);
          public               postgres    false    220            2           2606    17149    familia familia_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.familia
    ADD CONSTRAINT familia_pkey PRIMARY KEY (dni_familia);
 >   ALTER TABLE ONLY public.familia DROP CONSTRAINT familia_pkey;
       public                 postgres    false    217            4           2606    17151    institucion institucion_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT institucion_pkey PRIMARY KEY (dni_institu);
 F   ALTER TABLE ONLY public.institucion DROP CONSTRAINT institucion_pkey;
       public                 postgres    false    218            8           2606    17229 0   recuperacion_password recuperacion_password_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY public.recuperacion_password
    ADD CONSTRAINT recuperacion_password_pkey PRIMARY KEY (token);
 Z   ALTER TABLE ONLY public.recuperacion_password DROP CONSTRAINT recuperacion_password_pkey;
       public                 postgres    false    221            6           2606    17153    roles roles_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id_roles);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public                 postgres    false    219            9           2606    17167    familia fk_dni_institu_familia    FK CONSTRAINT     �   ALTER TABLE ONLY public.familia
    ADD CONSTRAINT fk_dni_institu_familia FOREIGN KEY (dni_institu_familia) REFERENCES public.institucion(dni_institu) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.familia DROP CONSTRAINT fk_dni_institu_familia;
       public               postgres    false    218    217    4660            :           2606    17172    institucion fk_id_roles_institu    FK CONSTRAINT     �   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT fk_id_roles_institu FOREIGN KEY (id_roles_institu) REFERENCES public.roles(id_roles) ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.institucion DROP CONSTRAINT fk_id_roles_institu;
       public               postgres    false    218    4662    219            �   !  x���Mk�1��o��=��Lf2��R�P�R�����L�-vw�[A��fU� �	�|��T���,O^����ֻeӷѿ/?O���;��f!- �i�����'�E�DO`U�|x����j���~_$0m��aY�[�E�5�s��Zäj���T2�^[+���"U��ǃ�cT(3�&B�C�� h��(�'Q#K�ݎ�&͌��n����������w���������'p���|��9�����뛱}q���ݬG��\��w�2 j/JR,�P�J RyJ莽�{�֪��T2�'��Y��c�̩�j�a�b�e������/��Xb�9����_pH�{I��>��_�_�/�ӻ��H�ĥ$�܆5�\� gjF���F�.�Ԣq��4&�	h0̑{�5���:ӧ�S��>�H@��AW���l i�O6B�_֖������������|����f5ӜXИ��.)�*�)�\����{F�b�'ށ����6��Z6$�N$�9Sh�2MtT�?����KDʳ�X����~ j� 8      �   F  x���Ok�9�ϞO�Ü�-K���N��nK����Y��ɟ���[J���=�^������ߣ־A�����\��W9���wϲ:��s�\1C������z���������s��}���������n-92!�;�cJK,��7�&!��X��+JM�����h�4f,��.)5h��1JL��I���^cN&� ��w��i]d�����I�$���`���1��xqy�z��p���-RC�TaD�eԙ��9�V{mC�'l<��Um �ԡ�tr�fm�4��3:���n֋C�J2�Υl:yz!�Fn�O�j�:�V� GF�Ý=���a���1��.�z���ӏ�ǟ��tJ����jI�w�7r�����E�"<utnR+����֩Vs�"^b%��^X�Q�(�Rl�%aj&���gZu��b���h�L�>�z.\fJi.E�8|0��ag���ɖ�*r��F��c���]���u��v�����r�rF.��d0�'Q�i�+bI�%+ �6�%fr�hͥ�Rh&!Ϲ讪"���if!^SLbC4�0Lh��	G��̬H%��S{Y���{��l��	�      �   �   x�����1D�s;�I c��X�n[i7��v3��zR��v��8�{wa��6��V�����:���}�EH(@�B��'Keu�Q����~��K!C��m٘�+�S�JG2*dk�H������s�僇�WP'[%�'/�{��@d>��M���3�������8;Wij��O-��yM�      �   B   x�3�LL����,.)JL�/�2�(JMN-(��9]�S�JR�,8�R�RRRBsrR��b���� ^A�     