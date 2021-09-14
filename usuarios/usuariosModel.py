import database.config as conexion

connect = conexion.dataConnect()
database=connect[0]
cursor=connect[1]

class Usuario:
    def __init__(self,nombre,apellidos,email,password):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.password=password
        # self.fecha="CURDATE()"

    def guardar(self):
        sql="INSERT INTO usuarios VALUE (null, %s, %s, %s,%s,now())"
        usuarios=(self.nombre,self.apellidos,self.email,self.password)
        cursor.execute(sql,usuarios)       
        database.commit()
        return f'{self.nombre} Guardado correctamente'

    def buscar(email):
        sql = f'SELECT * FROM usuarios WHERE email="{email}"'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    
    # def listar():
    #     sql="SELECT * FROM usuarios "
    #     cursor.execute(sql)
    #     result= cursor.fetchall()
    #     return result