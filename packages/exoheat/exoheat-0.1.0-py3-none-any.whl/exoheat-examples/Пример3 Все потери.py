#Пример выполнения задания на КМ-3, расчет тепловых потерь за счет теплопроводности
#Импорт классов и методов
from LocalisationData import Localisation

#Локализация проекта
loc = Localisation()

#Импортирую материалы
from Matherials import r_conc_sht, r_floor_CARBON_ECO, r_float_st2

#Импортирую методику расчета тепловых потерь за счет теплопроводности
from exoheat import WallLosses, FloorLosses, f_zon, WallInfiltration
#Вывожу инструкцию
print(help(WallLosses))
print(help(FloorLosses))
print(help(WallInfiltration))

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

t_st_N = WallLosses("ТП ст:Северная", loc, r_conc_sht, ограждение='наружное',
                    ориентир_потерь='С', F_c = F_ф, H_здания = H_зд)
t_st_S = WallLosses("ТП ст:Южная", loc, r_conc_sht, ограждение='наружное',
                    ориентир_потерь='Ю', F_c = F_ф, H_здания = H_зд)
t_st_W = WallLosses("ТП ст:Западная", loc, r_conc_sht, ограждение='наружное',
                    ориентир_потерь='З', F_c = F_б, H_здания = H_зд)
t_st_E = WallLosses("ТП ст:Восточная", loc, r_conc_sht, ограждение='наружное',
                    ориентир_потерь='В', F_c = F_б, H_здания = H_зд)
t_st_P = WallLosses("ТП Чердачное", loc, r_conc_sht, ограждение='чердачное',
                    ориентир_потерь='П', F_c = F_п, H_здания = H_зд)
#Расчете потерь через стены
##print("Q_ " + t_st_N.name + " = " + str(round(t_st_N.Q_losses(), 2)) + " кВт")
##print("Q_ " + t_st_S.name + " = " + str(round(t_st_S.Q_losses(), 2)) + " кВт")
##print("Q_ " + t_st_W.name + " = " + str(round(t_st_W.Q_losses(), 2)) + " кВт")
##print("Q_ " + t_st_E.name + " = " + str(round(t_st_E.Q_losses(), 2)) + " кВт")
##print("Q_ " + t_st_P.name + " = " + str(round(t_st_P.Q_losses(), 2)) + " кВт")
dict_Q[t_st_N.name] = t_st_N
dict_Q[t_st_S.name] = t_st_S
dict_Q[t_st_W.name] = t_st_W
dict_Q[t_st_E.name] = t_st_E
dict_Q[t_st_P.name] = t_st_P
#Расчете потерь через пол
F_zones = f_zon(l_ш, l_д)
##print("Массив площадей зон:" + str(F_zones))

t_pol_1 = FloorLosses("ТП пол зона 1", loc, r_floor_CARBON_ECO, ограждение='пол', зона=1, F_c = F_zones[0])
t_pol_2 = FloorLosses("ТП пол зона 2", loc, r_floor_CARBON_ECO, ограждение='пол', зона=2, F_c = F_zones[1])
t_pol_3 = FloorLosses("ТП пол зона 3", loc, r_floor_CARBON_ECO, ограждение='пол', зона=3, F_c = F_zones[2])
##print("Q_ " + t_pol_1.name + " = " + str(round(t_pol_1.Q_losses(), 2)) + " кВт")
##print("Q_ " + t_pol_2.name + " = " + str(round(t_pol_2.Q_losses(), 2)) + " кВт")
##print("Q_ " + t_pol_3.name + " = " + str(round(t_pol_3.Q_losses(), 2)) + " кВт")
dict_Q[t_pol_1.name] = t_pol_1
dict_Q[t_pol_2.name] = t_pol_2
dict_Q[t_pol_3.name] = t_pol_3

ip_st_N = WallInfiltration("Ип ст:Северная", loc, r_conc_sht,#Ип-инфильтрация под окном
                           ограждение='стена_непроизводственного_здания',
                           ориентир_потерь='С', H=H_здк,
                           h_нс=h_цнс, h_нн=0, h_нв=h_oнн, l_c=l_ш)
im_st_N = WallInfiltration("Им ст:Северная", loc, r_conc_sht,#Им-инфильтрация между окнами
                           ограждение='стена_непроизводственного_здания',
                           ориентир_потерь='С', H=H_здк,
                           h_нс=h_цнс, h_нн=h_oнн, h_нв=h_oнн + h_oнв, l_c=l_ш-l_oc)#за вычетом ширины окна
in_st_N = WallInfiltration("Ин ст:Северная", loc, r_conc_sht,#Ин-инфильтрация над окном
                           ограждение='стена_непроизводственного_здания',
                           ориентир_потерь='С', H=H_здк,
                           h_нс=h_цнс, h_нн=h_oнн + h_oнв, h_нв=H_зд, l_c=l_ш)
im_ok_N = WallInfiltration("Им ок:Северная", loc, r_float_st2,#Им-инфильтрация через окна
                           ограждение='окно_или_балконная_дверь_с_тройными_переплетами_из_пластика',
                           ориентир_потерь='С', H=H_здк,
                           h_нс=h_цнс, h_нн=h_oнн, h_нв=h_oнн + h_oнв, l_c=l_oc)

##print("Q_ " + ip_st_N.name + " = " + str(round(ip_st_N.Q_losses(), 5)) + " кВт")
##print("Q_ " + im_st_N.name + " = " + str(round(im_st_N.Q_losses(), 5)) + " кВт")
##print("Q_ " + in_st_N.name + " = " + str(round(in_st_N.Q_losses(), 5)) + " кВт")
##print("Q_ " + im_ok_N.name + " = " + str(round(im_ok_N.Q_losses(), 5)) + " кВт")
dict_Q[ip_st_N.name] = ip_st_N
dict_Q[im_st_N.name] = im_st_N
dict_Q[in_st_N.name] = in_st_N
dict_Q[im_ok_N.name] = im_ok_N

for key in dict_Q.keys():
    print("Q_ " + key + " = " + str(round(dict_Q[key].Q_losses(), 5)) + " кВт")

