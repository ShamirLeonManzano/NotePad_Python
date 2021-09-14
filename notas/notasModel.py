import database.config as conexion 

connect = conexion.dataConnect()
database=connect[0]
cursor=connect[1]

class Nota:

    def __init__(self, usuario_id,titulo,descripcion):            
        self.usuario_id = usuario_id
        self.titulo= titulo   
        self.descripcion= descripcion
        

    def guardar(self):
        sql="INSERT INTO notas value (null, %s, %s,%s,now())"
        nota=(self.usuario_id, self.titulo, self.descripcion)
        cursor.execute(sql,nota)
        database.commit()
        return f'La nota ha sido guardada.'

    def listar(idUser):
        sql=f'SELECT * FROM notas WHERE usuario_id="{idUser}"'
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
        
    def delete(titulo):
        sql = f'DELETE FROM notas WHERE titulo="{titulo}"'
        cursor.execute(sql)
        database.commit()
        return f'la nota {titulo} ha sido eliminada'

    def buscar(titulo):
        sql = f'SELECT * FROM notas WHERE titulo="{titulo}"'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    

     