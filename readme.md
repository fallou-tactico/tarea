# 📅 Cálculo de Años Bisiestos y Domingos en Primer Día de Mes (1900 - 2000)

Este proyecto resuelve el cálculo de cuántos domingos cayeron en el primer día de un mes a lo largo del siglo XX, tomando en cuenta las reglas de los años bisiestos.

## 🚀 Lógica y Estructura del Programa

El algoritmo se desarrolló siguiendo los siguientes pasos:

1. **Definición de condiciones para años bisiestos:** Se establecieron las reglas lógicas necesarias para que el programa identifique cuándo un año es bisiesto.
2. **Inicialización de variables base:** Se definieron las estructuras para almacenar los días de la semana y la cantidad de días correspondientes a cada mes.
3. **Contadores acumulativos:** Se crearon variables contadoras para registrar el total de días transcurridos, años bisiestos y las coincidencias encontradas.
4. **Iteración de años (`for`):** Se implementó un ciclo `for` con un rango de `1900` a `2001` (para incluir el año 2000 sin errores de límite en el rango).
5. **Ajuste de febrero:** Dentro del ciclo anual, se evalúa si el año en curso es bisiesto; de ser así, se suma el día extra correspondiente al mes de febrero.
6. **Sincronización de días y fechas (`for`):** Mediante un ciclo anidado, se van intercalando y avanzando simultáneamente los días del mes con los días de la semana (por ejemplo: *1 - Lunes, 2 - Martes*, etc.).
7. **Filtrado de coincidencias:** Se añadió una condición para detectar y contabilizar cada vez que el **día 1** del mes coincide con un **domingo**.
8. **Salida de resultados:** Finalmente, se imprimen en consola los totales obtenidos: días transcurridos, años bisiestos y cantidad de domingos que cayeron en día primero.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python *(cámbialo si usaste otro lenguaje como C++, Java o JavaScript)*