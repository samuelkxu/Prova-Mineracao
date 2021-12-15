import pandas as pd
import matplotlib.pyplot as plt

#Questao 1- Printa as 10 primeiras posições
titanic = pd.read_csv('./titanic.csv')

#print (titanic.head(10))

#Questao 2- Ordena em ordem alfabetica
titanic.sort_values(by=['Name'], inplace=True)

#print (titanic.head(10))

#Questao 3- Cria mais um Para Sobrevivente Sim ou Nao
titanic['Sobrevive'] = titanic['Survived'].map({1:'Sim', 0:'Nao'})

#print (titanic.head(10))

#Questao 4- Remove 
titanic = titanic.drop(columns=['SibSp', 'Parch', 'Ticket'])

#print (titanic.head(10))

#Questao 5- Traduz as colunas para portugues 
titanic = titanic.rename({'PassengerId':'ID Passageiro'}, axis="columns")
titanic = titanic.rename({'Survived':'Sobrevivente'}, axis="columns")
titanic = titanic.rename({'Pclass':'ClassePassageiro'}, axis="columns")
titanic = titanic.rename({'Name':'Nome'}, axis="columns")
titanic = titanic.rename({'Sex':'Sexo'}, axis="columns")
titanic = titanic.rename({'Age':'Idade'}, axis="columns")
titanic = titanic.rename({'Fare':'Tarifa'}, axis="columns")
titanic = titanic.rename({'Cabin':'Cabine'}, axis="columns")
titanic = titanic.rename({'Embarked':'Embarcou'}, axis="columns")

#print (titanic.head(10))

#Questao 6- Coluna Sexo Masculino e Feminino
titanic['Sexo'] = titanic['Sexo'].replace(['male'],['MASCULINO'])
titanic['Sexo'] = titanic['Sexo'].replace(['female'], ['FEMININO']) 

#print (titanic.head(10))

#Questao 7- Sobreviventes class
contSobrevive = titanic.groupby(['ClassePassageiro','Sobrevive'])['Sobrevivente'].count()

print(contSobrevive.head(10))

#Questao 8- Sobreviventes Sexo class
sexoSobrevive = titanic.groupby(['Sexo','Sobrevive'])['Sexo'].count()

print(sexoSobrevive.head(10))

#Questao 9- Grafico
contSobrevive.plot(kind = 'bar')
plt.show()


#Questao 10
titanic.to_excel('titanic.xlsx', index = None, header = True)