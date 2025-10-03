import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib import colors
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#Работа конструктора и инициализация внутренних переменных
H_зд = 3.1#м, высота отапливаемой части здания
l_ш = 9.5#м, ширина фасада
l_д = 11#м, длинна дома
h_цнс = 0.55#м - высота цокольного этажа(подвала) от уровня земли;
h_oнн = 0.95#м - высота от пола до подоконника;
h_oнв = 1.4#высоты окон;
l_oc = 1.6#м - ширина окон;
d_oc = 0.1#м - ширина отступа 100 мм от каждого угла, формируемого стенами эркера, а так же формируемого стенами эркера с домом
h_днв = 1.9#м - высоты дверей;
l_дc = 1.0#м - ширина дверей;
b_дc = 90#мм - толщина дверей;
l_шэ = 5.5#м - ширина эркера;
l_гэ = 1.6#м - глубина эркера;
l_дэ = 2**0.5 * l_гэ#м - диагональ эркера;
b_oc = 0.1 / 2**0.5#м - ширина отступа 100 мм от каждого угла
H_здк = H_зд + h_цнс + H_зд#м, высота здания от земли до конька


вид_скаты                = True
вид_фронтоны             = True
вид_пол_чердака          = True
вид_стены_перемычка      = True
вид_стены_над_окнами     = True
вид_стены_меж_окнами     = True
вид_стены_под_окнами     = True
вид_зоны_пола            = True
вид_пол                  = True
вид_стены_фундамента     = True
вид_основание_фундамента = True
вид_зоны_фундамента      = True

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Лента фундамента начиная от абсолютного значения продолжая приращениями
dx1 = [-l_дc/2, -l_ш/2+l_дc/2]#от двери по часовой Сев
dy1 = [+l_д /2,             0]
dx2 = [            0,     0,           0,     0,             0]#Два окна Запад
dy2 = [-l_д/4+l_oc/2, -l_oc, -l_д/2+l_oc, -l_oc, -l_д/4+l_oc/2]
dx3 = [+b_oc,  l_гэ-2*b_oc, +b_oc, d_oc, l_шэ-2*(l_гэ+d_oc), d_oc, b_oc, l_гэ-2*b_oc, b_oc]# Эркер Юг
dy3 = [-b_oc, -l_гэ+2*b_oc, -b_oc, 0   ,                 0 ,    0, b_oc, l_гэ-2*b_oc, b_oc]
dx4 = [(l_ш-l_шэ)/2-l_oc/2, l_oc, (l_ш-l_шэ)/2-l_oc/2]# Окно Юг
dy4 = [                  0,    0,                   0]
dx5 = [           0,     0,           0,     0,             0]#Два окна Восток
dy5 = [l_д/4-l_oc/2, +l_oc, +l_д/2-l_oc, +l_oc, +l_д/4-l_oc/2]
dx6 = [-l_ш/2+l_дc/2, -l_дc]#от двери по часовой Сев
dy6 = [0            ,     0]
dx = dx1 + dx2 + dx3 + dx4 + dx5 + dx6
dy = dy1 + dy2 + dy3 + dy4 + dy5 + dy6
#отметки уровней дома
dz = [0, h_цнс, h_oнн, h_oнв, H_зд - h_oнн - h_oнв]
#отметки facecolors для разукрашивания окон
dv = [0, 0, 1, -1, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 1, -1, 0, 0, 0]

#массивы с нарастающим итогом, для получения абсолютных значений координат
c_x = np.array([[sum(dx[:i+1]),]*2 for i in range(len(dx))])
c_y = np.array([[sum(dy[:i+1]),]*2 for i in range(len(dy))])

#массивы высот, высотные диапазоны
h_z = np.array([[sum(dz[:i+1]), sum(dz[:i+2])] for i in range(len(dz)-1)])

#массивы текстурных координат для окрашивния окон
c_v = np.array([[sum(dv[:i+1]), sum(dv[:i+1])] for i in range(len(dv))])
norm = colors.Normalize(vmin=c_v.min().min(), vmax=c_v.max().max())
c_NV = norm(c_v)
my_cm = colors.ListedColormap(['#CF695C', '#0343DFA0'])#заливка стен и окон(прозрачность) 

#массивы высот, сплошные повторы
c_z_цнс = np.array([h_z[0] for i in range(len(dx))])#фундамент
c_z_oнн = np.array([h_z[1] for i in range(len(dx))])#под окнами
c_z_oнв = np.array([h_z[2] for i in range(len(dx))])#высоты окон
c_z_здв = np.array([h_z[3] for i in range(len(dx))])#над окнами

#Отрисовка стен
if вид_стены_фундамента: ax.plot_surface(c_x, c_y, c_z_цнс, color = '#BFBFBF', linewidth=1, edgecolors='#4F4F4F')
if вид_стены_под_окнами: ax.plot_surface(c_x[:-1], c_y[:-1], c_z_oнн[:-1], color = '#CF695C', linewidth=0.5)
if вид_стены_меж_окнами: ax.plot_surface(c_x[:-1], c_y[:-1], c_z_oнв[:-1], facecolors = my_cm(c_NV), linewidth=1)
if вид_стены_над_окнами: ax.plot_surface(c_x[:-1], c_y[:-1], c_z_здв[:-1], color = '#CF695C', linewidth=0.5)

#---------------------------------------------------------------------------------------------
#Уровни полов, чердаков
#перевод в абсолютные координаты
a_x = np.array([sum(dx[:i+1]) for i in range(len(dx))])
a_y = np.array([sum(dy[:i+1]) for i in range(len(dy))])
a_z = np.array([sum(dz[:i+1]) for i in range(len(dz))])

dz_0 = np.array([a_z[0]]*len(dx))
dz_1 = np.array([a_z[1]]*len(dx))
dz_4 = np.array([a_z[4]]*len(dx))

verts_0 = [list(zip(a_x,a_y,dz_0))]
verts_1 = [list(zip(a_x,a_y,dz_1))]
verts_4 = [list(zip(a_x,a_y,dz_4))]

#Отрисовка уровней перекрытий
if вид_основание_фундамента: ax.add_collection3d(Poly3DCollection(verts_0, color = 'red'))#основание фундамента
if вид_пол                 : ax.add_collection3d(Poly3DCollection(verts_1, color = 'red'))#пол этажа
if вид_пол_чердака         : ax.add_collection3d(Poly3DCollection(verts_4, color = '#D8E4C0'))#чердачное перекрытие
#---------------------------------------------------------------------------------------------
#Зоны пола
def zon_arange(X_l, Y_l, X_r, Y_r, lenz = 4, d_zon = 2):
    '''Возвращает массив arange при делении пола на зоны(по умолчанию 4), по
    принципу внешние 3 зоны в виде одинаковых интервалов шириной d_zon
    (по умолчанию 2 м), а самая внутренняя она же 4-ая ключает все остальное
    X_l, м - левая начальная координата
    Y_l, м - левая начальная координата
    X_r, м - правая начальная координата
    Y_r, м - правая начальная координата
    lenz, шт - максимальное количество зон на которые можно разбивает площадь пола (по нормативу 4)
    d_zon, м - ширина зон в виде полосок по перемитру площади'''
    X = []
    Y = []
    _X_l = X_l + d_zon#левая сокращенная граница
    _X_r = X_r - d_zon#правая сокращенная граница
    _Y_l = Y_l + d_zon#левая сокращенная граница
    _Y_r = Y_r - d_zon#правая сокращенная граница
    v_l = True #можно взять зону в виде полоски
    if _X_r - _X_l < 0 and _Y_r - _Y_l < 0:
        v_l = False
    if v_l and lenz > 1: #продолжаем делить если есть на что
        X, Y = zon_arange(_X_l, _Y_l, _X_r, _Y_r, lenz - 1, d_zon)#рукурсия для расчета точек вложенных зон
    X.insert(0, X_l)#вставляем в начало массива
    Y.insert(0, Y_l)#вставляем в начало массива
    X.append(X_r)#вставляем в конец массива
    Y.append(Y_r)#вставляем в конец массива
    return X, Y

def zon_mesh_cm(lenz = 4, corners = True):
    '''Возвращает mesh матрицу с идентификаторами зон пола для разукраски,
    если corners = True то углы одельно выделяются цветом'''
    cm = np.zeros([lenz * 2 - 1, lenz * 2 - 1])
    for z in range(lenz):
        for y in range(len(cm) // 2 - z + 1):
            for x in range(len(cm) // 2 - z + 1):
                val = (z + 1) * (int(corners) + 1)
                if corners and x == y: val += 1
                #val = val / (int(corners) + 1) / (lenz + 1)
                cm[lenz - y - 1][lenz - x - 1] = val
                cm[lenz - y - 1][lenz + x - 1] = val
                cm[lenz + y - 1][lenz - x - 1] = val
                cm[lenz + y - 1][lenz + x - 1] = val
    return cm

x0, y0 = c_x[6][0], c_y[6][0]
X, Y = zon_arange(x0, y0, x0 + l_ш, y0 + l_д, lenz = 4, d_zon = 2)
X, Y = np.meshgrid(X, Y)
kX = abs(x0 + l_ш / 2 - X)
kY = abs(y0 + l_д / 2 - Y)
Z = (kX + kY) * 0.001

#массивы текстурных координат для окрашивния окон
lenz = len(X) // 2#количество зон
my_zon_cm = zon_mesh_cm(lenz = lenz, corners = True)#разбиваем пространство на номера зон

norm_zon = colors.Normalize(vmin=my_zon_cm.min().min(), vmax=my_zon_cm.max().max())#нормализуем значения от 0 до 1
c_NV_zon = norm_zon(my_zon_cm)
my_cmz = colors.ListedColormap(['#DF0000', '#FF0000', '#DFDF00', '#FFFF00', '#00DF00', '#00FF00', '#0000DF', '#0000FF'])#заливка стен и окон(прозрачность) 

#Отрисовка уровней зон пола
##if вид_зоны_пола      : ax.plot_surface(X, Y, -Z + a_z[0], cmap=cm.coolwarm, linewidth=0, antialiased=False)
if вид_зоны_пола      : ax.plot_surface(X, Y, -Z + a_z[0], facecolors = my_cmz(c_NV_zon), linewidth=0, antialiased=False)
if вид_зоны_фундамента: ax.plot_surface(X, Y, Z + a_z[1], facecolors = my_cmz(c_NV_zon), linewidth=0, antialiased=False)
#---------------------------------------------------------------------------------------------
#Дверь
dvz = [0, h_цнс, h_днв, H_зд - h_днв]
##myv_cm = colors.ListedColormap(['#F9C499', '#CF695C'])#заливка стен и дверей
##dvx1 = np.array([[-l_дc/2, +l_дc/2],]*(len(dvz)-1))#дверь Сев
##dvy1 = np.array([[+l_д /2, +l_д /2],]*(len(dvz)-1))
##dv_V1 = np.array([[0,0],[1,1],[-1,-1]])
##
###массивы высот, высотные диапазоны
##dvz1 = np.array([[sum(dvz[:i+1]), sum(dvz[:i+1])] for i in range(len(dvz))])[1:]
##
##ax.plot_surface(dvx1, dvy1, dvz1, facecolors = myv_cm(dv_V1), linewidth=1, edgecolors='brown')

#Перемычка над дверью
dv_x = [-l_дc/2, -l_дc/2, l_дc/2, l_дc/2]
dv_y = [  l_д/2,   l_д/2,  l_д/2,  l_д/2]
dvz1 = np.array([sum(dvz[:i+1]) for i in range(len(dvz))])
dv_z = [dvz1[2], dvz1[3],dvz1[3],dvz1[2]]
verts_dv = [list(zip(dv_x,dv_y,dv_z))]

#Отрисовка Перемычки над дверью
if вид_стены_перемычка: ax.add_collection3d(Poly3DCollection(verts_dv, color = '#CF695C'))
#---------------------------------------------------------------------------------------------
#Крыша от двери по часовой Сев
h_к = H_здк - (h_цнс + H_зд)#высота крыши
alfa_l = h_к/l_шэ#коэффициент склона крыши слева
alfa_r = h_к/(l_ш-l_шэ)#коэффициент склона крыши справа
#Раскладка левого ската от дальнего левого угла, конек там где заканчиватеся эркер
rx1 = [      -l_ш/2,    0,        +l_гэ,          l_шэ-2*l_гэ,        +l_гэ,   0]# запад юг
ry1 = [      +l_д/2, -l_д,        -l_гэ,                    0,        +l_гэ, l_д]
rz1 = [h_цнс + H_зд,    0, +l_гэ*alfa_l, (l_шэ-2*l_гэ)*alfa_l, +l_гэ*alfa_l,   0]
r_x1 = np.array([sum(rx1[:i+1]) for i in range(len(rx1))])
r_y1 = np.array([sum(ry1[:i+1]) for i in range(len(ry1))])
r_z1 = np.array([sum(rz1[:i+1]) for i in range(len(rz1))])
verts_6 = [list(zip(r_x1,r_y1,r_z1))]

#Раскладка правого ската от конека вправо вниз
rx2 = [-l_ш/2+l_шэ,           l_ш-l_шэ,    0,         -l_ш+l_шэ]#восток север
ry2 = [     -l_д/2,                  0, +l_д,                 0]
rz2 = [      H_здк, -(l_ш-l_шэ)*alfa_r,    0, (l_ш-l_шэ)*alfa_r]
r_x2 = np.array([sum(rx2[:i+1]) for i in range(len(rx2))])
r_y2 = np.array([sum(ry2[:i+1]) for i in range(len(ry2))])
r_z2 = np.array([sum(rz2[:i+1]) for i in range(len(rz2))])
verts_7 = [list(zip(r_x2,r_y2,r_z2))]
#Отрисовка скатов
if вид_скаты: ax.add_collection3d(Poly3DCollection(verts_6, color = '#4F292C', linewidth=1, edgecolors='#4F292C'))
if вид_скаты: ax.add_collection3d(Poly3DCollection(verts_7, color = '#4F292C', linewidth=1, edgecolors='#4F292C'))
#---------------------------------------------------------------------------------------------
#Фронтон передний 
fx1 = np.concatenate((r_x1[1:-1], r_x2[:-2]))
fy1 = np.concatenate((r_y1[1:-1], r_y2[:-2]))
fz1 = np.concatenate((r_z1[1:-1], r_z2[:-2]))
c_fx1 = np.array([[it,]*2 for it in fx1])
c_fy1 = np.array([[it,]*2 for it in fy1])
c_fz1 = np.array([[h_цнс + H_зд, it] for it in fz1])
#Фронтон задний 
fx2 = np.concatenate((r_x2[2:], r_x1[:1]))
fy2 = np.concatenate((r_y2[2:], r_y1[:1]))
fz2 = np.concatenate((r_z2[2:], r_z1[:1]))
c_fx2 = np.array([[it,]*2 for it in fx2])
c_fy2 = np.array([[it,]*2 for it in fy2])
c_fz2 = np.array([[h_цнс + H_зд, it] for it in fz2])

#Отрисовка фронтонов
if вид_фронтоны: ax.plot_surface(c_fx1, c_fy1, c_fz1, color = 'orange', linewidth=1, edgecolors='#4F4F4F')
if вид_фронтоны: ax.plot_surface(c_fx2, c_fy2, c_fz2, color = 'orange', linewidth=1, edgecolors='#4F4F4F')

#стены заливка '#BFBFBF'
#стены заливка '#FF796C'  FF796C
#окна заливка '#DBEEF4'
#окна линии '#4BACC6'
#дверь заливка '#F9C499'
#крыша '#D8E4C0'

ax.set_xlim(-8,8)
ax.set_ylim(-8,8)
ax.set_zlim(0,10)
plt.show()
