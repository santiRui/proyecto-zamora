PGDMP  +                    }         	   masamorra    17.4    17.4 ,    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    41063 	   masamorra    DATABASE     o   CREATE DATABASE masamorra WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-AR';
    DROP DATABASE masamorra;
                     postgres    false            �            1259    41104 
   asistencia    TABLE     �   CREATE TABLE public.asistencia (
    "id_asistencias " integer NOT NULL,
    fecha_asistencia character varying,
    "asistió" boolean,
    "justificación" character varying
);
    DROP TABLE public.asistencia;
       public         heap r       postgres    false            �            1259    41103    asistencia_id_asistencias _seq    SEQUENCE     �   CREATE SEQUENCE public."asistencia_id_asistencias _seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public."asistencia_id_asistencias _seq";
       public               postgres    false    223            �           0    0    asistencia_id_asistencias _seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public."asistencia_id_asistencias _seq" OWNED BY public.asistencia."id_asistencias ";
          public               postgres    false    222            �            1259    41111    curso    TABLE     �   CREATE TABLE public.curso (
    id_curso integer NOT NULL,
    "año" character varying,
    "división" character varying,
    turno character varying,
    ciclo boolean,
    especialidad boolean,
    asistencia integer NOT NULL
);
    DROP TABLE public.curso;
       public         heap r       postgres    false            �            1259    41129    curso_asistencia_seq    SEQUENCE     �   CREATE SEQUENCE public.curso_asistencia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.curso_asistencia_seq;
       public               postgres    false    225            �           0    0    curso_asistencia_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.curso_asistencia_seq OWNED BY public.curso.asistencia;
          public               postgres    false    226            �            1259    41110    curso_id_curso_seq    SEQUENCE     �   CREATE SEQUENCE public.curso_id_curso_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.curso_id_curso_seq;
       public               postgres    false    225            �           0    0    curso_id_curso_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.curso_id_curso_seq OWNED BY public.curso.id_curso;
          public               postgres    false    224            �            1259    41064    familia    TABLE     C  CREATE TABLE public.familia (
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
       public         heap r       postgres    false            �            1259    41070    institucion    TABLE       CREATE TABLE public.institucion (
    dni_institu integer NOT NULL,
    nombre character varying(100),
    apellido character varying(100),
    gmail character varying(150),
    telefono character varying(100),
    password text,
    id_roles_institu integer NOT NULL,
    roles character varying,
    curso integer NOT NULL,
    CONSTRAINT chk_gmail_institucion CHECK (((gmail)::text ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'::text)),
    CONSTRAINT chk_telefono_institucion CHECK (((telefono)::text ~ '^[0-9]{7,15}$'::text))
);
    DROP TABLE public.institucion;
       public         heap r       postgres    false            �            1259    41142    institucion_curso_seq    SEQUENCE     �   CREATE SEQUENCE public.institucion_curso_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.institucion_curso_seq;
       public               postgres    false    218            �           0    0    institucion_curso_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.institucion_curso_seq OWNED BY public.institucion.curso;
          public               postgres    false    227            �            1259    41077    recuperacion_password    TABLE     �   CREATE TABLE public.recuperacion_password (
    token character varying(100) NOT NULL,
    dni_usuario integer NOT NULL,
    tipo_usuario character varying(20) NOT NULL,
    fecha_expiracion timestamp without time zone NOT NULL
);
 )   DROP TABLE public.recuperacion_password;
       public         heap r       postgres    false            �            1259    41080    roles_id_roles_seq    SEQUENCE     {   CREATE SEQUENCE public.roles_id_roles_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.roles_id_roles_seq;
       public               postgres    false            �            1259    41081    roles    TABLE     �   CREATE TABLE public.roles (
    id_roles integer DEFAULT nextval('public.roles_id_roles_seq'::regclass) NOT NULL,
    nombre_roles character varying(100)
);
    DROP TABLE public.roles;
       public         heap r       postgres    false    220            ;           2604    41107    asistencia id_asistencias     DEFAULT     �   ALTER TABLE ONLY public.asistencia ALTER COLUMN "id_asistencias " SET DEFAULT nextval('public."asistencia_id_asistencias _seq"'::regclass);
 K   ALTER TABLE public.asistencia ALTER COLUMN "id_asistencias " DROP DEFAULT;
       public               postgres    false    223    222    223            <           2604    41114    curso id_curso    DEFAULT     p   ALTER TABLE ONLY public.curso ALTER COLUMN id_curso SET DEFAULT nextval('public.curso_id_curso_seq'::regclass);
 =   ALTER TABLE public.curso ALTER COLUMN id_curso DROP DEFAULT;
       public               postgres    false    225    224    225            =           2604    41130    curso asistencia    DEFAULT     t   ALTER TABLE ONLY public.curso ALTER COLUMN asistencia SET DEFAULT nextval('public.curso_asistencia_seq'::regclass);
 ?   ALTER TABLE public.curso ALTER COLUMN asistencia DROP DEFAULT;
       public               postgres    false    226    225            9           2604    41143    institucion curso    DEFAULT     v   ALTER TABLE ONLY public.institucion ALTER COLUMN curso SET DEFAULT nextval('public.institucion_curso_seq'::regclass);
 @   ALTER TABLE public.institucion ALTER COLUMN curso DROP DEFAULT;
       public               postgres    false    227    218            �          0    41104 
   asistencia 
   TABLE DATA           g   COPY public.asistencia ("id_asistencias ", fecha_asistencia, "asistió", "justificación") FROM stdin;
    public               postgres    false    223   �5       �          0    41111    curso 
   TABLE DATA           f   COPY public.curso (id_curso, "año", "división", turno, ciclo, especialidad, asistencia) FROM stdin;
    public               postgres    false    225   6       �          0    41064    familia 
   TABLE DATA           p   COPY public.familia (dni_familia, nombre, apellido, gmail, telefono, password, dni_institu_familia) FROM stdin;
    public               postgres    false    217   36       �          0    41070    institucion 
   TABLE DATA              COPY public.institucion (dni_institu, nombre, apellido, gmail, telefono, password, id_roles_institu, roles, curso) FROM stdin;
    public               postgres    false    218   d8       �          0    41077    recuperacion_password 
   TABLE DATA           c   COPY public.recuperacion_password (token, dni_usuario, tipo_usuario, fecha_expiracion) FROM stdin;
    public               postgres    false    219   �:       �          0    41081    roles 
   TABLE DATA           7   COPY public.roles (id_roles, nombre_roles) FROM stdin;
    public               postgres    false    221   �;       �           0    0    asistencia_id_asistencias _seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public."asistencia_id_asistencias _seq"', 1, false);
          public               postgres    false    222            �           0    0    curso_asistencia_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.curso_asistencia_seq', 1, false);
          public               postgres    false    226            �           0    0    curso_id_curso_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.curso_id_curso_seq', 1, false);
          public               postgres    false    224            �           0    0    institucion_curso_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.institucion_curso_seq', 4, true);
          public               postgres    false    227            �           0    0    roles_id_roles_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.roles_id_roles_seq', 8, true);
          public               postgres    false    220            B           2606    41086    familia familia_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.familia
    ADD CONSTRAINT familia_pkey PRIMARY KEY (dni_familia);
 >   ALTER TABLE ONLY public.familia DROP CONSTRAINT familia_pkey;
       public                 postgres    false    217            D           2606    41088    institucion institucion_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT institucion_pkey PRIMARY KEY (dni_institu);
 F   ALTER TABLE ONLY public.institucion DROP CONSTRAINT institucion_pkey;
       public                 postgres    false    218            J           2606    41128    asistencia pk_asistencia 
   CONSTRAINT     e   ALTER TABLE ONLY public.asistencia
    ADD CONSTRAINT pk_asistencia PRIMARY KEY ("id_asistencias ");
 B   ALTER TABLE ONLY public.asistencia DROP CONSTRAINT pk_asistencia;
       public                 postgres    false    223            L           2606    41118    curso pk_curso 
   CONSTRAINT     R   ALTER TABLE ONLY public.curso
    ADD CONSTRAINT pk_curso PRIMARY KEY (id_curso);
 8   ALTER TABLE ONLY public.curso DROP CONSTRAINT pk_curso;
       public                 postgres    false    225            F           2606    41090 0   recuperacion_password recuperacion_password_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY public.recuperacion_password
    ADD CONSTRAINT recuperacion_password_pkey PRIMARY KEY (token);
 Z   ALTER TABLE ONLY public.recuperacion_password DROP CONSTRAINT recuperacion_password_pkey;
       public                 postgres    false    219            H           2606    41092    roles roles_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id_roles);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public                 postgres    false    221            P           2606    41137    curso fk_asistencia    FK CONSTRAINT     �   ALTER TABLE ONLY public.curso
    ADD CONSTRAINT fk_asistencia FOREIGN KEY (asistencia) REFERENCES public.asistencia("id_asistencias ") NOT VALID;
 =   ALTER TABLE ONLY public.curso DROP CONSTRAINT fk_asistencia;
       public               postgres    false    223    4682    225            N           2606    41150    institucion fk_curso    FK CONSTRAINT     �   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT fk_curso FOREIGN KEY (curso) REFERENCES public.curso(id_curso) NOT VALID;
 >   ALTER TABLE ONLY public.institucion DROP CONSTRAINT fk_curso;
       public               postgres    false    225    4684    218            M           2606    41093    familia fk_dni_institu_familia    FK CONSTRAINT     �   ALTER TABLE ONLY public.familia
    ADD CONSTRAINT fk_dni_institu_familia FOREIGN KEY (dni_institu_familia) REFERENCES public.institucion(dni_institu) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.familia DROP CONSTRAINT fk_dni_institu_familia;
       public               postgres    false    217    218    4676            O           2606    41098    institucion fk_id_roles_institu    FK CONSTRAINT     �   ALTER TABLE ONLY public.institucion
    ADD CONSTRAINT fk_id_roles_institu FOREIGN KEY (id_roles_institu) REFERENCES public.roles(id_roles) ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.institucion DROP CONSTRAINT fk_id_roles_institu;
       public               postgres    false    4680    221    218            �      x������ � �      �      x������ � �      �   !  x���Mk�1��o��=��Lf2��R�P�R�����L�-vw�[A��fU� �	�|��T���,O^����ֻeӷѿ/?O���;��f!- �i�����'�E�DO`U�|x����j���~_$0m��aY�[�E�5�s��Zäj���T2�^[+���"U��ǃ�cT(3�&B�C�� h��(�'Q#K�ݎ�&͌��n����������w���������'p���|��9�����뛱}q���ݬG��\��w�2 j/JR,�P�J RyJ莽�{�֪��T2�'��Y��c�̩�j�a�b�e������/��Xb�9����_pH�{I��>��_�_�/�ӻ��H�ĥ$�܆5�\� gjF���F�.�Ԣq��4&�	h0̑{�5���:ӧ�S��>�H@��AW���l i�O6B�_֖������������|����f5ӜXИ��.)�*�)�\����{F�b�'ށ����6��Z6$�N$�9Sh�2MtT�?����KDʳ�X����~ j� 8      �   J  x����j�I���O�E�MI%�ū�؁�N6f6*�d�/���?��SC�٤nP��sNk�W��?�xW;�U�	R���Y�O�z|�J�Q8����^$,�^�������Ǿ��v}����U�N��ٝFD�1!C�9����^@�k#��U��I�XzjJ�5��e��.� ��S�a���C������ �a��u�q\lh� 󄓄1�IN?�ᤅ�(��xqy�z��p���-q#w(8��<���ĜG+���؁Z�sΪ�6���)wv,fmL=���^�&Du��cQ���Q����gvi�V�����a����#���Ξ�n����v]g��G=vY����G	��O�q������j����$z{|ْD�:-�I)�[r�>�N{55��9���j3��
�Q-� A3�ϵ�}�UfG�M#�A�1�<����S�y�s+��P�s;v�I��l	i��N��p#��1\��.�m��{�����+��5mk��S'I�h�M��a:��@�%)�6�%&v�hͥ��yƓ��ltWՁ�S��<�/Al�KŉM�h���S-VI!����^֙`��{��l�pp
�      �   �   x�����1D�s;�I c��X�n[i7��v3��zR��v��8�{wa��6��V�����:���}�EH(@�B��'Keu�Q����~��K!C��m٘�+�S�JG2*dk�H������s�僇�WP'[%�'/�{��@d>��M���3�������8;Wij��O-��yM�      �   B   x�3�LL����,.)JL�/�2�(JMN-(��9]�S�JR�,8�R�RRRBsrR��b���� ^A�     