#Пример выполнения задания на КМ-3, расчет тепловых потерь за счет теплопроводности
#Импорт классов и методов
from LocalisationData import Localisation

#Локализация проекта
loc = Localisation()

#Импортирую материалы
from Matherials import r_conc_sht, r_floor_CARBON_ECO

#Импортирую методику расчета тепловых потерь за счет теплопроводности
from exoheat import WallLosses, FloorLosses, f_zon
#Вывожу инструкцию
##print(help(WallLosses))
##print(help(FloorLosses))

H_зд = 3.1#м, высота отапливаемой части здания
l_ш = 9.5#м, ширина фасада
l_д = 11#м, длинна дома
F_ф = H_зд * l_ш#площадь фасада дома
F_б = H_зд * l_д#площадь боковой стены дома
F_п = l_ш * l_д#площаь пола и потолка
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
print("Q_ " + t_st_N.name + " = " + str(round(t_st_N.Q_losses(), 2)) + " кВт")
print("Q_ " + t_st_S.name + " = " + str(round(t_st_S.Q_losses(), 2)) + " кВт")
print("Q_ " + t_st_W.name + " = " + str(round(t_st_W.Q_losses(), 2)) + " кВт")
print("Q_ " + t_st_E.name + " = " + str(round(t_st_E.Q_losses(), 2)) + " кВт")
print("Q_ " + t_st_P.name + " = " + str(round(t_st_P.Q_losses(), 2)) + " кВт")

#Расчете потерь через пол
F_zones = f_zon(l_ш, l_д)
print("Массив площадей зон:" + str(F_zones))

t_pol_1 = FloorLosses("ТП пол зона 1", loc, r_floor_CARBON_ECO, ограждение='пол', зона=1, F_c = F_zones[0])
t_pol_2 = FloorLosses("ТП пол зона 2", loc, r_floor_CARBON_ECO, ограждение='пол', зона=2, F_c = F_zones[1])
t_pol_3 = FloorLosses("ТП пол зона 3", loc, r_floor_CARBON_ECO, ограждение='пол', зона=3, F_c = F_zones[2])
print("Q_ " + t_pol_1.name + " = " + str(round(t_pol_1.Q_losses(), 2)) + " кВт")
print("Q_ " + t_pol_2.name + " = " + str(round(t_pol_2.Q_losses(), 2)) + " кВт")
print("Q_ " + t_pol_3.name + " = " + str(round(t_pol_3.Q_losses(), 2)) + " кВт")
