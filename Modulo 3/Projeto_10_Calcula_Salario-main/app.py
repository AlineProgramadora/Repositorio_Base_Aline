# Você foi convidado a desenvolver uma Calculadora de Salário Mensal para sua turma. Seu programa deve:

# Perguntar quanto você ganha por hora (ex.: 25.50).
valor_hora=float(input("Digite quanto você ganha por hora: "))

# Perguntar quantas horas trabalhou no mês (ex.: 160).
horas=float(input("Digite quantas horas você trabalhou no mês:"))

# Calcular o salário do mês (valor_hora × horas).
salario=valor_hora * horas

# Exibir o resultado com 2 casas decimais.
print(f"Seu salario do mês é:R${salario:.2f}😲")
