medida = float(input('Uma distância em metros : '))
km = medida * 0.001
hm = medida * 0.01
dan = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print( 'km = {} \nhm = {} \ndan = {} \ndm = {} \ncm = {} \nmm = {} '.format(km,hm,dan,dm,cm,mm))