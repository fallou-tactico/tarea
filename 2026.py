def es_bisiesto(anio):
    
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


dia_semana_actual = 0 

domingos_primer_dia = 0
total_dias_siglo_xx = 0
anios_bisiestos = 0


for anio in range(1900, 2001):
    bisiesto = es_bisiesto(anio)
    
    
    if anio >= 1901 and bisiesto:
        anios_bisiestos += 1

    for mes in range(12):
        
        if anio >= 1901 and dia_semana_actual == 6:
            domingos_primer_dia += 1

       
        dias_en_este_mes = dias_por_mes[mes]
        if mes == 1 and bisiesto:  
            dias_en_este_mes = 29

        
        if anio >= 1901:
            total_dias_siglo_xx += dias_en_este_mes

        
        dia_semana_actual = (dia_semana_actual + dias_en_este_mes) % 7

print(f"Total de días (1 ene 1901 - 31 dic 2000): {total_dias_siglo_xx}")
print(f"Total de años bisiestos en ese periodo: {anios_bisiestos}")
print(f"Domingos que cayeron en día 1 de mes: {domingos_primer_dia}")