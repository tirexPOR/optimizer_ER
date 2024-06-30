import mysql.connector
from mysql.connector import Error

import Variables

def downloadList(armorType):
    global cursor, connection, records

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='project_db',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        query = "select a.Armor_name " \
                "from armor a inner join type t on a.Armor_type=t.Type_ID " \
                "where t.Type_name='" + armorType + "';"
        cursor.execute(query)

        records = []
        record = cursor.fetchone()
        while record:
            records.append(record[0])
            record = cursor.fetchone()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    return records

def downloadRes():
    global cursor, connection, records

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='project_db',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        world = ''
        enemies = ''

        for i in range(len(Variables.regions)):
            if Variables.regions[i] == True:
                world += '"' + Variables.regions[i + 1] + '", '
        for i in range(len(Variables.bosses)):
            if Variables.bosses[i] == True:
                enemies += '"' + Variables.bosses[i + 1] + '", '

        world = world.removesuffix(', ')
        enemies = enemies.removesuffix(', ')

        query = "select a.Armor_physic, a.Armor_vs_strike, a.Armor_vs_slash, a.Armor_vs_pierce, " \
                "a.Armor_magic, a.Armor_fire, a.Armor_electric, a.Armor_holy, a.Armor_imm, " \
                "a.Armor_rob, a.Armor_focus, a.Armor_vit, a.Armor_poise, a.Armor_weight " \
                "from (((armor a inner join type t on a.Armor_type=t.Type_ID) " \
                "inner join regions r on a.Armor_region=r.Region_ID) " \
                "inner join bosses b on a.Armor_boss=b.Boss_ID) " \
                "inner join classes c on a.Armor_class=c.Class_ID " \
                "where c.Class_name='" + Variables.classes[Variables.startClass] + "' and " \
                "a.Armor_weight<=" + str(Variables.load) + " or " \
                "c.Class_name = 'None' and " \
                "b.Boss_name in (" + enemies + ") and " \
                "r.Region_name in (" + world + ") and " \
                "a.Armor_weight<=" + str(Variables.load) + " " \
                "order by a.Armor_type, a.Armor_name asc;"

        cursor.execute(query)

        records = cursor.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    return records

def downloadLen(armorType):
    global cursor, connection, records

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='project_db',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        world = ''
        enemies = ''

        for i in range(len(Variables.regions)):
            if Variables.regions[i] == True:
                world += '"' + Variables.regions[i + 1] + '", '
        for i in range(len(Variables.bosses)):
            if Variables.bosses[i] == True:
                enemies += '"' + Variables.bosses[i + 1] + '", '

        world = world.removesuffix(', ')
        enemies = enemies.removesuffix(', ')

        query = "select count(*) " \
                "from (((armor a inner join type t on a.Armor_type=t.Type_ID) " \
                "inner join regions r on a.Armor_region=r.Region_ID) " \
                "inner join bosses b on a.Armor_boss=b.Boss_ID) " \
                "inner join classes c on a.Armor_class=c.Class_ID " \
                "where c.Class_name='" + Variables.classes[Variables.startClass] + "' and " \
                "a.Armor_weight<=" + str(Variables.load) + " and " \
                "t.Type_name='" + armorType + "' or " \
                "c.Class_name = 'None' and " \
                "b.Boss_name in (" + enemies + ") and " \
                "r.Region_name in (" + world + ") and " \
                "a.Armor_weight<=" + str(Variables.load) + " and " \
                "t.Type_name='" + armorType + "';"
        cursor.execute(query)

        record = cursor.fetchone()
        records = record[0]


    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    return records

def downloadNames():
    global cursor, connection, records

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='project_db',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        world = ''
        enemies = ''

        for i in range(len(Variables.regions)):
            if Variables.regions[i] == True:
                world += '"' + Variables.regions[i + 1] + '", '
        for i in range(len(Variables.bosses)):
            if Variables.bosses[i] == True:
                enemies += '"' + Variables.bosses[i + 1] + '", '

        world = world.removesuffix(', ')
        enemies = enemies.removesuffix(', ')

        query = "select a.Armor_name " \
                "from (((armor a inner join type t on a.Armor_type=t.Type_ID) " \
                "inner join regions r on a.Armor_region=r.Region_ID) " \
                "inner join bosses b on a.Armor_boss=b.Boss_ID) " \
                "inner join classes c on a.Armor_class=c.Class_ID " \
                "where c.Class_name='" + Variables.classes[Variables.startClass] + "' and " \
                "a.Armor_weight<=" + str(Variables.load) + " or " \
                "c.Class_name = 'None' and " \
                "b.Boss_name in (" + enemies + ") and " \
                "r.Region_name in (" + world + ") and " \
                "a.Armor_weight<=" + str(Variables.load) + " " \
                "order by a.Armor_type, a.Armor_name asc;"

        cursor.execute(query)
        records = []
        record = cursor.fetchone()
        while record:
            records.append(record[0])
            record = cursor.fetchone()


    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    return records

def downloadResSet(name):
    global cursor, connection, records

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='project_db',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        world = ''
        enemies = ''

        for i in range(len(Variables.regions)):
            if Variables.regions[i] == True:
                world += '"' + Variables.regions[i + 1] + '", '
        for i in range(len(Variables.bosses)):
            if Variables.bosses[i] == True:
                enemies += '"' + Variables.bosses[i + 1] + '", '

        world = world.removesuffix(', ')
        enemies = enemies.removesuffix(', ')

        query = 'select a.Armor_physic, a.Armor_vs_strike, a.Armor_vs_slash, a.Armor_vs_pierce, ' \
                'a.Armor_magic, a.Armor_fire, a.Armor_electric, a.Armor_holy, a.Armor_imm, ' \
                'a.Armor_rob, a.Armor_focus, a.Armor_vit, a.Armor_poise, a.Armor_weight ' \
                'from armor a where a.Armor_name="' + name + '";'

        cursor.execute(query)

        records = cursor.fetchone()


    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    return records
