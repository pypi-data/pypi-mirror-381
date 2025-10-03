#Импортирую материалы
from Matherials import r_conc_sht, r_concrete, r_srub_kirpich, r_floor_CARBON_ECO, r_float_st2

from Home_class import Home

from exoheat import SAPR

#демонстрация работы класса Home
tpl_in = (r_conc_sht, r_float_st2)
home1 = Home(*tpl_in)

#Автоматическая генерация отчета в виде сервера
sapr = SAPR()
sapr.report_losses_list([r_conc_sht, r_concrete, r_srub_kirpich, r_floor_CARBON_ECO, r_float_st2])
sapr.report_losses_list(home1.all_Q())
sapr.report_table(home1.get_Q()[3])
sapr.report_table(home1.get_S()[3])
sapr.report_mathplotlib(home1.get_plots())
sapr.report_mathplotlib(home1.get_plots_df())

sapr.start()
