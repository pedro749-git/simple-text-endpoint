# simple-text-endpoint
API técnica desarrollada con **Python** y **FastAPI** para el procesamiento de strings mediante un endpoint POST. Este proyecto ha sido diseñado siguiendo buenas prácticas de desarrollo, incluyendo tipado estático, pruebas automatizadas y despliegue continuo (CI/CD).

## 🚀 Inicio Rápido

He configurado un flujo de trabajo que despliega automáticamente la imagen en Docker Hub. Puedes probar la API en menos de un minuto sin necesidad de descargar el código fuente.

### Ejecutar desde Docker Hub (Recomendado)
```bash
docker run -d -p 8000:8000 --name text-api pedro749/simple-text-endpoint:latest
```
La API estará disponible en: http://localhost:8000

### 🛠️ Otras formas de ejecución
#### Opción A: Construcción local con Docker

Si prefieres construir la imagen desde el repositorio:

Build: 
```bash 
docker build -t text-api .
```
Run: 
```bash 
docker run -d -p 8000:8000 --name text-api text-api
```

#### Opción B: Ejecución local con uv

Este proyecto utiliza uv para una gestión de dependencias rápido y eficiente.
Instalar dependencias:
```bash 
uv sync
```
Lanzar servidor: 
```bash 
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📝 Documentación de la API
Endpoint: ```POST /text```

Procesa un texto y devuelve el texto original, el texto en mayúsculas y la longitud del texto.

Request Body:
```json 
{
  "text": "Hola Olek AI Studio"
}
```
Ejemplo de Petición (cURL):

```bash 

curl -X POST http://localhost:8000/text \
     -H "Content-Type: application/json" \
     -d '{"text": "Hola Olek AI Studio"}'
```
Respuesta Exitosa (200 OK):
```json 
{
  "original": "Hola Olek AI Studio",
  "uppercase": "HOLA OLEK AI STUDIO",
  "char_count": 19
}
```

## 🧪 Calidad y Automatización
### Tests Automatizados

Se han implementado tests unitarios con pytest para cubrir casos de éxito, strings vacíos y validación de errores.

- Ejecutar localmente: ```uv run pytest```

### CI/CD Pipeline

El proyecto incluye un flujo en GitHub Actions que se activa en cada push a la rama main:

- Test: Verifica que el código cumple los estándares y pasa las pruebas.

- Build & Push: Construye la imagen de Docker y la sube automáticamente a Docker Hub solo si los tests son exitosos.

## 🏗️ Stack Tecnológico
- Lenguaje: Python 3.12
- Framework: FastAPI
- Validación: Pydantic
- Gestor de paquetes: uv
- Contenedores: Docker
- Automatización: GitHub Actions
