from django.db import connection

def cantidad_alquileres(student_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT get_cantidad_alquileres(%s)", [student_id])
        result = cursor.fetchone()[0]
    return result

def actualizar_dias_retraso():
    with connection.cursor() as cursor:
        cursor.execute("CALL dias_de_retraso")