#import model_pechat
#import model_dop
#from model_pechat import Pechat # первый вариант 
#from model_dop import Print
#from model_pechat import Pechat as mp
#from model_dop import Print as md
#from all import * - импортировать все


arr_models = ["Чехол","Пенал","Ручка","Керпич"]
arr_pystoy = []
Pechat(arr_models, arr_pystoy) #model_pechat.
Print(arr_pystoy)               #model_dop. - второй вариант импорта через import model_pechat
