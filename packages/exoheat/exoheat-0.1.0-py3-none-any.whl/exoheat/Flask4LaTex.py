from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from exoheat import ThermalResistance as TR
from exoheat import WallLosses as WL
from exoheat import FloorLosses as FL
from exoheat import WallInfiltration as WI

app = Flask(__name__)

class SAPR:
    """Класс для генерации автоматического кода расчета на основе Flask, HTML, LaTex"""

    def __init__(self, port = 8183):
        """Конструктор для задания порта сервера"""
        self.port = port
        html_text = ''
        html_text += '<script type="text/javascript"\r\n'
        html_text += ' src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">\r\n'
        html_text += '</script>\r\n'
        self.html_text = html_text
        self.nbr = 0

    def report_matherial_params(self, tr):
        """Генератор отчета расчета по свойствам материала ограждений"""
        self.nbr += 1
        nbr = self.nbr
        html_text = self.html_text
        #------------
        html_text += '<h2>Расчет термодинамических показателей <br>'
        html_text += 'материала ограждающей конструкции: <br><b>"{0}";</b></h2>'.format(tr.name)
        data_dic = {}

        name = tr.name
        name = name.replace('  ',' ')
        name = name.replace(', ',',')
        names = name.split(',')
        if len(names) == len(tr.δ_m): data_dic['Слой'] = names
        ##print(len(names), len(tr.δ_m))
        data_dic['\(δ_{{m {} }}, м\)'.format(nbr)] = [round(it, 4) for it in tr.δ_m]
        data_dic['\(λ_{{m {} }}, \\frac{{ Вт }}{{ м \cdot ℃ }}\)'.format(nbr)] = [round(it, 3) for it in tr.λ_m]
        data_dic['\(c_{{m {} }}, \\frac{{ кДж }}{{ кг \cdot ℃ }}\)'.format(nbr)] = [round(it, 3) for it in tr.c_m]

        ro = tr.ρ_m.copy()
        for i in range(len(ro)):
            if ro[i] < 10: ro[i] = str(round(ro[i], 3))
            elif ro[i] < 100: ro[i] = str(round(ro[i], 2))
            elif ro[i] < 1000: ro[i] = str(round(ro[i], 1))
            elif ro[i] < 10000: ro[i] = str(round(ro[i], 0))
        data_dic['\(ρ_{{m {} }}, \\frac{{ Вт }}{{ кг \cdot м ^ {{3}} }}\)'.format(nbr)] = ro
        if tr.ц_m: data_dic['\(ц_{{m {} }}, \\frac{{ ₽ }}{{ м ^ {{3}} }}\)'.format(nbr)] = [round(it, 1) for it in tr.ц_m]

        df = pd.DataFrame(data_dic)
        html_text += df.to_html(header="false", table_id="table")

        html_text += '<p>Тип поверхности ограждения внутри помещения: "{0}",<br>'.format(tr.внутри.replace('_',' '))
        html_text += 'коэффициент теплоотдачи внутри помещения : \(α_{{ в {0} }} = {1:.1f}, \\frac{{Вт}}{{ м^{{2}} \cdot ℃ }}\);</p>'.format(nbr, tr.α_в)
        html_text += '<p>Тип поверхности ограждения снаружи помещения: <br>"{0}"<br>'.format(tr.снаружи.replace('_',' '))
        html_text += 'коэффициент теплоотдачи снаружи помещения : \(α_{{ н {0} }} = {1:.1f}, \\frac{{Вт}}{{ м^{{2}} \cdot ℃ }}\);</p>'.format(nbr, tr.α_н)

        html_text += '<p>Полные сопротивления теплопередаче через наружные ограждения здания:<br>'.format(tr.снаружи)
        html_text += '\(R_{{огр {0} }} = \\frac{{1}}{{ α_{{в {0} }} }} '.format(nbr)
        for i in range(len(tr.δ_m)):
            html_text += ' + \\frac{{ δ_{{m {0} \\_ {1} }} }}{{ λ_{{m {0} \\_ {1} }} }}'.format(nbr, i)
        html_text += ' + \\frac{{1}}{{ α_{{н {0} }} }} \) = <br>'.format(nbr)

        html_text += '\( = \\frac{{1}}{{ {0} }} '.format(round(tr.α_в, 3))
        for i in range(len(tr.δ_m)):
            html_text += ' + \\frac{{ {0} }}{{ {1} }}'.format(round(tr.δ_m[i], 4), round(tr.λ_m[i], 3))
        html_text += ' + \\frac{{1}}{{ {0} }} \);</p>'.format(round(tr.α_н, 3))
        html_text += '<p>\(R_{{огр {0} }} = {1}, \\frac{{ м^{{2}} \cdot ℃ }}{{ Вт }} \);</p>'.format(nbr, round(tr.R(), 3))

        html_text += '<p>Тепловая инерционность ограждающей конструкции:<br>'.format(tr.снаружи)
        html_text += '\(Д_{{огр {0} }} = 0.27 \cdot \\frac{{ δ_{{m {0} \\_ {1} }} }}{{ λ_{{m {0} \\_ {1} }} }} \cdot \sqrt{{ ρ_{{m {0} \\_ {1} }} \cdot c_{{m {0} \\_ {1} }} \cdot λ_{{m {0} \\_ {1} }} }} \)'.format(nbr, 0)
        if len(tr.δ_m) > 0:
            for i in range(len(tr.δ_m) - 2):
                html_text += ' + <br> \( + 0.27 \cdot \\frac{{ δ_{{m {0} \\_ {1} }} }}{{ λ_{{m {0} \\_ {1} }} }} \cdot \sqrt{{ ρ_{{m {0} \\_ {1} }} \cdot c_{{m {0} \\_ {1} }} \cdot λ_{{m {0} \\_ {1} }} }} \)'.format(nbr, i + 1)
            if len(tr.δ_m) > 1: html_text += ' + <br> \( + 0.27 \cdot \\frac{{ δ_{{m {0} \\_ {1} }} }}{{ λ_{{m {0} \\_ {1} }} }} \cdot \sqrt{{ ρ_{{m {0} \\_ {1} }} \cdot c_{{m {0} \\_ {1} }} \cdot λ_{{m {0} \\_ {1} }} }} = \)<br>'.format(nbr, len(tr.δ_m) -1)

        def tpl(i): return (round(tr.δ_m[i], 4), round(tr.λ_m[i], 3), round(tr.ρ_m[i], 3), round(tr.c_m[i], 3))

        html_text += '\( = 0.27 \cdot \\frac{{ {1} }}{{ {2} }} \cdot \sqrt{{ {3} \cdot {4} \cdot {2} }} \)'.format(nbr, *tpl(0))
        if len(tr.δ_m) > 0:
            for i in range(len(tr.δ_m) - 2):
                html_text += ' + <br> \( + 0.27 \cdot \\frac{{ {1} }}{{ {2} }} \cdot \sqrt{{ {3} \cdot {4} \cdot {2} }} \)'.format(nbr, *tpl(i + 1))
            if len(tr.δ_m) > 1: html_text += ' + <br> \( + 0.27 \cdot \\frac{{ {1} }}{{ {2} }} \cdot \sqrt{{ {3} \cdot {4} \cdot {2} }} ;\)</p>'.format(nbr, *tpl(len(tr.δ_m) -1))
        Д_огр = tr.Д_огр()
        html_text += '<p>\(Д_{{огр {0} }} = {1}, \\sqrt{{ c }} \);</p>'.format(nbr, round(Д_огр, 3))

        if 4 < Д_огр < 7:
            html_text += '<p>\( 4 < Д_{{огр {0} }} < 7 \);</p>'.format(nbr, round(Д_огр, 3))
            html_text += '<p>\( t^б_{{хн {0} }} = 0.5 \cdot ( t^{{ б5 }}_{{хн {0} }} + t^{{ б1 }}_{{хн {0} }} )  = '.format(nbr)
            html_text += ' 0.5 \cdot ( {1} + {2} ) = {3} , ℃ \);</p>'.format(nbr, round(tr.loc.t_б5_хн, 1), round(tr.loc.t_б1_хн, 1), round(tr.t_б_хн(), 1))

        elif 7 < Д_огр:
            html_text += '<p>\( 7 < Д_{{огр {0} }} \);</p>'.format(nbr, round(Д_огр, 3))
            html_text += '<p>\( t^б_{{хн {0} }} =  t^{{ б5 }}_{{хн {0} }} = '.format(nbr)
            html_text += '  {1} = {2} , ℃ \);</p>'.format(nbr, round(tr.loc.t_б5_хн, 1), round(tr.t_б_хн(), 1))
            
        elif 0 < Д_огр < 4:
            html_text += '<p>\( 0 < Д_{{огр {0} }} < 4 \);</p>'.format(nbr, round(Д_огр, 3))
            html_text += '<p>\( t^б_{{хн {0} }} =  t^{{ б1 }}_{{хн {0} }} = '.format(nbr)
            html_text += ' {1} = {2} , ℃ \);</p>'.format(nbr, round(tr.loc.t_б1_хн, 1), round(tr.t_б_хн(), 1))
        html_text += '<hr>'
        #------------
        self.html_text = html_text 

    def report_wall_losses(self, tr):
        """Генератор отчета расчета количества теплопотерь за счет теплопроводности через боковые ограждения"""
        self.nbr += 1
        nbr = self.nbr
        html_text = self.html_text
        #------------
        html_text += '<h2>Тепловые потери за счет теплопроводности<br>'
        html_text += 'через ограждающую конструкцию: <br><b>"{0}";</b></h2>'.format(tr.name)
        html_text += '<p>Идентификатор термического сопротивления: <br><b>"{0}";</b></p>'.format(tr.res.name)
        html_text += '<p>Термическое сопротивление: '
        html_text += '\( R_{{огр {0} }} = {1:.3f}, \\frac {{К \\cdot м²}}{{Вт}} \);</p>'.format(nbr, tr.res.R())
        if tr.H_здания:
            html_text += '<p>Высота здания: \(H_{{здания}} = {0}, м\);</p>'.format(tr.H_здания)
        html_text += '<p>Температура воздуха внутри помещения - \(t_{{ вр {0} }} = {1:.1f}, ℃\);</p>'.format(nbr, tr.loc.t_вр)
        html_text += '<p>Тип ограждения: "{1}" - \(a_{{ {0} }} = {2}\);</p>'.format(nbr, tr.ограждение, tr.а)

        html_text += '<p>Коэффициент повышения температуры наружного воздуха <br>по высоте помещения - \(k_n = 0.3 \);</p>'
        datamas_t = [nbr, round(tr.loc.t_вр,1), round(tr.H_здания,3), 0.3]
        #            0           1        2         3
        html_text += '<p>Расчетная средняя температура воздуха внутри помещения:</p>'
        if tr.ограждение == "наружное":
            html_text += '<p>\( t_{{ в {0} }} = t_{{ вр }} + 0.5 \cdot \\left ( H_{{здания}} - 2 \\right ) \cdot k_n '.format(*datamas_t)
            html_text += ' = {1} + 0.5 \cdot \\left ( {2} - 2 \\right ) \cdot {3} =  \);</p>'.format(*datamas_t)
            html_text += '<p>\( t_{{ в {0} }} = {1}, ℃ \);</p>'.format(*datamas_t)# среднее значение температуры внутреннего воздуха у боковых стен
        elif tr.ограждение == "чердачное":
            html_text += '<p>\( t_{{ в {0} }} = t_{{ вр }} + \\left ( H_{{здания}} - 2 \\right ) \cdot k_n '.format(*datamas_t)
            html_text += ' = {1} + \\left ( {2} - 2 \\right ) \cdot {3} =  \);</p>'.format(*datamas_t)
            html_text += '<p>\( t_{{ в {0} }} = {1}, ℃ \);</p>'.format(*datamas_t)# среднее значение температуры внутреннего воздуха у чердачного перекрытия
        elif tr.ограждение == "пол":
            html_text += '<p>\( t_{{ в {0} }} = t_{{ вр }} = {1}, ℃ \);</p>'.format(*datamas_t)# среднее значение температуры внутреннего воздуха у пола
        html_text += '<p>Ориентир потерь: "{1}" - \(\\beta_{{ {0} }} = {2} \);</p>'.format(nbr, tr.ориентир_потерь, tr.β)
        html_text += '<p>Площадь ограждающей конструкции: \(F_{{c}} = {0:.4}, м²\);</p>'.format(round(tr.F_c, 2))
        ##html_text += '<p>Расчетная средняя температура воздуха внутри помещения - \(t_{{ в {0} }} = {1:.1f}, ℃\);</p>'.format(nbr, tr.t_в1)
        html_text += '<p>Расчетная температура наружного воздуха - \(t_{{ хн }} = {0:.1f}, ℃\);</p>'.format(tr.res.t_б_хн())

        html_text += '<p>\(Q_{{огр {0} }}=0.001 \\cdot \\left ( t_{{в {0} }} - t_{{хн}} \\right ) \\cdot \\frac{{F_{{c}}}}{{R_{{огр {0} }}}} \\cdot a_{{ {0} }} \\cdot \\left ( 1 + \\beta_{{ {0} }} \\right ) = \)</p>'.format(nbr)
        datamas_Q = [nbr, round(tr.t_в1,1), round(tr.res.t_б_хн(),1), round(tr.F_c,2), round(tr.res.R(),3), round(tr.а,3), round(tr.β,3)]
        html_text += '<p>\(= 0.001 \\cdot \\left ( {1:.1f} - ( {2:.1f} ) \\right ) \\cdot \\frac{{ {3:.3f} }}{{ {4:.3f} }} \\cdot {5}  \\cdot \\left ( 1 + {6} \\right ) = \)</p>'.format(*datamas_Q)
        html_text += '<p>\(Q_{{огр {0} }} = {1:.3f}, кВт \)</p>'.format(nbr, tr.Q_losses())
        html_text += '<hr>'
        #------------
        self.html_text = html_text        

    def report_floor_losses(self, trp):
        """Генератор отчета расчета количества теплопотерь за счет теплопроводности через пол, потолок"""
        self.nbr += 1
        nbr = self.nbr
        html_text = self.html_text
        #------------
        html_text += '<h2>Тепловые потери за счет теплопроводности<br>'
        html_text += 'через ограждающие конструкции пола: <br><b>"{0}";</b></h2>'.format(trp.name)
        html_text += '<p>Идентификатор термического сопротивления: <br><b>"{0}";</b></p>'.format(trp.res.name)
        html_text += '<p>Термическое сопротивление: '
        html_text += '\( R_{{огр {0} }} = {1:.3f}, \\frac {{К \\cdot м²}}{{Вт}} \);</p>'.format(nbr, trp.res.R())
        html_text += '<p>Тип ограждения: "{1}" - \(a_{{ {0} }} = {2}\);</p>'.format(nbr, trp.ограждение, trp.а)
        html_text += '<p>Номер зоны пола: "{1}" - \(a_{{z {0} }} = {2:.3f}\);</p>'.format(nbr, trp.зона, trp.а_z)
        html_text += '<p>Площадь зоны пола: \(F_{{c {0} }} = {1:.4}, м²\);</p>'.format(trp.зона, trp.F_c)
        html_text += '<p>Расчетная средняя температура воздуха внутри помещения - \(t_{{вр {0} }} = {1:.1f}, ℃\);</p>'.format(nbr, trp.loc.t_вр)
        html_text += '<p>Расчетная температура наружного воздуха - \(t_{{ хн }} = {0:.1f}, ℃\);</p>'.format(trp.res.t_б_хн())

        html_text += '<p>\(Q_{{огр {0} }}=0.001 \\cdot \\left ( t_{{вр {0} }} - t_{{ хн }} \\right ) \\cdot \\frac{{F_{{c {1} }}}}{{R_{{огр {0} }} \\cdot a_{{z {0} }} }} \\cdot a_{{ {0} }} = \)</p>'.format(nbr, trp.зона)
        datamas = [nbr, round(trp.loc.t_вр,1), round(trp.res.t_б_хн(),1), round(trp.F_c,2), round(trp.res.R(),3), round(trp.а_z,3), round(trp.а,3)]
        html_text += '<p>\(=0.001 \\cdot \\left ( {1} - ( {2} ) \\right ) \\cdot \\frac{{ {3} }}{{ {4} \\cdot {5} }} \\cdot {6} = \)</p>'.format(*datamas)
        html_text += '<p>\(Q_{{огр {0} }} = {1:.3f}, кВт \)</p>'.format(nbr, trp.Q_losses())
        html_text += '<hr>'
        #------------
        self.html_text = html_text 

    def report_wall_infiltration(self, ti):
        """Генератор отчета расчета количества теплопотерь за счет инфильтрации через боковые ограждения"""
        self.nbr += 1
        nbr = self.nbr
        html_text = self.html_text
        #------------
        ti.Q_losses()#нужно запустить иначе не будет инициализации
        html_text += '<h2>Тепловые потери за счет инфильтрации<br>'
        html_text += 'через ограждающую конструкцию: <br><b>"{0}";</b></h2>'.format(ti.name)
        html_text += '<p>Идентификатор термического сопротивления: <br><b>"{0}";</b></p>'.format(ti.res.name)
        html_text += '<p>Термическое сопротивление: '
        html_text += '\( R_{{огр {0} }} = {1:.3f}, \\frac {{К \\cdot м²}}{{Вт}} \);</p>'.format(nbr, ti.res.R())
        html_text += '<p>Для типа ограждения: "{1}" беруться:</p>'.format(nbr, ti.ограждение.replace("_", " "))

        def p_or_m(val):
            if val > 0: return '+'
            else: return '-'

        if (ti.ограждение in ti.K_т_dict.keys()) and (ti.ограждение not in ["стык_панелей_непроизводственного_здания", "стык_панелей_производственного_здания"]):
            html_text += '<p>- коэффициент, учитывающий подогрев инфильтрующегося воздуха - \(K_{{ т {0} }} = {1} \);</p>'.format(nbr, ti.K_т)
            html_text += '<p>- коэффициент, поперечной воздухопроницаемости - \(G_{{ н {0} }} = {1}, \\frac{{ кг }}{{ м² \cdot ч }} \);</p>'.format(nbr, round(ti.G_н,3))
            html_text += '<p>Ориентир потерь: "{1}";</p>'.format(nbr, ti.ориентир_потерь)
            html_text += '<p>Высота здания от уровня земли до чердачного перекрытия или до центра<br>'
            html_text += 'вытяжных отверстий аэрационных фонарей: \(Н_{{ {0} }} = {1}, м \);</p>'.format(nbr, round(ti.H,3))
            html_text += '<p>Нижняя отметка всей стены: \(h_{{ нс {0} }} = {1}, м \);</p>'.format(nbr, round(ti.h_нс,3))
            html_text += '<p>Нижняя отметка участка ограждения: \(h_{{ нн {0} }} = {1}, м \\left ( Н_{{ нн {0} }} = {2}, м \\right ) \);</p>'.format(nbr, round(ti.h_нн,3), round(ti.h_нс + ti.h_нн,3))
            html_text += '<p>Вернхяя отметка участка ограждения: \(h_{{ нв {0} }} = {1}, м \\left ( Н_{{ нв {0} }} = {2}, м \\right ) \);</p>'.format(nbr, round(ti.h_нв,3), round(ti.h_нс + ti.h_нв,3))
            html_text += '<p>Ширина участка ограждения: \(l_{{ c {0} }} = {1}, м \);</p>'.format(nbr, round(ti.l_c,3))
            html_text += '<p>Расчетная средняя температура воздуха внутри помещения - \(t_{{ вр {0} }} = {1:.1f} ,℃\);</p>'.format(nbr, round(ti.loc.t_вр,3))
##            html_text += '<p>Плотность воздуха внутри помещения - \(ρ_{{в {0} }} = {1:.3f}, \\frac{{ кг }}{{ м³ }} \);</p>'.format(nbr, round(ti.ρ_в,3))
            html_text += '<p>Расчетная температура наружного воздуха - \(t_{{хн}} = {0:.1f} ,℃\);</p>'.format(ti.res.t_б_хн())
            html_text += '<p>Плотность воздуха наружная - \(ρ_{{н {0} }} = {1:.3f} , \\frac{{ кг }}{{ м³ }} \);</p>'.format(nbr, round(ti.ρ_н,3))
            html_text += '<p>Ориентир стены к ветру: "{0}"</p>'.format(ti.wall_direct)
            html_text += '<p>Уровень, через ограждения расположенные ниже которого будет <br>осуществляться инфильтрация воздуха:</p>'
            datamas_h = [nbr, round(ti.H,3), p_or_m(ti.vet[0]), 0.6, p_or_m(ti.vet[1]), -0.45,    1, round(ti.ρ_н,3), round(ti.loc.W_нр,3), 9.8, round(ti.ρ_в,3), round(ti.h_р, 3)]
            #             0    1              2:+-    3:K_1н       4:+-       5:K_1з  6:K_2          7                     8        9:g           10              11
            if ti.ρ_н != ti.ρ_в:
                html_text += '<p>\(H_{{р {0} }} = 0.5 \cdot Н_{{ {0} }} {2} 0.25 \cdot \\left ( K_{{1н}} {4} K_{{1з}} \\right ) \cdot '.format(*datamas_h)
                html_text += ' K_2 \cdot \\frac{{ ρ_{{н {0} }} \cdot W_{{нр}}^{{2}} }}{{ g \cdot \\left ( ρ_{{н {0} }} - ρ_{{в {0} }} \\right ) }} = \)</p>'.format(*datamas_h)
                html_text += '<p>\(H_{{р {0} }} = 0.5 \cdot {1} {2} 0.25 \cdot \\left ( {3} {4} ({5}) \\right ) \cdot '.format(*datamas_h)
                html_text += ' {6} \cdot \\frac{{ {7} \cdot {8} ^{{2}} }}{{ {9} \cdot \\left ( {7} - {10} \\right ) }} = \)</p>'.format(*datamas_h)
                html_text += '<p>\(H_{{р {0} }} = {11} , м \)'.format(*datamas_h)
            else:
                html_text += '<p>\(ρ_{{в {0} }} = ρ_{{н {0} }} = {1:.3f}, \\frac{{ кг }}{{ м³ }} \);</p>'.format(nbr, ti.ρ_в)
                html_text += '<p>\(H_{{ р }} = 0.5 \cdot Н_{{ {0} }} = 0.5 \cdot {1} = {11} , м \)'.format(*datamas_h)
                
            if ti.h_нн + ti.h_нс > ti.h_р:
                html_text += '<p>\( H_{{ р }} < Н_{{ нн {0} }} = h_{{ нс {0} }} + h_{{ нн {0} }} = {1} + {2} = {3}, м \)</p>'.format(nbr, round(ti.h_нс,3), round(ti.h_нн,3), round(ti.h_нс + ti.h_нн,3), datamas_h[11])
                html_text += '<p>Следовательно инфильтрации на данном участке не будет учитывается</p>'
                html_text += '<p>\(Q_{{ огр {0} }} = 0, кВт\)</p>'.format(nbr)
            elif ti.h_р > ti.h_нв + ti.h_нс: #площадь ограждение учавствует полностью в потерях за счет инфильтрации
                html_text += '<p>\( H_{{ р }} > Н_{{ нв {0} }} = h_{{ нв {0} }} + h_{{ нс {0} }} = {1} + {2} = {3},м \)</p>'.format(nbr, round(ti.h_нв,3), round(ti.h_нс,3), round(ti.h_нв + ti.h_нс,3), datamas_h[11])
                html_text += '<p>Следовательно, вся площадь данного участка будет задействована <br>для расчета потерь c инфильтраций:</p>'
                html_text += '<p>\(F_{{ c {0} }} = \\left ( h_{{нв {0} }} - h_{{нн {0} }} \\right ) \cdot l_{{с {0} }} '.format(nbr, round(ti.h_нв,3), round(ti.h_нн,3), ti.l_c)
                html_text += ' = \\left ( {1} - {2} \\right ) \cdot {3} = {4}, м² \)</p>'.format(nbr, round(ti.h_нв,2), round(ti.h_нн,3), round(ti.l_c,3), round(ti.F_c, 3))
                html_text += '<p>Расчетна высота от уровня \( h_{{ нс {0} }} \) до оси ограждения :</p>'.format(nbr)
                html_text += '<p>\(h_{{ н {0} }} = \\frac {{ h_{{нв {0} }} + h_{{нн {0} }} }}{{ 2 }} '.format(nbr, round(ti.h_нв,3), round(ti.h_нн,3), round(ti.h_н,3))
                html_text += ' = \\frac {{ {1} + {2} }}{{ 2 }} = {3}, м \) </p>'.format(nbr, round(ti.h_нв,3), round(ti.h_нн,3), round(ti.h_н,3))
                
            elif (ti.h_нн + ti.h_нс) < ti.h_р and ti.h_р < (ti.h_нв + ti.h_нс):#площадь ограждение учавствует частично в потерях за счет инфильтрации
                html_text += '<p>\( H_{{ р }} > Н_{{ нн {0} }} = h_{{ нн {0} }} + h_{{ нс {0} }} = {1} + {2} = {3},м \)</p>'.format(nbr, round(ti.h_нн,3), round(ti.h_нс,3), round(ti.h_нн + ti.h_нс,3), datamas_h[11])
                html_text += '<p>\( H_{{ р }} < Н_{{ нв {0} }} = h_{{ нв {0} }} + h_{{ нс {0} }} = {1} + {2} = {3},м \)</p>'.format(nbr, round(ti.h_нв,3), round(ti.h_нс,3), round(ti.h_нв + ti.h_нс,3), datamas_h[11])
                html_text += '<p>Следовательно, только часть площади данного участка будет <br>задействована для расчета потерь c инфильтраций:</p>'
                html_text += '<p>\(F_{{ c {0} }} = \\left ( H_{{ р }} - H_{{нн {0} }} \\right ) \cdot l_{{с {0} }} '.format(nbr)
                html_text += ' = \\left ( {1} - {2} \\right ) \cdot {3} = {4}, м² \)</p>'.format(nbr, datamas_h[11], round(ti.h_нн + ti.h_нс,3), round(ti.l_c,3), round(ti.F_c, 3))
         
                html_text += '<p>Расчетна высота от уровня \( h_{{ нс {0} }} \) до оси ограждения <br> задействованной для расчета потерь с инфильтрацией:</p>'.format(nbr)
                html_text += '<p>\(h_{{ н {0} }} = \\frac {{ H_{{ р }} - h_{{нс {0} }} + h_{{нн {0} }} }}{{ 2 }} '.format(nbr)
                html_text += ' = \\frac {{ {1} - {2} + {3} }}{{ 2 }} = {4}, м \) </p>'.format(nbr, round(ti.h_р,3), round(ti.h_нс,3), round(ti.h_нн,3), round(ti.h_н,3))
                
            datamas_hm = [nbr, round(ti.H,3), round(ti.h_нс,3), round(ti.h_н,3), round(ti.ρ_н,3), round(ti.ρ_в,3), 9.8,
            #              0            1              2                 3                  4                 5      6
                          p_or_m(ti.vet[0]), 0.6, p_or_m(ti.vet[1]), -0.45,    1, round(ti.ρ_н,3), round(ti.loc.W_нр,3), round(ti.dp_огр,1)]
            #                       7:+-   8:K_1н           9:+-    10:K_1з  11:K_2     12                      13                14
            html_text += '<p>\(\Delta p_{{огр {0} }} = \\left ( H_{{ {0} }} - h_{{нс {0} }} - h_{{н {0} }} \\right ) '.format(*datamas_hm)
            html_text += ' \cdot \\left ( ρ_{{н {0} }} - ρ_{{в {0} }} \\right ) \cdot g '.format(*datamas_hm)
            html_text += ' {7} 0.25 \cdot \\left ( K_{{1н}} {9} K_{{1з}} \\right ) \cdot K_2 \cdot ρ_{{н {0} }} \cdot W_{{нр}}^{{2}} =\)<br>'.format(*datamas_hm)

            html_text += ' \( = \\left ( {1} - {2} - {3} \\right ) '.format(*datamas_hm)
            html_text += ' \cdot \\left ( {4} - {5} \\right ) \cdot {6} '.format(*datamas_hm)
            html_text += ' {7} 0.25 \cdot \\left ( {8} {9} ({10}) \\right ) \cdot {11} \cdot {12} \cdot {13}^{{2}} =\)</p>'.format(*datamas_hm)

            html_text += '<p>\( \Delta p_{{огр {0} }} = {14}, Па \)</p>'.format(*datamas_hm)

            html_text += '<p>Расход инфильтруемого воздуха:</p>'
            datamas_Gи = [nbr, ti.G_н, round(ti.F_c, 2), round(abs(ti.dp_огр),1), round(ti.G_и, 2)]
            if ti.ограждение in ["стена_непроизводственного_здания", "стена_производственного_здания"]:
                #кг/ч, количество воздуха, поступающего в здание инфильтруясь через его наружные стены, покрытия и перекрытия
                html_text += '<p>\( G_{{ и {0} }} = 0.216 \cdot G_{{ н {0} }} \cdot F_{{ c {0} }} \cdot \\left | \Delta p_{{ огр {0} }} \\right | ^ {{0.667}} '.format(*datamas_Gи)
                html_text += ' = 0.216 \cdot {1} \cdot {2} \cdot \\left | {3} \\right | ^ {{0.667}} = \)</p>'.format(*datamas_Gи)
            if ti.ограждение in [",окно_или_балконная_дверь_с_тройными_переплетами_из_дерева",
                                 ",окно_или_балконная_дверь_с_тройными_переплетами_из_пластика",                                                                                           
                                 ",окно_или_балконная_дверь_с_раздельными_переплетами_из_дерева",                                                                                          
                                 ",окно_или_балконная_дверь_с_раздельными_переплетами_из_пластика",                                                                                        
                                 ",окно_или_балконная_дверь_с_одинарным_остеклением_из_дерева",                                                                                            
                                 ",окно_или_балконная_дверь_со_спаренными_переплетами_из_пластика",                                                                                        
                                 ",входная_дверь_в_квартиру",                                                                                                                              
                                 ",входная_дверь_непроизводственного_здания",                                                                                                              
                                 ",окно_дверь_или_ворота_производственного_здания"]:
                #кг/ч, количество воздуха, инфильтрующегося в помещение через окна, балконные двери, ворота, аэрационные фонари
                html_text += '<p>\( G_{{ и {0} }} = 0.216 \cdot G_{{ н {0} }} \cdot F_{{ c {0} }} \cdot \\left | \Delta p_{{ огр {0} }} \\right | ^ {{-0.333}} '.format(*datamas_Gи)
                html_text += ' = 0.216 \cdot {1} \cdot {2} \cdot \\left | {3} \\right | ^ {{-0.333}} = \)</p>'.format(*datamas_Gи)
            if ti.ограждение in ["аэрационный_проём", "аэрационный_проём_с_кондициоринованием"]:
                #кг/ч, количество воздуха, инфильтрующегося в помещение через аэрационные проемы и иные неплотности значительных размеров
                html_text += '<p>\( G_{{ и {0} }} = 3456 \cdot F_{{ c {0} }} \cdot \\left | \Delta p_{{ огр {0} }} \\right | ^ {{0.5}} '.format(*datamas_Gи)
                html_text += ' = 3456 \cdot {2} \cdot \\left | {3} \\right | ^ {{0.5}} = \)</p>'.format(*datamas_Gи)
            html_text += '<p>\( G_{{ и {0} }} = {4}, \\frac{{кг}}{{ч}} \)</p>'.format(*datamas_Gи)

        #щелевые варианты потерь
        elif ti.ограждение in ["стык_панелей_непроизводственного_здания", "стык_панелей_производственного_здания"]:#щелевые варианты потерь
            html_text += '<p>- коэффициент, учитывающий подогрев инфильтрующегося воздуха - \(K_{{ т {0} }} = {1} \);</p>'.format(nbr, round(ti.K_т,3))
            html_text += '<p>- коэффициент, поперечной воздухопроницаемости - \(G_{{ н {0} }} = {1}, \\frac{{ кг }}{{ м² \cdot ч }} \);</p>'.format(nbr, round(ti.G_н,3))
            html_text += '<p>Ориентир потерь: "{1}";</p>'.format(nbr, ti.ориентир_потерь)
            html_text += '<p>Высота здания от уровня земли до чердачного перекрытия или до центра<br>'
            html_text += 'вытяжных отверстий аэрационных фонарей: \(Н_{{ {0} }} = {1}, м \);</p>'.format(nbr, round(ti.H,3))
            html_text += '<p>Нижняя отметка всей стены, от которой отщитываются участки ограждений: <br>'
            html_text += '\(h_{{ нс {0} }} = {1}, м \);</p>'.format(nbr, round(ti.h_нс,3))
            
            html_text += '<p>Нижние отметки участков ограждений: </p>'
            for i in range(len(ti.h_нн)):
                html_text += '<p> \( h_{{ нн {0},{1} }} = {2}, м \\left ( Н_{{ нн {0},{1} }} = h_{{ нс {0} }} + h_{{ нн {0},{1} }} '.format(nbr, i+1, round(ti.h_нн[i],3))
                html_text += ' = {2} + {3} = {4}, м \\right ) \);</p>'.format(nbr, i+1, round(ti.h_нс,3), round(ti.h_нн[i],3), round(ti.h_нс + ti.h_нн[i],3))
            html_text += '<p>Вернхние отметки участков ограждений: </p>'
            for i in range(len(ti.h_нв)):
                html_text += '<p> \( h_{{ нв {0},{1} }} = {2}, м \\left ( Н_{{ нв {0},{1} }} = h_{{ нс {0} }} + h_{{ нв {0},{1} }} '.format(nbr, i+1, round(ti.h_нв[i],3))
                html_text += ' = {2} + {3} = {4}, м \\right ) \);</p>'.format(nbr, i+1, round(ti.h_нс,3), round(ti.h_нв[i],3), round(ti.h_нс + ti.h_нв[i],3))
            html_text += '<p>Ширины участков ограждений: </p>'
            for i in range(len(ti.l_c)):
                html_text += '<p>  \(l_{{ c {0} , {1} }} = {2}, м \);</p>'.format(nbr, i+1, round(ti.l_c[i],3))

            html_text += '<p>Расчетная средняя температура воздуха внутри помещения - \(t_{{ вр {0} }} = {1:.1f} ,℃\);</p>'.format(nbr, round(ti.loc.t_вр,3))
            html_text += '<p>Плотность воздуха внутри помещения - \(ρ_{{в {0} }} = {1:.3f}, \\frac{{ кг }}{{ м³ }} \);</p>'.format(nbr, round(ti.ρ_в,3))
            html_text += '<p>Расчетная температура наружного воздуха - \(t_{{хн}} = {0:.1f} ,℃\);</p>'.format(round(ti.res.t_б_хн(),3))
            html_text += '<p>Плотность воздуха наружная - \(ρ_{{н {0} }} = {1:.3f} , \\frac{{ кг }}{{ м³ }} \);</p>'.format(nbr, round(ti.ρ_н,3))
            html_text += '<p>Ориентир стены к ветру: "{0}"</p>'.format(ti.wall_direct)
            html_text += '<p>Уровень, через ограждения расположенные ниже которого будет <br>осуществляться инфильтрация воздуха:</p>'
            datamas_h = [nbr, ti.H, p_or_m(ti.vet[0]), 0.6, p_or_m(ti.vet[1]), -0.45,    1, round(ti.ρ_н,3), round(ti.loc.W_нр,3), 9.8, round(ti.ρ_в,3), round(ti.h_р, 2)]
            #             0    1              2:+-    3:K_1н       4:+-       5:K_1з  6:K_2          7                     8        9:g           10              11
            if ti.ρ_н != ti.ρ_в:
                html_text += '<p>\(H_{{ р }} = 0.5 \cdot Н_{{ {0} }} {2} 0.25 \cdot \\left ( K_{{1н}} {4} K_{{1з}} \\right ) \cdot '.format(*datamas_h)
                html_text += ' K_2 \cdot \\frac{{ ρ_{{н {0} }} \cdot W_{{нр}}^{{2}} }}{{ g \cdot \\left ( ρ_{{н {0} }} - ρ_{{в {0} }} \\right ) }} = \)</p>'.format(*datamas_h)
                
                html_text += '<p>\(H_{{ р }} = 0.5 \cdot {1} {2} 0.25 \cdot \\left ( {3} {4} ({5}) \\right ) \cdot '.format(*datamas_h)
                html_text += ' {6} \cdot \\frac{{ {7} \cdot {8} ^{{2}} }}{{ {9} \cdot \\left ( {7} - {10} \\right ) }} = \)</p>'.format(*datamas_h)
                
                html_text += '<p>\(H_{{ р }} = {11} , м \)'.format(*datamas_h)
            else:
                html_text += '<p>\(ρ_{{в {0} }} = ρ_{{н {0} }} = {1:.3f}, \\frac{{ кг }}{{ м³ }} \);</p>'.format(nbr, round(ti.ρ_в,3))
                html_text += '<p>\(H_{{ р }} = 0.5 \cdot Н_{{ {0} }} = 0.5 \cdot {1} = {11} , м \);</p>'.format(*datamas_h)

            if ti.h_нс >= ti.h_р:
                html_text += '<p>\( h_{{нс {0} }} = {1} \geq H_{{ р }} = {2} , м \);</p>'.format(nbr, round(ti.h_нс,3), round(ti.h_р,3))
                html_text += '<p> т.о. ни через один стык не будет осуществляться инфильтрация;</p>'.format(nbr, round(ti.h_нс,3), round(ti.h_р,3))
                
            for i in range(len(ti.l_c)):
                nbri = '{},{}'.format(nbr, i + 1)
                html_text += '<p> Расчет щелевого участка № {} :</p>'.format(nbri)
                ddi = {
                    'nbri': nbri,
                    'H' : round(ti.H,3),
                    'H_р' : round(ti.h_р,3),
                    'h_нс' : round(ti.h_нс,3),
                    'h_нн' : round(ti.h_нн[i],3),
                    'h_нв' : round(ti.h_нв[i],3),
                    'l_c' : round(ti.l_c[i],3),
                    'H_нн' : round(ti.h_нс + ti.h_нн[i],3),
                    'H_нв' : round(ti.h_нс + ti.h_нв[i],3),
                    'l_cч' : round(ti.m_L_c[i],3),
                    'h_н' : round(ti.m_h_н[i],3),
                    'dp_огр' : round(ti.dp_огр[i],3)}
                if ti.h_р >= ti.h_нс + ti.h_нв[i]:#щелевые ограждение учавствует полностью в потерях за счет инфильтрации
                    html_text += '<p>\( H_{{ р }} = {1} > Н_{{ нв {0} }} = {2},м \)</p>'.format(nbri, ddi['H_р'], ddi['H_нв'] )
                    html_text += '<p>cледовательно данная щель будет учавствовать в инфильтрации:</p>'
                    html_text += '<p>\( L_{{ cч {0} }} = L_{{ c {0} }} = {1},м ;\) '.format(nbri, ddi['l_cч'] )
                    
                    html_text += ' \( h_{{ н {0} }} = \\frac{{ h_{{ нн {0} }} + h_{{ нв {0} }} }}{{ 2 }} '.format(nbri)
                    html_text += ' = \\frac{{ {1} + {2} }}{{ 2 }} = {3}, м ;\)</p>'.format(nbri, ddi['h_нн'], ddi['h_нв'], round((ddi['h_нн'] + ddi['h_нв']) / 2, 3) )
                elif (ti.h_нс + ti.h_нв[i] >= ti.h_р) and (ti.h_р >= ti.h_нс + ti.h_нн[i]):#щелевые ограждение учавствует частично в потерях за счет инфильтрации
                    html_text += '<p>\( Н_{{ нн {0} }} = {1} \leq H_{{ р }} = {2} \leq Н_{{ нв {0} }} = {3}, м \)</p>'.format(nbri, ddi['H_нн'], ddi['H_р'], ddi['H_нв'] )
                    html_text += '<p>cледовательно данная щель будет учавствовать в инфильтрации частично:</p>'
                    html_text += '<p>\( L_{{ cч {0} }} = L_{{ c {0} }} \cdot \\frac{{ H_{{ р }} - h_{{ нс {1} }} - h_{{ нн {0} }} }}{{ h_{{ нв {0} }} - h_{{ нн {0} }} }} '.format(nbri, nbr)
                    html_text += ' = {0} \cdot \\frac{{ {1} - {2} - {3} }}{{ {4} - {3} }} = {5}, м \)</p>'.format(ddi['l_c'], ddi['H_р'], ddi['h_нс'], ddi['h_нн'], ddi['h_нв'], ddi['l_cч'])

                    html_text += '<p>\( h_{{ н {0} }} = h_{{ нн {0} }} + \\frac{{ H_{{ р }} - h_{{ нс {1} }} }}{{ 2 }} '.format(nbri, nbr)
                    html_text += ' = {0} + \\frac{{ {1} - {2} }}{{ 2 }} = {3} , м \)</p>'.format(ddi['h_нн'], ddi['H_р'], ddi['h_нс'], ddi['h_н'])

                datamas_hm = [nbri, nbr, ddi['H'], ddi['h_нс'], ddi['h_н'], round(ti.ρ_н,3), round(ti.ρ_в,3), 9.8,
                #              0     1        2         3            4               5                 6      7
                              p_or_m(ti.vet[0]), 0.6, p_or_m(ti.vet[1]), -0.45,    1, round(ti.ρ_н,3), round(ti.loc.W_нр,3), ddi['dp_огр']]
                #                       8:+-   9:K_1н           10:+-    11:K_1з  12:K_2       13                   14             15
                html_text += '<p>\(\Delta p_{{огр {0} }} = \\left ( H_{{ {0} }} - h_{{нс {1} }} - h_{{н {0} }} \\right ) '.format(*datamas_hm)
                html_text += ' \cdot \\left ( ρ_{{н {1} }} - ρ_{{в {1} }} \\right ) \cdot g '.format(*datamas_hm)
                html_text += ' {8} 0.25 \cdot \\left ( K_{{1н}} {10} K_{{1з}} \\right ) \cdot K_2 \cdot ρ_{{н {1} }} \cdot W_{{нр}}^{{2}} =\)<br>'.format(*datamas_hm)

                html_text += ' \( = \\left ( {2} - {3} - {4} \\right ) '.format(*datamas_hm)
                html_text += ' \cdot \\left ( {5} - {6} \\right ) \cdot {7} '.format(*datamas_hm)
                html_text += ' {8} 0.25 \cdot \\left ( {9} {10} ({11}) \\right ) \cdot {12} \cdot {13} \cdot {14}^{{2}} =\)</p>'.format(*datamas_hm)

                html_text += '<p>\( \Delta p_{{огр {0} }} = {15}, Па \)</p>'.format(*datamas_hm)

            html_text += '<p>Расход инфильтруемого воздуха:</p>' 
            html_text += '<p>\( G_{{ и {1} }} = \\sum_{{ i = 1 }}^{{ {2} }} \\left ( 0.1 \cdot G_н \cdot L_{{cч {1}i }} \cdot \Delta p_{{огр {1}i }} \\right ) = \)</p>'.format(nbri, nbr, len(ti.l_c))
            for i in range(len(ti.l_c)):
                if i == 0:
                    html_text += '<p>\( = 0.1 \cdot {0} \cdot {1} \cdot {2} + \)</p>'.format(round(ti.G_н,3), round(ti.m_L_c[i], 3), round(ti.dp_огр[i], 3))
                elif i == len(ti.l_c) - 1:
                    html_text += '<p>\( + 0.1 \cdot {0} \cdot {1} \cdot {2} = \)</p>'.format(round(ti.G_н,3), round(ti.m_L_c[i], 3), round(ti.dp_огр[i], 3))
                else:
                    html_text += '<p>\( + 0.1 \cdot {0} \cdot {1} \cdot {2} + \)</p>'.format(round(ti.G_н,3), round(ti.m_L_c[i], 3), round(ti.dp_огр[i], 3))
            html_text += '<p> \( G_{{ и }} = {0}, \\frac{{кг}}{{ч}} \) </p>'.format(round(ti.G_и,3))
                
        ##----------------------------------------------------------
        html_text += '<p>Тепловые потери за счет инфильтрации:</p>' 
        datamas_Q = [nbr, round(ti.loc.t_вр,1), round(ti.res.t_б_хн(),1), round(ti.loc.c_в,2), round(ti.G_и,3), round(ti.K_т,3)]
        html_text += '<p>\(Q_{{огр {0} }}=0.00028 \cdot \\left ( t_{{вр {0} }} - t_{{ хн }} \\right ) \cdot G_{{ и {0} }} \cdot K_{{ т {0} }} = \)</p>'.format(*datamas_Q)
        html_text += '<p>\(=0.00028 \cdot \\left ( {1} - ({2}) \\right ) \cdot {4} \cdot {5} = \)</p>'.format(*datamas_Q)
        html_text += '<p>\(Q_{{огр {0} }} = {1:.3f}, кВт \)</p>'.format(nbr, ti.Q_losses())
        html_text += '<hr>'
        #------------
        self.html_text = html_text

    def report_losses_list(self, mass):
        for item in mass:
            if type(item) is TR:
                self.report_matherial_params(item)
                #print(item.name)
            if type(item) is WL:
                self.report_wall_losses(item)
                #print(item.name)
            if type(item) is FL:
                self.report_floor_losses(item)
                #print(item.name)
            if type(item) is WI:
                self.report_wall_infiltration(item)
                #print(item.name)

    def report_table(self, df):
        html_text = self.html_text
        html_text += df.to_html(header="false", table_id="table")
        html_text += '<hr>'
        self.html_text = html_text

    def report_mathplotlib(self, fig):
        html_text = self.html_text
        
        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        html_text += f"<p><img src='data:image/png;base64,{data}'/></p>"
        html_text += '<hr>'
        self.html_text = html_text
        
    def start(self):
        """Процедура для запуска сервера. Запуск следует производить после того как былы заданы все отображаемые классы"""
        
        @app.route('/')
        def index():
            return self.html_text
        ##app.run(host='0.0.0.0', port=8181, debug = True)
        app.run(host='0.0.0.0', port = self.port)

        #отличный пример https://hplgit.github.io/web4sciapps/doc/pub/._web4sa_flask011.html

###Импорт классов и методов
##from LocalisationData import Localisation
###Локализация проекта
##loc = Localisation()
###Импортирую материалы
##from Matherials import r_conc_sht, r_concrete, r_srub_kirpich, r_floor_CARBON_ECO, r_float_st2
##
##from Home_class import Home
##
###демонстрация работы класса Home
##tpl_in = (r_conc_sht, r_float_st2)
####print("Домик 1 Стены: " + tpl_in[0].name + ' Окна: ' + tpl_in[1].name)
##home1 = Home(*tpl_in)
####home1.print_all_Q()
##
##
##sapr = SAPR()
##sapr.set_losses_list(home1.all_Q())
##sapr.start()
