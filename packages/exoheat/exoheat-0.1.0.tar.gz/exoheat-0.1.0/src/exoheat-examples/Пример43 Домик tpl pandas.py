#Пример выполнения задания на КМ-3, расчет тепловых потерь за счет теплопроводности

import pandas as pd

#Импорт классов и методов
from LocalisationData import Localisation

#Локализация проекта
loc = Localisation()

#Импортирую материалы
from Matherials import r_conc_sht, r_floor_CARBON_ECO, r_float_st2

#Импортирую методику расчета тепловых потерь за счет теплопроводности
from exoheat import FloorLosses, f_zon
from exoheat import WallLosses as WL
from exoheat import WallInfiltration as WI
#Вывожу инструкцию
##print(help(WL))
##print(help(FloorLosses))
##print(help(WI))

H_зд = 3.1#м, высота отапливаемой части здания
l_ш = 9.5#м, ширина фасада
l_д = 11#м, длинна дома
h_цнс = 0.55#м - высота цокольного этажа(подвала) от уровня земли;
h_oнн = 0.95#м - высота от пола до подоконника;
h_oнв = 1.4#высоты окон;
l_oc = 1.3#м - ширина окон;
H_здк = H_зд + h_цнс + H_зд#м, высота здания от земли до конька
F_ф = H_зд * l_ш#площадь фасада дома
F_б = H_зд * l_д#площадь боковой стены дома
F_п = l_ш * l_д#площаь пола и потолка
dict_Q = {}

def tpl_WL(r_mat,ориентир_потерь,F_бок,ограждение='наружное'):
    return (loc,r_mat,ограждение,ориентир_потерь,F_бок,H_зд)
t_st_N = WL("ТП ст:Сев", *tpl_WL(r_conc_sht,'С',F_ф))
t_st_S = WL("ТП ст:Южн", *tpl_WL(r_conc_sht,'Ю',F_ф))
t_st_W = WL("ТП ст:Зап", *tpl_WL(r_conc_sht,'З',F_б))
t_st_E = WL("ТП ст:Вос", *tpl_WL(r_conc_sht,'В',F_б))
t_st_P = WL("ТП Чердак", *tpl_WL(r_conc_sht,'П',F_п,ограждение='чердачное'))

#Расчете потерь через стены
dict_Q[t_st_N.name] = t_st_N
dict_Q[t_st_S.name] = t_st_S
dict_Q[t_st_W.name] = t_st_W
dict_Q[t_st_E.name] = t_st_E
dict_Q[t_st_P.name] = t_st_P
#Расчете потерь через пол
F_zones = f_zon(l_ш, l_д)
##print("Массив площадей зон:" + str(F_zones))

def tpl_FL(зона):
    return (loc, r_floor_CARBON_ECO, 'пол', зона, F_zones[зона-1])
t_pol_1 = FloorLosses("ТП пол зона 1", *tpl_FL(1))
t_pol_2 = FloorLosses("ТП пол зона 2", *tpl_FL(2))
t_pol_3 = FloorLosses("ТП пол зона 3", *tpl_FL(3))

dict_Q[t_pol_1.name] = t_pol_1
dict_Q[t_pol_2.name] = t_pol_2
dict_Q[t_pol_3.name] = t_pol_3

снз='стена_непроизводственного_здания'
о3п='окно_или_балконная_дверь_с_тройными_переплетами_из_пластика'
def tpl_WI(r_mat,ориентир_потерь,ограждение=снз):
    return (loc, r_mat, ограждение, ориентир_потерь,H_здк,h_цнс)
tpl_hhn = (h_oнн + h_oнв, H_зд)
tpl_hhm = (h_oнн        , h_oнн + h_oнв)
tpl_hhp = (0            , h_oнн)

in_st_N = WI("Ин ст:Сев",*tpl_WI(r_conc_sht,'С'),*tpl_hhn,l_c=l_ш)#Ин-инфильтрация над окном
im_st_N = WI("Им ст:Сев",*tpl_WI(r_conc_sht,'С'),*tpl_hhm,l_c=l_ш-l_oc)#Им-инфильтрация между окнами
ip_st_N = WI("Ип ст:Сев",*tpl_WI(r_conc_sht,'С'),*tpl_hhp,l_c=l_ш)#Ип-инфильтрация под окном
im_ok_N = WI("Им ок:Сев",*tpl_WI(r_float_st2,'С',о3п),*tpl_hhm,l_c=l_oc)#Им-инфильтрация между окнами

in_st_S = WI("Ин ст:Южн",*tpl_WI(r_conc_sht,'Ю'),*tpl_hhn,l_c=l_ш)#Ин-инфильтрация над окном
im_st_S = WI("Им ст:Южн",*tpl_WI(r_conc_sht,'Ю'),*tpl_hhm,l_c=l_ш-l_oc)#Им-инфильтрация между окнами
ip_st_S = WI("Ип ст:Южн",*tpl_WI(r_conc_sht,'Ю'),*tpl_hhp,l_c=l_ш)#Ип-инфильтрация под окном
im_ok_S = WI("Им ок:Южн",*tpl_WI(r_float_st2,'Ю',о3п),*tpl_hhm,l_c=l_oc)#Им-инфильтрация между окнами

in_st_W = WI("Ин ст:Зап",*tpl_WI(r_conc_sht,'З'),*tpl_hhn,l_c=l_ш)#Ин-инфильтрация над окном
im_st_W = WI("Им ст:Зап",*tpl_WI(r_conc_sht,'З'),*tpl_hhm,l_c=l_ш-l_oc)#Им-инфильтрация между окнами
ip_st_W = WI("Ип ст:Зап",*tpl_WI(r_conc_sht,'З'),*tpl_hhp,l_c=l_ш)#Ип-инфильтрация под окном
im_ok_W = WI("Им ок:Зап",*tpl_WI(r_float_st2,'З',о3п),*tpl_hhm,l_c=l_oc)#Им-инфильтрация между окнами


dict_Q[ip_st_N.name] = ip_st_N
dict_Q[im_st_N.name] = im_st_N
dict_Q[in_st_N.name] = in_st_N
dict_Q[im_ok_N.name] = im_ok_N



data_lst = [t_st_N, t_st_S, t_st_W, t_st_E, t_st_P, t_pol_1, t_pol_2, t_pol_3, ip_st_N, im_st_N, in_st_N, im_ok_N, ip_st_S, im_st_S, in_st_S, im_ok_S, ip_st_W, im_st_W, in_st_W, im_ok_W]
data_cost = [[t_st_N, ip_st_N, im_st_N, in_st_N, im_ok_N], [t_st_S, ip_st_S, im_st_S, in_st_S, im_ok_S],
             [t_st_W, ip_st_W, im_st_W, in_st_W, im_ok_W], [t_st_E, ], [t_st_P,], [t_pol_1, t_pol_2, t_pol_3]]

##for key in dict_Q.keys():
##    print("Q_ " + key + " = " + str(round(dict_Q[key].Q_losses(), 5)) + " кВт")

data_dict = {}
id_name = []
Q_val = []
F_val = []
for item in data_lst:
    id_name.append(item.name)
    Q_val.append(item.Q_losses())
    F_val.append(item.F_c)

##print([id_name, Q_val, F_val])
data_dict = {
  "Q, кВт": Q_val,
  "q, %": [i / sum(Q_val) * 100 for i in Q_val],
  "F, м²": F_val,
  "Q/F, кВт*м⁻²": F_val
}
##print(data_dict)
df = pd.DataFrame(data_dict, index = id_name)
df.loc['Итого:',:]= df.sum(axis=0)
print(df)

print()
#-----------------
data_dict = {}
id_name = ['ст:Сев', 'ст:Южн', 'ст:Зап', 'ст:Вос', 'Чердак', 'Пол']
Q_val = []
F_val = []
S_val = []
for item in data_cost:
    Q_vals = 0
    for it in item:
        Q_vals += it.Q_losses()
    Q_val.append(Q_vals)
    F_val.append(item[0].F_c)
    S_val.append(item[0].S_matherials())
F_val[-1] = F_val[-2]
##print(F_val)


data_dict = {
  'Q, кВт': Q_val,
  'q, %': [i / sum(Q_val) * 100 for i in Q_val],
  'F, м²': F_val,
  'Q/F, кВт*м⁻²': F_val,
  'S, ₽': S_val
}
##print(data_dict)
df = pd.DataFrame(data_dict, index = id_name)
df.loc['Итого:',:]= df.sum(axis=0)
df.round({'Q, кВт':3, 'q, %':2, 'F, м²':2, 'Q/F, кВт*м⁻²':2, 'S, ₽':1})
print(df)

#---------------------------------------------
import matplotlib.pyplot as plt

# Some data
labels = id_name

# Make figure and axes
fig, axs = plt.subplots(2, 2)

# A standard pie plot
wedges, texts, autotexts = axs[0, 0].pie(data_dict['Q, кВт'], labels=labels, autopct='%1.1f%%', shadow=True)
axs[0, 0].set_title('Q, кВт')

# Shift the second slice using explode
axs[0, 1].pie(data_dict['q, %'], labels=labels, autopct='%.0f%%', shadow=True,
              explode=(0, 0.1, 0, 0, 0, 0))
axs[0, 1].set_title('q, %')

# Adapt radius and text size for a smaller pie
patches, texts, autotexts = axs[1, 0].pie(data_dict['Q/F, кВт*м⁻²'], labels=labels,
                                          autopct='%.0f%%',
                                          textprops={'size': 'smaller'},
                                          shadow=True, radius=0.5)
axs[1, 0].set_title('Q/F, кВт*м⁻²')
# Make percent texts even smaller
plt.setp(autotexts, size='x-small')
autotexts[0].set_color('white')

# Use a smaller explode and turn of the shadow for better visibility
patches, texts, autotexts = axs[1, 1].pie(data_dict['S, ₽'], labels=labels,
                                          autopct='%.0f%%',
                                          textprops={'size': 'smaller'},
                                          shadow=False, radius=0.5,
                                          explode=(0, 0.05, 0, 0, 0, 0))
axs[1, 1].set_title('S, ₽')
plt.setp(autotexts, size='x-small')
autotexts[0].set_color('white')

plt.show()











    

