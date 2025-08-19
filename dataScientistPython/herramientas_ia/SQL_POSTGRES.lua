--SQL POSTGRES 
-- Genera un modelo de datos con las tablas customer, orders, oreders_detail, product, utilizando foreing keys

-- Crear tabla "Clientes"
CREATE TABLE Clientes (
  client_id SERIAL PRIMARY KEY,
  nombre VARCHAR(255),
  apellido VARCHAR(255),
  direccion VARCHAR(255),
  correo_electronico VARCHAR(255),
  numero_telefono VARCHAR(20)
  -- agregar otras columnas según sea necesario
);

-- Crear tabla "Reclamos"
CREATE TABLE Reclamos (
  reclamo_id SERIAL PRIMARY KEY,
  client_id INT REFERENCES Clientes(client_id),
  fecha DATE,
  descripcion TEXT,
  estado VARCHAR(50)
  -- agregar otras columnas según sea necesario
);

-- Crear tabla "Informacion Sensible"
CREATE TABLE Informacion_Sensible (
  informacion_id SERIAL PRIMARY KEY,
  client_id INT REFERENCES Clientes(client_id),
  tipo VARCHAR(50),
  valor TEXT
  -- agregar otras columnas según sea necesario
);

-- Crear tabla "Productos"
CREATE TABLE Productos (
  producto_id SERIAL PRIMARY KEY,
  nombre VARCHAR(255),
  descripcion TEXT
  -- agregar otras columnas según sea necesario
);

-- Crear tabla "Reclamos_Productos"
CREATE TABLE Reclamos_Productos (
  reclamo_id INT REFERENCES Reclamos(reclamo_id),
  producto_id INT REFERENCES Productos(producto_id),
  PRIMARY KEY (reclamo_id, producto_id)
);

-- Crear tabla "Relaciones_Productos_Clientes"
CREATE TABLE Relaciones_Productos_Clientes (
  cliente_id INT REFERENCES Clientes(client_id),
  producto_id INT REFERENCES Productos(producto_id),
  fecha_ultima_interaccion DATE,
  cantidad_interacciones INT,
  PRIMARY KEY (cliente_id, producto_id)
);

-- CREA indices compuestos para mejorar la velocidad de las consultas en la tabla orders
CREATE INDEX idx_orders_client_id ON Orders (client_id);

-- agrega las columnas created_at a las tabla orders_detail
ALTER TABLE Orders_Detail
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
