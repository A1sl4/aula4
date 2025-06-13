from geometria import calcular_area_circulo, calcular_area_retangulo, calcular_area_triangulo

selecao = int(input("selecione o que quer calcular\n se quiser circulo digite 1\nse quiser retangulo digite 2\n e se quiser triangulo digite 3\n "))

if selecao == 1:
    raio = float(input("digite o raio do seu circulo:\n"))
    area = calcular_area_circulo(raio)
    print("A area do seu circulo é: ",area)
    
elif selecao == 2:
    base = float(input("Digite a base do seu retangulo:\n"))
    altura = float(input("Digite a altura do seu retangulo:\n"))
    area = calcular_area_retangulo(base, altura)
    print("A area do seu retangulo é: ",area)
    
elif selecao == 3:
    base = float(input("Digite a base do seu triângulo:\n"))
    altura = float(input("Digite a altura do seu triângulo :\n"))
    area = calcular_area_triangulo(base, altura)
    print("A area do seu triângulo é: ",area)
    
