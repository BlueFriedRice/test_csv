import pymysql as ps
import pandas as pd
import os

main_container = Element("main_container")

room_option = Element("room_option")
patient_option = Element("patient_option")
room_option_name = room_option.value
patient_option_name = patient_option.value

new_row_field = ""

p_df = pd.read_csv(os.getcwd() + os.sep + "p_info2.csv", encoding="utf-8-sig")

def csv_to_py(p_df, room_option_name, patient_option_name):

    if room_option_name == '전체호실':
      p_df = p_df

    elif room_option_name == '1호실':
      p_df = p_df[p_df['no_room'] == 1]
      p_df = p_df.reset_index()

    elif room_option_name == '2호실':
      p_df = p_df[p_df['no_room'] == 2]
      p_df = p_df.reset_index()

    elif room_option_name == '3호실':
      p_df = p_df[p_df['no_room'] == 3]
      p_df = p_df.reset_index()

    elif room_option_name == '4호실':
      p_df = p_df[p_df['no_room'] == 4]
      p_df = p_df.reset_index()


    if patient_option_name == '전체 환자':
      result = p_df

    elif patient_option_name == '낙상 주의 환자':
      result = p_df[p_df['fallen'] == '예']

    elif patient_option_name == '욕창 주의 환자':  
      result = p_df[p_df['bedsore'] == '예']

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

result = csv_to_py(p_df, room_option_name, patient_option_name)

flag = 1
info_txt = 0
i = 0
for i in range(len(result)):
  bed_info, name_info, age_sex_info, fallen_info, bedsore_info, stat_info = create_new_card(flag)

  info(result.loc[i], bed_info, name_info, age_sex_info, fallen_info, bedsore_info, stat_info)
  
  flag = flag + 1

  if flag == 8:
    flag = 1

      