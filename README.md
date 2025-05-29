# 🚀 Colección de Scripts Utilitarios

## Descripción
Esta colección contiene scripts de Python diseñados para automatizar y simplificar tareas comunes de procesamiento de datos. Cada script está optimizado para resolver un problema específico de manera eficiente y fácil de usar.

## Scripts Disponibles

### 📊 separar_csv.py
Divide archivos CSV grandes en partes más pequeñas y manejables.

**Características:**
- División inteligente que mantiene la integridad de los datos
- Nombrado automático de archivos resultantes
- Mensajes de confirmación para seguimiento del proceso

**Uso:**
```bash
python separar_csv.py <archivo.csv> <numero_de_partes>
```

**Ejemplo:**
```bash
python separar_csv.py datos_ventas_2024.csv 5
```

Este comando dividirá el archivo `datos_ventas_2024.csv` en 5 partes iguales, generando:
- datos_ventas_2024_parte_1.csv
- datos_ventas_2024_parte_2.csv
- ...
- datos_ventas_2024_parte_5.csv

**Requisitos:**
- Python 3.6+
- pandas
- math (biblioteca estándar)
- sys (biblioteca estándar)
- os (biblioteca estándar)

## 🔧 Instalación de Dependencias

Para instalar las dependencias necesarias:

```bash
pnpm install pandas
```

## 🌟 Casos de Uso Comunes

### Procesamiento de Datos Grandes
Cuando necesites trabajar con archivos CSV demasiado grandes para ser procesados en memoria:
1. Divide el archivo en partes manejables con `separar_csv.py`
2. Procesa cada parte individualmente
3. Combina los resultados si es necesario

### Distribución de Trabajo
Para distribuir tareas de procesamiento entre varios sistemas:
1. Divide el archivo de datos con `separar_csv.py`
2. Asigna cada parte a un sistema o proceso diferente
3. Procesa en paralelo para mayor eficiencia

## 🤝 Contribuciones
¿Tienes ideas para nuevos scripts o mejoras? ¡Las contribuciones son bienvenidas!

## 📝 Licencia
Este proyecto está disponible como código abierto bajo la licencia MIT.
