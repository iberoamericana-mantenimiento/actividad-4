# Arquitectura de Patrones

Este repositorio contiene varios ejemplos de patrones de arquitectura implementados en Python. Los proyectos están organizados en diferentes carpetas, cada una representando un patrón de arquitectura diferente.

## Estructura del Proyecto

- `capas/`: Implementación del patrón de arquitectura en capas.
  - `app.py`: Punto de entrada para la aplicación en capas.
  - `data.py`: Módulo de datos que maneja la persistencia de usuarios.
  - `logic.py`: Módulo de lógica que maneja la lógica de negocio de usuarios.
  - `presentation.py`: Módulo de presentación que maneja la interfaz de usuario.

- `microservices/`: Implementación del patrón de microservicios.
  - `app.py`: Punto de entrada para la aplicación de microservicios.
  - `comment_service.py`: Servicio de comentarios.
  - `models.py`: Modelos de datos para usuarios, posts y comentarios.
  - `post_service.py`: Servicio de posts.
  - `user_service.py`: Servicio de usuarios.

- `mvc/`: Implementación del patrón Modelo-Vista-Controlador (MVC).
  - `app.py`: Punto de entrada para la aplicación MVC.
  - `controllers.py`: Controladores que manejan la lógica de negocio.
  - `index.html`: Vista que muestra los datos.
  - `models.py`: Modelos de datos para usuarios, posts y comentarios.

- `pipeline/`: Implementación del patrón de arquitectura de pipeline.
  - `app.py`: Punto de entrada para la aplicación de pipeline.
  - `all_in_lower.py`: Módulo que convierte el texto a minúsculas.
  - `no_numbers.py`: Módulo que elimina los números del texto.
  - `to_list.py`: Módulo que convierte el texto en una lista.

- `server-client/`: Implementación del patrón cliente-servidor.
  - `app.py`: Punto de entrada para la aplicación cliente-servidor.
  - `client.py`: Cliente que interactúa con el servidor.
  - `server.py`: Servidor que maneja las solicitudes del cliente.

## Ejecución de los Proyectos

### Capas

Para ejecutar el proyecto de capas, navega a la carpeta `capas` y ejecuta el siguiente comando:

```sh
python app.py
```

### Microservicios

Para ejecutar el proyecto de `microservicios`, navega a la carpeta microservices y ejecuta el siguiente comando:

```sh
python app.py
```

### MVC

Para ejecutar el proyecto `mvc`, navega a la carpeta mvc y ejecuta el siguiente comando:

```sh
python app.py
```

### Pipeline

Para ejecutar el proyecto de `pipeline`, navega a la carpeta pipeline y ejecuta el siguiente comando:

```sh
python app.py
```

### Cliente-Servidor

Para ejecutar el proyecto `cliente-servidor`, navega a la carpeta server-client y ejecuta los comandos:

```sh
python app.py

python server.py
```

## Historias de usuario

- [Capas](./user-histories/US-001.md)
- [Microservicios](./user-histories/US-002.md)
- [MVC](./user-histories/US-003.md)
- [Pipeline](./user-histories/US-004.md)
- [Cliente-Servidor](./user-histories/US-005.md)
