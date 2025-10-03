#Демонстрация работы класса Home
#Пример выполнения задания на КМ-3, КМ-4 расчет тепловых потерь за счет теплопроводности и инфильтрации
import pandas as pd
import matplotlib.pyplot as plt

#Импорт классов и методов
from LocalisationData import Localisation

#Локализация проекта
loc = Localisation()

#Импортирую материалы
from Matherials import r_conc_sht, r_concrete, r_srub_kirpich, r_floor_CARBON_ECO, r_float_st2

#Импортирую методику расчета тепловых потерь за счет теплопроводности
from exoheat import f_zon
from exoheat import WallLosses as WL
from exoheat import FloorLosses as FL
from exoheat import WallInfiltration as WI
#Вывожу инструкцию
##print(help(WL))
##print(help(FL))
##print(help(WI))

class Home:
    """Мой класс он создаст мне расчет домика"""
    #создание конструктора класса
    def __init__(self, r_walls, r_okna):
        """Конструктор класса Home"""
        #Работа конструктора и инициализация внутренних переменных
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

        def tpl_WL(r_mat,ориентир_потерь,F_бок,ограждение='наружное'):
            return (loc,r_mat,ограждение,ориентир_потерь,F_бок,H_зд)
        t_st_N = WL("ТП ст:Сев", *tpl_WL(r_walls,'С',F_ф))
        t_st_S = WL("ТП ст:Южн", *tpl_WL(r_walls,'Ю',F_ф))
        t_st_W = WL("ТП ст:Зап", *tpl_WL(r_walls,'З',F_б))
        t_st_E = WL("ТП ст:Вос", *tpl_WL(r_walls,'В',F_б))
        t_st_P = WL("ТП Чердак", *tpl_WL(r_walls,'П',F_п,ограждение='чердачное'))

        #Расчете потерь через пол
        F_zones = f_zon(l_ш, l_д)
        ##print("Массив площадей зон:" + str(F_zones))

        def tpl_FL(зона):
            return (loc, r_floor_CARBON_ECO, 'пол', зона, F_zones[зона-1])
        t_pol_1 = FL("ТП пол зона 1", *tpl_FL(1))
        t_pol_2 = FL("ТП пол зона 2", *tpl_FL(2))
        t_pol_3 = FL("ТП пол зона 3", *tpl_FL(3))

        снз='стена_непроизводственного_здания'
        о3п='окно_или_балконная_дверь_с_тройными_переплетами_из_пластика'
        def tpl_WI(r_mat,ориентир_потерь,ограждение=снз):
            return (loc, r_mat, ограждение, ориентир_потерь,H_здк,h_цнс)
        tpl_hhn = (h_oнн + h_oнв, H_зд)
        tpl_hhm = (h_oнн        , h_oнн + h_oнв)
        tpl_hhp = (0            , h_oнн)

        in_st_N = WI("Ин ст:Сев",*tpl_WI(r_walls,'С'),*tpl_hhn,l_c=l_ш)#Ин-инфильтрация над окном
        im_st_N = WI("Им ст:Сев",*tpl_WI(r_walls,'С'),*tpl_hhm,l_c=l_ш-l_oc)#Им-инфильтрация между окнами
        ip_st_N = WI("Ип ст:Сев",*tpl_WI(r_walls,'С'),*tpl_hhp,l_c=l_ш)#Ип-инфильтрация под окном
        im_ok_N = WI("Им ок:Сев",*tpl_WI(r_okna,'С',о3п),*tpl_hhm,l_c=l_oc)#Им-инфильтрация между окнами

        in_st_S = WI("Ин ст:Южн",*tpl_WI(r_walls,'Ю'),*tpl_hhn,l_c=l_ш)#Ин-инфильтрация над окном
        im_st_S = WI("Им ст:Южн",*tpl_WI(r_walls,'Ю'),*tpl_hhm,l_c=l_ш-l_oc)#Им-инфильтрация между окнами
        ip_st_S = WI("Ип ст:Южн",*tpl_WI(r_walls,'Ю'),*tpl_hhp,l_c=l_ш)#Ип-инфильтрация под окном
        im_ok_S = WI("Им ок:Южн",*tpl_WI(r_okna,'Ю',о3п),*tpl_hhm,l_c=l_oc)#Им-инфильтрация между окнами

        in_st_W = WI("Ин ст:Зап",*tpl_WI(r_walls,'З'),*tpl_hhn,l_c=l_ш)#Ин-инфильтрация над окном
        im_st_W = WI("Им ст:Зап",*tpl_WI(r_walls,'З'),*tpl_hhm,l_c=l_ш-l_oc)#Им-инфильтрация между окнами
        ip_st_W = WI("Ип ст:Зап",*tpl_WI(r_walls,'З'),*tpl_hhp,l_c=l_ш)#Ип-инфильтрация под окном
        im_ok_W = WI("Им ок:Зап",*tpl_WI(r_okna,'З',о3п),*tpl_hhm,l_c=l_oc)#Им-инфильтрация между окнами

        self.lst_all = [t_st_N, t_st_S, t_st_W, t_st_E, t_st_P, t_pol_1, t_pol_2, t_pol_3,
                        in_st_N, im_st_N, ip_st_N, im_ok_N,
                        in_st_S, im_st_S, ip_st_S, im_ok_S,
                        in_st_W, im_st_W, ip_st_W, im_ok_W]
        self.data_cost = [[t_st_N, ip_st_N, im_st_N, in_st_N, im_ok_N],
                          [t_st_S, ip_st_S, im_st_S, in_st_S, im_ok_S],
                          [t_st_W, ip_st_W, im_st_W, in_st_W, im_ok_W],
                          [t_st_E, ], [t_st_P,], [t_pol_1, t_pol_2, t_pol_3]]

    def all_Q(self):
        """Функция класса """
        return self.lst_all

    def print_all_Q(self):
        """Функция класса """
        for item in self.lst_all:
            print("Q_ " + item.name + " = " + str(round(item.Q_losses(), 5)) + " кВт")

    def get_Q(self):
        """Возвращает таблицу теплового баланса"""
        data_dict = {}
        id_name = []
        Q_val = []
        F_val = []
        for item in self.lst_all:
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
        data_round = {
          "Q, кВт": 3,
          "q, %": 2,
          "F, м²": 2,
          "Q/F, кВт*м⁻²": 3
        }
        ##print(data_dict)
    
        df = pd.DataFrame(data_dict, index = id_name)
        df.loc['Итого:',:]= df.sum(axis=0)
        df.round(data_round)
##        print(df)
        return (data_dict, id_name, data_round, df)

    def get_S(self):
        """Возвращает таблицу стоимостных показателей"""
        data_dict = {}
        id_name = ['ст:Сев', 'ст:Южн', 'ст:Зап', 'ст:Вос', 'Чердак', 'Пол']
        Q_val = []
        F_val = []
        S_val = []
        for item in self.data_cost:
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
        data_round = {
          'Q, кВт': 3,
          'q, %': 2,
          'F, м²': 2,
          'Q/F, кВт*м⁻²': 2,
          'S, ₽': 1
        }
        ##print(data_dict)
    
        df = pd.DataFrame(data_dict, index = id_name)
        df.loc['Итого:',:]= df.sum(axis=0)
        df.round(data_round)
##        print(df)
        return (data_dict, id_name, data_round, df)

    def get_plots(self):
        # Some data
        labels = self.get_S()[1]#['ст:Сев', 'ст:Южн', 'ст:Зап', 'ст:Вос', 'Чердак', 'Пол']
        print(labels)
        data_dict = self.get_S()[0]
        print(data_dict)
        
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

        #plt.show()
        return fig

    def get_plots_df(self):
        # Some data
        print('☺☻☺')
        labels = self.get_S()[3].index[:-1]
        print(labels)
        data_dict = self.get_S()[3]#data_dict.loc[:,'Q, кВт']
        print(data_dict)
        
        # Make figure and axes
        fig, axs = plt.subplots(2, 2)

        # A standard pie plot
        wedges, texts, autotexts = axs[0, 0].pie(data_dict.loc[:,'Q, кВт'][:-1], labels=labels, autopct='%1.1f%%', shadow=True)
        axs[0, 0].set_title('Q, кВт')

        # Shift the second slice using explode
        axs[0, 1].pie(data_dict.loc[:,'q, %'][:-1], labels=labels, autopct='%.0f%%', shadow=True,
                      explode=(0, 0.1, 0, 0, 0, 0))
        axs[0, 1].set_title('q, %')

        # Adapt radius and text size for a smaller pie
        patches, texts, autotexts = axs[1, 0].pie(data_dict.loc[:,'Q/F, кВт*м⁻²'][:-1], labels=labels,
                                                  autopct='%.0f%%',
                                                  textprops={'size': 'smaller'},
                                                  shadow=True, radius=0.5)
        axs[1, 0].set_title('Q/F, кВт*м⁻²')
        # Make percent texts even smaller
        plt.setp(autotexts, size='x-small')
        autotexts[0].set_color('white')

        # Use a smaller explode and turn of the shadow for better visibility
        patches, texts, autotexts = axs[1, 1].pie(data_dict.loc[:,'S, ₽'][:-1], labels=labels,
                                                  autopct='%.0f%%',
                                                  textprops={'size': 'smaller'},
                                                  shadow=False, radius=0.5,
                                                  explode=(0, 0.05, 0, 0, 0, 0))
        axs[1, 1].set_title('S, ₽')
        plt.setp(autotexts, size='x-small')
        autotexts[0].set_color('white')

        #plt.show()
        return fig

