import pymysql as ps

"""DataBase 정보"""
sql_args = {
    'host' : '127.0.0.1',   ## local host
    'port' : 3306,          ## local port
    'user' : 'admin',        ## Database ID
    'password' : 'tkdgns',  ## Database Password
    'db' : 'hong3'           ## DB name
}

main_container = Element("main_container")

room_option = Element("room_option")
patient_option = Element("patient_option")
room_option_name = room_option.value
patient_option_name = patient_option.value

new_row_field = ""

def DB_to_py(sql_args, room_option_name, patient_option_name):
  # 초기값 설정
    conn = None
    cursor = None

    sql = ""

    # DB Connection
    db = ps.connect(host = sql_args['host'], port = sql_args['port'], user = sql_args['user'], 
                    password = sql_args['password'], db = sql_args['db'], charset = 'utf8')

    # Cursor 객체 생성
    cursor = db.cursor(ps.cursors.DictCursor)

    if patient_option_name == '전체 환자':
      select_sql = "select * from {}".format(room_option_name)
      cursor.execute(select_sql)
      result = cursor.fetchall()

    elif patient_option_name == '낙상 주의 환자':
      select_sql = '''select * from {} 
                      where fallen = %s'''.format(room_option_name)
      cursor.execute(select_sql, '예')
      result = cursor.fetchall()

    elif patient_option_name == '욕창 주의 환자':  
      select_sql = '''select * from {} 
                      where fallen = %s'''.format(room_option_name)
      cursor.execute(select_sql, '예')
      result = cursor.fetchall()

    return result

def create_new_card(flag):

  if flag == 1:
    global new_row_field
    new_row_field = create("div", classes = "field has-addons")
    main_container.element.appendChild(new_row_field.element)

  new_card_field = create("div", classes = "column is-one-seventh")
  new_row_field.element.appendChild(new_card_field.element)

  new_card = create("div", classes = 'box')
  new_card_field.element.appendChild(new_card.element)

  bed_info = create("h6", classes = 'bed_info')
  name_info = create("h6", classes = 'name_info')
  age_sex_info = create("h6", classes = 'age_sex_info')
  fallen_info = create("h6", classes = 'fallen_info')
  bedsore_info = create("h6", classes = 'bedsore_info')
  stat_info = create("h6", classes = 'stat_info')

  new_card.element.appendChild(bed_info.element)
  new_card.element.appendChild(name_info.element)
  new_card.element.appendChild(age_sex_info.element)
  new_card.element.appendChild(fallen_info.element)
  new_card.element.appendChild(bedsore_info.element)
  new_card.element.appendChild(stat_info.element)

  return bed_info, name_info, age_sex_info, fallen_info, bedsore_info, stat_info

def info(result_args, bed_info, name_info, age_sex_info, fallen_info, bedsore_info, stat_info):
  bed_txt = "• {}병동 {}호실 {}번 침대".format(result_args['no_ward'],
                                              result_args['no_room'],
                                              result_args['no_bed'])
  name_txt = "• {}".format(result_args['p_name'])
  age_sex_txt = "• {}세, {}".format(result_args['age', 'sex'],)
  fallen_txt = "• {}".format(result_args['fallen'])
  bedsore_txt = "• {}".format(result_args['bedsore'])
  stat_txt = "• {}".format(result_args['status'])

  bed_info.element.innerText = bed_txt
  name_info.element.innerText = name_txt
  age_sex_info.element.innerText = age_sex_txt
  fallen_info.element.innerText = fallen_txt
  bedsore_info.element.innerText = bedsore_txt
  stat_info.element.innerText = stat_txt

result = DB_to_py(sql_args, room_option_name, patient_option_name)

flag = 1
info_txt = 0
i = 0
for i in range(len(result)):
  bed_info, name_info, age_sex_info, fallen_info, bedsore_info, stat_info = create_new_card(flag)

  info(result[i], bed_info, name_info, age_sex_info, fallen_info, bedsore_info, stat_info)
  
  flag = flag + 1

  if flag == 8:
    flag = 1

      