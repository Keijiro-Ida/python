
import sqlite3
import re

dbname = 'customer.db'
con = sqlite3.connect(dbname)
cur = con.cursor()


def create_ship_ad(post_number, address, building, number):
    if  '】' in address:
        address = address.split('】')[1]

    if(re.search('^[0-9]{3}-[0-9]{4}', address)):
        post_number = address[0:8]
        address = address[8:].strip()

    cur.execute('update customer set shipping_post_number = ?, shipping_address = ?, shipping_address_building = ? where number=?', (post_number, address, building,number))

def create_pick_ad(post_number, address, building, number):

    if  '】' in address:
        address = address.split('】')[1]

    if(re.search('^[0-9]{3}-[0-9]{4}', address)):
        post_number = address[0:8]
        address = address[8:].strip()

    cur.execute('update customer set pick_up_post_number = ?, pick_up_address = ?, pick_up_address_building = ? where number=?', (post_number, address, building,number))

def create_ad(post_number, address, building, number):

    if(re.search('^[0-9]{3}-[0-9]{4}', address)):
        # print(address[0:8])
        post_number = address[0:8]
        address = address[8:].strip()

    cur.execute('UPDATE customer SET current_post_number = ?, current_address = ?, current_address_building = ? WHERE number=?', (post_number, address, building,number))

def create_cur_ad(post_number, address, building, number):

    if '】' in address:
        address = address.split('】')[1].strip()


    if(re.search('^[0-9]{3}-[0-9]{4}', address)):


        post_number = address[0:8]
        address = address[8:].strip()

    cur.execute('UPDATE customer SET current_post_number = ?, current_address = ?, current_address_building = ? WHERE number=?', (post_number, address, building,number))

def create_oth_ad(post_number, address, building, number):
    other = address.split('】')[0].replace('【', '')
    address = address.split('】')[1]
    if(re.search('^[0-9]{3}-[0-9]{4}', address)):

        post_number = address[0:8]
        address = address[8:].strip()

    address = '【' + other + '】' + address

    cur.execute('UPDATE customer SET other_post_number = ?, other_address = ? WHERE number=?', (post_number, address,number))

def add_bld(num, building, number):
    if num != 4 and '】' in building :
        building = building.split('】')[1]
    if num == 1:
        cur.execute('UPDATE customer SET current_address_building = ? WHERE number=?', (building, number))
    elif num == 2:
        cur.execute('UPDATE customer SET shipping_address_building = ? WHERE number=?', (building, number))
    elif num == 3:
        cur.execute('UPDATE customer SET pick_up_address_building = ? WHERE number=?', (building, number))
    else:
        cur.execute('UPDATE customer SET other_address_building = ? WHERE number=?', (building, number))


cur.execute("select * from customer")

list = cur.fetchall()
print(len(list))

for i in range(len(list)):
    print(str(i))
    if list[i][4] != None:
        add_arr = list[i][4].splitlines()
    else:
        add_arr = ['']
    address = add_arr[0]
    number = int(list[i][1])
    building = list[i][5]
    post_number = None

    if len(add_arr) == 1:

        if 'ボール' in address:
            create_ship_ad(post_number, address, building, number)

        elif '集荷' in address:

            create_pick_ad(post_number, address, building, number)

        else:

            create_ad(post_number, address, building, number)

    else:
        add_length = len(add_arr)

        if building != None:
            bld_arr = building.splitlines()
        building = None

        for j in range(add_length):
            address = add_arr[j]
            post_number = None

            if '現住所' in address:

               create_cur_ad(post_number, address, building, number)

            elif 'ボール' in address:

                create_ship_ad(post_number, address, building, number)

            elif '集荷先' in address or 'レコード' in address:

                create_pick_ad(post_number, address, building, number)


            elif '】' in address:

                create_oth_ad(post_number, address, building, number)

            else:
                cur.execute('UPDATE customer SET current_post_number = ?, current_address = ?, current_address_building = ? WHERE number=?', (post_number, address, building,number))

        for j in range(len(bld_arr)):
            building = bld_arr[j]

            if '現住所' in building:

               add_bld(1,  building, number)

            elif 'ボール' in building:
                add_bld(2, building, number)


            elif '集荷先' in building or 'レコード' in building:

                add_bld(3, building, number)

            else:
                add_bld(4, building, number)








con.commit()
con.close()
