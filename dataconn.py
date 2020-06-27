import sqlite3

class DataConn:
    filename = None
    def __init__(self, filename):
        self.filename = filename
    
    def build_tables(self):
        # DO NOT CALL IT TWICE ON THE SAME FILE
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                     (uid INTEGER PRIMARY KEY, 
                      username TEXT NOT NULL, 
                      password TEXT NOT NULL)''')
        c.execute('''CREATE TABLE projects
                     (id INTEGER PRIMARY KEY, 
                      name TEXT NOT NULL, 
                      owner_uid INTEGER NOT NULL, 
                      permission INTEGER NOT NULL)''')
        c.execute('''CREATE TABLE layers
                     (id INTEGER PRIMARY KEY, 
                      name TEXT NOT NULL, 
                      url TEXT NOT NULL, 
                      type TEXT NOT NULL,
                      location TEXT NOT NULL,
                      pid INTEGER NOT NULL)''')
        conn.commit()
        conn.close()
    
    def add_user(self, username, password):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute(''' INSERT INTO users(username, password)
                      VALUES('{}', '{}')
                   '''.format(username, password))
        conn.commit()
        conn.close()
   
    def check_login(self, username, password):
        """
        Get user id with username and password. 
        If the username or password are wrong, return None
        """
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute('''SELECT uid FROM users
                     WHERE username='{}' AND password='{}';'''.format(username, password))
        uid_list = c.fetchall()
        conn.close()
        if len(uid_list) == 0:
            return None
        else:
            return uid_list[0][0]

    def add_project(self, project_name, owner_uid):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute(''' INSERT INTO projects(name, owner_uid, permission)
                      VALUES('{}',{}, 7);'''.format(project_name, owner_uid))
        conn.commit()
        conn.close()
    
    def add_layer(self, layer_name, url, layer_type, location, project_id):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute(''' INSERT INTO layers(name, url, type, location, pid)
                      VALUES('{}','{}', '{}', '{}', {});'''.format(layer_name, url, layer_type, location, project_id))
        conn.commit()
        conn.close()
    def get_projects_of_user(self, uid):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute('''SELECT id, name, permission FROM projects
                     WHERE owner_uid=?''', str(uid))
        pj_list = c.fetchall()
        pj_list = [{'pid': p[0], 
                    'name': p[1], 
                    'permission': p[2]} for p in pj_list]
        conn.close()
        return pj_list

    def update_user_password(self, username, new_password):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute(''' UPDATE users
                      SET password='{}' WHERE username='{}';'''.format(
                      new_password, username))
        conn.commit()
        conn.close()
    
    def get_layers_of_project(self, pid):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute('''SELECT id, name, url, type, location FROM layers
                     WHERE pid=?''', str(pid))
        layer_list = c.fetchall()
        layer_list = [{'id': p[0], 
                       'name': p[1], 
                       'url': p[2], 
                       'type': p[3],
                       'location': p[4]} for p in layer_list]
        conn.close()
        return layer_list


if __name__ == "__main__":
    conn = DataConn('demo.db')
    conn.build_tables()
    conn.add_user("admin", "admin")
    # conn.add_project("Default Project", 1)
